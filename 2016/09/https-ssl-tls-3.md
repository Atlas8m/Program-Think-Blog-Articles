# 扫盲 HTTPS 和 SSL-TLS 协议[3]：密钥交换（密钥协商）算法及其原理 

-----

<div class="post-body entry-content">
　　先插播一个好消息：<br/>
　　本月初俺发了一篇《<a href="../../2016/09/About-WoSign.md" rel="nofollow" target="_blank">老流氓 CNNIC 的接班人——聊聊“沃通/WoSign”的那些破事儿</a>》。前2天看到新闻说，Mozilla 组织（Firefox）已经把沃通的根证书加入黑名单了，为期一年。一年之后看它的表现再决定是否永久性屏蔽。<br/>
　　对这种流氓公司，就应该给它点颜色看看（老实说，俺还觉得处罚偏轻了）<br/>
<br/>
<hr/>　　本系列的<a href="../../2014/11/https-ssl-tls-2.md">前一篇</a>，咱们聊了“密钥交换的难点”以及“证书体系”的必要性。今天这篇来介绍一下实战中使用的“密钥协商算法”。<br/>
<a name="more"></a><br/>
<br/>
<h2>★密钥交换/协商机制要达到啥【目的】？</h2><br/>
　　<a href="../../2014/11/https-ssl-tls-2.md">前一篇</a>介绍了 SSL/TLS 的身份认证机制。这个机制是为了防止攻击者通过【篡改】网络传输数据，来假冒身份，以达到“中间人攻击/MITM”的目的。<br/>
　　而今天要聊的“密钥协商机制”是：（在身份认证的前提下）如何规避【偷窥】的风险。<br/>
　　通俗地说，即使有攻击者在偷窥你与服务器的网络传输，客户端（client）依然可以利用“密钥协商机制”与服务器端（server）协商出一个用来加密应用层数据的密钥（也称“会话密钥”）。<br/>
<br/>
<br/>
<h2>★密钥交换/协商机制的几种【类型】</h2><br/>
　　俺总结了一下，大致有如下几种类型：<br/>
<br/>
<h3>◇类型1——依靠【非】对称加密算法</h3><br/>
　　原理：<br/>
　　拿到公钥的一方先生成随机的会话密钥，然后利用公钥加密它；再把加密结果发给对方，对方用私钥解密；于是双方都得到了会话密钥。<br/>
<br/>
　　举例：<br/>
　　<a href="https://en.wikipedia.org/wiki/RSA_(cryptosystem)" rel="nofollow" target="_blank">RSA</a><br/>
<br/>
<h3>◇类型2——依靠专门的密钥交换算法</h3><br/>
　　原理：<br/>
　　这个原理比较复杂，一两句话说不清楚，待会儿聊到 DH 的那个章节会详谈。<br/>
<br/>
　　举例：<br/>
　　<a href="https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange" rel="nofollow" target="_blank">DH 算法</a>及其变种<br/>
<br/>
<h3>◇类型3——依靠通讯双方事先已经共享的“秘密”</h3><br/>
　　原理：<br/>
　　既然双方已经有共享的秘密（这个“秘密”可能已经是一个密钥，也可能只是某个密码/password），只需要根据某种生成算法，就可以让双方产生相同的密钥（并且密钥长度可以任意指定）<br/>
<br/>
　　举例：<br/>
　　<a href="https://en.wikipedia.org/wiki/Pre-shared_key" rel="nofollow" target="_blank">PSK</a> 和 <a href="https://en.wikipedia.org/wiki/Secure_Remote_Password_protocol" rel="nofollow" target="_blank">SRP</a>（可能很多同学没听过这俩玩意儿。别担心，本文后续部分有介绍）<br/>
<br/>
<br/>
<h2>★基于【RSA】的密钥协商</h2><br/>
<h3>◇概述</h3><br/>
　　这大概是 SSL 最古老的密钥协商方式——早期的 SSLv2 只支持一种密钥协商机制，就是它！<a href="../../2014/11/https-ssl-tls-2.md">（前一篇）介绍身份认证重要性</a>的时候，也是拿 RSA 来演示。<br/>
　　（再次唠叨）<a href="https://en.wikipedia.org/wiki/RSA_(cryptosystem)" rel="nofollow" target="_blank">RSA</a> 是一种【非】对称加密算法。在本系列<a href="../../2014/11/https-ssl-tls-1.md">第1篇</a>的背景知识介绍中，已经聊过这种算法的特点——加密和解密用使用【不同的】密钥。并且“非对称加密算法”既可以用来做“加密/解密”，还可以用来做“数字签名”。<br/>
<br/>
<h3>◇密钥协商的步骤</h3><br/>
　　（下列步骤只阐述原理，具体的协议细节在下一篇讲）<br/>
<br/>
1. 客户端连上服务端<br/>
2. 服务端发送 CA 证书给客户端<br/>
3. 客户端验证该证书的可靠性<br/>
4. 客户端从 CA 证书中取出公钥<br/>
5. 客户端生成一个随机密钥 k，并用这个公钥加密得到 k'<br/>
6. 客户端把 k' 发送给服务端<br/>
7. 服务端收到 k' 后用自己的私钥解密得到 k<br/>
8. 此时双方都得到了密钥 k，协商完成。<br/>
<br/>
<h3>◇如何防范偷窥（嗅探）</h3><br/>
　　攻击方式1<br/>
　　攻击者虽然可以监视网络流量并拿到公钥，但是【无法】通过公钥推算出私钥（这点由 RSA 算法保证）<br/>
<br/>
　　攻击方式2<br/>
　　攻击者虽然可以监视网络流量并拿到 k'，但是攻击者没有私钥，【无法解密】 k'，因此也就无法得到 k<br/>
<br/>
<h3>◇如何防范篡改（假冒身份）</h3><br/>
　　攻击方式1<br/>
　　如果攻击者在第2步篡改数据，伪造了证书，那么客户端在第3步会发现（这点由证书体系保证）<br/>
<br/>
　　攻击方式2<br/>
　　如果攻击者在第6步篡改数据，伪造了k'，那么服务端收到假的k'之后，解密会失败（这点由 RSA 算法保证）。服务端就知道被攻击了。<br/>
<br/>
<br/>
<h2>★基于【DH】的密钥协商</h2><br/>
<h3>◇概述</h3><br/>
　　DH 算法又称“Diffie–Hellman 算法”。这是两位数学牛人的名称，他们创立了这个算法。该算法用来实现【安全的】“密钥交换”。它可以做到——“通讯双方在完全没有对方任何预先信息的条件下通过不安全信道创建一个双方共享的私有密钥”。这句话比较绕口，通俗地说，可以归结为两个优点：<br/>
1. 通讯双方事先【不】需要有共享的秘密。<br/>
2. 用该算法协商密码，即使协商过程中被别人全程偷窥（比如“网络嗅探”），偷窥者也【无法】知道协商得出的密钥是啥。<br/>
<br/>
　　但是 DH 算法本身也有缺点——它【不】支持认证。也就是说：它虽然可以对抗“偷窥”，却无法对抗“篡改”，自然也就无法对抗“中间人攻击/MITM”（在本系列的<a href="../../2014/11/https-ssl-tls-2.md">前一篇</a>，俺已经强调过了——缺乏身份认证，【必定会】遭到“中间人攻击/MITM”）。<br/>
　　为了避免遭遇 MITM 攻击，DH 需要与其它签名算法（比如 <a href="https://en.wikipedia.org/wiki/RSA_(cryptosystem)" rel="nofollow" target="_blank">RSA</a>、<a href="https://en.wikipedia.org/wiki/Digital_Signature_Algorithm" rel="nofollow" target="_blank">DSA</a>、<a href="https://en.wikipedia.org/wiki/Elliptic_Curve_DSA" rel="nofollow" target="_blank">ECDSA</a>）配合——靠签名算法帮忙来进行身份认证。当 DH 与 RSA 配合使用，称之为“DH-RSA”，与 DSA 配合则称为“DH-DSA”，以此类推<br/>
　　反之，如果 DH 【没有】配合某种签名算法，则称为“DH-ANON”（ANON 是洋文“匿名”的简写）。此时会遭遇“中间人攻击/MITM”。（具体的中间人攻击手法，可以参见本系列<a href="../../2014/11/https-ssl-tls-2.md">前一篇</a>）<br/>
<br/>
　　关于该算法的更多介绍，可以参见维基百科（<a href="https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange" rel="nofollow" target="_blank">这个条目</a>）。<br/>
<br/>
<h3>◇数学原理</h3><br/>
　　（如果你属于那种“看了数学公式就犯晕的人”，可以直接略过本小节，不影响你看后续的章节）<br/>
<br/>
　　从概念上讲：DH 依赖的是：求解“离散对数问题”的复杂性。具体的算法如下：<br/>
　　通讯双方（张三、李四）需要先约定好算法参数（algorithm parameters）：一个素数 p 作为模数，一个素数 g 作为基数（g 也称为“生成元”）。这两个算法参数是可以对外公开滴。<br/>
　　对于张三而言，需要先想好一个秘密的自然数 a 作为私钥（不能公开），然后计算 <code>A = g<sup>a</sup> mod p</code> 作为自己的公钥（可以公开）。<br/>
　　对李四而言也类似，先想好一个秘密的自然数 b 作为私钥（不能公开），然后计算 <code>B = g<sup>b</sup> mod p</code> 作为自己的公钥（可以公开）。<br/>
　　张三和李四互相交换各自的公钥。<br/>
　　然后张三计算出 <code>k = B<sup>a</sup> mod p</code>，李四计算出 <code>k = A<sup>b</sup> mod p</code><br/>
<br/>
　　该算法至少确保了如下几点：<br/>
1. 张三和李四分别计算出来的 k 必定是一致的<br/>
2. 张三和李四都无法根据已知的数来推算出对方的私钥（张三无法推算出 b，李四无法推算出 a）<br/>
3. 对于一个旁观者（偷窥者），虽然能看到 p，g，A，B，但是无法推算出 a 和 b（就是说，旁观者无法推算出双方的私钥），自然也无法推算出 k<br/>
<br/>
　　<b>举例</b><br/>
　　前面说得都是符号，比较抽象。下面拿具体数字举例：<br/>
假设约定的算法参数：模数是 <code>97</code>，基数是 <code>3</code><br/>
张三用的私钥是 <code>6</code>，李四用的私钥是 <code>21</code>，用 python 代码演示如下（python 语言用“两个连续星号”表示“幂运算”，用百分号表示“取模运算”）：<br/>
<br/>
<div class="source"><pre><span class="n">p</span> <span class="o">=</span> <span class="mi">97</span>
<span class="n">g</span> <span class="o">=</span> <span class="mi">3</span>

