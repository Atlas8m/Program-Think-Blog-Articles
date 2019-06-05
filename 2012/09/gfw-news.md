# 2012年9月翻墙快报（兼谈复活 TOR 的方法） 

-----

<div class="post-body entry-content">
<b>翻墙的普及需要大家一起努力，希望有更多网友早日呼吸到互联网上自由的空气！</b><br/>
<br/>
<br/>
<h2>★近期翻墙动态</h2><br/>
　　据说朝廷的18大马上要召开了。按照惯例，GFW 又加强了封锁的力度。根据网友们的反馈，最新版的 无界 和 自由门 都不灵了。赛风的最新版本比较奇怪——有些网友能用，有些不能（貌似跟地域或宽带提供商有关）。另外，世界通的 Skype 通道依然可用。<br/>
<br/>
　　所有新版本的翻墙软件，都汇总到“<a href="https://onedrive.live.com/?id=F5B0090663FEEADA!730" rel="nofollow" target="_blank">微软网盘</a>”（墙外）。考虑到某些网友尚无法翻墙，俺特地准备了<b>墙内可用</b>的下载链接。注意：<span style="color:red;font-weight:bold;">下载后是个 BMP 图片，其实是个压缩包。把文件扩展名从 bmp 改为 7z，即可用 7zip 或者 WinRAR 打开，把翻墙工具解压出来。</span>。有些翻墙软件支持邮件方式获取，俺也一并列入下述表格。<a name="more"></a><br/>
<br/>
<table border="1" cellspacing="0"><tr><th>软件名称</th><th>版本号</th><th><font color="red">墙内下载</font>链接</th><th>邮件获取</th></tr>
<tr><td>世界通</td><td>4.1.0</td><td><a href="http://img610.ph.126.net/jimNYb8Ngf6SHxl1RIHlsA==/1949777163676558355.bmp" rel="nofollow">这里</a></td><td>（暂无）</td></tr>
<tr><td>赛风</td><td>3.42</td><td><a href="http://blob-s-docs.googlegroups.com/docs/OgAAAC2lwM6EJ9y1bqDORxV3N8VWb0JtWsDszPFUtzHiHnLD6vLl6VhRmdBSPuWJ4OBU_tw1UhR-qKrqSvfq0Y04y3kA15jOjCDaWrziHp-7Gll2v1NsBmnK5Fs8" rel="nofollow">这里</a></td><td>get@psiphon3.com</td></tr>
<tr><td>TOR</td><td>0.2.2.38</td><td>（暂无）</td><td>gettor@torproject.org</td></tr>
</table><br/>
<br/>
<h2>★用公共代理复活 TOR</h2><br/>
　　由于这次封锁的力度比较大。赛风、无界、自由门 这三款常用翻墙工具受到不同程度的影响。世界通的 Skype 通道虽然能用，但速度似乎不够快。所以，俺再给大伙儿支个招。<br/>
　　TOR 作为老牌的翻墙代理，最近两年来被 GFW 彻底封杀。几乎所有 TOR 的目录服务器和网桥中继，都被 GFW 列入 IP黑名单。但是依然有办法让 TOR 复活。<br/>
<br/>
<h3>◇如何获取TOR软件包</h3><br/>
　　可以通过邮件的方式，直接拿到 TOR 的软件包。具体操作如下：<br/>
发送主题为“help”的<span style="color:red;">纯文本</span>邮件到<b><a href="mailto:gettor@torproject.org" target="_blank">gettor@torproject.org</a></b>，收到回复后根据邮件的提示再回复一次，即可在你的邮箱中收取 TOR 的软件包。记得要用 <span style="color:red;">HTTPS</span> 方式上 <b>Gmail</b>，以确保最佳效果。切记要用<b>纯文本</b>的邮件格式。<br/>
<br/>
<h3>◇什么是公共代理？</h3><br/>
　　公共代理，全称是“公共的代理服务器”。这是互联网上的一些好心人架设的代理服务器。所谓“公共”，就是说任何人都能使用这些代理，无需额外费用。<br/>
　　常见的公共代理有如下类型：SOCKS 和 HTTP。其中，SOCKS 代理又细分为两种：SOCKS4 和 SOCKS5（SOCKS5 比 SOCKS4 高级）。<br/>
　　从协议的层次而言，SOCKS 代理位于网络的第5层（OSI 模型的会话层），而 HTTP 代理位于网络的第7层（OSI 模型的应用层）。从协议的角度来说，SOCKS 代理的性能会高于 HTTP 代理。<br/>
<br/>
<h3>◇如何找到公共代理？</h3><br/>
　　其实俺手头有几个能用的 SOCKS 公共代理。但是捏，因为朝廷的爪牙们也在关注俺博客。如果把这几个 SOCKS 代理公布出来，不出几天就会被封掉。而且俺信奉“授人以鱼不如授人以渔”。所以捏，就多费点口水，介绍一下公共代理的获取方式。<br/>
　　要找到公共代理，简而言之，就是用 Google 搜！<br/>
　　互联网上有成千上万的免费代理可以使用。而且有很多专门的代理网站。这些网站会帮你收集汇总速度快的，运行稳定的代理服务器。有些网站还能做到每日更新。<br/>
　　所以，你只需要通过 Google 搜索 <b>SOCKS proxy</b> 或搜索 <b>HTTP proxy</b>，就能找到很多的代理网站。<br/>
　　找到代理网站之后，上面往往列出几十个代理，该用哪个捏？<br/>
<b>首先，不要选天朝之内的代理</b><br/>
因为咱们找代理是为了翻墙。你找一个墙内的代理，那属于白忙活。<br/>
做得好的代理网站，会列出每一个代理所在的国家。假如没有列出国家信息，你可以找一个查 IP 归属地的网站或软件，很容易就能判断某个代理位于哪国。<br/>
<b>其次，选一个速度快的</b><br/>
很多代理网站做得很人性化，它们会列出每一个代理服务器的延时。延时越小，说明速度越快。<br/>
<b>最后，测试连通性</b><br/>
公共代理也是 GFW 封杀的目标。你在代理网站上找到的公共代理，其中有些没准已经被封了。<br/>
那么，如何判断某个代理是否还能用？很简单，用操作系统自带的 ping 命令测试一下。【假设】你找到的代理，其 IP 是 <code>1.2.3.4</code> 那么你可以用如下命令测试：<br/>
<pre>ping 1.2.3.4</pre><br/>
如果显示超时 <code>Request time out</code> 说明这个代理很可能被 GFW 封了——那你就只好再选另一个代理了；如果显示 <code>reply from 1.2.3.4</code> 那就说明这个代理可用。<br/>
对于熟悉IT技术的网友，也可以用操作系统自带的 telnet 命令，直接测试代理的端口是否能连得上。telnet 命令比 ping 命令更准确，可惜的是，Win7 默认不带此命令 :(<br/>
<br/>
<h3>◇如何设置？</h3><br/>
　　找到好用的公共代理之后，如何配置 TOR 让它通过公共代理联网？具体教程可以参见之前的博文：<br/>
《<a href="../../2009/09/break-through-gfw-with-tor.md">戴“套”翻墻的方法</a>》<br/>
<br/>
<br/>
<h2>★相关翻墙教程</h2><br/>
　　下面这些教程都在俺博客上（墙外）。不会翻墙的网友，可以先用【墙外的】RSS 阅读器订阅俺博客（订阅地址：<a href="http://feeds2.feedburner.com/programthink" target="_blank">http://feeds2.feedburner.com/programthink</a>），就可以看到所有教程。<br/>
<br/>
<h3>◇基础教程</h3><br/>
<a href="../../2009/05/how-to-break-through-gfw.md">如何翻墙</a>（传说中的扫盲教程，定期更新）<br/>
<a href="../../2011/09/gfw-faq.md">常见翻墙问题答疑</a>（传说中的 FAQ，定期更新）<br/>
<a href="../../2011/03/how-to-get-gfw-tools.md">获取翻墙软件方法大全</a>（教你在无法翻墙的情况下拿到翻墙软件）<br/>
<a href="../../2013/01/cross-host-use-gfw-tool.md">多台电脑如何共享翻墙通道</a><br/>
<br/>
<h3>◇具体软件使用教程</h3><br/>
<a href="../../2013/04/gfw-vpngate.md">扫盲 VPN Gate——分布式的 VPN 服务器</a><br/>
<a href="../../2013/11/tor-faq.md">关于 TOR 的常见问题解答</a><br/>
<a href="../../2011/10/gfw-psiphon.md">双管齐下的赛风3</a><br/>
<a href="../../2010/03/choose-free-gate.md">自由門——TOR 被封之后的另一个选择</a><br/>
<a href="../../2011/12/gfw-wujie.md">新版本无界——赛风3失效后的另一个选择</a><br/>
<a href="../../2011/09/gfw-vpn-hotspot-shield.md">扫盲 VPN 翻墙——以 Hotspot Shield 为例</a><br/>
<a href="../../2009/09/break-through-gfw-with-tor.md">戴“套”翻墻的方法</a><br/>
<a href="../../2012/06/gfw-i2p.md">简单扫盲 I2P 的使用</a><br/>
<a href="../../2011/05/through-gfw-with-skype.md">基于 Skype 翻墙</a><br/>
<br/>
<br/>
<h2>★俺的联系方式</h2><br/>
　　如果碰到翻墙的问题，或者想给俺提意见/建议，欢迎来信（ <code>program.think@gmail.com</code> ）。<b>给俺写信最好用 Gmail 或 Hotmail，国内的邮箱很可能会被墙，导致俺收不到。</b>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2012/09/gfw-news.html
