# 如何隐藏你的踪迹，避免跨省追捕[5]：用多重代理隐匿公网 IP 

-----

<div class="post-body entry-content">
　　最近，天朝的两会即将通过新版本的刑事诉讼法（在新条款中，党国的爪牙可以【<b>合法地</b>】进行秘密拘捕——太阴险啦，良心大大滴坏！）。所以，俺要继续完善<a href="../../2010/04/howto-cover-your-tracks-0.md">“如何隐藏踪迹”系列</a>，帮助大伙儿躲避朝廷的网络追捕。<br/>
　　关于多重代理，在前几个月的翻墙贴《<a href="../../2011/09/gfw-vpn-hotspot-shield.md">扫盲 VPN 翻墙——以 Hotspot Shield 为例</a>》中，稍微提到过。今天来完整地介绍一下。<br/>
<a name="more"></a><br/>
<br/>
<h2>★什么是多重代理？</h2><br/>
　　先声明一下：本文所说的“代理”是广义的，包括了：“传统意义上的代理”与“VPN”。<br/>
　　平时咱们用代理来翻墙，大部分属于一重代理（如下图）。也就是说，不论你用的是 VPN 还是 HTTP Proxy 还是 SOCKS Proxy，当中都只有【一个】服务器进行中转。<br/>
<center><img alt="不见图 请翻墙" src="images/Rgn4KkxdyjmPB38AzrpvSsbN4fipGKcQ1H0ZuoerIncEbSCABXF23FGZ5xY2qw4RZ24dQv0Dq3gqGnn-pMNXbfb4AyXV1sOht7JCc6Q8hqatkUwaSg"/></center><br/>
　　单重代理可以（在一定程度上）保护你的隐私，防范跨省追捕。关于这点，俺在《<a href="../../2010/04/howto-cover-your-tracks-1.md">如何隐藏你的踪迹，避免跨省追捕[1]：网络方面的防范</a>》一文已经介绍过了。但如果你对隐私的防范，要求比较高（比如说，你是六扇门的重点关注对象），那单重代理的安全性就不太够了——你需要使用多重代理。<br/>
　　那多重代理是啥样的捏？为了简单起见，俺画了下面这幅双重代理的示意图。<br/>
<center><img alt="不见图 请翻墙" src="images/3ISXywMCtIOfvEZv9FKqIvqGaRRAHaK0qTUxLGMGzK0_zorEGwwL_bqunsnfwYaTJrbOtLtTvaBzONtO4GuXcIwFTBszoDVO8Bwm3jIPOpIW3cfviA"/></center><br/>
<br/>
<h2>★需要哪些软件？</h2><br/>
<h3>◇Tor + 其它翻墙工具</h3><br/>
　　理论上，你可以随便挑选两款翻墙工具，然后搞出一个二级代理。但是这样的效果未必理想。<br/>
　　根据俺的经验，最佳组合是：用 Tor（俗称“套”）搭配其它的翻墙工具（比如：赛风、无界、自由门、VPN...），组合出多重代理。<br/>
<br/>
<h3>◇为啥要“戴套”？</h3><br/>
　　长期翻墙的网友，应该都听说过 Tor 这个老牌的翻墙工具（俺曾经扫盲过“<a href="../../2009/09/break-through-gfw-with-tor.md">戴套翻墙</a>”的技术）。那些从来没听说过 Tor 的网友，可以翻墙看“<a href="https://zh.wikipedia.org/wiki/Tor" rel="nofollow" target="_blank">这里</a>”的介绍。<br/>
　　其实拿 Tor 来翻墙，颇有杀鸡用牛刀的嫌疑。Tor 的主要强项在于：<b>提供匿名的网络访问，保护你的隐私</b>。比如名气很大的<a href="https://zh.wikipedia.org/wiki/%E7%B6%AD%E5%9F%BA%E8%A7%A3%E5%AF%86" rel="nofollow" target="_blank">维基解密</a>（WikiLeaks），还有名气很大且很牛逼的<a href="https://en.wikipedia.org/wiki/Anonymous_%28group%29" rel="nofollow" target="_blank">匿名黑客组织</a>（洋文叫“Anonymous”，最近连续黑掉多个大公司及美国政府部门），他们的成员都是用 Tor 来确保自己的匿名。<br/>
　　为啥 Tor 能确保匿名捏？<br/>
其一，<br/>
Tor 在全球有很多节点，当你利用 Tor 上网的时候，从你的电脑到某个网站，需要经过若干个 Tor 节点（通常是3个节点，俗称“三级跳”）。<br/>
其二，<br/>
第1个节点虽然知道你的公网 IP，但不知道你访问了啥网站；第3个节点虽然知道你访问了啥网站，但不知道你的公网 IP。<br/>
其三，<br/>
上述的“三级跳”线路是【动态变化】滴（通常每隔10分钟变化一次），这就使得警方难以追溯。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/GJSTx_KBgpvLFpFY5qNc_gkWuMA_KDAmoVBCOXgqTEdoXJsVnsXZRQBPvKTX2_gnJkjzJWZP7D3HcuiqYLAqcuE7VnRuZKQQ9ufP_1GpDpOTtmsqDw"/><br/>
（Tor 网络的示意图）</center><br/>
　　假如你有些悟性，自然会发现：Tor 本身就是一个多重代理！既然这样，为啥还要拿 Tor 跟其它翻墙工具搭配捏？主要因为万恶的 GFW 把全球大部分的 Tor 节点都进行了 IP 封锁。因此，如果你不幸身处天朝，是很难直接访问到 Tor 节点滴！所以，咱们只好委屈一下，拿 Tor 搭配其它翻墙工具。<br/>
<br/>
<br/>
<h2>★如何配置？</h2><br/>
　　其实配置并不难，只需如下几步：<br/>
<br/>
<h3>◇第1步：运行翻墙工具</h3><br/>
　　首先，你需要准备好一个【能用的】翻墙工具——可以是 HTTP 代理（比如：<a href="../../2011/12/gfw-wujie.md">无界</a>、<a href="../../2010/03/choose-free-gate.md">自由门</a>、<a href="../../2011/10/gfw-psiphon.md">赛风</a>），也可以是 SOCKS 代理，还可以是 VPN（比如 <a href="../../2011/09/gfw-vpn-hotspot-shield.md">Hotspot Shield</a>）。先把这个翻墙工具运行起来。<br/>
　　这个翻墙工具用来作为 Tor 的【前置代理】。<br/>
<br/>
<h3>◇第2步：安装 Tor</h3><br/>
　　如果你使用 Linux 并且发行版的官方仓库已经包含了 Tor，那么就从官方仓库直接安装。<br/>
　　否则的话，请【翻墙】到 Tor 的官方网站，下载一个 Tor 的软件包（下载页面在“<a href="https://www.torproject.org/download/" rel="nofollow" target="_blank">这里</a>”）。<br/>
　　目前官网上提供两种软件包，分别是：<br/>
“Tor Browser Bundle”（面向傻瓜用户）<br/>
“Expert Bundle”（俗称“裸 Tor”，面向高级用户）<br/>
<br/>
<h3>◇第3步：配置 Tor</h3><br/>
　　如果你下载了“Tor Browser”，参见如下这篇教程：<br/>
《<a href="../../2018/04/gfw-tor-browser-7.5-meek.md">“如何翻墙”系列：扫盲 Tor Browser 7.5——关于 meek 插件的配置、优化、原理</a>》<br/>
　　如果你下载了“Expert Bundle”，并且你的操作系统是 Linux/UNIX，参见如下这篇教程：<br/>
《<a href="../../2015/03/Tor-Arm.md">扫盲 Arm——Tor 的界面前端（替代已死亡的 Vidalia）</a>》<br/>
<br/>
<h3>◇第4步：设置浏览器</h3><br/>
　　刚才说了：Tor 有两种软件包（Bundle）。这两者的【监听端口号】略有差异。因此在配置浏览器时，也略有差异。分别说明如下：<br/>
<br/>
　　<b>Tor Browser Bundle</b><br/>
　　Tor 的监听端口为 <code>9150</code><br/>
　　由于这种软件包已经内置了 Firefox，且 Firefox 已经绑定到 Tor。因此，你【无需任何设置】。<br/>
<br/>
　　<b>Expert Bundle</b>（裸 Tor）<br/>
　　Tor 的监听端口为 <code>9050</code><br/>
　　对于这种软件包，你要把浏览器的【SOCKS 代理】指向 Tor（地址 <code>127.0.0.1</code> 端口 <code>9050</code>），就可以通过 Tor 匿名上网了。<br/>
　　<b>为了保险起见，可以用浏览器访问 Tor 官网的检查页面（在“<a href="https://check.torproject.org/" rel="nofollow" target="_blank">这里</a>”），验证一下你是否真的通过 Tor 上网。</b><br/>
<br/>
<h3>◇第5步：设置其它网络软件</h3><br/>
　　如果你想让其它的网络软件（比如：聊天软件、下载工具）通过 Tor 来隐藏你的 IP，也很容易。参见刚才浏览器的代理设置——SOCKS 代理，地址 <code>127.0.0.1</code>，端口号使用 <code>9050</code>（裸 Tor）或 <code>9150</code>（Tor Browser）。以 MSN 为例，你只需在 MSN 的网络设置界面填写 Tor 的 SOCKS 代理即可。<br/>
　　为了保险起见，到 Tor 的管理界面看一下 Tor 的网络流量。只要该网络软件使用的时候，Tor 的管理界面显示出流量，就说明这些网络软件已经通过 Tor 匿名上网了。<br/>
<br/>
<br/>
<h2>★多重代理的【好处】</h2><br/>
<h3>◇防范追踪</h3><br/>
　　举个例子：<br/>
　　假设你用 VPN 翻墙并发表一些抨击党国的言论。万一 VPN 提供商在 VPN 服务器上记录了你的网络流量，而党国又逼迫该 VPN 供应商交出这些流量记录。那么，党国的爪牙就【<b>有可能</b>】分析出你的上网行为。<br/>
　　用了多重代理之后，任何一个代理服务器记录你的网络流量，都无法对你的流量进行分析。<br/>
　　比方说你用的是“Tor + 赛风”。虽然赛风服务器知道你的真实公网 IP，但是无法知道你访问哪个网站及访问的的内容（因为 Tor 的流量是加密的）；而 Tor 的“最后一个节点”（出口节点）虽然知道你访问了哪个网站以及访问的内容，但是它不知道你来自哪里（不清楚你的真实公网 IP）。<br/>
<br/>
<h3>◇伪装国籍</h3><br/>
　　除了上述好处，使用 Tor 还有另一个好处——伪装国籍。比方说，你想让自己看起来像是美国的用户，只需要修改 Tor 的配置文件，使用美国境内的【出口节点】。这种情况下，你访问的网站就会以为你来自美国。<br/>
<br/>
<br/>
<h2>★多重代理的【坏处】</h2><br/>
　　当然啦，有利就有弊。以下是多重代理的一些缺点：<br/>
<br/>
<h3>◇配置复杂</h3><br/>
　　跟单重代理比起来，多重代理显然需要更多的设置。很多网友属于技术门外汉，多半对它望而却步。所以，俺才会专门写这么一篇博文，扫盲多重代理。<br/>
<br/>
<h3>◇性能下降</h3><br/>
　　通常来说，多重代理的性能会比单重代理要差一些。<br/>
　　根据俺近几年的经验——只要【前置代理】的速度足够快，“前置代理 + Tor”的速度也慢不到哪里去。以下是俺电脑上的 Tor 流量截图（基于“赛风+Tor”）。<br/>
<center><img alt="不见图 请翻墙" src="images/99PJcrFDw0ooSRN-JikBLgbK0OTvXMVMV2qcJbkRY3HoJWKKiob6Dt6JApixCjwXTX7HsO5B4-pFRTFiyJKLpKL_umZRDnLC83df4U8Cabs1kI33Pw"/></center><br/>
<b><a href="../../2010/04/howto-cover-your-tracks-0.md#index">回到本系列的目录</a></b><br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2013/11/tor-faq.md">关于 Tor 的常见问题解答</a>》<br/>
《<a href="../../2015/03/Tor-Arm.md">扫盲 Arm——Tor 的界面前端（替代已死亡的 Vidalia）</a>》<br/>
《<a href="../../2009/09/break-through-gfw-with-tor.md">戴“套”翻墻的方法</a>》
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2012/03/howto-cover-your-tracks-5.html