<span class="n">a</span> <span class="o">=</span> <span class="mi">6</span>
<span class="n">b</span> <span class="o">=</span> <span class="mi">21</span>

<span class="n">A</span> <span class="o">=</span> <span class="p">(</span><span class="n">g</span><span class="o">**</span><span class="n">a</span><span class="p">)</span> <span class="o">%</span> <span class="n">p</span>
<span class="n">B</span> <span class="o">=</span> <span class="p">(</span><span class="n">g</span><span class="o">**</span><span class="n">b</span><span class="p">)</span> <span class="o">%</span> <span class="n">p</span>

<span class="k">print</span><span class="p">((</span><span class="n">B</span><span class="o">**</span><span class="n">a</span><span class="p">)</span> <span class="o">%</span> <span class="n">p</span><span class="p">)</span>  <span class="c"># 此处输出 47</span>
<span class="k">print</span><span class="p">((</span><span class="n">A</span><span class="o">**</span><span class="n">b</span><span class="p">)</span> <span class="o">%</span> <span class="n">p</span><span class="p">)</span>  <span class="c"># 此处输出 47</span>
</pre></div><br/>
　　最后打印出来的两个 <code>47</code> 就是双方都计算出了【相同的】结果（这个数值可以用作之后的“会话密钥”）<br/>
<br/>
　　上面因为是举例，用的数字都比较小。在实战中需要注意如下几点，以降低被攻击的风险。<br/>
1. <code>p</code> 必须是质数且足够大（【至少】300位）<br/>
2. <code>a</code> ＆ <code>b</code> 也要足够大（【至少】100位），且必须是随机生成。<br/>
3. <code>g</code> 必须是质数，【不】需要很大，比如 2 或 3 或 5 都可以。<code>g</code> 如果太大并【不能】显著提升安全性，反而白白浪费了性能。<br/>
<br/>
<h3>◇密钥协商的步骤</h3><br/>
　　（下列步骤只阐述原理，具体的协议细节在下一篇讲）<br/>
<br/>
1. 客户端先连上服务端<br/>
2. 服务端生成一个随机数 s 作为自己的私钥，然后根据算法参数计算出公钥 S（算法参数通常是固定的）<br/>
3. 服务端使用某种签名算法把【算法参数（模数 p，基数 g）和服务端公钥 S】作为一个整体进行签名<br/>
4. 服务端把【算法参数（模数 p，基数 g）、服务端公钥S、签名】发送给客户端<br/>
5. 客户端收到后验证签名是否有效<br/>
6. 客户端生成一个随机数 c 作为自己的私钥，然后根据算法参数计算出公钥 C<br/>
7. 客户端把 C 发送给服务端<br/>
8. 客户端和服务端（根据上述 DH 算法）各自计算出 k 作为会话密钥<br/>
<br/>
<h3>◇如何防范偷窥（嗅探）</h3><br/>
　　嗅探者可以通过监视网络传输，得到算法参数（模数 p，基数 g）以及双方的公钥，但是【无法】推算出双方的私钥，也【无法】推算出会话密钥（这是由 DH 算法在数学上保证的）<br/>
<br/>
<h3>◇如何防范篡改（假冒身份）</h3><br/>
　　攻击方式1<br/>
　　攻击者可以第4步篡改数据（修改算法参数或服务端公钥）。但因为这些信息已经进行过数字签名。篡改之后会被客户端发现。<br/>
<br/>
　　攻击方式2<br/>
　　攻击者可以在第7步篡改客户端公钥。这步没有签名，服务端收到数据后不会发现被篡改。但是，攻击者篡改之后会导致“服务端与客户端生成的会话密钥【不一致】”。在后续的通讯步骤中会发现这点，并导致通讯终止。<br/>
　　（下一篇讲具体协议的时候会提到：协议初始化/握手阶段的末尾，双方都会向对方发送一段“验证性的密文”，这段密文用各自的会话密钥进行【对称】加密，如果双方的会话密钥不一致，这一步就会失败，进而导致握手失败，连接终止）<br/>
<br/>
<br/>
<h2>★DH 的变种——基于【椭圆曲线】的 ECDH</h2><br/>
　　DH 算法有一个变种，称之为 ECDH（全称是“Elliptic Curve Diffie-Hellman”）。维基条目在“<a href="https://en.wikipedia.org/wiki/Elliptic_Curve_Diffie-Hellman" rel="nofollow" target="_blank">这里</a>”<br/>
　　它与 DH 类似，差别在于：<br/>
DH 依赖的是——求解“离散对数问题”的困难。<br/>
ECDH 依赖的是——求解“椭圆曲线离散对数问题”的困难。<br/>
<br/>
　　ECDH 的数学原理比 DH 更复杂。考虑到本文读者大都【不是】数学系出身，俺就不展开啦。<br/>
　　ECDH 跟 DH 一样，也是【不支持】认证滴——同样需要与其它签名算法（比如 <a href="https://en.wikipedia.org/wiki/RSA_(cryptosystem)" rel="nofollow" target="_blank">RSA</a>、<a href="https://en.wikipedia.org/wiki/Digital_Signature_Algorithm" rel="nofollow" target="_blank">DSA</a>、<a href="https://en.wikipedia.org/wiki/Elliptic_Curve_DSA" rel="nofollow" target="_blank">ECDSA</a>）配合。<br/>
<br/>
<br/>
<h2>★基于【PSK】的密钥协商</h2><br/>
<h3>◇概述</h3><br/>
　　PSK 是洋文“Pre-Shared Key”的缩写。顾名思义，就是【预先】让通讯双方共享一些密钥（通常是【对称加密】的密钥）。所谓的【预先】，就是说，这些密钥在 TLS 连接尚未建立之前，就已经部署在通讯双方的系统内了。<br/>
　　这种算法用的不多，它的好处是：<br/>
1. 不需要依赖公钥体系，不需要部属 CA 证书。<br/>
2. 不需要涉及非对称加密，TLS 协议握手（初始化）时的性能好于前述的 RSA 和 DH。<br/>
　　更多介绍可以参见维基百科，链接在“<a href="https://en.wikipedia.org/wiki/Pre-shared_key" rel="nofollow" target="_blank">这里</a>”。<br/>
<br/>
<h3>◇密钥协商的步骤</h3><br/>
（由于 PSK 用的不多，下面只简单介绍一下步骤，让大伙儿明白其原理）<br/>
<br/>
　　在通讯【之前】，通讯双方已经预先部署了若干个共享的密钥。<br/>
　　为了标识多个密钥，给每一个密钥定义一个唯一的 ID<br/>
　　协商的过程很简单：客户端把自己选好的密钥的 ID 告诉服务端。<br/>
　　如果服务端在自己的密钥池子中找到这个 ID，就用对应的密钥与客户端通讯；否则就报错并中断连接。<br/>
<br/>
<h3>◇如何防范偷窥（嗅探）</h3><br/>
　　使用这种算法，在协商密钥的过程中交换的是密钥的标识（ID）而【不是】密钥本身。<br/>
　　就算攻击者监视了全过程，也无法知晓密钥啥。<br/>
<br/>
<h3>◇如何防范篡改（假冒身份）</h3><br/>
　　PSK 可以单独使用，也可以搭配签名算法一起使用。<br/>
　　对于单独使用<br/>
　　如果攻击者篡改了协商过程中传送的密钥 ID，要么服务端发现 ID 无效（协商失败），要么服务端得到的 ID 与客户端不一致，在后续的通讯步骤中也会发现，并导致通讯终止。<br/>
　　（下一篇讲具体协议的时候会提到：协议初始化/握手阶段的末尾，双方都会向对方发送一段“验证性的密文”，这段密文用各自的会话密钥进行【对称】加密，如果双方的会话密钥不一致，这一步就会失败，进而导致握手失败，连接终止）<br/>
<br/>
　　对于搭配签名算法<br/>
　　如果攻击者篡改了协商过程中传送的密钥 ID，验证签名会失败<br/>
<br/>
<h3>◇补充说明</h3><br/>
　　PSK 与 RSA 具有某种相似性——既可以用来搞“密钥协商”，也可以用来搞“身份认证”。<br/>
　　所以，PSK 可以跟 DH（及其变种）进行组合。例如：DHE-PSK、ECDHE-PSK<br/>
　　关于 PSK 的更多细节，可以参见 <a href="https://tools.ietf.org/html/rfc4279" rel="nofollow" target="_blank">RFC4279</a><br/>
<br/>
<br/>
<h2>★基于【SRP】的密钥协商</h2><br/>
<h3>◇概述</h3><br/>
　　SRP 是洋文“Secure Remote Password”的缩写。这个算法有点类似于刚才提到的 PSK——只不过 client/server 双方共享的是比较人性化的密码（password）而不是密钥（key）。该算法采用了一些机制（盐/salt、随机数）来防范“嗅探/sniffer”或“字典猜解攻击”或“重放攻击”。<br/>
　　这个算法应该用得很少——OpenSSL 直到2012年才开始支持该算法。所以俺这里就不展开了。有兴趣的同学可以去看 <a href="https://tools.ietf.org/html/rfc2945" rel="nofollow" target="_blank">RFC2945</a> 的协议描述。<br/>
<br/>
<h3>◇密钥协商的步骤</h3><br/>
　　（由于 SRP 用的不多，俺偷懒一下，略去此小节）<br/>
<br/>
<br/>
<h2>★扫盲一下【前向保密】（PFS）</h2><br/>
<h3>◇【回溯性破解】及其危险性</h3><br/>
　　从技术上讲，攻击者如果能够对通讯双方进行【嗅探】，也就能够把通讯双方的传输数据存储下来。如果攻击者比较牛逼，以至于能拿到通讯双方的私钥，那就【有可能】根据私钥推导出会话密钥，从而解密之前存储的历史数据。<br/>
　　有些同学可能会问：攻击者如何拿到私钥捏？<br/>
　　【常见】的情况有如下几种：<br/>
场景1——入侵双方的操作系统（搞定了操作系统，自然就能搞定系统中存储的私钥）；<br/>
场景2——利用协议【设计】的漏洞（能达到这种水准的，通常是 NSA 之类的国家队，养了足够多的密码学大牛）<br/>
场景3——利用协议【实现】的安全漏洞（比如前几年惊艳全球的“<a href="../../2014/04/openssl-heartbleed.md">心脏滴血漏洞</a>”，【有可能】会导致私钥泄漏。协议本身没问题，是 OpenSSL 的【代码实现】出了 bug）<br/>
场景4——通过<a href="../../2009/05/social-engineering-0-overview.md" rel="nofollow" target="_blank">社会工程学</a>（比如政府部门可以直接要求本国的网站交出私钥）。<br/>
<br/>
<h3>◇容易遭受回溯破解的密钥协商算法</h3><br/>
　　本文前面提到了几种密钥交换/协商算法，如下这几种【特别容易】遭到“回溯破解”。<br/>
<br/>
　　<b>RSA</b><br/>
　　攻击者事先存储了通讯的密文（历史数据）。<br/>
　　由于 RSA 的私钥是稳定的（长期不变）。假设有一天，攻击者拿到了 RSA 的私钥，就可以用这个私钥解密握手过程的密文，从而得到会话密钥（session key），然后用会话密钥解密会话的密文，得到会话的明文。<br/>
<br/>
　　<b>PSK（Pre-Shared Key）</b><br/>
　　攻击者事先存储了通讯的密文（历史数据）。<br/>
　　由于双方共享的 key 是稳定的（长期不变）。如果有一天，攻击者拿到了通讯双方共享的 key，就可以用这个 key 解密握手过程的密文，从而得到会话密钥（session key），然后用会话密钥解密会话的密文，得到会话的明文。<br/>
<br/>
　　<b>SRP（Secure Remote Password）</b><br/>
　　攻击者事先存储了通讯的密文（历史数据）。<br/>
　　由于双方共享的 password ＆ salt 是稳定的（长期不变）。如果有一天，攻击者拿到了通讯双方共享的 password 和 salt，就可以用来解密握手过程的密文，从而得到会话密钥（session key），然后用会话密钥解密会话的密文，得到会话的明文。<br/>
<br/>
<h3>◇解决方法——“前向保密/完美正向加密”</h3><br/>
　　相比前面这几种密钥协商算法，DH 和 ECDH 是比较能抗“回溯破解”滴。为啥这么说捏？下面解释：<br/>
　　对于 DH 算法，通讯双方握手需要生成各自的私钥（前面提到的整数 a 和 b），然后根据 DH 算法计算得出会话密钥。换句话说，会话密钥依赖于双方的私钥 a 与 b。DH 算法的优势在于——双方的私钥（a ＆ b）是可以【动态生成】滴！<br/>
　　为了对抗“回溯性破解”，可以强制要求双方每次都生成【随机的】私钥。而且每次生成的两个私钥用完就丢弃（销毁）。如此一来，攻击者就难以破解过往的历史数据。DH 算法经过如此改良之后叫做 DHE（追加的字母 E 表示【ephemeral】）。<br/>
　　与 DH 类似，ECDH 也可以做类似的改良，变成 ECDHE，以对抗“回溯破解”。<br/>
<br/>
　　能够对抗“回溯破解”的密钥交换算法，被称为“前向保密”，洋文叫“forward secrecy”，缩写为 FS。它还有另一个称呼——“完美正向加密”（洋文是“perfect forward secrecy”，缩写为 PFS）。关于这方面的更多介绍，可以参见维基百科（链接在“<a href="https://en.wikipedia.org/wiki/Forward_secrecy" rel="nofollow" target="_blank">这里</a>”）。<br/>
<br/>
<br/>
<h2>★各种算法组合的【一览表】</h2><br/>
<center><table border="1" cellpadding="3" cellspacing="0"><tbody>
<tr style="background:lightgrey;"><th>算法组合</th><th>密钥交换</th><th>身份认证</th><th>是否会遭遇<br/>
中间人攻击</th><th>是否具备<br/>
前向保密</th><th>SSL 2.0</th><th>SSL 3.0</th><th>TLS 1.0</th><th>TLS 1.1</th><th>TLS 1.2</th><th>TLS 1.3</th></tr>
<tr><td>RSA</td><td>RSA</td><td>RSA</td> <td style="background:lightgreen;">否</td><td style="background:lightpink;">否</td> <td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:white;">否</td></tr>
<tr><td>DH-RSA</td><td>DH</td><td>RSA</td> <td style="background:lightgreen;">否</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:white;">否</td></tr>
<tr><td>DH-DSA</td><td>DH</td><td>DSA</td> <td style="background:lightgreen;">否</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:white;">否</td></tr>
<tr><td>DHE-RSA</td><td>DHE</td><td>RSA</td> <td style="background:lightgreen;">否</td><td style="background:lightgreen;">是</td> <td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td></tr>
<tr><td>DHE-DSA</td><td>DHE</td><td>DSA</td> <td style="background:lightgreen;">否</td><td style="background:lightgreen;">是</td> <td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:white;">否</td></tr>
<tr><td>ECDH-RSA</td><td>ECDH</td><td>RSA</td> <td style="background:lightgreen;">否</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:white;">否</td></tr>
<tr><td>ECDH-ECDSA</td><td>ECDH</td><td>ECDSA</td> <td style="background:lightgreen;">否</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:white;">否</td></tr>
<tr><td>ECDHE-RSA</td><td>DHE</td><td>RSA</td> <td style="background:lightgreen;">否</td><td style="background:lightgreen;">是</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td></tr>
<tr><td>ECDHE-ECDSA</td><td>DHE</td><td>ECDSA</td> <td style="background:lightgreen;">否</td><td style="background:lightgreen;">是</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td></tr>
<tr><td>PSK</td><td>PSK</td><td>PSK</td> <td style="background:lightgreen;">否</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:darkgrey;">？</td></tr>
<tr><td>PSK-RSA</td><td>PSK</td><td>RSA</td> <td style="background:lightgreen;">否</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:darkgrey;">？</td></tr>
<tr><td>DHE-PSK</td><td>DHE</td><td>PSK</td> <td style="background:lightgreen;">否</td><td style="background:lightgreen;">是</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:darkgrey;">？</td></tr>
<tr><td>ECDHE-PSK</td><td>DHE</td><td>PSK</td> <td style="background:lightgreen;">否</td><td style="background:lightgreen;">是</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:darkgrey;">？</td></tr>
<tr><td>SRP</td><td>SRP</td><td>SRP</td> <td style="background:lightgreen;">否</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:darkgrey;">？</td></tr>
<tr><td>SRP-RSA</td><td>SRP</td><td>RSA</td> <td style="background:lightgreen;">否</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:darkgrey;">？</td></tr>
<tr><td>SRP-DSA</td><td>SRP</td><td>DSA</td> <td style="background:lightgreen;">否</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:white;">否</td></tr>
<tr><td>DH-ANON</td><td>DH</td><td style="background:red;">无</td> <td style="background:red;">是</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:white;">否</td></tr>
<tr><td>ECDH-ANON</td><td>ECDH</td><td style="background:red;">无</td> <td style="background:red;">是</td><td style="background:lightpink;">否</td> <td style="background:white;">否</td><td style="background:white;">否</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:lightgreen;">是</td><td style="background:white;">否</td></tr>
</tbody></table></center><br/>
　　（注：2018年8月，TLS 1.3 正式发布。俺又对本文略作补充）<br/>
<br/>
<br/>
<a href="../../2014/11/https-ssl-tls-0.md">回到本系列的目录</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2016/09/https-ssl-tls-3.html
