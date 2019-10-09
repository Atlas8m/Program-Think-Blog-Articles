# 扫盲 HTTPS 和 SSL-TLS 协议[4]：历史版本的演变及 Record 协议的细节 

-----

<div class="post-body entry-content">
　　俺一直在等 TLS 1.3 定稿（之所以这么期待，因为 1.3 是一次【大】升级）。<br/>
　　前些天（2018年8月），IETF 终于发布了 <a href="https://tools.ietf.org/html/rfc8446" rel="nofollow" target="_blank">RFC 8446</a>，标志着 TLS 1.3 协议大功告成。于是俺就来继续完成本系列的后面几篇。<br/>
　　本系列的<a href="../../2016/09/https-ssl-tls-3.md">前一篇</a>，咱们聊了“密钥交换/密钥协商”的相关算法。从这篇开始，会逐步谈及协议的细节，今天就从 Record 协议说起。由于恰逢 TLS 1.3 新鲜出炉，俺也顺便聊聊 SSL/TLS 历史上几个版本的演变及差异。<br/>
<a name="more"></a><br/>
<br/>
<h2>★名词解释</h2><br/>
　　对于本文会涉及到的几个专业术语，先放上相应的解释。<br/>
<br/>
<h3>◇块加密算法</h3><br/>
　　“块加密算法”又称“分组加密算法”，洋文叫做“Block Cipher”，相关的维基百科链接在“<a href="https://en.wikipedia.org/wiki/Block_cipher" rel="nofollow" target="_blank">这里</a>”。<br/>
　　顾名思义，就是这类加密算法要求：被加密的明文数据必须分成【相同大小】的若干坨（每一坨的大小称为【块长度】）。<br/>
　　以目前流行的对称加密算法 AES 为例。AES 的【块长度】是“128 比特”（16字节）。也就是说，AES 要求被加密的明文必须是【128位】的整数倍。<br/>
　　由于【块加密算法】对明文的长度有要求，所以用这类算法对明文数据进行加密之前，要先进行【补齐】——在明文数据末尾追加一些垃圾数据，使之达到【块长度】的整数倍。<br/>
<br/>
<h3>◇流加密算法</h3><br/>
　　与“块加密算法”相对应的是“流加密算法”，洋文叫做“Stream Cipher”，相关的维基百科页面在“<a href="https://en.wikipedia.org/wiki/Stream_cipher" rel="nofollow" target="_blank">这里</a>”。<br/>
　　与“块加密算法”最大的差别在于——流加密算法对明文数据的长度【没有】要求（可以是任意字节数）。<br/>
　　典型的流加密算法是 <a href="https://en.wikipedia.org/wiki/RC4" rel="nofollow" target="_blank">RC4</a>（顺便提一句：RC4 里面的 R 也就是 RSA 的那个 R）<br/>
<br/>
<h3>◇MAC（消息认证码）</h3><br/>
　　MAC 是洋文“Message Authentication Code”的缩写，维基百科的介绍在“<a href="https://en.wikipedia.org/wiki/Message_authentication_code" rel="nofollow" target="_blank">这里</a>”。这玩意儿是通讯及密码学的常见的概念——用 MAC 算法来确保某个信息在传输的过程中【没有】被篡改。<br/>
　　说到这儿，某些聪明的同学已经联想到【散列函数】——用散列函数计算出来的哈希值确实可以用来作为 MAC。这种基于哈希（HASH）的“消息验证代码”也称作“HMAC”。不了解哈希算法的同学可以看这篇博文：《<a href="../../2013/02/file-integrity-check.md">扫盲文件完整性校验——关于散列值和数字签名</a>》<br/>
<br/>
<h3>◇MAC 的几种搞法</h3><br/>
　　常见的有如下三种。俺从维基百科剽窃了对应的流程图，大伙儿看图就明白其原理，省得俺浪费力气打字了。<br/>
<br/>
　　<b>Encrypt-then-MAC （EtM）</b><br/>
<center><img alt="不见图 请翻墙" src="images/ZQkpnuTEiUkPvn2psD0gPxtUbENwZP1onhRNDCb2F7JAovU6bGFTBwu20aop2R4WFlwWx0Hd-B0meLWd8xKHhRFzisfxSO0Epf8oeNK8w0Q6pwcLgTLVqDZrVlLa01V46i6ZaGHus50"/><br/>
　　先加密明文得到密文，再根据密文计算 MAC，最后把密文与 MAC 合并成一坨</center><br/>
　　<b>Encrypt-and-MAC （E＆M）</b><br/>
<center><img alt="不见图 请翻墙" src="images/BKYtLQ_do3AKtTYeI-Atao5MztF_PLPvjdsv4TVPneDWJGZZ6RVFq7QqaTMF-ulgEnupLr8IJCB989gnXGEomqSxPqupKky6xOrWwqs3Vhk7qeqQHGkoiCDI8cxGwmkZT9HCFTgMsp0"/><br/>
　　对明文加密得到密文，对明文计算 MAC，最后把密文与 MAC 合并成一坨</center><br/>
　　<b>MAC-then-Encrypt （MtE）</b><br/>
<center><img alt="不见图 请翻墙" src="images/SUX0koVBgoYe2zey_lL1ptgiFtyTgHHXfrKi2AwSl3cELjk9ObToDlPUODdugOOsPKFbK-jzBFPmwT2fZlEpJIMOj44TS2p8EHOVWVoeWtZ3F_cQrkU4lOobrIb4o3dhdWlNHseog74"/><br/>
　　对明文计算 MAC，把明文与 MAC 合并成一坨，然后一起加密</center><br/>
<h3>◇AE（带认证的加密）</h3><br/>
　　传统的加密算法只负责实现【保密性】，而不负责【完整性】。这么说有点抽象，俺举个例子：<br/>
　　假设你把一段明文 P 加密为一段密文 C，通过网络把 C 发送给另一个人。中途如果被攻击者篡改了（把 C 修改为 C'），那么接收方收到 C' 之后，还是可以正常进行解密操作（当然，解密之后得到的就不再是 P 了，而是得到一段无意义的数据）<br/>
　　为了解决上述弊端，业界引入 AE（Authenticated Encryption）算法的概念。也就是说，AE 算法不但能做到【保密性】还可以做到【完整性】。<br/>
　　刚才扫盲的三种 MAC 实现方式，【从理论上讲】就可以算 AE 啦。但上述那三种 MAC 的实现方式有个弊端——【解密】的一方还要自己进行 MAC 的验证操作。这种搞法既麻烦又增加额外风险。比如说：写解密代码的程序猿万一太粗心忘记进行验证，岂不前功尽弃？<br/>
<br/>
<h3>◇【真正的】AE</h3><br/>
　　为了避免上述提到的弊端，密码学界那帮专家又捣鼓出一些新的算法（比如 CCM、GCM）。这些算法可以在解密的同时验证数据的有效性，而且这些算法也【不】需要再额外存储一个独立的 MAC 数据。<br/>
　　本文后续部分提及的 AE，如果没有特别说明，就是指这类【真正的】AE。<br/>
　　知名的那些 AE 算法，可以组合现有的加密算法。比如说：从 TLS 1.2 开始引入的 GCM 和 CCM，这两个 AE 算法都可以组合 AES128 与 AES256 加密算法。<br/>
　　组合现有加密算法的好处不光是避免重新发明轮子，而且还可以充分利用硬件加速。比如 AES 作为对称加密的标准算法，某些芯片（比如 Intel/AMD）会把 AES 算法直接做成 CPU 指令，以实现硬件加速。<br/>
<br/>
<h3>◇AEAD</h3><br/>
　　AEAD 是洋文“Authenticated Encryption with Associated Data”的缩写，普通话叫做“带关联数据的认证加密”。简而言之，AEAD 是 AE 的变种。为了方便理解，俺再来找个栗子：<br/>
　　比如说在网络通讯中，数据包的【头部】必须是明文且保证完整性；而数据包的【载荷】既要加密（保密性）又要保证完整性。这时候 AEAD 算法就派上用场啦——数据包的【头部】就是 AEAD 算法里面的【关联数据】。<br/>
<br/>
<h3>◇前向保密 / 完美正向加密</h3><br/>
　　在本系列的前一篇《<a href="../../2016/09/https-ssl-tls-3.md">密钥交换（密钥协商）算法及其原理</a>》，俺已经补充了一个章节，简单扫盲了一下“回溯性破解”与“前向保密”的概念。<br/>
　　所以这里就不再浪费口水啦。<br/>
<br/>
<br/>
<h2>★SSL/TLS 历史版本的演变及差异</h2><br/>
　　趁着 TLS 1.3 正式发布的大好时机，简单扫盲一下 SSL/TLS 各个版本的差异。<br/>
<br/>
<h3>◇SSL 1.0</h3><br/>
　　在本系列的<a href="../../2014/11/https-ssl-tls-1.md">第一篇</a>，俺曾经提到：SSL 是上世纪90年代中期，由<a href="https://zh.wikipedia.org/wiki/%E7%B6%B2%E6%99%AF" rel="nofollow" target="_blank">网景公司</a>设计的。早期设计者是网景公司的 <a href="https://en.wikipedia.org/wiki/Taher_Elgamal" rel="nofollow" target="_blank">Taher Elgamal</a>（一位埃及的密码学家）。此人也被誉为“SSL 它爹”。<br/>
　　SSL 1.0 【从没】正式发布过，所以业界对它了解不多。之所以没有正式发布，据说是设计完之后发现了若干严重的安全缺陷，就不好意思再拿出来丢人现眼。<br/>
<br/>
<h3>◇SSL 2.0</h3><br/>
　　SSL 2.0 是 1995 年正式发布滴，坦率地说，协议设计比较粗糙。<br/>
　　比如俺在前一篇介绍过“密钥交换算法”和“身份认证算法”。在这两方面，SSL 2.0 都仅仅支持 RSA 这一种算法。<br/>
　　另一个值得吐槽之处是：SSL 2.0【没有】考虑到“前向保密”（洋文是“<a href="https://en.wikipedia.org/wiki/Forward_secrecy" rel="nofollow" target="_blank">forward secrecy</a>”），因此会遭遇【回溯性破解】的风险。（关于“前向保密”与“回溯性破解”，请看本文开头的名词解释）<br/>
<br/>
<h3>◇SSL 3.0</h3><br/>
　　SSL 2.0 发布之后不久，又被发现若干安全漏洞。所以又赶紧在 1996 年发布了 SSL 3.0 版本。（接连两个版本都不太灵光，看来“SSL 它爹”的水平实在令人不敢恭维）<br/>
　　这个 3.0 版本可以说是另起炉灶——换了几个密码学专家，【重新设计】了 SSL 协议。所以 SSL 3.0 相比 SSL 2.0 有很大差别。<br/>
　　关于 SSL 3.0 的权威技术规范，可以参见 <a href="https://tools.ietf.org/html/rfc6101" rel="nofollow" target="_blank">RFC 6101</a><br/>
<br/>
　　请允许俺稍微跑题一下：<br/>
　　重新设计 SSL 3.0 的那些专家，为首的是来自斯坦福大学的 <a href="https://en.wikipedia.org/wiki/Paul_Kocher" rel="nofollow" target="_blank">Paul Kocher</a>——此人堪称密码学奇才，SSL 3.0 发布的那年（1996），他才23岁（回想俺23岁的时候，在密码学方面是只菜鸟，真是情何以堪）。<br/>
　　在同一年，他还发表了篇论文，描述了一种【全新的】密码学攻击方式——<a href="https://en.wikipedia.org/wiki/Timing_attack" rel="nofollow" target="_blank">timing attack</a>（基于时间因素的边信道攻击）。这种攻击手法的原理，说起来并不算复杂，但很有创意，之前从来没人想到过。<br/>
<br/>
<h3>◇TLS 1.0</h3><br/>
　　TLS 1.0 是 1999 年发布滴，技术规范参见 <a href="https://tools.ietf.org/html/rfc2246" rel="nofollow" target="_blank">RFC 2246</a>。<br/>
　　为啥从 SSL 改名为 TLS 捏？主要是安全性在 Web 世界中越来越重要，因此 <a href="https://zh.wikipedia.org/wiki/%E4%BA%92%E8%81%94%E7%BD%91%E5%B7%A5%E7%A8%8B%E4%BB%BB%E5%8A%A1%E7%BB%84" rel="nofollow" target="_blank">IETF</a> 组织急需把 SSL 的协议【标准化】，为了以示区别，另外起个名字叫 TLS（洋文“Transport Layer Security”的缩写）。<br/>
　　虽然协议名改了，但其实 TLS 1.0 与 SSL 3.0 的差别不大。这点从协议版本号也可以看出来——TLS 1.0 内部的协议版本号其实是【3.1】。<br/>
<br/>
<h3>◇TLS 1.1</h3><br/>
　　TLS 1.1 是 2006 年发布滴，技术规范是 <a href="https://tools.ietf.org/html/rfc4346" rel="nofollow" target="_blank">RFC 4346</a>。<br/>
　　发布该版本的主要动机是：修补 CBC（<a href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher-block_chaining_(CBC)" rel="nofollow" target="_blank">cipher-block chaining</a>）相关的漏洞，以防范某些攻击（比如“<a href="https://en.wikipedia.org/wiki/Padding_oracle_attack" rel="nofollow" target="_blank">padding oracle attack</a>”）。<br/>
　　在 1.1 版本，原有的“【隐式】初始化向量”改为“【显式】初始化向量”，修正了 CBC 方式下填充数据的缺陷。<br/>
<br/>
<h3>◇TLS 1.2</h3><br/>
　　TLS 1.2 是 2008 年发布滴，技术规范是 <a href="https://tools.ietf.org/html/rfc5246" rel="nofollow" target="_blank">RFC 5246</a>。<br/>
　　相比 TLS 1.1 的变化如下：<br/>
<blockquote>支持 <a href="https://en.wikipedia.org/wiki/AEAD_block_cipher_modes_of_operation" rel="nofollow" target="_blank">AEAD</a> 加密模式（参见 <a href="https://tools.ietf.org/html/rfc5116" rel="nofollow" target="_blank">RFC 5116</a>）<br/>
加密算法废弃了 DES、DES40、IDEA、RC2<br/>
HMAC 增加了 SHA256</blockquote><br/>
<h3>◇TLS 1.3</h3><br/>
　　俺写本文时，TLS 1.3 刚刚新鲜出炉没几天（2018年8月），其技术规范是 <a href="https://tools.ietf.org/html/rfc8446" rel="nofollow" target="_blank">RFC 8446</a>。<br/>
　　从2008到2018，真所谓“十年磨一剑”。目前看来，这个 1.3 版本是一次雄心勃勃的升级，相对 TLS 1.2 加了不少东西，也删了不少东西。考虑到篇幅，俺挑几个主要的来说说：<br/>
<blockquote>首先要表扬的是：TLS 1.3 完善了 SNI（<a href="https://en.wikipedia.org/wiki/Server_Name_Indication" rel="nofollow" target="_blank">Server Name Identification</a>）扩展，非常有利于翻墙工具借助【依附的自由】对抗网络封锁；<br/>
其次是强制使用“完美正向加密（PFS）”，所以很多做不到 PFS 的密钥协商算法在 TLS 1.3 规范中被无情地抛弃了（比如：RSA、静态 DH、静态 ECDH...）；<br/>
传统的 HMAC 也被无情地抛弃了，今后只使用 AEAD 方式来保障完整性（关于 AEAD，请看本文开头的名词解释）；<br/>
原有的对称加密算法只保留 AES（3DES、RC4 废弃），另增加 <a href="https://en.wikipedia.org/wiki/ChaCha20" rel="nofollow" target="_blank">CHACHA20</a> 流加密算法；<br/>
压缩特性被废除（以消除 <a href="https://en.wikipedia.org/wiki/CRIME" rel="nofollow" target="_blank">CRIME 攻击</a>的风险）；<br/>
初始握手的过程有大的改变（这个等下一篇再聊）<br/>
......</blockquote><br/>
<br/>
<h2>★Record 协议概述</h2><br/>
　　很多介绍 SSL/TLS 的文章都把 record 协议给忽略了。可能这些文章的作者觉得 record 协议不太重要。但俺出于负责任的心态，觉得还是有必要跟大伙儿聊一下。<br/>
　　SSL/TLS 协议在通讯的过程中会把需要传输的数据分成一坨一坨的，每次都只发送或接收一坨。在洋文中，每一坨称作一个 record。下面要聊的“Record 协议”，就是用来定义这个 record 的格式。<br/>
<br/>
<br/>
<h2>★Record 协议的结构</h2><br/>
　　Record 协议比较简单，主要结构见下表：<br/>
<br/>
<center><table border="1" cellpadding="3" cellspacing="0"><tbody>
<tr style="background:lightgrey;"><th>字段名称</th><th>字段长度</th><th>备注</th></tr>
<tr><td>类型</td><td>1字节</td><td> </td></tr>
<tr><td>版本</td><td>2字节</td><td>TLS 1.3 废弃，仅留作向下兼容</td></tr>
<tr><td>载荷长度</td><td>2字节</td><td> </td></tr>
<tr><td>消息</td><td>0~N 字节</td><td> </td></tr>
<tr><td>消息认证码</td><td>0~N 字节</td><td>TLS 1.3 不需要该字段</td></tr>
<tr><td>填充</td><td>0~N 字节</td><td> </td></tr>
</tbody></table></center><br/>
<h3>◇类型（type）</h3><br/>
　　“类型”字段是个枚举值，协议允许的有效值如下：<br/>
<center><table border="1" cellpadding="3" cellspacing="0"><tbody>
<tr style="background:lightgrey;"><th>十六进制</th><th>十进制</th><th>含义</th><th>备注</th></tr>
<tr><td>0x14</td><td>20</td><td>ChangeCipherSpec（切换到加密方式）</td><td>TLS 1.3 废弃</td></tr>
<tr><td>0x15</td><td>21</td><td>Alert（告警）</td><td> </td></tr>
<tr><td>0x16</td><td>22</td><td>Handshake（握手）</td><td> </td></tr>
<tr><td>0x17</td><td>23</td><td>Application（应用层数据）</td><td> </td></tr>
<tr><td>0x18</td><td>24</td><td>Heartbeat（心跳）</td><td>始于 TLS 1.3</td></tr>
</tbody></table></center>　　（关于表格中每一种类型，下面会有详细介绍）<br/>
<br/>
<h3>◇版本（version）</h3><br/>
　　“版本”字段含两个字节，分别表示：主版本号 和 次版本号。有效值如下：<br/>
<center><table border="1" cellpadding="3" cellspacing="0"><tbody>
<tr style="background:lightgrey;"><th>主版本号</th><th>次版本号</th><th>含义</th></tr>
<tr><td>0x2</td><td>0x0</td><td>SSL 2.0</td></tr>
<tr><td>0x3</td><td>0x0</td><td>SSL 3.0</td></tr>
<tr><td>0x3</td><td>0x1</td><td>TLS 1.0</td></tr>
<tr><td>0x3</td><td>0x2</td><td>TLS 1.1</td></tr>
<tr><td>0x3</td><td>0x3</td><td>TLS 1.2</td></tr>
</tbody></table></center>　　注：从 TLS 1.3 版本开始，“版本”字段已经被废弃，仅用于向后兼容。<br/>
<br/>
<h3>◇长度（length）</h3><br/>
　　“长度”字段含两个字节，表示载荷长度。<br/>
　　对于【明文】的 record，【没有】“消息认证码”字段，也【没有】“填充”字段——“载荷长度”也就是消息的长度。<br/>
　　对于【加密】的 record——“载荷长度”是“消息、消息验证码、填充”三者的长度之和。<br/>
　　SSL/TLS 协议规定了长度字段最多只能表示 <code>0~16384</code> 字节（<code>2<sup>14</sup> = 16384</code>）。<br/>
<br/>
<h3>◇消息（message）</h3><br/>
　　每个 record 的“消息”字段的内容取决于“类型”字段。关于这个“消息”字段，待会儿再聊。<br/>
<br/>
<h3>◇消息认证码（MAC）</h3><br/>
　　关于 MAC 这个概念，参见本文开头部分的名词解释，此处不再浪费口水。<br/>
　　在 SSL/TLS 协议中，MAC 对于明文的 record 没有意义（为啥没意义，请自行思考）。<br/>
　　对于【加密】的 record，要分两种情况：<br/>
其一，如果是【传统的】块加密与流加密，会带有额外的 MAC；<br/>
其二，如果使用 AEAD 加密模式，其本身已经内置了【完整性】的校验，不需额外的 MAC。<br/>
　　前面提到，AEAD 是从 TLS 1.2 开始引入，到了 TLS 1.3 就【只支持】AEAD 啦。所以 TLS 1.3 【没有】MAC 部分。<br/>
　　SSL/TLS 各个版本实现【完整性】的方式：<br/>
<center><table border="1" cellpadding="3" cellspacing="0"><tbody>
<tr style="background:lightgrey;"><th>算法</th><th>SSL 2.0</th><th>SSL 3.0</th><th>TLS 1.0</th><th>TLS 1.1</th><th>TLS 1.2</th><th>TLS 1.3</th></tr>
<tr><td>HMAC-MD5</td><td style="background:LightGreen;">是</td><td style="background:LightGreen;">是</td><td style="background:LightGreen;">是</td><td style="background:LightGreen;">是</td><td style="background:LightGreen;">是</td><td style="background:Pink;">否</td></tr>
<tr><td>HMAC-SHA1</td><td style="background:Pink;">否</td><td style="background:LightGreen;">是</td><td style="background:LightGreen;">是</td><td style="background:LightGreen;">是</td><td style="background:LightGreen;">是</td><td style="background:Pink;">否</td></tr>
<tr><td>HMAC-SHA256</td><td style="background:Pink;">否</td><td style="background:Pink;">否</td><td style="background:Pink;">否</td><td style="background:Pink;">否</td><td style="background:LightGreen;">是</td><td style="background:Pink;">否</td></tr>
<tr><td>AEAD</td><td style="background:Pink;">否</td><td style="background:Pink;">否</td><td style="background:Pink;">否</td><td style="background:Pink;">否</td><td style="background:LightGreen;">是</td><td style="background:LightGreen;">是</td></tr>
</tbody></table></center><br/>
<h3>◇填充（padding）</h3><br/>
　　只有当 record 是加密的，并且使用的加密算法属于【块加密算法】，才会使用“填充”字段。<br/>
<br/>
<br/>
<h2>★各种类型 Record 简介</h2><br/>
　　从 Record 协议的头部类型字段可以看出，总共有5种类型的 Record。下面简单说一下：<br/>
<br/>
<h3>◇握手（Handshake）</h3><br/>
　　Record 协议的“类型”字段为 <code>22</code>（<code>0x16</code>），表示这条 record 是 Handshake 类型。<br/>
　　“握手”的意思就是——通讯双方初次打交道，需要交换一些初始化的信息。<br/>
　　对于 SSL/TLS 协议，为了建立起【可靠的】加密信道，通讯双方需要在握手的过程交换很多信息（加密算法、压缩算法、MAC 算法、等等）。所以这个握手的过程是比较复杂滴，需要耗费很多口水。俺留到本系列的下一篇，专门来聊“握手的细节”。<br/>
　　由于握手的过程，加密信道尚未建立，所以用来进行握手的 record 是【明文】滴，并且也【没有】“MAC”字段及“填充”字段。<br/>
<br/>
<h3>◇切换到加密方式（ChangeCipherSpec）</h3><br/>
　　Record 协议的“类型”字段为 <code>20</code>（<code>0x14</code>），表示这条 record 是 ChangeCipherSpec 类型。<br/>
　　这个 ChangeCipherSpec 也是跟握手过程相关滴，留到下一篇。<br/>
　　注：从 TLS 1.3 版本开始，ChangeCipherSpec 类型的 record 已经被废弃，仅用于向后兼容。<br/>
<br/>
<h3>◇应用层数据（Application）</h3><br/>
　　Record 协议的“类型”字段为 <code>23</code>（<code>0x17</code>），表示这条 record 是 Application 类型。<br/>
　　也就是说，这条 record 的载荷部分存放的是上层（应用层）协议的数据。既然传输的是上层数据，肯定得是【加密】滴！但不一定有“MAC”字段。要看具体的 SSL/TLS 版本（如下）：<br/>
1. 对于 TLS 1.1 及之前的版本，总是使用 HMAC 进行完整性校验，所以总是含有“MAC”字段。<br/>
2. 对于 TLS 1.2，如果握手之后采用 AEAD 加密模式，就没有 MAC；反之，则有 MAC。<br/>
3. 对于 TLS 1.3 及之后的版本，只支持 AEAD，【不】再有“MAC”字段。<br/>
　　另外，在 TLS 1.2 及【之前】的版本中，还支持“对应用层数据进行压缩”。本来俺还想聊聊这方面的实现细节。但是 TLS 1.3 已经【废弃】了压缩选项（为了防 <a href="https://en.wikipedia.org/wiki/CRIME" rel="nofollow" target="_blank">CRIME 攻击</a>），恐怕未来版本也不会再有压缩选项了。搞得俺也没积极性来聊这个话题了 :(<br/>
<br/>
<h3>◇告警（Alert）</h3><br/>
　　Record 协议的“类型”字段为 <code>21</code>（<code>0x15</code>），表示这条 record 是 Alert 类型。<br/>
　　这种类型的 record 用来发送警告或出错信息。<br/>
　　在通讯的过程（包括握手过程）中，有时候某一方会发现不对劲（比如收到的数据出现缺失或错误），这时候就要发送一条 Alert 类型的 record 给对方。<br/>
　　不对劲的情况分为两种，洋文分别称之为 Warning 和 Fatal。两者的差别在于：<br/>
<blockquote>Warning 表示通讯出现【不稳定】的情况（这种“不稳定”通常是【可恢复】滴）<br/>
Fatal 表示通讯出现【不可靠】的情况（比如：证书失效、数据被篡改。这种“不可靠”通常是【不可恢复】滴）</blockquote>　　如果不对劲的情况属于 Warning，通讯可能会继续也可能会断开；如果不对劲的情况属于 Fatal，通讯会在发送 Alert 之后立即断开。<br/>
　　这种类型的 record，其“消息”字段仅有2字节，头一个字节表示告警的“级别/Level”（1表示 warning，2表示 fatal）；后一个字节表示具体的描述（有一个对照表，用不同的整数表示不同的情况）。<br/>
　　如果在握手【之后】发送告警，此时双方已经建立起加密信道，则告警 record 的“消息”字段是【密文】的。<br/>
　　如果在握手【之前】发送告警，此书尚未建立加密信道，则告警 record 的“消息”字段是【明文】的。<br/>
<br/>
<h3>◇心跳（Heartbeat）</h3><br/>
　　Record 协议的“类型”字段为 <code>24</code>（<code>0x18</code>），表示这条 record 是 Heartbeat 类型。<br/>
　　这种类型的 record 用来发送心跳信息。<br/>
　　所谓的【心跳】，主要用来确认“通讯的对端”依然正常。在 SSL/TLS 连接建立之后，有可能在某些情况下出现【通讯空闲】（上层的协议在某个时间段没有数据传输）。这时候就需要依靠【心跳机制】来判断对方是否还活着。<br/>
　　由于“心跳”的传输是在加密信道建立之后，所以“心跳”的 record 也是加密滴。<br/>
　　关于这个心跳机制的技术细节，请参见 RFC6520（链接在“<a href="https://tools.ietf.org/html/rfc6520" rel="nofollow" target="_blank">这里</a>”）。<br/>
　　这个心跳协议的 RFC 发布于2012年（晚于2008年的 TLS 1.2），因此目前只有 TLS 1.3 版本才支持它。<br/>
<br/>
<br/>
<a href="../../2014/11/https-ssl-tls-0.md">回到本系列的目录</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2018/09/https-ssl-tls-4.html
