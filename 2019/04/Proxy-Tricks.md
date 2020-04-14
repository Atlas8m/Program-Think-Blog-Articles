# 如何让【不支持】代理的网络软件，通过代理进行联网（不同平台的 N 种方法） 

-----

<div class="post-body entry-content">
　　先提醒一下：明天就到5月份啦。今年是“六四事件”30周年，GFW 肯定要发飙。大伙儿要提前做好预防措施——手头同时备几个翻墙梯子。<br/>
　　今天要聊的这个话题，也是跟“翻墙”有点沾边滴，而且是为后续的某些博文做铺垫。<br/>
<a name="more"></a><br/>
<br/>
<h2>★本文的“目标读者”和“使用场景”</h2><br/>
<h3>◇使用场景</h3><br/>
　　有时候，你因为种种原因，需要使用某款【网络】软件，但是该软件又【不】提供“代理设置”的配置界面和功能。<br/>
　　如果你直接使用该【网络】软件的话，（在网络通迅过程中）服务器端可能会记录并保存【客户端 IP】（也就是你的【公网 IP】）。如此一来，可能会产生一些隐私方面的风险和担忧。<br/>
　　俺今天要聊的话题就是——<b>如何让那些【没有】代理功能的软件，也通过代理进行联网</b>。<br/>
<br/>
<h3>◇目标读者</h3><br/>
　　首先，本文面向那些【有一定折腾能力】的同学。在这篇教程中，俺会介绍 N 种【思路】（方法论）。考虑到篇幅，每一种方法的配置，都只是【点到为止】。喜欢折腾的同学，可以根据俺给出的思路，配合俺介绍的软件，自己动手实践一下。<br/>
　　其次，本文面向的是那些“比较注重隐私和隐匿性”的同学们。因为只有当你比较注重这些，才愿意为此而折腾。<br/>
<br/>
<h3>◇关于【匿名化】</h3><br/>
　　本文的主题是——<b>如何让【没有】代理功能的软件，也通过代理进行联网</b>。<br/>
　　对于特别注重隐私和匿名的同学，仅仅使用“代理”当然是【不够】滴！<b>为了实现【匿名性】，你不仅要让网络软件走代理，而且还要通过【匿名网络】来消除网络痕迹。</b><br/>
　　所以，在本文每一个方法论的末尾，都附上一个<q>如何匿名化</q>的小节。讲述该方法论如何搭配【匿名网络】。（为了打字省力，俺以 Tor 来举例；使用 I2P 的同学，请依样画葫芦。）<br/>
<br/>
　　由于本文讨论的是【代理】的话题，所以本文涉及的【隐匿性措施】都仅仅是【网络层面】。但俺要强调的是——<b>为了做到彻底的防范，你需要在【每一个层面】保护你的隐匿性</b>。很多人虽然使用 Tor，但还是暴露了身份。因为他们【忽视】了其它某些层面的防范。<br/>
　　下面这篇教程介绍了<b>【每一个层面】的防范</b>：<br/>
《<a href="../../2019/01/Security-Guide-for-Political-Activists.md">为啥朝廷总抓不到俺——十年反党活动的安全经验汇总</a>》<br/>
<br/>
<br/>
<h2>★预备知识</h2><br/>
<h3>◇“HTTP 代理”与“SOCKS 代理”有啥【差异】？</h3><br/>
　　简而言之，“HTTP 代理”是针对【HTTP 协议】而设计的（此处所说的 HTTP 协议包括 HTTPS）；而“SOCKS 代理”是为了支持【多种协议】而设计的。<br/>
　　另外，“SOCKS 代理”的层次比“HTTP 代理”更【低】——它对应于 OSI 7层模型的第5层【会话层】（session layer）。<br/>
<br/>
<h3>◇“SOCKS4”、“SOCKS4a”、“SOCKS5”都有啥【差异】？</h3><br/>
　　为了直观，放一个对照表（如下）。详细的说明参见维基百科的“<a href="https://en.wikipedia.org/wiki/SOCKS" rel="nofollow" target="_blank">这个页面</a>”。<br/>
<center><table border="1" cellpadding="3" cellspacing="0"><tbody>
<tr style="background:lightgrey;"><th> </th><th>远程域名解析</th><th>　IPv6　</th><th>　UDP　</th></tr>
<tr align="center"><td>SOCKS4</td><td>NO</td><td>NO</td><td>NO</td></tr>
<tr align="center"><td>SOCKS4a</td><td>YES</td><td>NO</td><td>NO</td></tr>
<tr align="center"><td>SOCKS5</td><td>YES</td><td>YES</td><td>YES</td></tr>
</tbody></table></center><br/>
　　“远程域名解析”需要单独强调一下。<br/>
　　当年设计 SOCKS4 的时候，并未考虑 DNS 的问题。所以客户端与 SOCKS4 服务端建立连接时，需要发送“4字节”的 IPv4 地址。<br/>
　　后来 SOCKS4a 增加了这个特性（又叫做“服务端 DNS 解析”）。客户端可以把【域名】发给 SOCKS 代理的服务端，然后由 SOCKS 服务端完成域名解析。这个特性【很重要】，原因至少包括——<br/>
如果你在【本机】进行域名解析，并且你的操作系统的 DNS 是传统的设置。那么，你的“DNS 查询请求”会通过网络【直连】。在这种情况下，如果 ISP 监控你的网络流量，就可以看出你在访问【哪些域名】的网站。<br/>
　　有鉴于上述原因，你使用的 SOCKS 代理，至少要是 SOCKS4a（SOCKS5 当然更好）。<br/>
<br/>
<h3>◇两种 HTTP 代理——“转发”和“隧道”</h3><br/>
　　<b>HTTP 转发</b><br/>
　　这是传统的方式。网络软件（比如：浏览器、IM）把自己想要的 URL 网址发给 HTTP proxy，当 proxy 拿到 URL 之后，向目标网站发起 HTTP 请求，获取 URL 对应的内容（页面/脚本/图片/等等），然后 proxy 把内容返回给网络软件。<br/>
　　使用这种代理，网络软件在进行 HTTP 通讯时，采用的依然是 HTTP 协议中常见的那几个 method（GET/POST/PUT/等等）。<br/>
　　这种代理也被称作“relay 或 forward”<br/>
<br/>
　　<b>HTTP 隧道</b><br/>
　　另外还有一种不太一样的 HTTP Proxy，使用一个专门的 HTTP method——【CONNECT】。用了 CONNECT 这个 method 之后，网络软件发给 proxy 的就【不再是】URL 网址了，可以是任意的【主机:端口】二元组。proxy 拿到“目标主机 &amp; 端口”之后，尝试与该主机建立连接。然后，proxy 就可以充当“目标主机”和“网络软件”之间的中转——网络软件发出的数据通过 proxy 转发给目标主机的指定端口，而目标主机发出的数据也通过 proxy 返回给网络软件。<br/>
　　这种方式可以用来实现“各种 TCP over HTTP”（比如：SSH over HTTP 或 RDP over HTTP），所以也称为“隧道”（tunnel）。<br/>
　　（关于“HTTP tunnel”的更多介绍，参见维基百科的“<a href="https://en.wikipedia.org/wiki/HTTP_tunnel" rel="nofollow" target="_blank">这个页面</a>”）<br/>
<br/>
<h3>◇“HTTP 代理”与“SOCKS 代理”如何【互相转换】？</h3><br/>
　　如果你使用的网络软件，仅仅支持 HTTP 或 SOCKS 的【其中一种】，而你用的代理是【另外一种】。那么就需要进行两种代理协议的【转换】。<br/>
<br/>
　　<b>HTTP 转 SOCKS</b><br/>
　　（如果你手头只有 SOCKS proxy，但你使用的网络软件只支持 HTTP 代理，就需要使用这种转换）<br/>
　　通过 Privoxy 来进行这种转换。Privoxy 本身可以充当 HTTP proxy，然后可以把数据转给别的 SOCKS proxy。<br/>
　　关于 Privoxy 的详细教程，参见《<a href="../../2014/12/gfw-privoxy.md">如何用 Privoxy 辅助翻墙？</a>》<br/>
<br/>
　　<b>SOCKS 转 HTTP</b><br/>
　　（如果你手头只有 HTTP proxy，但你使用的网络软件只支持 SOCKS 代理，就需要使用这种转换）<br/>
　　通过 Tor（或 Tor Browser） 来进行这种转换。“Tor 客户端”本身可以充当 SOCKS proxy，然后可以把数据转给别的 HTTP proxy。<br/>
　　关于 Tor 的详细教程，参见如下几篇：<br/>
《<a href="../../2013/11/tor-faq.md">“如何翻墙”系列：关于 Tor 的常见问题解答</a>》<br/>
《<a href="../../2018/04/gfw-tor-browser-7.5-meek.md">“如何翻墙”系列：扫盲 Tor Browser 7.5——关于 meek 插件的配置、优化、原理</a>》<br/>
《<a href="../../2015/03/Tor-Arm.md">扫盲 Arm——Tor 的界面前端（替代已死亡的 Vidalia）</a>》<br/>
<br/>
<h3>◇端口转发（Port Forward）</h3><br/>
　　本文后续部分会聊到“端口转发”这个招数。不太了解这个概念的同学，先看下面这篇博文（其中扫盲了“端口转发”的概念和工具）<br/>
《<a href="../../2013/01/cross-host-use-gfw-tool.md">多台电脑如何【共享】翻墙通道——兼谈【端口转发】的几种方法</a>》<br/>
<br/>
<br/>
<h2>★方案1：VPN</h2><br/>
　　先来聊 VPN，因为这是大伙儿最容易想到的方法，也是操作起来最简单滴。<br/>
<br/>
<h3>◇原理</h3><br/>
　　简而言之，VPN 具有类似于“全局代理”的效果。也就是说，只要操作系统中开启了 VPN，整个系统中所有软件的网络传输，都会自动通过 VPN 服务器中转。所以，就算某个软件本身不支持代理，只要该软件运行在 VPN 的环境中，该软件的网络传输也会经过 VPN 服务器中转。此时，目标网站看到的是【VPN 服务器】的 IP 地址。<br/>
<br/>
　　数据流的示意图如下：<br/>
<blockquote>网络软件  &lt;&lt;==&gt;&gt;  VPN客户端  &lt;&lt;==&gt;&gt;  VPN服务器  &lt;&lt;==&gt;&gt;  目标网站</blockquote><br/>
<h3>◇优点——配置简单</h3><br/>
　　由于 VPN 本身具有“全局代理”的效果，网络软件【无需任何配置】。<br/>
　　这是该方案最主要的优点。<br/>
<br/>
<h3>◇缺点——缺乏灵活性</h3><br/>
　　同样是由于“全局代理”的效果，导致这个方案【缺乏灵活性】。<br/>
　　比如说：如果你希望某个网络软件直接联网，另一个网络软件走代理。用 VPN 就行不通啦。<br/>
　　再比如说：你有两个不同的软件，需要走不同的代理，用 VPN 也不好弄。<br/>
<br/>
<h3>◇相关软件及配置</h3><br/>
　　VPN 的软件非常多（各个平台都有），而且懂的人也很多，俺就不列举了。<br/>
<br/>
<h3>◇如何匿名化？</h3><br/>
　　某些 VPN 软件（比如 VPNgate）本身提供了【代理设置】的功能——也就是说，可以让【VPN 客户端】通过代理联网。<br/>
　　对于这类 VPN，你可以采用【VPN over Tor】的方式，就可以实现【匿名化】。由于 VPN 本身具有【全局】性质，所以你在搞“VPN over Tor”的招数时，“Tor 客户端”必须位于【另一台主机】。<br/>
　　对于【VPN over Tor】的方式，就算 VPN 服务器记录了【访问者 IP】，这个 IP 也只不过是【Tor 出口节点】的 IP，与你本人的公网 IP 毫无关系。由于 Tor 的匿名网络会经过【三次随机跳转】，而且每隔几分钟就会变换线路（详情参见《<a href="../../2013/11/tor-faq.md">关于 Tor 的常见问题解答</a>》）；这种情况下，逆向追溯非常非常难。数据流的示意图如下：<br/>
<blockquote>网络软件  &lt;&lt;==&gt;&gt;  VPN客户端  &lt;&lt;==&gt;&gt;  Tor客户端  &lt;&lt;==&gt;&gt;  Tor匿名网络（3重跳转）  &lt;&lt;==&gt;&gt;  VPN服务器  &lt;&lt;==&gt;&gt;  目标网站</blockquote><br/>
　　如果你采用俺常年唠叨的【基于 TOR 的双重代理】，让某个翻墙工具作为 Tor 的【前置代理】，则数据流变得更加复杂（逆向追溯【更加不可能】）：<br/>
<blockquote>网络软件  &lt;&lt;==&gt;&gt;  VPN客户端  &lt;&lt;==&gt;&gt;  Tor客户端  &lt;&lt;==&gt;&gt;  翻墙工具客户端  &lt;&lt;==&gt;&gt;  翻墙服务器  &lt;&lt;==&gt;&gt;  Tor匿名网络（3重跳转）  &lt;&lt;==&gt;&gt;  VPN服务器  &lt;&lt;==&gt;&gt;  目标网站</blockquote><br/>
　　请注意：<br/>
　　由于 Tor 有很长一段时间（2010~2014）无法在天朝独立联网（GFW 屏蔽了 Tor 在全球的节点），因此很多墙内的同学会采用“Tor over VPN”的方式，让 Tor 联网。“Tor over VPN”与“VPN over Tor”，这两者是【相反】滴，别搞混喽。<br/>
<br/>
<br/>
<h2>★方案2：对“网络软件”的进程注入</h2><br/>
　　说“进程注入”，可能很多读者不知所云。但如果举 SocksCap 的例子，很多同学就明白俺要说啥了。<br/>
<br/>
<h3>◇原理</h3><br/>
　　以 SocksCap 为代表的这类软件，可以对其它上网软件的进程进行注入（把自己的某个动态库注入到上网软件的进程中）。<br/>
　　通过注入自己的动态库，就可以截获（被注入的）上网软件的网络行为，并修改其网络行为使网络通讯的数据转向指定的代理。<br/>
<br/>
<h3>◇优点——比较灵活，可以实现【进程级】的设置</h3><br/>
　　相比 VPN 方式，该方法的主要优势在于【灵活性】。<br/>
　　所谓的【进程级】就是说——即使对【同一个软件】的多个进程，你可以通过该方法，让某几个进程的网络通信走代理，而另几个进程则网络直连。。<br/>
<br/>
<h3>◇缺点1——兼容性比较差</h3><br/>
　　该方法的最大缺点是【兼容性】。<br/>
　　因为不同的软件，其内部实现方式，差异很大。采用“进程注入”，【未必】都有效。<br/>
　　俺在 Windows 和 Linux 下都尝试过这种方式，经常发现有些网络软件用这招不灵（未能实现转发）。<br/>
<br/>
<h3>◇缺点2——稳定性比较差</h3><br/>
　　另一个缺点是——有可能导致软件运行不稳定。<br/>
　　因为不同的网络软件，可能由不同的编程语言开发，可能由不同的编译器编译，编译时可能有不同的编译选项。<br/>
　　所以，对网络软件搞了进程注入之后，可能会出现一些奇奇怪怪的问题，甚至可能导致网络软件在运行时崩溃。<br/>
<br/>
<h3>◇相关软件及配置</h3><br/>
　　下面这几款软件，都是通过进程注入的方式，让网络软件的网络流量转向 SOCKS 代理。<br/>
<br/>
　　<b>SocksCap（Windows）</b><br/>
　　在 Windows 的同类软件中，SocksCap 大概是最老牌滴。使用教程参见“<a href="https://www.socksproxychecker.com/sockscap.html" rel="nofollow" target="_blank">这个页面</a>”。<br/>
　　目前网上流传最广的是 2.40 版本，大约2006年左右发布。开发该软件的“Permeo 公司”如今已经没了，当年的官网也没了。如果你要找这个软件，要从【靠谱的】网站下载。保险起见，附上 2.40 版本安装包的 SHA256 校验码（如下）<br/>
<pre>f381cae0f28d72bd1380159ca80b09e5526aa53d49d8dc963f7eace0c8f32d97</pre>　　由于 SocksCap 只能对32位的软件进行注入。如今“64位系统”越来越流行，它就显得有点落伍了；后来有人开发了一个 SocksCap64，基本模仿 SocksCap 的功能，但可以支持64位系统。<br/>
　　请注意，SocksCap64 与 SocksCap 虽然名称差不多，但这俩的作者【完全没关系】。<br/>
　　使用过程中，有个细节要提醒一下——小心 DNS 泄露信息。<br/>
　　SocksCap 的界面上可以配置“域名解析”（Name Resolution）。你要记得用【远程解析】。<br/>
<br/>
　　<b>tsocks（Linux &amp; Mac OS &amp; BSD）</b><br/>
　　你可以把这个软件理解为“Linux 版的 SocksCap”。其官网在“<a href="http://tsocks.sourceforge.net/" rel="nofollow" target="_blank">这里</a>”。<br/>
　　它的最后一个版本发布于2002年10月。可能是因为功能本身很简单，而且也不需要再加新功能，所以就没有更新了。<br/>
　　顺便说一下：几大主流的 Linux 发行版（Debian 家族、Fedora 家族、Arch 家族、Gentoo 家族 ......），其软件仓库中都已经包含了 tsocks。<br/>
<br/>
　　<b>ProxyChains（Linux &amp; Mac OS &amp; BSD）</b><br/>
　　proxychains 相当于 tsocks 的增强版，包括如下特性：<br/>
1. 支持【更多的】代理类型（除了各种 SOCKS 代理，还支持各种 HTTP 代理）。<br/>
2. 可以实现【链式】的代理（ProxyChains 这个名称就来自于此）<br/>
3. 用户可以定义一堆代理，让它“随机选择”<br/>
　　它的官网在“<a href="http://proxychains.sourceforge.net/" rel="nofollow" target="_blank">这里</a>”。后来又出了 proxychains-ng （ng 表示“new generation”），官网在“<a href="https://github.com/rofl0r/proxychains-ng" rel="nofollow" target="_blank">这里</a>”<br/>
　　顺便说一下：几大主流的 Linux 发行版（Debian 家族、Fedora 家族、openSUSE 家族、Arch 家族、Gentoo 家族 ......），其软件仓库中都已经包含了 ProxyChains 或 ProxyChains-ng。<br/>
<br/>
　　<b>PySocks（专用于 python）</b><br/>
　　作为曾经的程序猿，而且还比较喜欢 Python，顺便介绍一个库（如果你不是搞 Python 开发的，这个东东与你无关）。<br/>
　　它的代码仓库在“<a href="https://github.com/Anorov/PySocks" rel="nofollow" target="_blank">这里</a>”。使用它，只需增加4行代码（如下），就可以让整个 Python 进程的网络链接都转向指定的 SOCKS 代理。<br/>
<div class="source"><pre><span class="kn">import</span> <span class="nn">socket</span>
<span class="kn">import</span> <span class="nn">socks</span>
<span class="n">socks</span><span class="o">.</span><span class="n">set_default_proxy</span><span class="p">(</span><span class="n">socks</span><span class="o">.</span><span class="n">SOCKS5</span><span class="p">,</span> <span class="n">addr</span><span class="p">,</span> <span class="n">port</span><span class="p">)</span> <span class="c"># addr 和 port 表示 SOCKS 代理的地址和端口</span>
<span class="n">socket</span><span class="o">.</span><span class="n">socket</span> <span class="o">=</span> <span class="n">socks</span><span class="o">.</span><span class="n">socksocket</span>
</pre></div>　　其原理与刚才介绍的那几个工具差不多——它替换掉 socket 标准库的入口函数，其它 python 库（不管是标准库还是第三方库）只要想联网，终归都要直接或间接地依赖 socket 进行网络通讯，因此都会被重定向到指定的 SOCKS 代理。<br/>
<br/>
<h3>◇如何匿名化？</h3><br/>
　　如果你使用普通的翻墙代理，数据流的示意图如下：<br/>
<blockquote>网络软件  &lt;&lt;==(进程注入工具转发)==&gt;&gt;  翻墙工具客户端  &lt;&lt;==&gt;&gt;  翻墙服务器  &lt;&lt;==&gt;&gt;  目标网站</blockquote><br/>
　　为了强化【隐匿性】，你可以改用 Tor 匿名网络，数据流的示意图如下（逆向追溯已经非常难）<br/>
<blockquote>网络软件  &lt;&lt;==(进程注入工具转发)==&gt;&gt;  Tor客户端  &lt;&lt;==&gt;&gt;  Tor匿名网络（3重跳转）  &lt;&lt;==&gt;&gt;  目标网站</blockquote><br/>
　　如果你采用俺常年唠叨的【基于 TOR 的双重代理】，让某个翻墙工具作为 Tor 的【前置代理】，则数据流变得更加复杂（逆向追溯【更加不可能】）：<br/>
<blockquote>网络软件  &lt;&lt;==(进程注入工具转发)==&gt;&gt;  Tor客户端  &lt;&lt;==&gt;&gt;  翻墙工具客户端  &lt;&lt;==&gt;&gt;  翻墙服务器  &lt;&lt;==&gt;&gt;  Tor匿名网络（3重跳转）  &lt;&lt;==&gt;&gt;  目标网站</blockquote><br/>
<br/>
<h2>★方案3：对“端口转发工具”的进程注入（某些情况需要改 hosts）</h2><br/>
　　（注：本文开头部分的“预备知识”已经提到了【端口转发】的概念）<br/>
<br/>
<h3>◇原理</h3><br/>
　　（上一章节提到）由于网络软件的千差万别，对网络软件搞进程注入，经常会出现一些【兼容性问题】。所以，咱们要转换一下思路，不去动网络软件，而在【端口转发】的软件上做文章。因为端口转发工具（比如：rinetd）通常很简单，对其进行注入，出问题的概率要小很多。<br/>
　　而“修改 hosts”是为了进行【域名欺骗】，从而让网络软件把数据流发送【本机】的某个端口，以便咱们实现“端口转发”。由于端口转发工具已经被注入，所以它在转发的那一瞬间，网络流量已经被重定向到指定的代理。<br/>
　　这个方案的原理有点复杂（比较绕），俺举2个例子，帮你理解。<br/>
<br/>
　　<b>例1——邮件客户端</b><br/>
　　假设你用邮件客户端软件来收发 email。并且你有多个邮箱，位于不同的邮件服务器。其中有些邮件服务器已经被 GFW 屏蔽。<br/>
　　如果你对邮件客户端设置了代理，那所有邮箱（包括国内邮箱）的收发都要经过代理，就不爽了。比较爽的方法是——只对【被封锁】的邮件服务器走代理。<br/>
　　为了达到这个效果，你需要进行如下步骤：<br/>
1. 在邮件客户端配置 POP3 和 SMTP 的服务器域名时，【不】要填写真实域名，而是填写本机地址（比如分别填写 <code>127.0.0.1</code> 和 <code>127.0.0.2</code>）。<br/>
2. 使用某个【端口转发工具】（比如：rinetd）在上述两个地址进行监听，端口号还是采用 POP3 和 SMTP 的端口号。并配置2条【转发规则】，分别转发到 POP3 和 SMTP 服务器的【真实地址】的相应端口。<br/>
3. 对“端口转发工具”搞【进程注入】（参见“方案2”）。因此，当 TCP 流量被转发的瞬间，就被自动重定向到翻墙代理<br/>
<br/>
　　<b>例2——系统升级</b><br/>
　　“邮件客户端”的例子比较特殊，因为网络通讯的对象（邮件服务器）是【界面可配置】滴。如果某个网络软件连接的服务器，【没有】相应的配置界面或配置文件，咋办捏？<br/>
　　下面俺举“Windows 系统升级”的例子。在这种情况下，并【没有】界面让你配置微软官方的升级服务器的域名或 IP 地址。这时候咋办捏？<br/>
　　首先，你要研究一下，系统升级软件，访问的是哪个域名的哪个端口？<br/>
　　其次，通过【修改 hosts】的方法，把“升级服务器的域名”指向某个【本机】地址（为了叙述方便，假设用 <code>127.1.2.3</code>）。<br/>
　　接下来的手法就差不多啦——同样对 rinetd 配置转发规则（转发到升级服务器【真实的】IP），同样对 rinetd 进行注入。<br/>
　　【系统级 hosts】在域名查询时具有最高的优先级，因此升级程序会误以为上述的 <code>127.1.2.3</code> 是升级服务器的 IP，并尝试与这个 IP 的监听端口进行通讯，于是数据会被 rinetd 收到并转发。由于 rinetd 已经被进程注入，于是 rinetd 转发数据流的时候，会被重定向到你指定的代理。<br/>
<br/>
<h3>◇优点1——软件级的灵活性</h3><br/>
　　这个优点是相比“方案1”（VPN）而言滴。<br/>
　　此招数只影响某个特定的软件，所以比 VPN 更灵活。<br/>
<br/>
<h3>◇优点2——更好的兼容性</h3><br/>
　　相比方案2（对网络软件的进程注入），这招的兼容性更好，因为这招【不去动】网络软件，注入的对象改为“端口转发工具”。<br/>
<br/>
<h3>◇缺点——适用范围很窄</h3><br/>
　　由于要事先配置好“端口转发”，所以这个招数适用于——只与少数固定的“IP/域名”进行通讯的软件。<br/>
　　如果某个网络软件需要通讯的对端是不确定的（比如 P2P 软件，比如浏览器），就【没法】用这招。<br/>
　　所以说，这个方案的适用范围【很窄】。<br/>
<br/>
<h3>◇软件及配置</h3><br/>
　　<b>系统级 hosts 文件</b><br/>
　　首先，所有知名的桌面操作系统（Windows/Linux/Mac OS/BSD），都可以定制【系统级】hosts 文件。<br/>
<br/>
　　<b>端口转发工具</b><br/>
　　端口转发的工具有很多，俺个人推荐 rinetd。理由包括：<br/>
1. 这个工具很小，很简单（越简单，搞“进程注入”的成功率越高）<br/>
2. 这个工具跨平台（Windows、Linux、UNIX 都可以用）<br/>
3. 这个工具非常老牌，很多系统的软件仓库都已经内置了。<br/>
　　关于 rinetd 的使用，可以参见如下博文：<br/>
《<a href="../../2013/01/cross-host-use-gfw-tool.md">多台电脑如何【共享】翻墙通道——兼谈【端口转发】的几种方法</a>》<br/>
<br/>
　　<b>进程注入工具</b><br/>
　　“方案2”已经介绍了这类工具，此处再重复一遍。<br/>
　　对于 Windows，你可以用 SocksCap 对 rinetd 进行注入；在 POSIX 系统（POSIX 是“Linux/Mac/BSD”的统称），可以用 tsocks 或 proxychains 对 rinetd 进行注入。<br/>
　　有个细节要提醒一下：<br/>
　　（在 POSIX 系统上）由于要对 rinetd 进行注入，所以 rinetd【不】能以常规的 daemon 方式启动；而必须用“注入工具”来启动 rinetd。<br/>
<br/>
<h3>◇如何匿名化？</h3><br/>
　　（这部分与前面的“方案2”相同，略）<br/>
<br/>
<br/>
<h2>★方案4：防火墙转发——本机模式</h2><br/>
　　前面介绍的几个招数，都有一些严重缺陷，令人不爽：<br/>
<blockquote>方案1：VPN——不够灵活<br/>
方案2：对网络软件的进程注入——兼容性差<br/>
方案3：hosts + 端口转发——只适用于“通讯对端比较固定”的网络软件</blockquote>　　<b>下面要介绍的是【终极大杀器】，可以解决前面所有弊端</b>，那就是——<br/>
“防火墙”转发给“透明代理”（Transparent Proxy），然后“透明代理”再转给真实代理（比如 Tor）。<br/>
　　使用这个方案，网络软件完全感觉不到代理的存在。从这个角度而言，它有点像 VPN。但是它与 VPN 又不太一样，因为这个方案可以对同一个系统的不同网络行为作【细颗粒度】的区分，使得某些数据走代理，另一些数据则直连。<br/>
<br/>
<h3>◇原理</h3><br/>
　　这个方案的关键在于操作系统内置的【主机防火墙】。<br/>
　　如今的几大桌面系统（Windows、Linux、Mac OS、BSD），都自带了【内核级】的防火墙，下面俺以 Linux 自带的 iptables 来说事儿。<br/>
　　iptables 功能非常强，而且具备高度的可定制性。你可以定制 iptables 的规则，使得符合某些条件的数据包，被重定向到本机的某个指定端口。<br/>
　　然后，你用某个特定的软件充当【透明代理】，对这个端口进行监听，于是这个透明代理就可以截获这些被重定向的数据包，然后透明代理再把这些数据包转发给咱们真正需要的代理（比如 Tor）。<br/>
　　iptables 可以针对不同条件进行重定向，俺举几个例子：<br/>
针对“端口”的范围（只有当“源端口”或“目的端口”符合某些条件，才进行重定向）<br/>
针对“IP地址”的范围（只有当“源IP”或“目的IP”符合某些条件，才进行重定向）<br/>
针对“用户”（只对特定用户产生的数据包，才进行重定向）<br/>
针对“网卡”（只有某个网卡的数据包，才进行重定向）<br/>
......<br/>
<br/>
　　刚才是拿 Linux 内核自带的 iptables 说事儿。<br/>
　　熟悉 OpenBSD 的同学，可以研究其自带的 pf 防火墙；熟悉 FreeBSD 的同学，可以研究其自带的 ipf 防火墙；看看这2款 BSD 系统是否也可以这么玩（俺自己没亲自试过，不保证）。<br/>
　　Windows 自带的防火墙是否能做到类似效果捏？貌似不支持。<br/>
　　（注：多年不用 Windows 了，写本文时，还特地开了个 Windows 虚拟机，简单看了一下内置防火墙的配置，好像没有这种功能）<br/>
<br/>
<h3>◇优点1——足够灵活</h3><br/>
　　在本文介绍的所有方案中，这个方案的灵活性是最好的。<br/>
　　前面提到：方案2（对网络软件的进程注入）的灵活性非常好，能做到【进程级】的灵活性。而方案4的灵活性甚至超过方案2，因为它能实现【数据包级】的灵活性。<br/>
<br/>
<h3>◇优点2——足够好的兼容性和稳定性</h3><br/>
　　由于这个方案依赖的是【内核级】的主机防火墙，它处在操作系统的底层。因此【不】会受到软件的影响。<br/>
　　另外，这个方案【不】需要搞“进程注入”，也【不】影响网络软件的稳定性。<br/>
<br/>
<h3>◇优点3——不受“更换软件”的影响</h3><br/>
　　由于防火墙规则针对的是数据包的属性（比如：IP、端口）以及操作系统相关的属性（比如：用户组），与网络软件本身没啥关系。<br/>
　　也就是说，你一旦设定好相关的规则，即使你换了不同的网络软件，这些防火墙规则依然有效（不用再改）<br/>
<br/>
<h3>◇缺点——配置的门槛偏高</h3><br/>
　　“门槛偏高”体现在——你必须足够熟悉操作系统自带的防火墙，懂得如何设定规则，以便对特定的数据包进行【重定向】。<br/>
<br/>
<h3>◇缺点——Windows 的【可行性】，俺还不确定</h3><br/>
　　关于这点，下面的某个小节会提到。<br/>
<br/>
<h3>◇软件及配置</h3><br/>
　　完成该方案需要三样东西：<br/>
1. 防火墙和相关规则<br/>
2. 透明代理<br/>
3. 实际的代理（比如 Tor）<br/>
　　重点说说前面两样。<br/>
<br/>
　　<b>防火墙的配置</b><br/>
　　（下面以 Linux 下的 iptables 举例）<br/>
　　考虑到本文只是提供思路和方法论，对 iptables 的配置，俺只提几个注意事项。具体的命令，请自行查阅手册。<br/>
　　【注意事项1】<br/>
　　iptables 默认的 table 是 <code>filter</code>，大部分使用 iptables 的同学，都是针对 <code>filter</code> 进行配置。<br/>
　　但本文要聊的【数据包重定向】，必须在【<code>nat</code>】这个 table 上进行配置。<br/>
　　【注意事项2】<br/>
　　对于“本机模式”的防火墙转发，你需要重定向的是【本机软件】产生的数据包，所以你要在【<code>OUTPUT</code>】这个 chain 中追加规则。<br/>
　　【注意事项3】<br/>
　　你需要用到 <code>-j REDIRECT</code> 选项和 <code>--to-ports 端口号</code> 选项（此处的“端口号”就是透明代理的监听端口号）<br/>
　　【注意事项4】<br/>
　　如果“透明代理”位于【另一个系统】，上述 iptables 的选项要略做修改。<br/>
把 <code>-j REDIRECT</code> 改为 <code>-j DNAT</code>（REDIRECT 与 DNAT 的差异，参见“<a href="http://gsoc-blog.ecklm.com/iptables-redirect-vs.-dnat-vs.-tproxy/" rel="nofollow" target="_blank">这篇洋文</a>”）<br/>
把 <code>--to-ports 端口</code> 改为 <code>--to 地址:端口</code>（此处的“地址”就是“透明代理”所在的另一个系统的地址）<br/>
<br/>
　　<b>透明代理的配置</b><br/>
　　对于 POSIX 系统（Linux/Mac OS/BSD），俺推荐的是 redsocks 这个工具（官网在“<a href="http://darkk.net.ru/redsocks/" rel="nofollow" target="_blank">这里</a>”，官方代码仓库在“<a href="https://github.com/darkk/redsocks/" rel="nofollow" target="_blank">这里</a>”）。<br/>
　　它的名气大（主流的 Linux 发行版，软件仓库都已经内置），支持的代理种类也齐全——可以把收到的数据包转发给各种代理（各种 SOCKS 代理，各种 HTTP 代理）。<br/>
　　redsocks 本身的配置还算简单。安装好之后，直接修改 <code>/etc/redsocks.conf</code> 这个配置文件。而且配置文件中已经写了相当多注释，很容易看懂。<br/>
　　关于 redsocks，也说几个注意事项。<br/>
　　【注意事项1】<br/>
　　对于“本机模式”，redsocks 监听端口可以绑定到 <code>127.0.0.1</code>，也可以绑定到 <code>0.0.0.0</code>，但【不要】绑定到网卡的 IP 地址。<br/>
　　【注意事项2】<br/>
　　如果你要转发的“实际代理”是“HTTP 代理”，要区分不同类型（参见本文开头的<q>预备知识</q>章节）。<br/>
　　在 redsocks 配置文件中，用 <code>http-connect</code> 表示“HTTP 隧道”，用 <code>http-relay</code> 表示“HTTP 转发”。<br/>
　　【注意事项3】<br/>
　　redsocks 每次接收到数据会记录日志（你可以在它的配置文件中指定日志文件的位置）<br/>
　　在转发失败（数据不通）的情况下，先去看 redsocks 的日志。如果 redsocks 的日志没有东西，通常说明你的防火墙规则配置错误（所以 redsocks 没收到数据）。如果 redsocks 记录了日志，你可以根据日志判断——是否在转发给“实际代理”时出了问题。<br/>
<br/>
<h3>◇Windows 系统的可行性还【不确定】</h3><br/>
　　这个方案能否用于 Windows 系统，俺【不】清楚。至少有两个地方存在不确定性：<br/>
1. Windows 自带的防火墙是否能做到类似的【重定向】效果<br/>
2. Windows 上是否有类似 redsocks 这样的软件（可以充当【透明代理】，并把数据转发到其它代理）<br/>
　　如果读者中有人知道这两个问题的答案，欢迎到博客上留言。先行谢过。<br/>
<br/>
<h3>◇关于 DNS 的转发</h3><br/>
　　redsocks 本身支持 DNS 的转发，具体参见它的配置文件中的【redudp】和【dnstc】这两个部分。<br/>
　　由于传统的 DNS 协议是【UDP】，所以，一定要基于【SOCKS5 代理】才能进行转发（“SOCK4 代理”不行，“HTTP 代理”也不行）。<br/>
　　如果你手头只有其它代理，偏偏缺少 SOCK5 代理，咋办捏？<br/>
　　你可以在本地开启【DNS proxy】。这种 proxy 把自己伪装成一个 DNS server，然后把收到的 DNS 查询请求转发给真正的 DNS server。<br/>
　　但是 DNS proxy 把 DNS 请求转发出去，还是要走 UDP 协议，还是得依靠 SOCKS5 代理。所以你必须使用一种特殊的 DNS proxy——可以把“传统 DNS”转成“DNS over HTTPS”。“DNS over HTTPS”简称 DoH，具体介绍请看<a href="../../2018/10/Comparison-of-DNS-Protocols.md">这篇博文</a>。由于 DoH 包裹在 HTTPS 流量中，自然可以用各种代理（SOCKS or HTTP）进行转发。<br/>
　　Facebook 开源了一个【DoH proxy】（基于 python 开发，代码仓库在“<a href="https://github.com/facebookexperimental/doh-proxy" rel="nofollow" target="_blank">这里</a>”），就可以实现上述效果。感兴趣的同学可以去体验一下。<br/>
<br/>
<h3>◇如何匿名化？</h3><br/>
　　（下面以 redsocks 为例）<br/>
<br/>
　　如果 redsocks 把数据转发给普通的翻墙代理，数据流的示意图如下：<br/>
<blockquote>网络软件  &lt;&lt;==(内核防火墙转发)==&gt;&gt;  redsocks  &lt;&lt;==&gt;&gt;  翻墙工具客户端  &lt;&lt;==&gt;&gt;  翻墙服务器  &lt;&lt;==&gt;&gt;  目标网站</blockquote><br/>
　　让 redsocks 把数据转发给本机的 Tor，就可以实现匿名化。数据流的示意图如下（逆向追溯已经非常难）<br/>
<blockquote>网络软件  &lt;&lt;==(内核防火墙转发)==&gt;&gt;  redsocks  &lt;&lt;==&gt;&gt;  Tor客户端  &lt;&lt;==&gt;&gt;  Tor匿名网络（3重跳转）  &lt;&lt;==&gt;&gt;  目标网站</blockquote><br/>
　　如果你采用俺常年唠叨的【基于 TOR 的双重代理】，让某个翻墙工具作为 Tor 的【前置代理】，则数据流变得更加复杂（逆向追溯【更加不可能】）：<br/>
<blockquote>网络软件  &lt;&lt;==(内核防火墙转发)==&gt;&gt;  redsocks  &lt;&lt;==&gt;&gt;  Tor客户端  &lt;&lt;==&gt;&gt;  翻墙工具客户端  &lt;&lt;==&gt;&gt;  翻墙服务器  &lt;&lt;==&gt;&gt;  Tor匿名网络（3重跳转）  &lt;&lt;==&gt;&gt;  目标网站</blockquote><br/>
<br/>
<h2>★方案5：防火墙转发——网关模式</h2><br/>
　　接下来聊“防火墙转发”的另一个模式——网关模式。<br/>
<br/>
<h3>◇原理</h3><br/>
　　对于“网关模式”，你需要【N + 1 个】主机——其中的 N 个主机充当【隔离主机】，还有一个充当【网关主机】。<br/>
　　（注：本章节所说的“主机”，可以是“物理主机”，也可以是“虚拟机/VM”。关于“虚拟机”，俺写了<a href="../../2012/10/system-vm-0.md">扫盲的系列教程</a>）<br/>
　　<b>对于【网关主机】</b><br/>
　　“方案4”提到的那三样东西（防火墙规则，透明代理，实际代理），都在【网关】主机上进行配置。<br/>
　　充当【网关】的主机可以是【双】网卡，也可以是【单】网卡（到底用哪种，视具体情况而定）。<br/>
　　<b>对于【隔离主机】</b><br/>
　　只需要在网卡中设置【默认网关】，“默认网关”的地址就填写“网关主机的网卡地址”。如果网关主机是【双】网卡，注意别填错喽。<br/>
<br/>
<h3>◇相比“方案4”的优点——支持任何操作系统</h3><br/>
　　前面俺提到：“本机模式的防火墙转发”（方案4），只能用于【桌面的】POSIX 系统，Windows 上有可能搞不定，移动设备更加搞不定。<br/>
　　而如果你用了“网关模式的防火墙转发”（方案5），只有“网关主机”需要是 POSIX，“隔离主机”可以是任何系统（甚至可以是移动设备）。<br/>
<br/>
<h3>◇相比“方案4”的优点——降低了配置的工作量</h3><br/>
　　假设你有好几个操作系统，都需要搞“防火墙转发”。如果用“本机模式”，每个系统都要配置；如果用“网关模式”，只需要对“网关主机”配置【一次】，其它几个系统作为“隔离主机”，除了设一下“默认网关”，【不用】再进行别的设置。<br/>
<br/>
<h3>◇其它优点</h3><br/>
　　（参见“方案4”，略）<br/>
<br/>
<h3>◇缺点——配置的门槛偏高</h3><br/>
　　（参见“方案4”，略）<br/>
<br/>
<h3>◇软件及配置</h3><br/>
　　本方案与“方案4”大致相同，只不过多了一个主机作【网关】。然后你把 redsocks 和代理软件（比如 Tor）部署到【网关】上，防火墙规则也在【网关】上设置。<br/>
　　由于部署方式变成【跨主机】，防火墙规则需要适当改动。说几个注意事项（以 iptables 为例）<br/>
　　【注意事项1】<br/>
　　对于“方案4”（本机模式），你要转发的数据包来自【本机】的软件，你的转发规则必须添加到【<code>OUTPUT</code>】这个 chain 中。<br/>
　　对于“方案5”（网关模式），你要转发的数据包来自【另一个主机】，你的转发规则必须添加到【<code>PREROUTING</code>】这个 chain 中。<br/>
　　下面这张图有助于让你理解 iptables 中不同的 chain 的拓扑关系。<br/>
　　<center><img alt="不见图 请翻墙" src="images/iLg0ODd4X9298Us6KVz15OLn0y-4CFZeXq4qYuuAPzf-OtaJW9DJNjoyzrGMTQBJN-KGXBOTYqlewqHyxjte3Xisp6w_7sa5ecdMxIZBRwnDWxs9vBBe7VMIOHaw0RXTDJF6ZAnfSgM"/></center><br/>
　　关于 redsocks，也说几个注意事项。<br/>
　　【注意事项1】<br/>
　　前面提到：“本机模式”，redsocks 监听端口可以绑定到 <code>127.0.0.1</code>，也可以绑定到 <code>0.0.0.0</code>，但【不要】绑定到网卡的 IP 地址。<br/>
　　而对于“网关模式”，redsocks 监听端口可以绑定到“网卡地址”，也可以绑定到 <code>0.0.0.0</code>，但【不要】绑定到 <code>127.0.0.1</code>。（请注意上述两者，有点差别）<br/>
　　【注意事项2】<br/>
　　如果你想【混用】这两种模式（既作为网关，转发别的主机的数据包到透明代理；同时又转发本机软件的数据包到透明代理）。那么 iptables 既要设置【<code>OUTPUT</code>】这个 chain，也要设置【<code>PREROUTING</code>】这个 chain。此时，redsocks 的监听端口【必须】绑定到 <code>0.0.0.0</code> 才能“鱼和熊掌兼得” :)<br/>
<br/>
<h3>◇DNS 的两种玩法</h3><br/>
　　使用“网关模式”，DNS 有两种玩法：<br/>
<br/>
　　<b>方法1</b><br/>
　　类似“方案4”，通过配置网关的防火墙规则，使得所有“隔离主机”的 DNS 数据包被转向 redsocks 的 UDP 端口。<br/>
<br/>
　　<b>方法2</b><br/>
　　你也可以让“网关主机”充当 DNS server，然后在“隔离主机”中配置 DNS，指向“网关主机”。如此一来，所有“隔离主机”的 DNS 请求都由“网关主机”完成，然后“网关主机”采用【DNS proxy】的技巧（具体参见前一个章节的<q>关于 DNS 的转发</q>）。<br/>
<br/>
　　以上两种方法，都可以确保你的所有主机的所有 DNS 请求通过自己指定的代理，而你只需在网关一个地方进行配置。<br/>
<br/>
<h3>◇如何匿名化？</h3><br/>
　　（参见“方案4”，略）<br/>
<br/>
<h3>◇网关模式下，Tor 如何部署？</h3><br/>
　　对于特别注重隐匿性的同学，肯定希望让每个“隔离主机”都用上【匿名网络】（比如 Tor）。这时候就涉及到——“Tor 如何部署”这个问题。<br/>
　　关于这个话题，可能很多人会觉得——把 Tor 和 Tor 的前置代理都放到“网关主机”。<br/>
　　这么干，配置会比较简单。但俺认为这种部署方式【不好】！<br/>
　　因为这样部署，你的 N 个“隔离主机”会共用同一个 Tor 环境。这样有啥风险捏？具体解释请参见《<a href="../../2019/01/Security-Guide-for-Political-Activists.md">为啥朝廷总抓不到俺——十年反党活动的安全经验汇总</a>》一文中的 <q>★【网络】层面的防范</q> 这个章节。<br/>
　　所以，更好的部署是：【每个隔离主机】都有自己的 Tor 客户端，“网关主机”只部署“透明代理”和“Tor 的前置代理”。如此一来，每个隔离主机都有【各自独立】的 Tor 环境。<br/>
<br/>
<br/>
<h2>★结尾</h2><br/>
　　今天聊的只是俺个人经验，未必全面。<br/>
　　如果你有其它技巧，欢迎在俺博客留言，分享给大伙儿 :)<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2013/01/cross-host-use-gfw-tool.md">多台电脑如何【共享】翻墙通道——兼谈【端口转发】的几种方法</a>》<br/>
《<a href="../../2014/12/gfw-privoxy.md">如何用 Privoxy 辅助翻墙？</a>》<br/>
《<a href="../../2019/11/POSIX-TUI-from-TTY-to-Shell-Programming.md">扫盲 Linux＆UNIX 命令行——从“电传打字机”聊到“shell 脚本编程”</a>》<br/>
《<a href="../../2018/10/Comparison-of-DNS-Protocols.md">对比4种强化域名安全的协议——DNSSEC，DNSCrypt，DNS over TLS，DNS over HTTPS</a>》<br/>
《<a href="../../2019/01/Security-Guide-for-Political-Activists.md">为啥朝廷总抓不到俺——十年反党活动的安全经验汇总</a>》<br/>
《<a href="../../2010/04/howto-cover-your-tracks-0.md">如何隐藏你的踪迹，避免跨省追捕</a>》（系列）<br/>
《<a href="../../2013/11/tor-faq.md">“如何翻墙”系列：关于 Tor 的常见问题解答</a>》<br/>
《<a href="../../2018/04/gfw-tor-browser-7.5-meek.md">“如何翻墙”系列：扫盲 Tor Browser 7.5——关于 meek 插件的配置、优化、原理</a>》<br/>
《<a href="../../2015/03/Tor-Arm.md">扫盲 Arm——Tor 的界面前端（替代已死亡的 Vidalia）</a>》<br/>
《<a href="../../2012/10/system-vm-0.md">扫盲操作系统虚拟机</a>》（系列）
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2019/04/Proxy-Tricks.html
