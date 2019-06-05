# “如何翻墙”系列：双管齐下的赛风3 

-----

<div class="post-body entry-content">
　　话说今年赶巧是辛亥革命100周年，而天朝的中宣部对“革命”二字向来十分忌惮。所以，从9月底“沦陷日”前夕一直到现在，GFW 就没消停过。以前俺一直推荐大伙儿使用的自由门，近期虽然发布了 7.1.8、7.1.9和7.2.0这几个新版本，但是都不给力。俺在9月30日写了《<a href="../../2011/09/gfw-vpn-hotspot-shield.md">扫盲 VPN 翻墙——以 Hotspot Shield 为例</a>》一文，结果10月10日下午，Hotspot Shield就英勇牺牲。好在半年前介绍的“<a href="../../2011/05/through-gfw-with-skype.md">世界通+Skype</a>”依然坚挺，只是偶尔会掉线（从掉线的时间分布判断，可能是用的人太多导致）。但是大伙儿要牢记：在天朝从事翻墙运动，千万不能在一棵树上吊死。为了让大伙儿多一条翻墙的路，今天再来普及另外一款翻墙工具——赛风。<a name="more"></a><br/>
<br/>
<br/>
<h2>★赛风为何物？</h2><br/>
　　赛风是由多伦多大学的<a href="http://citizenlab.org/" rel="nofollow" target="_blank">公民实验室（Citizen Lab）</a>搞出来的一款翻墙软件，专门用来帮助各国网民突破政府的网络限制和网络审查。赛风的官网在“<a href="http://psiphon.ca/" rel="nofollow" target="_blank">这里</a>”，可惜是洋文的。<br/>
　　早期的赛风2是纯网页代理，只有服务端软件，没有客户端软件。前不久推出赛风3之后，开始提供客户端软件。你只要在自己的电脑上运行客户端，就可以翻墙。<br/>
<br/>
<br/>
<h2>★赛风3的特色</h2><br/>
<h3>◇同时支持两种翻墙模式</h3><br/>
　　为啥说赛风是双管齐下捏？因为它同时支持 VPN 翻墙和代理翻墙。（尚不清楚这两者区别的同学，请看俺在《<a href="../../2009/05/how-to-break-through-gfw.md">如何翻墙</a>》一文的扫盲）这种玩法在翻墙界比较少见，可以说是赛风3的一大特色。具体的操作后面会介绍。<br/>
<br/>
<h3>◇绿色且小巧</h3><br/>
　　赛风的客户端是绿色软件，无需安装。它只有一个300多 KB 的 EXE 文件，堪称小巧。而且这个 EXE 文件带有数字签名。简单验证一下数字签名，就可以确保该文件没有中毒或者被恶意篡改。<br/>
<br/>
<h3>◇操作简单且傻瓜化</h3><br/>
　　赛风的界面极其简单，没有任何可配置的东西。你只需用鼠标双击 EXE，把它运行起来，就 OK 了。如果它运行在 VPN 模式，你连浏览器都无需设置；如果它运行在代理模式（SSH 模式），你顶多只要设置一下浏览器的 HTTP 代理。<br/>
<br/>
<h3>◇开放源代码</h3><br/>
　　最后，非常难能可贵的是，该软件还是开源滴，遵循 GPL 协议。虽然目前“赛风3”的客户端目前只有 Windows 版本，相信不久就会有热心网友通过改造源代码，把它移植到 Linux 系统和 Mac OS 系统。如果你用的是苹果系统或者 Linux 系统，暂时可以采用 <a href="http://www.winehq.org/" rel="nofollow" target="_blank">Wine</a> 来运行赛风。<br/>
<br/>
<br/>
<h2>★赛风软件的获取</h2><br/>
　　赛风3的获取，也很简单。你只需往赛风官网提供的邮箱 <b><code>get@psiphon3.com</code></b> 发送任意邮件，即可收到自动回复。以前，自动回复的邮件仅仅包含下载链接（而且链接往往被 GFW 封杀）；如今，<b>自动回复的邮件直接就附上了赛风</b>的可执行程序（邮件里的附件名叫 <code>psiphon3.asc</code>，改为 <code>psiphon3.exe</code> 即可直接运行）。<br/>
　　说到发邮件，俺又要啰嗦了。千万别用国内的邮箱发，容易被墙而且不安全。国内那几大门户网站，迫于党的淫威，都会配合党的走狗进行邮件内容的审查。国外的邮件，俺首先推荐 Google 的 Gmail 邮箱，其次可以用微软的 Hotmail 或 Outlook 邮箱。<br/>
<br/>
<br/>
<h2>★赛风3的使用</h2><br/>
　　先说明一下，赛风【无需管理员权限】即可运行。这下，喜欢上网吧的同学有福了。<br/>
　　你用鼠标双击 EXE 文件之后，会出现如下界面。左上角的箭头不停旋转，表示在尝试连接。<br/>
<center><img alt="不见图 请翻墙" src="images/r_Rt2wpOm5GqXKJzRQnVGlhwHpqx0RvSGTTt1QRC0vNNpZYo5XzBxkNHr0jAmkUPdjFWNuveo23R5wk4n4hn9Ckd1GB8J2sboIKJ3M7oRVs_Oe4ROt6t09ZjCvKorsuKlmQ"/></center><br/>
<h3>◇VPN 模式</h3><br/>
　　如果 VPN 连接成功，会出现如下界面。左上角的图标变为绿色，且有 VPN 字样。这时候，你电脑中的每一个网络软件（包括浏览器、聊天软件、邮件软件）<b>无需任何设置</b>，即可通过 VPN 翻墙。非常爽！<br/>
<center><img alt="不见图 请翻墙" src="images/PHj9r-uhPmVuN-b-BxFknhWeSCERoVdi-MfbUab2F0-59Tbh3dturUtH2rgadXXVuHm7QSpwdrqxm1rcIy9Zwgy5_ecZP5grSAPaASlLSadXhhk6Hf408ndHbi7XQ81QktA"/></center><br/>
<h3>◇SSH 模式（代理模式）</h3><br/>
　　万一 VPN 连不上，它会尝试用 SSH 方式连接墙外的赛风服务器。连接成功后，出现如下界面。左上角的图标变为绿色，且有 SSH 字样。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/2mgqIJmb7MiYvNxKq15qca6EM0gtpIR3WaOca9xi0YtaHvQxQNpOMpA8h0R6sh4tFOppCyEtRqcVjlQoDHep6sWi0HqU8GLHLGSOl8wk3jSWNP_kxYRUH_f06TqPuRLutPY"/></center><br/>
　　这时候，你只需把浏览器的 HTTP 代理设置成如下，即可浏览墙外的风景。<br/>
地址 <code>127.0.0.1</code><br/>
端口 <code>8080</code><br/>
<br/>
　　在代理模式下，赛风3还支持 SOCKS 代理。打个比方，假如想让某个聊天软件通过赛风3翻墙，只需把聊天工具的 SOCKS 代理设置成如下：<br/>
地址 <code>127.0.0.1</code><br/>
端口 <code>1080</code><br/>
　　除了“聊天工具”，其它很多类型的网络软件，只要该软件支持 SOCKS 代理的，配置都大同小异。<br/>
<br/>
<br/>
<h2>★补充说明</h2><br/>
　　今天提到的某些内容，会增加到俺写的翻墙扫盲教程——《<a href="../../2009/05/how-to-break-through-gfw.md">如何翻墙</a>》以及《<a href="../../2011/09/gfw-faq.md">常见翻墙问题答疑</a>》。这两份文档，俺会不定期更新，力图做到与时俱进。<br/>
　　另外，如果你是一位翻墙的新手，在看完本文之后，最好也看一下俺写的翻墙扫盲教程——《<a href="../../2009/05/how-to-break-through-gfw.md">如何翻墙</a>》。<br/>
　　如有其它翻墙方面的疑问，也可以到俺博客留言。<br/>
　　最后，祝大伙儿早日掌握各种翻墙姿势，呼吸到互联网上自由的空气！<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）：</b><br/>
<a href="../../2009/05/how-to-break-through-gfw.md">如何翻墙</a>（传说中的扫盲教程，定期更新）<br/>
<a href="../../2011/09/gfw-faq.md">常见翻墙问题答疑</a>（传说中的 FAQ，定期更新）<br/>
<a href="../../2011/03/how-to-get-gfw-tools.md">获取翻墙软件方法大全</a>（教你在无法翻墙的情况下拿到翻墙软件）<br/>
<a href="../../2013/04/gfw-vpngate.md">扫盲 VPN Gate——分布式的 VPN 服务器</a><br/>
<a href="../../2013/11/tor-faq.md">关于 TOR 的常见问题解答</a><br/>
<a href="../../2010/03/choose-free-gate.md">自由門——TOR 被封之后的另一个选择</a><br/>
<a href="../../2011/12/gfw-wujie.md">新版本无界——赛风3失效后的另一个选择</a><br/>
<a href="../../2011/09/gfw-vpn-hotspot-shield.md">扫盲 VPN 翻墙——以 Hotspot Shield 为例</a><br/>
<a href="../../2009/09/break-through-gfw-with-tor.md">戴“套”翻墻的方法</a><br/>
<a href="../../2012/06/gfw-i2p.md">简单扫盲 I2P 的使用</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2011/10/gfw-psiphon.html
