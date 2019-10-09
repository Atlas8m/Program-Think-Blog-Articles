# 近期安全动态和点评（2019年1季度） 

-----

<div class="post-body entry-content">
　　上一篇博文的评论数又猛涨（每次俺戳到衙门的痛点，评论都挺多）。<br/>
<br/>
<h2>★引子：关于《近期安全动态和点评》这种形式</h2><br/>
　　最近这些年，俺写了不少信息安全的教程，也获得很多读者的认可（对大伙儿的捧场，再次表示感谢）。<br/>
　　久而久之，经常会有读者来询问信息安全相关的新闻或业界动态。俺如果有空，通常会在评论区回复相关的提问。<br/>
　　对于那些特别重要的事情，俺会专门发一篇博文进行介绍（比如：“<a href="../../2014/04/openssl-heartbleed.md">心脏滴血漏洞</a>”、“<a href="../../2014/06/truecrypt-dead.md">TrueCrypt 之死</a>”、“<a href="../../2016/08/Trojan-Horse-DCM.md">黑暗幽灵木马（DCM）</a>”...）。<br/>
　　但是捏，大部分的安全新闻和动态，重要性都不是那么高，相关的讨论也没有那么多。如果针对某个事情单独写一篇博文，篇幅会太短（可能就只有几句话）。而且俺也不喜欢发短篇博文。<br/>
　　权衡之下，想到这种形式——<br/>
用单篇博文汇总最近一个季度的安全新闻和动态，然后再附上俺本人的评论。必要时，也可以分享俺的经验。<br/>
<a name="more"></a><br/>
<br/>
<h2>★隐私保护</h2><br/>
<h3>◇朝廷监控屁民的数据库被曝光，含【3.64亿】自然人</h3><br/>
《<a href="https://www.ithome.com.tw/news/129102" rel="nofollow" target="_blank">中國用來存放監控資料的 MongoDB 資料庫曝光了 @ iThome</a>》<br/>
<blockquote style="background-color:#DDD;">中國政府監控民眾網路行為的政策幾乎舉世皆知，但一名資安研究人員Victor Gevers揭露了一個可公開存取、且存放著中國監控民眾的資料庫，進一步向外界展示了中國的監控規模。<br/>
<br/>
此一可公開存取的MongoDB資料庫位於中國，它蒐集了3.64億個連結真實身分的網路個人檔案，紀錄他們在六大社交平台上的聊天內容或檔案傳輸行為，而且透過各省份與縣市的警察局與座落在其它17個地區的MongoDB資料庫同步，這些資料庫都擁有同樣的監控網路名稱，也全都允許公開存取。<br/>
<br/>
Gevers從資料庫上找到的六大社交平台代號為imsg、qg、qqmesg、wwhmsg、wxmsg及yymsg，推測它們分別是<br/>
IS語音服務、QQ Group、QQ Message、wangwang message（阿里旺旺）、微信及YY傳訊<br/>
......</blockquote><br/>
　　<b>编程随想注：</b><br/>
　　据俺了解到的情况，前几年公安部就已经在搭建一个大数据的平台，用来汇总各类 SNS 的数据，并以此来建立很详细的【人际关系网络】。所有墙内的帐号（手机、微信、微博、QQ、支付宝、等等），都整合到这个平台上，并且每个帐号都关联到具体的【自然人】。<br/>
　　利用这样一个平台，六扇门的爪牙就可以很方便地进行各种数据挖掘。所以，早在很多年以前，俺就反复警告：<b>【不要】用天朝的网络服务进行【敏感】活动</b>。<br/>
　　不得不说，<b>奥威尔在《<a href="https://docs.google.com/document/d/144NKDAcg-ip8rwhRtE9fdPan8ZSxqNaEh1A-sYYa7nk/" target="_blank">1984</a>》中预言的【电幕】，正越来越接近现实。</b>如何对抗这种趋势捏？下面这篇博文可以供你参考。<br/>
《<a href="../../2015/08/Technology-and-Freedom.md">“对抗专制、捍卫自由”的 N 种技术力量</a>》<br/>
<br/>
<br/>
<h3>◇“美团 &amp; 饿了么”的手机 APP 涉嫌偷听用户说话</h3><br/>
《<a href="http://www.sohu.com/a/302373460_123753" rel="nofollow" target="_blank">美团饿了么否认“偷听”，那为何我们说啥就推荐啥？ @ 搜狐</a>》<br/>
<blockquote style="background-color:#DDD;">据《IT时报》报道，2018年11月中旬，上海的孙女士在和同事闲聊时提到想喝CoCo奶茶，在打开饿了么APP时，在推荐商家首位看见了CoCo奶茶。让孙女士疑惑的是，自己之前从未在饿了么买过CoCo奶茶，“此前也没有使用任何手机App搜索过CoCo奶茶的相关信息。”<br/>
<br/>
几乎在同一时间，北京网友燃玉(化名)跟朋友说想吃鳗鱼饭，1分钟后打开支付宝上的饿了么应用，推荐位顶部恰巧显示着一家鳗鱼饭的外卖店，此时距离他上次下单鳗鱼饭相隔23天。<br/>
<br/>
《IT时报》的记者耗时三个月模拟用户的使用场景，对iPhone、Android手机和iPad上的美团外卖和饿了么APP进行跟踪测试。从测试结果来看，在谈及某种食物后，打开外卖APP出现相关推荐的概率高达60%-70%。<br/>
......</blockquote><br/>
　　<b>编程随想注：</b><br/>
　　下面这篇是俺写于4年前的博文，其中提到了手机的【硬件】（麦克风、摄像头、GPS、陀螺仪）如何泄漏你的个人信息。<br/>
《<a href="../../2015/01/privacy-protection-10.md">如何保护隐私[10]：移动设备的隐私问题</a>》<br/>
<br/>
<h3>◇“京东金融” APP 盗取用户截屏</h3><br/>
《<a href="http://tech.sina.com.cn/digi/2019-02-16/doc-ihrfqzka6311093.shtml" rel="nofollow" target="_blank">网友曝京东金融App会获取用户截图、照片 @ 新浪</a>》<br/>
<blockquote style="background-color:#DDD;">网友上传的视频显示，其先打开京东金融App，并让其在后台运行。然后打开手机上的银行应用，然后截图。随后打开文件管理器，找到京东金融的文件目录，在此目录下，出现了刚刚的银行应用截图。<br/>
<br/>
不仅如此，该网友后续又发微博称，“京东金融不止偷截图，还会偷照片。”同时又附上一个视频说明，视频显示同样先打开京东金融App，并让其在后台运行。然后打开一个美颜相机App，用该App拍一张图片，之后会在京东金融的文件目录中找到该图片。<br/>
......</blockquote><br/>
<h3>◇抖音国际版被美国 FTC 处以巨额罚款</h3><br/>
《<a href="http://tech.163.com/19/0228/07/E939GT2000097U7R.html" rel="nofollow" target="_blank">违规搜集儿童隐私，抖音国际版在美被罚570万美元 @ 网易</a>》<br/>
<blockquote style="background-color:#DDD;">网易科技讯2月28日消息，据TechCrunch报道，美国联邦贸易委员会（FTC）今天发布了一项重要裁决，短视频应用抖音国际版（TikTok）因违反美国《儿童隐私法》，将被处以570万美元罚款，并将影响该应用在13岁以下儿童中的使用方式。</blockquote><br/>
<h3>◇【两亿】中国求职者简历被泄露</h3><br/>
《<a href="https://www.solidot.org/story?sid=59295" rel="nofollow" target="_blank">两亿中国求职者数据泄露 @ Solidot</a>》<br/>
<blockquote style="background-color:#DDD;">HackenProof <a href="https://blog.hackenproof.com/industry-news/202-million-private-resumes-exposed" rel="nofollow" target="_blank">报告</a>，网络风险研究总监 Bob Diachenko 于 12 月 28 日分析 BinaryEdge 搜索引擎数据时发现了一个公开的没有任何保护或身份验证的 MongoDB 数据库，数据库容量为 854 GB，包含了 202,730,434 名中国求职者的数据，数据包括了详细的求职者信息如技能、工作经验、电话号码、电子邮件、婚姻状况、子女状况、政治面貌、身高、体重、驾照、文化水平和薪水期望等等。</blockquote><br/>
<h3>◇Chrome 74 之后，用户无法再禁用“点击追踪”</h3><br/>
　　<b>编程随想注：</b><br/>
　　“点击追踪”是 HTML5 引入的特性，术语叫做“ping 属性”。如果网站在“超链接”中加入该属性，当用户点击这个超链接的时候，链接所在网站会得到点击的通知。很多网站用“点击追踪”来统计【外链】的点击情况。<br/>
　　Google 作为搜索引擎，用户点击搜索结果，当然属于【外链点击】。所以，“点击追踪”这个功能对 Google 而言很有用（可以统计用户曾经点击过搜索结果中的哪些网站）。<br/>
<br/>
　　在 74 版本之前，Chrome 还有“点击追踪的选项”（也就是说，用户可以关闭该选项，禁用“点击追踪”）。到了 74 版本之后，Chrome 连这个开关选项也【去掉】了——因此，普通用户再也【无法禁止】“点击追踪”了。<br/>
　　不得不说，Chrome 在【侵犯隐私】的邪路上越走越远。具体的原因，俺已经多次聊过——因为 Google 的主要利润来源是【在线广告收入】。所以，Chrome 的隐私保护，不但比 Firefox 差，而且很可能会【越来越差】。<br/>
　　引申阅读：<br/>
《<a href="../../2018/09/Why-You-Should-Switch-from-Chrome-to-Firefox.md">弃用 Chrome 改用 Firefox 的几点理由——关于 Chrome 69 隐私丑闻的随想</a>》<br/>
<br/>
<br/>
<h2>★高危漏洞</h2><br/>
<h3>◇Chrome 高危漏洞</h3><br/>
《<a href="https://security.googleblog.com/2019/03/disclosing-vulnerabilities-to-protect.html" rel="nofollow" target="_blank">Disclosing vulnerabilities to protect users across platforms @ Google 官方博客</a>》<br/>
《<a href="https://www.zdnet.com/article/google-chrome-zero-day-was-used-together-with-a-windows-7-zero-day/" rel="nofollow" target="_blank">Google: Chrome zero-day was used together with a Windows 7 zero-day @ ZDNet</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　这个 Chrome 漏洞的编号是：<code>CVE-2019-5786</code>，存在于 FileReader API 中，攻击者可以利用该漏洞实现【远程执行代码】（Remote Code Execution）。由于该漏洞高度危险，Google（在24小时内）紧急发布了 <code>72.0.3626.121</code> 版本，进行修复。<br/>
　　讽刺的是：和该漏洞一起曝光的另一个漏洞是——“Win7 的【提权漏洞】”。攻击者如果同时利用这两个漏洞，不但能【远程】执行代码，还可以在执行代码后【提权】（拿到“管理员权限”）。（对攻击者而言）这两个漏洞堪称完美组合。<br/>
<br/>
<h3>◇WinRAR 高危漏洞</h3><br/>
《<a href="https://www.solidot.org/story?sid=59906" rel="nofollow" target="_blank">WinRAR bug 正被利用安装难以检测的恶意程序 @ Solidot</a>》<br/>
<blockquote style="background-color:#DDD;">流行的解压缩软件 WinRAR 曝出了一个至少 14 年历史的代码执行漏洞，<br/>
安全公司 Check Point 的研究人员在 UNACEV2.DLL 的过滤函数中发现了一个漏洞，允许将代码提取到 Windows 启动文件夹，在 Windows 重启之后执行。<br/>
现在，McAfee 研究人员报告该漏洞正被利用安装难以检测的恶意程序。</blockquote><br/>
　　<b>编程随想注：</b><br/>
　　WinRAR 这个软件，早就该丢到垃圾桶了——这玩意儿不但是【闭源】滴，而且还要【注册】。让人非常不爽！<br/>
　　WinRAR 的完美替代品是【7zip】——不但【开源】、【免费】，而且还【跨平台】。<br/>
　　顺便说一下：<br/>
　　如果对压缩率要求【不】高，俺通常用 zip 格式，因为这种格式已经成为【事实标准】（比如：<a href="https://github.com/programthink/books" target="_blank">俺网盘</a>分享的 HTML 格式电子书，会把多个 HTML 打包成一个 zip）<br/>
　　如果对压缩率要求【很】高，俺通常用 7z 格式（很多情况下，7z 压缩率超过 rar）<br/>
<br/>
<h3>◇apt 高危漏洞</h3><br/>
《<a href="https://www.debian.org/security/2019/dsa-4371" rel="nofollow" target="_blank">Debian 官方安全公告</a>》<br/>
《<a href="https://justi.cz/security/2019/01/22/apt-rce.html" rel="nofollow" target="_blank">Remote Code Execution in apt/apt-get @ 漏洞发现者的博客</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　apt 是 Debian 发行版默认使用的【软件包管理器】。考虑到 Debian 有【非常多】的衍生发行版（比如：Ubuntu），apt 的影响面非常大。<br/>
　　<b>这个漏洞（CVE-2019-3462）很危险！</b>——<br/>
其一，该漏洞本身就是【远程】执行漏洞。<br/>
其二，为了安装和更新软件，Linux 用户通常会以【root】身份运行“软件包管理器”。所以，apt 的“远程执行漏洞”，会让攻击者直接获得【最高权限】。<br/>
<br/>
　　【不彻底】的解决方法：<br/>
　　当然是升级到修复该漏洞的 apt 版本。<br/>
<br/>
　　【彻底】的解决方法：<br/>
　　除了这次，apt 在【2016年】曾经曝光过另一个安全漏洞（CVE-2016-1252）。所以，咱们可以合理地怀疑——apt 的网络模块中还存在其它高危漏洞。<br/>
　　（对于使用 apt 的同学）俺认为彻底的解决办法是——<b>搭建【私有的】升级镜像</b>。搞了这个玩意儿之后，你的 apt 工具只是通过【内网 or 本地文件】的方式获得升级包。因此，apt 就算有安全漏洞，至少漏洞也【不会】暴露到公网上。这种玩法，本质上就是——【降低攻击面】（这个原则也是俺经常唠叨滴）。<br/>
　　搞了自己的升级镜像后，你可以用其它网络工具（rsync、curl、wget）从发行版的官方网站同步升级包。由于“同步升级包”的操作可以用【普通用户】的权限进行（甚至可以在另一个 OS 中进行），即使用来同步的网络工具出了安全问题，也不至于太惨。<br/>
　　升级镜像的另一个好处是——如果你有多个【同种的】OS，采用私有的升级镜像，可以大大提升速度——（传输一次，升级 N 次）。对于使用虚拟机的同学，这个好处会特别明显——你可以把私有的升级镜像放在 Host OS，并以【共享目录】的方式提供给 Guest OS。如此一来，每个 Guest OS 都【无需】再去下载升级包。<br/>
<br/>
<br/>
<h2>★网络与 Web</h2><br/>
<h3>◇针对“域名服务商”的 DNS 劫持攻击</h3><br/>
《<a href="https://www.solidot.org/story?sid=59282" rel="nofollow" target="_blank">研究称 DNS 劫持攻击规模惊人 @ Solidot</a>》<br/>
<blockquote style="background-color:#DDD;">攻击者首先设法窃取目标 DNS 服务商管理面板的登录凭证，然后修改目标域名的 IP 地址，将其指向攻击者控制的服务器。攻击者之后再利用 Let’s Encrypt 自动生成合法证书。当用户访问目标域名，他们会先访问攻击者的服务器然后再重定向到合法服务器，整个过程用户唯一的感觉可能就是延迟略微增加。攻击者之后能收集到用户名和密码，而终端用户对此几乎一无所知。</blockquote><br/>
　　<b>编程随想注：</b><br/>
　　这种攻击手法，再次凸显了【DNS】与【CA 证书】的重要性。攻击者如果【同时搞定】这两者，就可以实现【完美的钓鱼】。关于这点，俺在9年前（2010）的某篇博文中提到过：<br/>
<blockquote style="background-color:#DDD;">既然老流氓 CNNIC 已经成为合法的 CA，那它就能堂而皇之地制作并发布 CA 证书。然后捏，再配合 GFW 进行【域名污染】。那 GFW 就可以轻松搞定任何网站的 HTTPS 加密传输。<br/>
......<br/>
可能有些小朋友心里会犯嘀咕：GFW 会有这么坏吗？俺想篡改鲁迅他老人家的一句话来回答：<b>俺向来是不惮以最坏的恶意，来推测党国</b>。GFW 和 CNNIC 作为党国的2条走狗，一起进行中间人攻击（一个负责在 DNS 上做手脚、另一个负责伪造 CA 证书），简直是“天生一对、黄金搭档”啊！</blockquote>　　引申阅读：<br/>
《<a href="../../2010/02/introduce-digital-certificate-and-ca.md">数字证书及 CA 的扫盲介绍</a>》<br/>
《<a href="../../2010/02/remove-cnnic-cert.md">CNNIC 证书的危害及各种清除方法</a>》<br/>
<br/>
<h3>◇可【突破两步验证】的网络钓鱼工具</h3><br/>
《<a href="https://www.zdnet.com/article/new-tool-automates-phishing-attacks-that-bypass-2fa/" rel="nofollow" target="_blank">New tool automates phishing attacks that bypass 2FA @ ZDNet</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　波兰的安全研究人员 Piotr Duszyński 发布了名为“<a href="https://github.com/drk1wi/Modlishka" rel="nofollow" target="_blank">Modlishka</a>”的工具（该名称是波兰语“螳螂”）。这个玩意儿可以实现<b>【更逼真】的钓鱼攻击，并且可以突破【两步验证】</b>。<br/>
　　该工具本质上是一个【反向代理】，其原理类似于“中间人攻击/MITM”（由“钓鱼网站”充当中间人）。受害者看到的界面，是从【真实的】网站传回到钓鱼网站的界面，受害者输入的密码，也会被转发给真实的网站。“两步验证”在这种攻击面前是【不堪一击】滴。<br/>
<br/>
　　前一个小节提到了【DNS 劫持】，在此基础上再进行这种高级钓鱼，会让很多人防不胜防。<b>这种钓鱼攻击能否成功，关键在于 CA 证书。</b>如果钓鱼网站使用的是“貌似合法的 CA 证书”，则浏览器【不会】弹出“无效证书”的警告，因此受害者也就【不会】怀疑网站是假的。<br/>
　　由于创建“貌似合法的 CA 证书”，正变得越来越容易（参见前一个小节提到的手法），因此这种钓鱼也就变得越来越危险。<br/>
　　俺的建议是——<br/>
　　你在某个【专用】的浏览器实例中操作特别重要的帐号（也就是说，这个实例只操作这个帐号，不访问其它网站）然后在该实例中采用【证书白名单策略】——只留下这个帐号对应网站所需的 CA 证书，其它证书全部禁掉。当然啦，你还需要保留一个【通用】的实例，用来进行日常的上网浏览。如此一来，假设你有 N 个重要帐号，需配置 N + 1 个实例。<br/>
　　浏览器的选择：<br/>
　　Chrome 和 Firefox 都可以创建“多实例”，但 Chrome 有个【缺点】——它用的是操作系统的证书。因此，Chrome【无法】使用刚才介绍的招数。<br/>
　　相比之下，Firefox 使用的是【自带证书】。因此，你可以创建多个 Firefox 实例，并通过配置让每个实例的证书都采用各自的【白名单策略】。<br/>
<br/>
<h3>◇Google 的公共 DNS 服务正式支持 DoH（DNS over HTTPS）</h3><br/>
《<a href="https://www.cnbeta.com/articles/tech/807293.htm" rel="nofollow" target="_blank">谷歌公共 DNS 正式支持 DoH 加密 @ cnBeta</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　Google 的公共 DNS，也就是 <code>8.8.8.8</code> 和 <code>8.8.4.4</code> 这俩。<br/>
　　其实这两个 DNS 在去年就已经提供 DoH 服务，但还处于【试运行阶段】。从2019年1月，开始【正式】支持 DoH。<br/>
　　关于 DoH 的好处，可以参考俺之前的博文：<br/>
《<a href="../../2018/10/Comparison-of-DNS-Protocols.md">对比4种强化域名安全的协议——DNSSEC，DNSCrypt，DNS over TLS，DNS over HTTPS</a>》<br/>
《<a href="../../2014/01/dns.md">扫盲 DNS 原理，兼谈“域名劫持”和“域名欺骗／域名污染”</a>》<br/>
<br/>
　　关于浏览器的支持：<br/>
Firefox 从 62 版本开始支持 DoH，具体参见 Mozilla 官方博客（链接在“<a href="https://blog.nightly.mozilla.org/2018/06/01/improving-dns-privacy-in-firefox/" rel="nofollow" target="_blank">这里</a>”）。<br/>
Chrome/Chromium 从 66 版本开始支持 DoH。具体参见 Chromium 官网的 issue（链接在“<a href="https://bugs.chromium.org/p/chromium/issues/detail?id=799753" rel="nofollow" target="_blank">这里</a>”）。<br/>
<br/>
<br/>
<h2>★移动设备</h2><br/>
<h3>◇2018年全年，针对移动设备的攻击，堪称有屎以来最高</h3><br/>
《<a href="https://securelist.com/mobile-malware-evolution-2018/89689/" rel="nofollow" target="_blank">Mobile malware evolution 2018 @ Securelist</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　上述报告来自 Kaspersky Lab。<br/>
　　俺已经在博客上唠叨无数次了——【不要】用手机操作重要帐号，也【不要】用手机进行敏感活动。<br/>
<br/>
<h3>◇大部分 Android 杀毒软件【不】靠谱</h3><br/>
《<a href="https://www.solidot.org/story?sid=59896" rel="nofollow" target="_blank">三分之二的 Android 杀毒应用没有价值 @ Solidot</a>》<br/>
<blockquote style="background-color:#DDD;">杀毒软件测试机构 AV-Comparatives 测试了 Google Play 商店里的 250 款杀毒应用，检查这些应用对 2000 恶意应用样本的检测情况。结果显示，只有 80 款应用能阻止最少数量的恶意样本。不到十分之一的应用能阻止所有恶意应用，超过三分之二的应用检出率不到 30%</blockquote><br/>
<h3>◇贝佐斯的手机被入侵</h3><br/>
《<a href="http://www.sohu.com/a/305282847_116132" rel="nofollow" target="_blank">贝索斯手机隐私遭入侵，疑为沙特政府所为 @ 搜狐</a>》<br/>
《<a href="https://www.cnn.com/2019/03/31/media/jeff-bezos-gavin-de-becker-saudi-arabia-leak/" rel="nofollow" target="_blank">Jeff Bezos investigator: Saudi Arabia obtained private information @ CNN</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　作为目前的世界首富，而且还是顶级 IT 公司的老板，贝佐斯显然拥有顶级的安全顾问团队。<br/>
　　如果连他的手机都会被入侵（而且是被“深度渗透”），这说明啥捏？你自己想一下吧。<br/>
　　另外，<br/>
　　博客的长期读者都知道，俺特别喜欢抹黑朝廷，中国政府的御用骇客也老早就盯上俺了（请看“<a href="../../2017/05/my-blog-under-government-backed-attack.md">这篇博文</a>”和“<a href="../../2016/06/github-take-down-zhao-repository.md">这篇博文</a>”）。<br/>
　　俺写政治博文将近【十年】（而且写了很多“煽颠性质”的博文）。至少到今天，俺还没有倒下。其中一个重要经验是：俺【从不】在手机上使用这个身份。<br/>
　　当然啦，除了这个经验，还有其它很多经验，具体参见：<br/>
《<a href="../../2019/01/Security-Guide-for-Political-Activists.md">为啥朝廷总抓不到俺——十年反党活动的安全经验汇总</a>》<br/>
<br/>
<br/>
<h2>★安全工具</h2><br/>
<h3>◇几款主流的【密码管理器】都有安全缺陷</h3><br/>
　　下面是由 ISE（Independent Security Evaluators）发布的一篇挺详细的评估报告，涵盖了最常用的几款密码管理器（LastPass、KeePass、1Password、Dashlane）。<br/>
《<a href="https://www.securityevaluators.com/casestudies/password-manager-hacking/" rel="nofollow" target="_blank">Password Managers——Under the Hood of Secrets Management @ ISE</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　考虑到那篇报告很长，而且是洋文，俺简单说一下。<br/>
　　几款主流密码管理器的缺陷，都与【内存】有关——比如说：有的软件居然把【主密码】（master password）以【明文形式】留在内存中。这么弱智的做法，一旦遭到【冷启动攻击】，攻击者就可以拿到主密码，进而拿到管理器中的所有密码。<br/>
　　即使不考虑“冷启动攻击”，如果你的系统开启了【休眠功能】（大部分 Windows 系统都开启了），内存中的主密码（在休眠时）会被保存到硬盘的“休眠文件”中。因此，如果你遭遇了警方的【取证软件】，你的“主密码”（master password）同样有曝光的风险。<br/>
　　引申阅读：<br/>
《<a href="../../2019/02/Use-Disk-Encryption-Anti-Computer-Forensics.md">如何用“磁盘加密”对抗警方的【取证软件】和【刑讯逼供】，兼谈数据删除技巧</a>》<br/>
<br/>
<h3>◇NSA 发布【逆向工程框架】——Ghidra</h3><br/>
<a href="https://www.nsa.gov/resources/everyone/ghidra/" rel="nofollow" target="_blank">NSA 官网</a><br/>
<a href="https://github.com/NationalSecurityAgency/ghidra" rel="nofollow" target="_blank">Ghidra @ Github</a><br/>
<br/>
　　<b>编程随想注：</b><br/>
　　该软件本身能运行于 Windows、Linux、Mac OS 三大主流操作系统，可以分析多种处理器指令集。<br/>
　　该工具仅限于政府内部使用。直到前几年，维基解密公布了美国国安局（NSA）内部资料（<a href="https://en.wikipedia.org/wiki/Vault_7" rel="nofollow" target="_blank">Vault7</a>），这款工具才开始为人所知。<br/>
　　另，<br/>
　　该工具开源之后不久，被发现自身有安全漏洞，如今已修复。<br/>
<br/>
<h3>◇Metasploit 发布 5.0 版本</h3><br/>
　　Metasploit 是大名鼎鼎的【渗透测试框架】，主要用于安全攻防人员。不了解的同学请看“<a href="https://en.wikipedia.org/wiki/Metasploit_Project" rel="nofollow" target="_blank">维基百科</a>”。<br/>
　　这是它在【2011年】之后首次发布新版本（大版本）。增加的新特性参见“<a href="https://github.com/rapid7/metasploit-framework/wiki/Metasploit-5.0-Release-Notes" rel="nofollow" target="_blank">这个链接</a>”。<br/>
<br/>
<br/>
<h2>★操作系统</h2><br/>
<h3>◇匿名操作系统的对比</h3><br/>
《<a href="https://www.solidot.org/story?sid=59846" rel="nofollow" target="_blank">最好的匿名操作系统 @ Solidot</a>》<br/>
<blockquote style="background-color:#DDD;">安全研究员 David Balaban <a href="https://hackernoon.com/best-operating-systems-for-anonymity-comparing-titans-3501fd5cba3b" rel="nofollow" target="_blank">对比了五个匿名操作系统</a>：Tails OS，Whonix，Kodachi，Qubes 和 Subgraph，分析了各个系统的优缺点。Qubes 和 Subgraph 都是隔离应用来实现安全，它们其实不是为匿名设计的。Tails OS 基于 Debian，所有流量都经过 Tor，设计作为 Live CD 或 Live USB 使用，不在主系统留下痕迹，会话结束之后所有痕迹就抹掉了，它不适合作为一个永久性的操作系统使用。Whonix 也是基于 Debian，通过 VirtualBox 和 Tor 实现匿名，内置了大量应用，但不具有可携性，硬件需要也比较高。Kodachi 基于 Debian，通过 VPN 和 Tor 实现匿名，硬件需求不高，作者认为它是目前最好的匿名操作系统。</blockquote><br/>
　　<b>编程随想注：</b><br/>
　　如果你对安全性（包括隐匿性）要求很高，但又【不】擅长技术，上述对比可以供参考。<br/>
　　对于擅长折腾的同学，俺建议选某个 Linux 或 BSD 的【成熟】发行版，然后根据自己的需要进行【高度定制】（裁剪），只留下自己需要的部分（从而把攻击面降到最低），然后再搭配上自己需要的加固措施。<br/>
<br/>
<br/>
<h2>★硬件与物理安全</h2><br/>
<h3>◇Spectre &amp; Meltdown 漏洞的普及性文章</h3><br/>
《<a href="https://spectrum.ieee.org/computing/hardware/how-the-spectre-and-meltdown-hacks-really-worked" rel="nofollow" target="_blank">How the Spectre and Meltdown Hacks Really Worked @ IEEE</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　一年前（2018年初）曝光的 Spectre 和 Meltdown 在信息安全界可以称得上是【划时代】滴！因为其利用的是 CPU 的【设计缺陷】（而且还是【根本性】缺陷）。不熟悉这两个漏洞的同学，可以看维基百科的介绍（<a href="https://en.wikipedia.org/wiki/Spectre_(security_vulnerability)" rel="nofollow" target="_blank">这里</a> 和 <a href="https://en.wikipedia.org/wiki/Meltdown_(security_vulnerability)" rel="nofollow" target="_blank">这里</a>）<br/>
　　上述文章是专门研究这两个漏洞的三个学者在今年2月份撰写的【扫盲性质】文章，介绍漏洞的【原理】。<br/>
　　由于这两个漏洞涉及到 CPU 的【根本性】缺陷，极难搞定（就像两个幽灵，会在未来几年不断困扰 IT 行业）。为了说明这点，再引述一篇今年2月份的报道：<br/>
《<a href="https://hardware.slashdot.org/story/19/02/21/1630210/" rel="nofollow" target="_blank">Google Researchers Say Software Alone Can't Mitigate Spectre Chip Flaws @ Slashdot</a>》<br/>
<br/>
<h3>◇针对 Intel 处理器的新型 Spoiler 攻击</h3><br/>
《<a href="https://www.solidot.org/story?sid=59784" rel="nofollow" target="_blank">所有英特尔处理器面临新的 Spoiler 攻击 @ Solidot</a>》<br/>
<blockquote style="background-color:#DDD;">美国和德国的计算机科学家在预印本网站 ArXiv 上发表<a href="https://arxiv.org/pdf/1903.00446.pdf" rel="nofollow" target="_blank">论文</a>(PDF)，<a href="https://www.theregister.co.uk/2019/03/05/spoiler_intel_processor_flaw/" rel="nofollow" target="_blank">披露了</a>针对英特尔处理器的新攻击 SPOILER。他们在英特尔内存子系统私有实现中发现了地址推测的一个弱点，能透露内存布局数据，让翻转比特的 Rowhammer 攻击更容易执行。研究人员检查了 ARM 和 AMD 处理器，但没有发现它们表现出类似的行为。新的漏洞很难在不重新设计处理器微架构的情况下修复或缓解。Spoiler 攻击不同于 Spectre 攻击，它无需提权就可以在用户空间利用。研究人员称，Spoiler 大幅加快了 Rowhammer 和缓存攻击。Rowhammer 翻转比特攻击影响所有处理器，但要利用 Rowhammer 你可能需要花费数周时间，而在 SPOILER 的帮助下，攻击将可以在数秒内完成，Rowhammer 攻击将变得切实可行。</blockquote><br/>
　　<b>编程随想注：</b><br/>
　　简单扫盲一下【Row Hammer 攻击】<br/>
　　如今的集成电路，集成度越来越高；当集成度高到一定程度，【相邻】的内存单元就有可能出现电磁影响。这种攻击就是利用相邻内存单元之间的电磁影响，在进行足够多的访问次数后，让某个比特的值发生改变（0、1 互换）。因此也被称为“比特翻转”（洋文叫“bit flipping”）。<br/>
　　假如攻击者能够修改某些【关键的比特位】，就可以实现【权限提升】或【代码执行】。<br/>
　　在硬件层面引入 ECC（error-correcting code），可以【部分防止】这种内存错误；但某些精心构造的“Row Hammer 攻击”能绕过 ECC 的防护机制。<br/>
<br/>
<h3>◇超微（Super Micro）主板的 BMC 后门</h3><br/>
《<a href="https://t.cj.sina.com.cn/articles/view/6533357275/1856b1edb00100mxif" rel="nofollow" target="_blank">超微服务器主板组件爆漏洞 @ 新浪</a>》<br/>
<blockquote style="background-color:#DDD;">这项漏洞是出现在超微主板上的基板管理控制器（baseboard management controller, BMC）上。BMC是一个具高度权限的组件，提供多种接口，包括系统接口、IPMB接口、LAN及Serial/Modem接口，可让数据中心管理员通过智能平台管理接口（Intelligent Platform Management Interface, IPMI）指令远程执行、或在服务器不开机状态下安装操作系统、安装修改app、或对多台服务器变更状态。然而由于BMC提供的接口对系统内、外部来的IPMI指令欠缺足够验证，因此常被用来传送恶意IPMI指令、或遭恶意软件挖掘BMC漏洞。<br/>
......<br/>
Eclypsium研究人员挑选IBM的SoftLayer云裸机服务进行了概念验证攻击，原因是SoftLayer服务执行在超微服务器上。IBM SoftLayer的裸机云服务提供企业客户租用，服务期满客户资料删除后，可以再租给下一家企业。在实验中，研究人员租用了SoftLayer服务、在其Supermicro的BMC上修改了一些程序代码，开了一个名为Cloudborne的后门，并且在其BMC的IMPI界面中新开另一个用户账号。之后再将服务还给IBM，又再租了新服务。<br/>
研究人员发现，在转换客户期间，IBM SoftLayer的确进行了回收（reclaimation）过程，将多的账号清掉，但是BMC被植入的后门还是在，显示并未经过刷新。研究人员表示，结合漏洞让黑客得以利用后门读取托管在同一台服务器上的新企业客户的云环境，以窃取数据、发动Dos攻击，或是植入任何恶意软件。</blockquote><br/>
　　<b>编程随想注：</b><br/>
　　俺在去年底的博文《<a href="../../2018/12/weekly-share-127.md">每周转载：盘点一下贸易战爆发后的【中美对抗】（2018年4季度）</a>》，提到了如下：<br/>
<blockquote style="background-color:#DDD;">《彭博商业周刊》报道称——<br/>
在中国组装的超微主板被植入了恶意芯片，黑客借此渗透了美国政府和大型企业的数据中心，受影响的企业包括了亚马逊和苹果。<br/>
<br/>
编程随想注：<br/>
到俺写本文为止，这几家公司（超微、亚马逊、苹果）都发表声明予以否认。此事目前有争议，尚未定论。<br/>
从技术上讲，这么做是【可行】滴。硬件层面的安全漏洞能规避操作系统的安全防护机制。</blockquote>　　如今，超微主板的 BMC（基板管理控制器）被发现有缺陷，可以被攻击者用来留下后门。而超微的某些主板是在咱们天朝组装滴。<br/>
　　这两件事情，很容易让人产生联想。<br/>
<br/>
<h3>◇隐藏在 USB 线里的 WIFI</h3><br/>
《<a href="https://www.solidot.org/story?sid=59621" rel="nofollow" target="_blank">隐藏在 USB 线里的 WIFI @ Solidot</a>》<br/>
<blockquote style="background-color:#DDD;">你可能认为 USB 线没什么可怕的，大多数人都会随身带些 USB 线以方便给便捷式设备充电或访问设备内部资料，但如果看起来一模一样的 USB 线包含了隐藏的后门？你插上之后就容易遭到网络攻击？<br/>
安全研究员 <a href="https://twitter.com/_MG_" rel="nofollow" target="_blank">_MG_</a>历时一个月制作的<a href="https://mg.lol/blog/omg-cable/" rel="nofollow" target="_blank">O.MG Cable</a>，将 WIFI 微控制器秘密安装在 USB 连接器内，能通过 USB 设备发送载荷，<a href="https://hackaday.com/2019/02/18/wifi-hides-inside-a-usb-cable/" rel="nofollow" target="_blank">实现远程控制</a>。</blockquote><br/>
<br/>
<h2>★安全编程</h2><br/>
<h3>◇微软产品的漏洞，有【七成】源自“内存问题”</h3><br/>
《<a href="https://www.zdnet.com/article/microsoft-70-percent-of-all-security-bugs-are-memory-safety-issues/" rel="nofollow" target="_blank">Microsoft: 70 percent of all security bugs are memory safety issues @ ZDNet</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　熟悉 C/C++ 的“程序猿/程序媛”，应该很清楚小标题所说的“内存问题”是指哪些。举个栗子：安全漏洞中大名鼎鼎的【缓冲区溢出】（包括“栈溢出”和“堆溢出”），都与内存问题有关。<br/>
　　前几天，<a href="https://github.com/programthink/books" target="_blank">俺的网盘</a>上分享了两本书，分别是：《<a href="https://docs.google.com/document/d/1gYOn_6nFNWkcJ62MsBIhs57bA0ydHpfqp11lQ2R1Ko4/" target="_blank">C 语言安全编程规范</a>》和《<a href="https://docs.google.com/document/d/1zi7_dcLXnVCc9ePEgdhnU1xxuYgM5RavsmkEp7gKRnM/" target="_blank">C++ 语言安全编程规范</a>》。<br/>
　　这两本书出自 <a href="https://en.wikipedia.org/wiki/CERT_Coordination_Center" rel="nofollow" target="_blank">CERT/CC</a>，权威性应该是 OK 滴（在安全圈混的人，多半都听说过 CERT）。<br/>
<br/>
<h3>◇哪些编程语言的漏洞更多？</h3><br/>
《<a href="https://developers.slashdot.org/story/19/03/25/0322202/" rel="nofollow" target="_blank">Which Programming Language Has The Most Security Vulnerabilities? @ Slashdot</a>》<br/>
<blockquote style="background-color:#DDD;">Across the seven most widely-used programming languages, here's how the vulnerabilities were distributed:<br/>
<br/>
C (47%)<br/>
PHP (17%)<br/>
Java (11%)<br/>
JavaScript (10%)<br/>
Python (5%)<br/>
C++ (5%)<br/>
Ruby (4%)</blockquote><br/>
　　<b>编程随想注：</b><br/>
　　上述统计只针对【7种】流行的编程语言，统计数字来自 TechRepublic 网站。（经热心读者提醒：TechRepublic 网站的数据又是源自 WhiteSource 网站的<a href="https://resources.whitesourcesoftware.com/blog-whitesource/is-one-language-more-secure" rel="nofollow" target="_blank">这个链接</a>，特此说明）<br/>
　　C 语言占了接近一半，这在意料之中（参见前一个小节）。C++ 的漏洞显著低于 C，这很大程度得益于 C++ 标准库中提供了很多“类/模板”（比如：string、vector、shared_ptr），可以封装原始类型，尤其是指针类型。作为对比，C 语言经常要【显式】进行内存分配/释放。而在 C++ 中，很多内存分配/释放变为【隐式】（在封装库内部完成）。<br/>
　　另，<br/>
　　C++ 的漏洞比例竟然【低于】Java 和 JS，俺还是有点小小的惊讶 :)<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2019/01/Security-Guide-for-Political-Activists.md">为啥朝廷总抓不到俺——十年反党活动的安全经验汇总</a>》<br/>
《<a href="../../2013/06/privacy-protection-0.md">如何保护隐私</a>》（系列）<br/>
《<a href="../../2010/06/howto-prevent-hacker-attack-0.md">如何防止黑客入侵</a>》（系列）<br/>
《<a href="../../2010/04/howto-cover-your-tracks-0.md">如何隐藏你的踪迹，避免跨省追捕</a>》（系列）<br/>
《<a href="../../2015/08/Technology-and-Freedom.md">“对抗专制、捍卫自由”的 N 种技术力量</a>》<br/>
《<a href="../../2019/02/Use-Disk-Encryption-Anti-Computer-Forensics.md">如何用“磁盘加密”对抗警方的【取证软件】和【刑讯逼供】，兼谈数据删除技巧</a>》<br/>
《<a href="../../2018/10/Comparison-of-DNS-Protocols.md">对比4种强化域名安全的协议——DNSSEC，DNSCrypt，DNS over TLS，DNS over HTTPS</a>》<br/>
《<a href="../../2014/01/dns.md">扫盲 DNS 原理，兼谈“域名劫持”和“域名欺骗／域名污染”</a>》<br/>
《<a href="../../2018/09/Why-You-Should-Switch-from-Chrome-to-Firefox.md">弃用 Chrome 改用 Firefox 的几点理由——关于 Chrome 69 隐私丑闻的随想</a>》<br/>
《<a href="../../2010/02/introduce-digital-certificate-and-ca.md">数字证书及 CA 的扫盲介绍</a>》<br/>
《<a href="../../2010/02/remove-cnnic-cert.md">CNNIC 证书的危害及各种清除方法</a>》
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2019/04/Security-News.html
