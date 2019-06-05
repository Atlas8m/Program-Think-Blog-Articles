# “如何翻墙”系列：戴“套”翻墻的方法 

-----

<div class="post-body entry-content">
<h2>★TOR 与 GFW 对抗的几个阶段</h2><br/>
　　1.<br/>
　　本文最早写于党国的六十大寿临近之际。当时 GFW 发飚，很多翻墙工具纷纷落马。只有 TOR 还比较坚挺，依靠网桥模式，突破封锁。所以当时俺写了此文，顺便普及了一把网桥中继的知识。<br/>
　　2.<br/>
　　后来，网桥中继的模式已经不灵光了（大部分中继都被 GFW 封杀了）。<br/>
　　3.<br/>
　　所以，俺把本文的后半部分重写了，介绍了一种新的方法——利用互联网上的公共代理，让 TOR 复活。<br/>
　　4.<br/>
　　再后来，用公共代理的方式，也不灵了（很难找到合适的公共代理，估计也是因为 GFW 的屏蔽）<br/>
　　5.<br/>
　　2014年10月，TOR 官方推出了基于 meek 的插件，TOR 又复活了（具体配置参见《<a href="../../2014/10/gfw-tor-meek.md">TOR 已复活——meek 流量混淆插件的安装、优化、原理</a>》）<br/>
<br/>
　　另外，俺在2013年补充了一篇《<a href="https://program-think.blogspot.ro/2013/11/tor-faq.html">关于 TOR 的常见问题解答</a>》，有兴趣的同学也可以参考。<a name="more"></a><br/>
<br/>
<br/>
<h2>★如何获取 TOR 软件包</h2><br/>
　　先说明一下：本文提及的 TOR，是指包含了“TOR、vidalia、polipo、Firefox”的套装软件包。此软件包很牛很强大，非常适合傻瓜用户。<br/>
　　另外，考虑到本文的大多数读者是一些非IT专业的电脑用户，俺尽量用通俗的大白话且讲得比较啰嗦，请那些懂行的同学不要嫌烦。不懂行的同学，一定要耐心看完全文哦！<br/>
<br/>
<h3>◇方法1：通过 Web 网页代理获取</h3><br/>
　　通过<b>加密</b>的 Web 网页代理，访问 TOR 的官方站点（在“<a href="https://www.torproject.org/" rel="nofollow" target="_blank">这里</a>”），下载最新的软件包。记住，一定要用<b>加密的</b>（也就是 <b>HTTPS</b> 协议）网页代理。<br/>
　　这个方法的缺点是：在非常时期，可能很难找到好用的加密 Web 网页代理。<br/>
<br/>
<h3>◇方法2：通过邮件获取</h3><br/>
　　这个方式在封锁加剧的时期，比较合适。除非我党把所有国外的 Email 提供商都和谐掉，否则咱们总是有机可趁。具体操作如下：<br/>
　　发送主题为“help”的<span style="color:red;">纯文本</span>邮件到<b><a href="mailto:gettor@torproject.org" target="_blank">gettor@torproject.org</a></b>，收到回复后根据邮件的提示再回复一次，即可在你的邮箱中收取 TOR 的软件包。记得要用 <span style="color:red;">HTTPS</span> 方式上<b> Gmail</b>，以确保最佳效果。切记要用<b>纯文本</b>的邮件格式。<br/>
<br/>
<br/>
<h2>★如何用 TOR 上网（访问 Web）</h2><br/>
　　先介绍一下 TOR 的基本用法。那些已经安装了 TOR 还是上不了网的同学，直接看后面的一节：<b>如何使用网桥中继</b>。<br/>
　　事先声明：考虑到大多数网民都在用 Windows，下面以 Windows 系统的 TOR 来作介绍。使用苹果系统或利牛克斯系统的用户，不要怪俺歧视哦 :)<br/>
<br/>
<h3>◇步骤1（解压缩软件包）</h3><br/>
　　首先，把 TOR 软件包解压缩到某个目录下。<br/>
　　如果你连“解压缩”也不会，那你不需要再看这个帖子了，先去普及完电脑使用常识再回来学翻墙。<br/>
<br/>
<h3>◇步骤2（启动TOR）</h3><br/>
　　在上述目录下有一个名叫“Start Tor Browser.exe”的程序，双击启动之。然后，会跳出一个“Vidalia Control Panel”的窗口。<br/>
<center><img alt="不见图 请翻墙" src="images/ViCha45zPwh79e4Bom2epEQBR7Y-11jAQ5Kzu_7x4CwLhWG8Iu0PMwMrR1RMaZ5Z7L5DGHzphvy12Ol7h48dfZdpm1OfixB-cksDFoStacSv8cd_tFrNdXHdTn-Z700pqjODLLZe"/></center><br/>
　　假如你不喜欢/不习惯洋文的界面，可以点控制面板中的“Settings”按钮，进入到“Apperance”标签页，选择你喜欢的语言（比如中文）。<br/>
<center><img alt="不见图 请翻墙" src="images/4tKTw4FSUJOyZhUWMoWGtELaVb69qSFayai64zmueVCbl5KD7_mubMkGfDNjUjf7wbjOygnkiDu6q2DJDYwFdi3pLGyJngisxwjWS3AJp5bD1y6HC_KbGovDyq7pnTAjR8w8DNrm"/></center><br/>
　　设置好之后，控制面板立马变为中文的，效果如下图所示：<br/>
<center><img alt="不见图 请翻墙" src="images/I3p7KryEc9q9kC5KfPZAj3cgrN46GuJHZLYQ0FC9whzele9Wq3dr3gtb4NphB0knfyZNJoZMBBv5D0oapiVS9xAZN-lrV_cCzG0QRBjzCWwaQWfPfNkibsmLs_YNeomfTsVNhTYO"/></center><br/>
<h3>◇步骤3（启动内置浏览器）</h3><br/>
　　如果能够正常连接到互联网，则该程序会自动运行内置的一个 Firefox 浏览器。如果这个内置浏览器直接能访问被墙的网站，那恭喜你，翻墙成功啦！<br/>
　　但是别高兴得太早。从2010年之后，在天朝之内运行 TOR 是很难直接联网的。因为 TOR 的目录服务器和大部分的网桥中继都被 GFW 封掉了。在本文的后续章节，会告诉你如何应对。<br/>
<br/>
<h3>◇步骤4（如何用自个儿的浏览器）</h3><br/>
　　有很多网友不喜欢它内置的 Firefox，想用自己的浏览器翻墙，也没有关系。直接在你自个的浏览器中设置 <b>HTTP代理</b>。代理的地址设置为：127.0.0.1；代理的端口设置为：8118 即可。<br/>
　　大约从2013年开始，<b>TOR 官网提供的 Vidalia 套件默认不提供 HTTP 代理了，但仍然提供 SOCKS 代理</b>。你可以在自个儿的浏览器中设置 <b>SOCKS代理</b>，代理的地址设置为：127.0.0.1；代理的端口设置为：9050 或 9150<br/>
（<b>补充说明：2.3.25 版本之后的 TOR 软件包，端口号有变化。对于 Browser Bundle，SOCKS 端口号变为 9150，对于其它的 Bundle 依然使用 9050</b>）<br/>
<br/>
　　Firefox 的代理设置如下图（至于 Chrome、IE、或其它浏览器，列位看官请依样画葫芦）：<br/>
<center><img alt="不见图 请翻墙" src="images/chrmCSXntveQ-Ht6JWGJVUfxBx2N-Qs_TVxXo5bkYTju8kH8ZTaulunqAc7Ao_Tz9EdbGeH4igsgmbobNl0h2IQ_JYNf9Gll-jeNdZ76iagxp9rTtSaeW46R71WcMAHk70gONPTz"/></center><br/>
　　如果你嫌那个内置的 Firefox 碍手碍脚，想把它去掉，可以修改 TOR 软件包的配置文件。该文件在 TOR 所在目录下的 <b>Data\Vidalia\vidalia.conf</b><br/>
<br/>
把里面如下的配置项<br/>
<blockquote style="background-color:#DDD;">BrowserDirectory=FirefoxPortable<br/>
BrowserExecutable=tbb-firefox.exe</blockquote>修改为<br/>
<blockquote style="background-color:#DDD;">BrowserDirectory=<br/>
BrowserExecutable=</blockquote><br/>
<br/>
<h2>★如何用 TOR 访问非 Web 应用</h2><br/>
　　TOR 除了可以帮助你访问 Web 页面，还可以干更多事情。<br/>
　　因为 TOR 既可以当 HTTP 代理，也可以当 <b>SOCKS代理</b>，具体的配置是本机（IP 地址127.0.0.1）的 9050 或 9150 端口（<b>补充说明：对于 2.3.25 之后的 TOR Browser Bundle，SOCKS 端口号修改为 9150，其它的 Bundle 依然使用 9050</b>）。凡是支持 SOCKS 代理的网络应用程序（比如：QQ、MSN Messener），都可以通过 TOR 的 SOCKS 代理来联网。<br/>
　　顺便提醒一个小细节：TOR 的 9051 端口，是控制端口，别跟 SOCKS 端口搞混了。<br/>
<br/>
<h2>★<del>通过网桥中继让 TOR 复活</del></h2><br/>
　　<b>从2010年开始，GFW 逐步地封杀 TOR 的网桥中继。如今，大部分网桥中继都已经被 GFW 屏蔽掉了。用“网桥中继”来复活 TOR，已经很难成功了。所以，请跳过本章节的内容，直接看下一节。</b><br/>
<br/>
<h2>★通过双重代理让 TOR 复活</h2><br/>
　　所谓的“双重代理”就是——用其它翻墙工具（可以是翻墙代理，也可以是翻墙 VPN）组合 TOR。如此一来，TOR 就可以用其它翻墙工具的通道进行联网，实现复活。具体的配置方式请看《<a href="../../2012/03/howto-cover-your-tracks-5.md">如何隐藏你的踪迹，避免跨省追捕[5]：用多重代理隐匿公网IP</a>》。<br/>
　　可能有的同学会问，既然已经有其它翻墙工具可用，为啥还要用 TOR 来搞双重代理？这么干的原因在于：双重代理可以提高很好的隐匿性。具体的好处请参见《<a href="https://program-think.blogspot.ro/2013/11/tor-faq.html">关于 TOR 的常见问题解答</a>》，这里就不再罗嗦。<br/>
<br/>
<br/>
<h2>★通过公共代理让 TOR 复活</h2><br/>
<h3>◇什么是公共代理？</h3><br/>
　　公共代理，全称是“公共的代理服务器”。这是互联网上的一些好心人架设的代理服务器。所谓“公共”，就是说任何人都能使用这些代理，无需额外费用。<br/>
　　常见的公共代理有如下类型：SOCKS 和 HTTP。其中，SOCKS 代理又细分为两种：SOCKS4 和 SOCKS5（SOCKS5 比 SOCKS4 高级）。<br/>
　　从协议的层次而言，SOCKS 代理位于网络的第5层（OSI模型的会话层），而 HTTP 代理位于网络的第7层（OSI模型的应用层）。从协议的角度来说，SOCKS 代理的性能会高于 HTTP 代理。<br/>
<br/>
<h3>◇如何找到公共代理？</h3><br/>
　　其实俺手头有几个能用的 SOCKS 公共代理。但是捏，因为朝廷的爪牙们也在关注俺博客。如果把这几个 SOCKS 代理公布出来，不出几天就会被封掉。而且俺信奉“授人以鱼不如授人以渔”。所以捏，就多费点口水，介绍一下公共代理的获取方式。<br/>
　　要找到公共代理，简而言之，就是用 Google 搜！<br/>
　　互联网上有成千上万的免费代理可以使用。而且有很多专门的代理网站。这些网站会帮你收集汇总速度快的，运行稳定的代理服务器。有些网站还能做到每日更新。<br/>
　　所以，你只需要通过 Google 搜索 <b>SOCKS proxy</b> 或搜索 <b>HTTP proxy</b>，就能找到很多的代理网站。<br/>
　　找到代理网站之后，上面往往列出几十个代理，该用哪个捏？<br/>
<b>首先，不要选天朝之内的代理</b><br/>
因为咱们找代理是为了翻墙。你找一个墙内的代理，那属于白忙活。<br/>
<b>其次，选一个速度快的</b><br/>
很多代理网站做得很人性化，它们会列出每一个代理服务器的延时。延时越小，说明速度越快。<br/>
<b>最后，测试连通性</b><br/>
公共代理也是 GFW 封杀的目标。你在代理网站上找到的公共代理，其中有些没准已经被封了。<br/>
那么，如何判断某个代理是否还能用？很简单，用操作系统自带的 ping 命令测试一下。假如你找到的代理，IP 是 1.2.3.4 那么你可以用如下命令测试。<br/>
<blockquote style="background-color:#DDD;">ping 1.2.3.4</blockquote>如果显示超时 <q style="background-color:#DDD;">Request time out</q> 说明这个代理很可能被 GFW 封了——那你就只好再选另一个代理了；如果显示 <q style="background-color:#DDD;">reply from 1.2.3.4</q> 那就说明这个代理可用。<br/>
对于熟悉IT技术的网友，也可以用操作系统自带的 telnet 命令，直接测试代理的端口是否能连得上。telnet 命令比 ping 命令更准确，可惜的是，Win7 默认不带此命令 :(<br/>
<br/>
　　<b>为啥有的公共代理，TOR没法用？</b><br/>
　　因为有好几个网友询问此类问题，俺再补充一下。互联网上的公共代理服务器有好多种，支持的协议也不同。对 TOR 的客户端而言，公共代理服务器需要支持 HTTPS 协议或者 SOCKS 协议，TOR 客户端才能联网。<br/>
<br/>
<h3>◇如何设置？</h3><br/>
　　到“Vidalia 控制面板”中，点击“设定”按钮；进入“网络”标签页；在里面勾选“我使用代理服务器连接到网络”。如下图所示：<br/>
<center><img alt="不见图 请翻墙" src="images/_8-IJG3K9KUOLXo0sVZHEiB3Adsfn-O56fbGJ1SmSiBYsJD_hWscu0Cajb0vUEeaJ-ayAyHy340LTeRQbrH8R2j22eA4y4P0gtvK1YKXdg5-3uQLEO2qK-9YnxBt-WCFisUmKbFY"/></center><br/>
　　勾选之后，会出现如下界面；把你找来的公共代理的“地址”、“端口”、“类型”设置好。提醒一下，<b>代理的类型别选错了</b>！<br/>
<center><img alt="不见图 请翻墙" src="images/up_Bce_3-KA_5fBGIsnaIfNKh_66qWkwguqnBXF8UuSD1Ct0-QyQXmifaEYxCxb3UdQ8SiUIeyuKcMKy6cIkv1Q5iVrZvvi12-l0ouxXERpxnl8ERpxcKCmXd1BNkH39f9sP-NRd"/></center><br/>
　　完成上述步骤之后，重启一下 TOR 并稍等片刻，洋葱头应该就变绿了。<br/>
<br/>
<br/>
<h2>★通过 meek 插件让 TOR 复活</h2><br/>
　　这是2014年才出现的新招数，<b>由 TOR 官方提供</b>。<br/>
　　该招数的具体教程，请参见《<a href="../../2014/10/gfw-tor-meek.md">TOR 已复活——meek 流量混淆插件的安装、优化、原理</a>》。<br/>
<br/>
<br/>
<h2>★俺的联系方式</h2><br/>
　　如果碰到翻墙的问题，或者想给俺提意见/建议，欢迎来信（ <u>program.think@gmail.com</u>）。<b>给俺写信最好用 Gmail 或 Hotmail，国内的邮箱很可能会被墙，导致俺收不到。</b><br/>
　　最后，希望大家都能够传播翻墙姿势，帮助周围的人重新呼吸到互联网上自由的空气！！！<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
<a href="../../2014/10/gfw-tor-meek.md">TOR 已复活——meek 流量混淆插件的安装、优化、原理</a><br/>
<a href="https://program-think.blogspot.ro/2013/11/tor-faq.html">关于 TOR 的常见问题解答</a><br/>
<a href="../../2009/05/how-to-break-through-gfw.md">如何翻墙</a>（传说中的扫盲教程，定期更新）<br/>
<a href="../../2011/03/how-to-get-gfw-tools.md">获取翻墙软件方法大全</a>（教你在无法翻墙的情况下拿到翻墙软件）<br/>
<a href="../../2013/04/gfw-vpngate.md">扫盲 VPN Gate——分布式的 VPN 服务器</a><br/>
<a href="../../2011/10/gfw-psiphon.md">双管齐下的赛风3</a><br/>
<a href="../../2011/12/gfw-wujie.md">新版本无界——赛风3失效后的另一个选择</a><br/>
<a href="../../2010/03/choose-free-gate.md">自由門——TOR 被封之后的另一个选择</a><br/>
<a href="../../2011/09/gfw-vpn-hotspot-shield.md">扫盲 VPN 翻墙——以 Hotspot Shield 为例</a><br/>
<a href="../../2012/06/gfw-i2p.md">简单扫盲 I2P 的使用</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2009/09/break-through-gfw-with-tor.html
