# 近期安全动态和点评（2020年3季度） 

-----

<div class="post-body entry-content">
　　由于9月底刚发了一篇《<a href="../../2020/09/Academic-Scandals-in-China.md">二十年目睹之怪现状——中国学术界、科技界的“奇葩排行榜”</a>》，长假期间忙了别的事情，又要花时间回复读者评论。导致3季度的《近期安全动态和点评》到今天才发。抱歉 :(<br/>
<a name="more"></a><br/>
<br/>
<h2>★隐私保护</h2>
<br/>
<h3>◇基于“上网历史”的指纹</h3>
<br/>
《<a href="https://www.solidot.org/story?sid=65389" rel="nofollow" target="_blank">用户的浏览历史是独一无二的 @ Solidot</a>》<br/>
<blockquote>
2012年，法国和 Google 的研究人员分析了382,269名用户的浏览历史所构成的大型数据集，调查浏览历史是否能作为指纹跟踪用户。研究人员发现（<a href="https://hal.inria.fr/hal-00747841/document" rel="nofollow" target="_blank">PDF</a>），绝大部分用户的浏览历史是独一无二的，并且相当稳定，可作为指纹使用。<br/>
在本月举行的 USENIX 会议上，Mozilla 的研究人员重复了这项研究并进行了延伸（<a href="https://www.usenix.org/system/files/soups2020-bird.pdf" rel="nofollow" target="_blank">PDF</a>）。研究人员使用的数据集包含了5.2万名 Firefox 用户在两周内的浏览历史，分析显示了48,919个可区分的浏览资料，即 99% 的浏览历史是独一无二的。超过八成用户可通过浏览历史重新识别身份。<br/>
研究人员还发现，只需要考虑50个最流行网站就足以获得独特指纹。这项研究凸显出收集浏览历史所带来的个人隐私问题，研究人员称他们发现大量第三方在收集用户浏览历史将其作为标识符使用。</blockquote>
　　<b>编程随想注：</b><br/>
　　至少有两个维度可以收集某人的浏览历史——<br/>
其一，通过【网络监控】进行收集（比如：“电信运营商 or 公司网管”就可以做到这点）<br/>
其二，通过【本机软件】进行收集（比如：某些流氓软件会收集浏览器的历史）<br/>
　　多年来，俺一直唠叨【全程加密代理】。这么干不仅仅是为了翻墙，还可以避免 ISP（电信运营商）看到你的“浏览历史”。另外，那些安全要求很高的同学，不光要做到“全程加密代理”，甚至要做到【全程匿名网络】。<br/>
　　（如果你对安全性的要求很高，一定要记得看这篇汇总《<a href="../../2019/01/Security-Guide-for-Political-Activists.md">为啥朝廷总抓不到俺——十年反党活动的安全经验汇总</a>》）<br/>
<br/>
<h3>◇VPN 的隐私问题</h3>
<br/>
《<a href="https://it.slashdot.org/story/20/07/17/2338230/" rel="nofollow" target="_blank">VPN With 'Strict No-Logs Policy' Exposed Millions of User Log Files @ Slashdot</a>》<br/>
<br/>
《<a href="https://www.solidot.org/story?sid=64970" rel="nofollow" target="_blank">声称不记录日志的 VPN 公司，泄露了2000万用户日志 @ Solidot</a>》<br/>
<blockquote>
声称保护用户隐私的公司却不能保护自己的，声称不记录任何日志的公司却被发现记录了大量用户日志。<br/>
香港 VPN 服务商 UFO VPN 因其 Elasticsearch 数据库没有任何密码保护而<a href="https://www.hackread.com/vpn-firm-zero-logs-policy-leaks-20-million-user-logs/" rel="nofollow" target="_blank">暴露了超过2000万用户日志</a>。Comparitech 的研究人员在7月1日发现了总容量为 894GB 的数据库，其中包含了明文密码、IP 地址、用户连接的时间戳、会话令牌、设备信息、操作系统和地理位置信息。这不仅意味着用户账号容易被接管，也意味着用户能被跟踪，而使用会话令牌加密的数据能被解密。该公司声称它收集的信息都是匿名的，只是用于分析网络性能和问题，改进服务质量。</blockquote>
　　<b>编程随想注：</b><br/>
　　很多 VPN 提供商都号称“从不记录用户日志”。但关键是——它是否记录日志，VPN 用户【无法】验证。<br/>
　　安全上的一个很重要的经验是：<b>对于你【无法】验证的东西，应该作出更坏（更危险）的假设，然后在这个更坏（更危险）的前提下，构造你的防御措施。</b><br/>
　　以“使用 VPN”为例。当你无法确认“VPN 提供商是否记录用户日志”，你应该假设：自己使用的【每个】VPN 服务器都【永久】地记录了你的【每个】上网行为。<br/>
　　在这样的假设下，你应该咋办捏？为了防止 VPN 提供商耍流氓，俺在多年前就一直唠叨：VPN 用户要学会【戴套】——也就是“Tor over VPN”，相当于双重代理，具体教程参见《<a href="../../2010/04/howto-cover-your-tracks-0.md">如何隐藏你的踪迹，避免跨省追捕</a>》系列的其中一篇。<br/>
　　不光是 VPN，当你使用 SNS 平台，也要记得刚才所说的“更坏假设”。大多数 SNS 平台（微信、抖音、快手、Facebook、Twitter ......）都会厚着脸皮说：它们很关注用户隐私。而你根本【无法】验证这点。<br/>
<br/>
<h3>◇港版《国安法》引发隐私关注</h3>
<br/>
《<a href="https://www.solidot.org/story?sid=64892" rel="nofollow" target="_blank">Signal 成为香港下载量最高的应用 @ Solidot</a>》<br/>
<blockquote>
根据 App Annie 的数据，在香港国安法生效之后安全消息应用 Signal 成为香港地区苹果和 Google 应用商店下载量最高的应用。<br/>
Signal 最吸引人的功能是端对端加密，被广泛认为是最安全的加密消息应用。端对端的加密和解密是在通讯端的双方进行的，因此服务商也无法知道会话内容，这能有效防止第三方监听。<br/>
Signal 的其它功能包括阅后即焚，以及最小化用户数据收集。当其它社交服务纷纷表示暂停香港政府的用户数据请求，Signal 表示它根本没有用户数据可以提供。</blockquote>
<br/>
《<a href="https://cn.wsj.com/articles/whatsapp%E5%B0%86%E6%9A%82%E5%81%9C%E5%A4%84%E7%90%86%E9%A6%99%E6%B8%AF%E6%89%A7%E6%B3%95%E6%9C%BA%E6%9E%84%E5%85%B3%E4%BA%8E%E7%B4%A2%E5%8F%96%E7%94%A8%E6%88%B7%E6%95%B0%E6%8D%AE%E7%9A%84%E8%AF%B7%E6%B1%82-11594077313" rel="nofollow" target="_blank">谷歌、Facebook 和 Twitter 暂停处理香港政府的用户数据请求 @ WSJ/华尔街日报</a>》<br/>
<br/>
《<a href="https://www.ftchinese.com/story/001088553" rel="nofollow" target="_blank">美国科技公司拒绝与香港证监会分享客户数据 @ FT/金融时报</a>》<br/>
<br/>
<h3>◇美国“棱镜门丑闻”的新进展</h3>
<br/>
《<a href="https://www.solidot.org/story?sid=65439" rel="nofollow" target="_blank">美国法庭判决 Snowden 曝光的大规模监视项目是非法的 @ Solidot</a>》<br/>
<blockquote>
在前 NSA 合同工 Edward Snowden 曝光美国大规模监视项目7年之后，美国第九巡回上诉法庭<a href="https://www.reuters.com/article/us-usa-nsa-spying/u-s-court-mass-surveillance-program-exposed-by-snowden-was-illegal-idUSKBN25T3CK" rel="nofollow" target="_blank">判决此类项目是非法的</a>。法庭认为，无搜查令的撒网式大规模秘密收集数百万美国人的电话记录违反了外国情报监视法，可能还构成了违宪。<br/>
目前在俄罗斯避难的 Snowden 表示，这一裁决证明他当年公开 NSA 大规模国内监视证据的决定是正确的。他说没想到自己能活着看到美国的法庭谴责 NSA 的活动是非法的。<br/>
在 Snowden 曝光前，美国情报官员坚称 NSA 从未明知故犯的收集美国人的信息。在 Snowden 曝光后，美国官员改口称大规模监视在打击国内极端主义上扮演着重要的作用。美国官员还引用了多位极端主义者被定罪作为大规模监视合法的证据，但第九巡回上诉法庭指出，此类说辞与机密记录不一致。ACLU 则表示这是隐私权一次胜利。</blockquote>
　　<b>编程随想注：</b><br/>
　　美国第九巡回上诉法庭的这个判决，从某种意义上算是对斯诺登的平反。<br/>
　　当年斯诺登曝光【棱镜门丑闻】时，俺发了博文《<a href="../../2013/06/usa-vs-china.md">中美政府信息监控的差异——“棱镜门”丑闻随想</a>》。<br/>
　　总体而言，俺是支持斯诺登，反对美国政府的大规模监控。或者说，反对任何政府的大规模监控。在博客上，俺不止一次唠叨：不论是在哪种政治体制下，公民都要始终对【公权力】（政府＆政客）保持足够高的警惕性。<br/>
　　另外，某些读者【误以为】俺是“美粉”，其实不然。7年前（2013）俺发上述博文时，文中的第一个章节是：<q>★写在前面的话——如何客观看待“美国”？</q><br/>
<br/>
<h3>◇Firefox 引入新的防护机制，对抗广告商的“redirect tracking”</h3>
<br/>
　　《<a href="https://blog.mozilla.org/security/2020/08/04/firefox-79-includes-protections-against-redirect-tracking/" rel="nofollow" target="_blank">Firefox 79 includes protections against redirect tracking @ Mozilla</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　Firefox 从79版本开始，引入了新的 ETP 2.0（Enhanced Tracking Protection 2.0），用来对抗广告商的“redirect tracking”。<br/>
　　考虑到大部分读者不太了解“广告商的伎俩”，稍微解释一下：<br/>
　　俺在《<a href="../../2013/06/privacy-protection-0.md">如何保护隐私</a>》系列教程中，已经扫盲了【cookie】的基本概念，也解释了“第一方 cookie”与“第三方 cookie”的差别。<br/>
　　最近这些年，很多在线广告采用“第三方 cookie”来追踪用户身份。于是很多浏览器（比如 Firefox）提供了一个隐私选项——禁用【所有的】“第三方 cookie”。<br/>
　　当越来越多用户采用这类选项，广告商当然不爽啦。于是就搞了个“redirect tracking”技术。当你访问某些网站的时候，网站先让你的浏览器【重定向/跳转】到广告商的网站，然后再跳转回来（回到你真正访问的网站）。如此一来，广告商的网站就可以在你的浏览器中保存“第一方 cookie”。<br/>
　　而 Firefox 新引入的 ETP 2.0 会每隔24小时清理这些“redirect tracking”植入的 cookie。也就是说，隔天之后，如果你再访问同样的网站，在线广告商并不知道“你就是昨天的你”。<br/>
<br/>
<br/>
<h2>★高危漏洞</h2>
<br/>
<h3>◇GRUB2 高危漏洞（BootHole）——同时影响多种操作系统</h3>
<br/>
《<a href="https://www.cnbeta.com/articles/tech/1009469.htm" rel="nofollow" target="_blank">安全启动功能曝出 BootHole 新漏洞，影响大量 Linux 与 Windows 系统 @ cnBeta</a>》<br/>
<blockquote>
安全研究公司 Eclypsium 刚刚曝光了安全启动（Secure Boot）功能中的一个新漏洞，并将之命名为 BootHole 。其特别存在于 Secure Boot 的 GRUB2 文件中，攻击者可借此对受害者的系统实现“近乎完全的控制”。而且无论是 Linux、还是数量相当庞大的 Windows 操作系统，都会受到 UEFI 固件中的这个漏洞的影响。<br/>
Eclypsium 指出，只要使用了标准的微软第三方 UEFI 证书授权，这些支持 Secure Boot 功能的 Windows 设备都会受到 BootHole 漏洞的影响，包括大量的 Windows 台式机、笔记本、工作站、服务器、以及其它相关技术领域。<br/>
鉴于 Secure Boot 对启动过程的把控非常重要，BootHole 漏洞的影响力也可见一斑。对于攻击者来说，其能够在操作系统加载之前执行任意的恶意代码，同时避开多个安全措施的管控，最终使其获得对目标系统近乎完全的控制权。<br/>
......</blockquote>
　　<b>编程随想注：</b><br/>
　　UEFI 的 Secure Boot 机制（简称：SB 机制）用来构建【UEFI 启动时的信任链】，这个“SB 机制”企图做到——只加载可信的（经过签名的）二进制代码。具体的“信任链机制”参见维基百科的“<a href="https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface#SECURE-BOOT" rel="nofollow" target="_blank">这个链接</a>”。<br/>
　　想法很美好，现实很无情——这个信任链的任何一个环节都会是潜在的【<a href="../../2015/04/Single-Point-of-Failure.md">单点故障</a>】。也就是说，只要信任链的的某一环有弱点，整个信任链就瓦解了。<br/>
　　在半年前的《<a href="../../2020/04/Security-News.md">近期安全动态和点评（2020年1季度）</a>》，当时正好在点评 Intel 芯片的“CSME 漏洞”。俺说了一句——<b>UEFI 的安全性并没有某些同学想象的那么好</b>。不幸被言中 :)<br/>
　　这次的 BootHole 高危漏洞（编号：<code>CVE-2020-10713</code>），就是上述所说的【单点故障】。<br/>
　　简而言之： GRUB2 内部用来解析配置文件（<code>grub.cfg</code>）的函数有缓冲区溢出的漏洞。攻击者可以构造一个特殊的 <code>grub.cfg</code> 文件，从而触发该漏洞，并获得执行代码的机会。<br/>
　　关于该漏洞的细节，有篇很详细的技术介绍——《<a href="https://eclypsium.com/2020/07/29/theres-a-hole-in-the-boot/" rel="nofollow" target="_blank">There's a Hole in the Boot @ Eclypsium</a>》<br/>
<br/>
　　由于攻击针对的是引导程序（boot loader）本身，与操作系统无关。因此，不论你用的是哪一种系统，只要你的 boot loader 是 GRUB2，都可能中招。<br/>
　　【引导程序】的漏洞很危险——它是在操作系统【之前】运行滴。它如果出现“可执行代码”的漏洞，攻击代码也是在操作系统【之前】被执行。此时，攻击代码可以玩很多猫腻——<br/>
比如说：攻击代码可以在 OS 启动之前，先把系统中的安全模块和杀毒软件干掉。<br/>
比如说：全盘加密的解锁通常是在 GRUB 之后进行，攻击代码有机会窃取【密码 or 密钥】（注：“密码 ＆ 密钥”是完全不同的两个概念，对“加密盘”而言，密钥无法修改，而密码可以修改。因此，“密钥失窃”更严重）<br/>
......<br/>
<br/>
<h3>◇Windows 漏洞</h3>
<br/>
《<a href="https://krebsonsecurity.com/2020/07/wormable-flaw-leads-july-microsoft-patches/" rel="nofollow" target="_blank">'Wormable' Flaw Leads July Microsoft Patches @ Krebs on Security</a>》<br/>
<br/>
《<a href="https://www.solidot.org/story?sid=64953" rel="nofollow" target="_blank">Windows 例行安全更新修复了一个【蠕虫级】漏洞 @ Solidot</a>》<br/>
<blockquote>
微软本周二（注：7月14日）释出了例行安全更新，修复了123个安全漏洞，其中一个位于 Windows Server 属于高危蠕虫级漏洞，软件巨人警告可能很快它就会遭到利用，目前还没有任何有关该漏洞正被利用的报告。编号为 CVE-2020-1350 的漏洞为远程可利用 bug，危险等级10/10，影响绝大部分 Windows Server 版本，攻击者通过发送特质 DNS 请求就可利用该漏洞安装恶意程序。它被称为蠕虫级漏洞是因为恶意程序无需用户交互就能在存在漏洞的计算机之间传播。<br/>
其它17个高危漏洞影响 Office、Internet Exploder、SharePoint、Visual Studio 和 .NET Framework。</blockquote>
　　<b>编程随想注：</b><br/>
　　【蠕虫级】的漏洞比较少见。这类漏洞通常位于那些长时间运行，并且开启监听端口的软件中（比如系统的 service 或 daemon）。当蠕虫感染了某台主机后，会主动对外扫描，一旦发现别的主机也有同样的漏洞，直接感染之；如此循环往复。因此，蠕虫的扩散非常快。<br/>
　　某些老网民应该还记得十多年前的“红色代码 ＆ 震荡波”——这俩就是典型的蠕虫。<br/>
　　另外，本文发出后，有热心读者在评论区反馈——上述引文中的<q>Internet Exploder</q>存在拼写错误。<br/>
　　特声明：原文如此，俺只是照样贴出。<br/>
<br/>
《<a href="https://www.solidot.org/story?sid=65654" rel="nofollow" target="_blank">黑客正在利用最近修复的 Windows 高危漏洞 Zerologon @ Solidot</a>》<br/>
<blockquote>
微软在8月份的例行更新中修复了被命名为 Zerologon 的高危漏洞 CVE-2020-1472，它允许本地网络的任意攻击者完全控制 Active Directory。该漏洞可被用于发动勒索软件攻击或植入间谍软件。发现该漏洞的安全研究员上周公布了能可靠利用漏洞的概念验证代码。<br/>
本周<a href="https://arstechnica.com/information-technology/2020/09/one-of-this-years-most-severe-windows-bugs-is-now-under-active-exploit/" rel="nofollow" target="_blank">微软发出警告</a>，黑客正在利用该漏洞。它没有提供细节，只是提供了攻击使用的文件数字签名。美国国土安全部也发出警告，建议企业尽快打补丁或者将域控制器从互联网上移除。</blockquote>
<br/>
<h3>◇家用路由器的漏洞</h3>
<br/>
《<a href="https://www.solidot.org/story?sid=64884" rel="nofollow" target="_blank">家用路由器被发现存在大量漏洞 @ Solidot</a>》<br/>
<blockquote>
你正在使用的家用路由器非常有可能存在众多的安全隐患，需要尽可能快的更新固件，如果厂商有新固件释出的话。<br/>
德国的 Fraunhofer Institute for Communication 最近<a href="https://www.fkie.fraunhofer.de/content/dam/fkie/de/documents/HomeRouter/HomeRouterSecurity_2020_Bericht.pdf" rel="nofollow" target="_blank">测试了</a>127款家用路由器，其中 91% 运行了某个版本的嵌入式 Linux 系统。<br/>
研究人员<a href="https://hothardware.com/news/millions-of-home-wi-fi-routers-linux-exploits" rel="nofollow" target="_blank">发现</a>，<b>没有一款路由器免于安全漏洞</b>，其中许多款存在数以百计的安全问题。四分之一的路由器超过一年时间没有收到任何安全方面的更新，部分路由器没有收到更新的时间长达五年。研究人员称，部分路由器很容易被破解，或存在用户无法改变的已知硬编码密码。知名路由器厂商 D-Link、TP-Link 和 Linksys 在定期更新上远远落在后面，其中 Linksys 的一款路由器 WRT54GL 使用的是2002年释出的 Linux 内核版本2.4.20，存在579个高危漏洞。</blockquote>
　　<b>编程随想注：</b><br/>
　　前不久，正好有读者在评论区问俺：如何用路由器隔离多台物理主机。<br/>
　　当时俺就提到：【不要】光依赖家用路由器进行网络隔离，因为家用路由器本身可能被入侵。更保险的做法是——在每一台物理主机的物理系统（Host OS）配置防火墙规则。为了尽可能严格，配置规则时应该采用【白名单风格】。<br/>
　　聊到这里，顺便扫盲一下两种风格，白名单 VS 黑名单：<br/>
　　白名单风格——先全部禁止，然后把允许的从中排除掉。<br/>
　　黑名单风格——先全部允许，然后把禁止的从中排除掉。<br/>
　　（这两种风格不光体现在“信息安全领域”，在别的很多领域也有体现。比如说：企业管理、人际交往、等等）<br/>
<br/>
<h3>◇X Server（Xorg Server）高危漏洞</h3>
<br/>
　　《<a href="https://lwn.net/Articles/829639/" rel="nofollow" target="_blank">X.Org server security advisory @ LWN</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　“X Server”中文称作“X 服务器”。在 X11 体系（X Window System）中，它充当服务端。为了与显卡等设备打交道，它通常以【管理员权限】（root 权限）运行。<br/>
　　8月底曝光了 X server 的一系列漏洞（编号：<code>CVE-2020-14345</code>，<code>CVE-2020-14346</code>，<code>CVE-2020-14347</code>，<code>CVE-2020-14361</code>，<code>CVE-2020-14362</code>），影响1.20.9之前的所有版本。<br/>
　　当 X server 以【root】权限运行时，如果攻击者可以获得【本地执行代码】的机会，就可以利用这些漏洞实现【提权】（从“普通用户权限”提升为“管理员权限”）。考虑到 X server 在 Linux/UNIX 的【桌面】系统中很普遍，这个漏洞值得注意。<br/>
<br/>
<br/>
<h2>★新冷战与网络战</h2>
<br/>
<h3>◇关于“科技脱钩”</h3>
<br/>
《<a href="https://www.bbc.com/zhongwen/simp/world-53682476" rel="nofollow" target="_blank">美国净网行动开辟五大战线，科技铁幕全面脱钩中国的影响 @ BBC/英国广播公司</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　上述这篇 BBC 的报道，俺在8月份的博文《<a href="../../2020/08/weekly-share-146.md">每周转载：“中美对抗”进入【科技脱钩】阶段（网文7篇）</a>》已经引用过了。与“中美脱钩”相关的话题，可以参见8月份那篇。<br/>
<br/>
《<a href="https://cn.reuters.com/article/britain-huawei-5g-decision-0714-tues-idCNKCS24G01Q" rel="nofollow" target="_blank">英国宣布2027年底前清除 5G 网络中的华为设备，中美博弈中选边美国 @ 路透社</a>》<br/>
<blockquote>
　　路透伦敦7月14日<br/>
　　英国首相约翰逊下令，在2027年底之前彻底清除 5G 网络中的华为设备，此举暗示全球最大电信设备制造商华为在西方不受欢迎，可能会激怒中国。在英国准备退欧之际，对华为安全性的担忧迫使约翰逊在美中这两个全球竞争对手之间做出选择。<br/>
　　约翰逊此前一直受到来自美国总统特朗普的巨大压力，而北京则警告近年来寻求与中国拉近距离的伦敦方面，如果站在华盛顿一边，来自中国的数十亿美元投资将面临风险。<br/>
　　英国禁止华为参与其 5G 网络建设的决定受到美国驻英国大使 Woody Johnson 的欢迎，他表示，这是公平贸易和人权的胜利。他周二在推特上表示:“英国决定禁止华为进入其 5G 网络，以保护国家安全，这也是公平贸易和人权的胜利。”<br/>
　　约翰逊1月时曾宣布将华为设备在英国 5G 网络中非核心部分的占比限制在 35% 以内，这一决定于周二（注：7月14日）逆转。约翰逊宣布，禁止英国电信运营商在年底以后再从华为购买任何 5G 设备，并给运营商七年的时间移除现有华为设备。<br/>
　　英国文化大臣道登（Oliver Dowden）对议会表示：“这不是一个容易的决定，但对于英国电信网络、我们的国家安全和经济来说，无论是现在还是长期来看，这都是正确的决定。到下一次大选时，我们已经依法将华为设备完全从我们的 5G 网络中移除。”<br/>
　　英国称立场转变的原因是美国对芯片技术实施新制裁的影响，隶属于英国情报机构政府通讯总部（GCHQ）的英国国家网络安全中心曾告诉大臣们，这影响了华为保持可靠供应商地位的能力。<br/>
　　美国国家安全顾问奥布莱恩（Robert O'Brien）表示，英国的行动反映出一种日益增强的共识，即华为和其他不受信任的供应商对国家安全构成威胁，因为它们仍然“对中国共产党负有义务”。根据2017年出台的《中华人民共和国国家情报法》，任何组织和公民都应当依法支持、协助和配合国家情报工作。<br/>
<br/>
......</blockquote>
<br/>
《<a href="https://www.rfi.fr/cn/%E6%B3%95%E5%9B%BD/20200722-%E5%9B%9E%E5%A3%B0%E6%8A%A5-%E6%AD%A5%E8%8B%B1%E5%9B%BD%E5%90%8E%E5%B0%98%E6%B3%95%E5%9B%BD%E5%8F%98%E7%9B%B8%E5%BC%83%E7%94%A8%E5%8D%8E%E4%B8%BA" rel="nofollow" target="_blank">步英国后尘，法国变相弃用华为 @ RFI/法广</a>》<br/>
<blockquote>
　　根据路透社7月22日独家报导<br/>
　　法国当局已告知计划购买华为 5G 设备的电信运营商（SFR 和 Bouygues Telecom/布衣格电信），一旦设备许可证到期，将无法续签，从而有效地将把华为变相地淘汰出法国移动网络。<br/>
　　法国网络安全机构 ANSSI 本月表示，运营商的设备（包括华为设备）需要持有三到八年的许可证，但是，法国网络安全机构 ANSSI 督促运营商不要选用华为，以免更换时遇麻烦。<br/>
　　目前，法国运营商必须申请数十个设备许可证，才能覆盖全国不同地区。消息人士称，法国网络安全机构 ANSSI 已把很多大城市的许可证政策告知了运营商，即华为设备的授权大部分是三年或五年，而爱立信或诺基亚的设备大部分都获得了八年许可证。<br/>
　　消息人士补充说，法国当局在最近几个月的非正式对话中告知运营商，此后不会续签华为设备的许可证，但未在文件中正式说明。消息人士称，鉴于许可证的期限很短，这等于说，华为将在法国 5G 网络中在2028年前被逐步淘汰。<br/>
　　一位消息人士称，鉴于 5G 等新的移动技术至少需要八年才得到投资回报，所以在法国政府对许可证的限制下，电信运营商很难冒险投资华为设备。这位知情人士补充说：“给三年的许可证，就等于是（对华为）一口回绝。”<br/>
　　消息人士表示，法国对华为的立场与英国相似，只是“但政府的沟通方式有所不同。”并且“华为对此无能为力。”</blockquote>
<br/>
《<a href="https://cn.reuters.com/article/canada-huawei-0825-tues-wrapup-idCNKBS25M06K" rel="nofollow" target="_blank">加拿大实际上已将华为排挤出 5G 建设，但嘴上不能说 @ 路透社</a>》<br/>
<blockquote>
　　路透渥太华8月25日<br/>
　　加拿大是五眼联盟中，唯一尚未正式将华为排除在 5G 网络建设之外的国家；但它实际上已经这么做了，手段就是一直拖着不做出决定，从而迫使电信企业不敢与华为合作。<br/>
　　六名知情消息人士指出，随着中美围绕华为展开角力，这个做法让夹在中间的加拿大两边不得罪。加拿大和五眼联盟中的盟友——英国、新西兰和澳洲——都被美国施压，被要求以安全理由排除华为。<br/>
<br/>
......<br/>
<br/>
　　消息人士称，加拿大运营商认为美国的遏制让它们别无选择，只能将华为排除在 5G 网络之外，至少目前是如此。鉴于形势的敏感性，消息人士要求匿名。“他们进行了政治盘算，称‘我们最好是什么都不做，这样一来，我们就不会让中国感到不快，也不会惹美国不高兴’，”一位了解政府官员立场的消息人士称。<br/>
　　避免得罪中国已成为一个重要考量。华为财务长孟晚舟自2018年12月被加拿大警方拘捕以来，一直在抗争美国的引渡要求。<br/>
　　中国指控加拿大公民迈克尔（Michael Spavor）和康明凯（Michael Kovrig）从事间谍活动而将他们逮捕。加拿大称，让他们获得自由是当务之急。“若不是为了这两名加拿大人，加拿大早就表态说不会使用华为 5G 科技了，”一位外交消息人士表示。但政府官员们否认这两人的命运与 5G 有关。<br/>
　　2018年，澳洲和和新西兰都禁止服务提供商使用华为 5G 设备。可以肯定的是，未来某一天加拿大会做出一个决定。与加拿大官员沟通过的另外两位消息人士表示，他们认为加拿大发布禁令只是时间问题。<br/>
<br/>
......</blockquote>
<br/>
《<a href="https://www.dw.com/a-54184646" rel="nofollow" target="_blank">哪些国家禁用、限用华为 5G 技术 @ DW/德国之声</a>》<br/>
<blockquote>
　　英国政府本周（注：7月14日）宣布将华为全面排除在 5G 建设之外，几经反复后，英国终于顺应了华盛顿的要求。迄今为止有哪些国家对华为采取了禁用或限制措施？<br/>
<br/>
英国：<br/>
英国政府7月14日宣布，将禁止华为参与英国 5G 网建设，并将在2027年前拆除已经采用的华为设备。直到今年年初，英国首相约翰逊还曾部分允许华为参与 5G 网络建设。英国政府禁止使用华为技术，一方面是出于安全考虑，另一方面也是基于美国此前对华为推出的制裁措施可能带来的技术影响。<br/>
<br/>
美国：<br/>
今年6月30日，美国联邦通信委员会（FCC）将华为和另一家中国电信企业中兴列为对美国国家安全的威胁。由此，这两家公司在美国乡村地区的运营商用户必须将已经在使用的设备从网络中更换掉，同时不得使用金额为83亿美元的联邦通用服务基金的补贴购买华为和中兴的任何设备。今年5月，美国政府就已推出管制，禁止使用美国软件和技术的外国公司将半导体产品出售给华为。长期以来，华盛顿一直在向盟友施加压力，要求各国在 5G 网建设中不采用华为设备。<br/>
<br/>
澳大利亚：<br/>
2018年8月，澳大利亚就已将华为排除在该国 5G 网络建设之外。此外，澳大利亚曾计划让华为铺设通往所罗门群岛和巴布亚-新几内亚的海底通信光缆，但最终决定自行建设这一工程。<br/>
<br/>
新西兰：<br/>
2018年11月，新西兰政府同样以国家安全为理由，禁止无线网络营运商 Spark 在 5G 网络中使用华为技术。但 Spark 目前除了使用诺基亚和三星的产品，华为也仍是供货商之一。<br/>
<br/>
加拿大：<br/>
加拿大两家最大的电信运营商今年6月决定，与爱立信和诺基亚合作建设 5G 网络。到目前为止，加拿大政府尚未做出规定，是否允许华为为该国 5G 网络提供设备。<br/>
<br/>
日本：<br/>
2018年12月，日本推出规定，禁止部分公共机构的通信设备使用恐有国安疑虑的厂商产品。虽未直接指名道姓，但普遍认为这一做法实质上就是禁用华为等中国厂商制造的产品。日本媒体今年6月报道，日本政府近期将修改采购方针，追加禁用恐有国安疑虑的厂商产品的公共机构名单，被认为意在扩大禁用华为的机构范围。<br/>
<br/>
欧盟：<br/>
2020年1月，欧盟宣布，成员国可将“高风险”供货商排除在 5G 核心网络建设之外，或限制其设备技术的使用。这一步骤的针对目标即是华为。<br/>
<br/>
德国：<br/>
德国政府迄今未对是否在 5G 网络中禁用华为做出最后决定。普遍预测，柏林政府将在今年夏天之后再做决定。德国最大的电信运营商德国电信（Deutsche Telekom）多次警告，不应禁止单个供货商的产品。<br/>
<br/>
法国：<br/>
据法国国家网络安全署负责人波帕（Guillaume Poupard）称，法国不会完全禁止华为的网络技术，但将鼓励那些尚未使用华为技术的电信企业不选择这家中国公司的产品。<br/>
<br/>
意大利：<br/>
今年7月初，路透社援引消息人士报道，意大利电信（Telecom Italia）已经将华为排除在该公司正在准备于意大利和巴西进行的 5G 核心设备招标之外。此外意大利《共和国报》报道，意大利政府正在考虑是否将华为排除在 5G 建设项目之外。<br/>
<br/>
新加坡：<br/>
新加坡最大的电信公司今年6月决定选用诺基亚和爱立信产品建设该国的 5G 网络。<br/>
<br/>
印度：<br/>
印度媒体今年6月援引政府官员称，印度政府将禁止中国为任何国有电信运营商提供电信设备，也可能禁止私有运营商使用华为和中兴的设备。</blockquote>
<br/>
<br/>
<h3>◇关于“天朝的网络安全丑闻”</h3>
<br/>
《<a href="https://www.solidot.org/story?sid=64997" rel="nofollow" target="_blank">GoldenSpy 之前有 GoldenHelper @ Solidot</a>》<br/>
<blockquote>
上月底，安全公司 Trustwave 披露了藏身于航天信息股份有限公司智慧税务软件中的恶意后门 GoldenSpy。在这一报道公布之后，智慧税务软件下载了一个卸载程序，抹掉了所有 GoldenSpy 存在证据。<br/>
Trustwave 在后续调查中发现了另一个与金税发票软件相关的恶意程序，它也与航天信息有关联。虽然功能上与 GoldenSpy 差别很大，但两者有很多相似之处。研究人员根据其指令控制域名 help.tax-helper.ltd 将其命名为 GoldenHelper。GoldenHelper 活跃时间是在2018年1月到2019年7月，位于 GoldenSpy 之前，利用了多种技巧隐藏其恶意行为和逃避检测，包括随机生成文件名，用假的文件扩展如 .gif、.jpg 和 .zip 下载可执行文件，随机文件系统位置和时间戳，使用基于 IP 的域名生成算法去改变指令服务器位置，等等。GoldenHelper 使用了浙江诺诺网络科技有限公司的证书签名，该公司是航天信息的子公司。包含 GoldenHelper 的税务软件由百望云开发。百望云和航天信息是金税发票系统的两家官方供应商。<br/>
Trustwave 猜测，GoldenHelper 突然终止活动的原因可能是很多安全软件将其样本识别为恶意程序。</blockquote>
　　<b>编程随想注：</b><br/>
　　税务软件比较特殊，其安装具有某种【强制性】。用这种方式对【外企】植入后门，可谓用心良苦。<br/>
　　为了便于大伙儿理解上下文，把与之相关的前一篇报道也贴出来。下面这篇，在《<a href="../../2020/07/Security-News.md">近期安全动态和点评（2020年2季度）</a>》已经引用过。<br/>
<br/>
<br/>
《<a href="https://www.solidot.org/story?sid=64772" rel="nofollow" target="_blank">航天信息的智慧税务软件被指含有恶意程序 @ Solidot</a>》<br/>
<blockquote>
两家最近在中国开设办事处的英国公司被当地银行要求安装了航天信息股份有限公司的智慧税务软件，安全公司 Trustwave <a href="https://www.trustwave.com/en-us/resources/library/documents/the-golden-tax-department-and-the-emergence-of-goldenspy-malware/" rel="nofollow" target="_blank">称该税务软件包含了恶意程序</a>。Trustwave 为英国公司提供了网络安全服务，它观察到客户网络的可疑请求，它随后对税务软件进行了分析，发现它除了提供纳税功能外还包含了一个隐藏的后门，该后门被称为 GoldenSpy，具有系统级运行权限，允许远程攻击者连上被感染的系统，执行命令或上传和安装其它软件。<br/>
很多此类的软件都有远程访问功能以调试服务，但 Trustwave 称它发现的功能在恶意程序中更常见。GoldenSpy 安装了两个相同的版本作为持久性的自启服务；税务软件的卸载功能不卸载 GoldenSpy；GoldenSpy 是在税务软件安装两个小时后下载安装的，之后会悄悄运行；GoldenSpy 不连税务软件的网络基础设施，而是访问域名 ningzhidata.com</blockquote>
<br/>
《<a href="https://www.bleepingcomputer.com/news/security/new-goldenhelper-malware-found-in-official-chinese-tax-software/" rel="nofollow" target="_blank">New GoldenHelper malware found in official Chinese tax software @ BleepingComputer</a>》<br/>
　　<b>编程随想注：</b><br/>
　　关于天朝税务软件包含恶意木马（GoldenSpy ＆ GoldenHelper），上述这篇洋文报道写得比较详细。<br/>
<br/>
《<a href="https://www.solidot.org/story?sid=65537" rel="nofollow" target="_blank">深圳振华数据库泄露 @ Solidot</a>》<br/>
<blockquote>
整合境外数据信息为国内机构提供服务的深圳振华数据信息技术有限公司的<a href="https://www.theguardian.com/world/2020/sep/14/zhenhua-data-full-list-leak-database-personal-details-millions-china-tech-company" rel="nofollow" target="_blank">一个数据库外泄</a>。数据库包含了大约240万人的信息，绝大部分收集自社交网络。<br/>
澳大利亚堪培拉的网络安全咨询公司 Internet 2.0 分析了其中25万人的记录，有5.2万美国人、3.5万澳洲人和1万英国人。<b>这些数据包括了政客，如英国首相 Boris Johnson，政客的亲戚、王室、名人和军人。</b><br/>
深圳振华的一名发言人表示，这只是数据整合，该公司否认与中国政府或军方有关联，称其客户主要为研究组织和商业团体。</blockquote>
　　<b>编程随想注：</b><br/>
　　对于天朝公司而言，不管有没有与中国军方合作，都会【否认】这点（原因你懂的）。因此，深圳振华的上述官方声明，毫无意义。<br/>
<br/>
<br/>
<h2>★网络攻击</h2>
<br/>
<h3>◇推特（Twitter）遭遇史诗级的“帐号劫持攻击”</h3>
<br/>
《<a href="https://www.bbc.com/zhongwen/simp/science-53429460" rel="nofollow" target="_blank">美国多个名人推特账户遭黑客攻击，发送比特币诈骗信息 @ BBC/英国广播公司</a>》<br/>
<blockquote>
......<br/>
<br/>
　　“这可能是目前主流社交媒体平台遭受的最严重的一次黑客攻击，”网络安全公司 CrowdStrike 联合创始人阿帕洛维奇（Dmitri Alperovitch）向路透社表示。<br/>
　　最开始，由特斯拉（Tesla）及 SpaceX 所有人马斯克的官方账号发出的几条推文声称，他会在“接下来30分钟”对向他数字钱包地址支付的比特币作出双倍返还。<br/>
　　“受新冠肺炎影响，我想要慷慨一点，”那则推文称，还附上了一个比特币链接地址。<br/>
<br/>
　　这些推文在发出后数分钟内便被删除。但在马斯克最初的推文被移除后，又陆续出现了第二、第三号“中招”人物。其他被攻击的账号包括：<ul>
<li>饶舌歌手坎耶·韦斯特</li>
<li>韦斯特的妻子、电视真人秀明星金·卡戴珊（Kim Kardashian）</li>
<li>美国前总统奥巴马</li>
<li>美国前副总统拜登，他同时还是民主党本届总统候选人</li>
<li>媒体巨头麦克·布隆伯格（Mike Bloomberg）</li>
<li>拼车软件优步（Uber）</li>
<li>苹果（Apple）</li>
</ul>
......<br/>
<br/>
　　这些“比特币翻倍”骗局在推特上已经存在多年，但这次史无前例地出现大范围的公众人物账号被攻击。<br/>
　　如此多不同的账号同时被攻入说明，这是推特平台自身的问题。事件发生之初，一些说法认为，是有人设法获取了一定程度的管理权限，可以绕过所有他们想要的账户的密码。<br/>
　　如果拥有这种权力，这些侵入者本可以造成更大程度的破坏，他们也本可以使用看上去措辞更加睿智的推文，可以用此来伤害他人或者其他机构的声誉。但他们的动机看上去很明确，即用最短的时间赚最多数量的金钱。这些黑客应该已经清楚，这些推文不会在网络上停留很久，所以这正是一次“破窗抢劫”行动。<br/>
<br/>
......</blockquote>
<br/>
《<a href="https://www.solidot.org/story?sid=65105" rel="nofollow" target="_blank">Twitter 称：黑客利用手机钓鱼攻击窃取员工凭证 @ Solidot</a>》<br/>
<blockquote>
Twitter 官方博客<a href="https://blog.twitter.com/en_us/topics/company/2020/an-update-on-our-security-incident.html" rel="nofollow" target="_blank">披露</a>了黑客攻击的更多细节：7月15日，攻击者对少数 Twitter 员工发动手机钓鱼攻击，成功的攻击不仅让攻击者能访问公司内网，还能利用特定员工凭证访问内部支持工具。在利用凭证访问内部系统之后攻击者获得了 Twitter 内部流程的情报（比如谁能访问账号管理工具）。然后利用这些情报攻击者针对了能访问账号管理工具的员工，使用这些员工的凭证攻击者劫持了130个账号，使用其中45个账号发帖，访问了36个账号的 DM 私信，下载了7个账号的数据。Twitter 表示它仍然在继续进行调查，与执法机构合作识别攻击者的身份。</blockquote>
　　<b>编程随想注：</b><br/>
　　Twitter 官方承认：是公司自己的雇员遭遇【社会工程学】类型的攻击。去年（2019）推特 CEO 的推特帐号被劫持，攻击者也是采用【社会工程学】的手法。差别在于——去年的“社会工程学”是针对手机运营商的员工（以实现“SIM 卡劫持攻击”，参见“<a href="../../2019/09/Security-News.md">这篇博文</a>”），而今年这次是针对 Twitter 的内部员工。<br/>
　　“社会工程学”利用的是【人的弱点】——而这往往是最难防御滴。对这个领域感兴趣的同学，可以看俺网盘上分享的2本书：<br/>
《<a href="https://docs.google.com/document/d/1nQXEKqw6WrrgblIdJQ8V-WBxyGcCtw3oxgfgRkA1iGw/" target="_blank">欺骗的艺术</a>》（作者是大名鼎鼎的【凯文·米特尼克 / Kevin Mitnick】）<br/>
《<a href="https://docs.google.com/document/d/188NKsl2wukTXlvDkTwJI3OgOpGkziNLi27PlWFbGsEk/" target="_blank">社会工程——安全体系中的人性漏洞</a>》<br/>
<br/>
<h3>◇勒索软件</h3>
<br/>
《<a href="https://it.slashdot.org/story/20/09/10/1829253/" rel="nofollow" target="_blank">Ransomware Accounted For 41% of All Cyber Insurance Claims in H1 2020 @ Slashdot</a>》<br/>
<br/>
《<a href="https://www.solidot.org/story?sid=65515" rel="nofollow" target="_blank">勒索软件占到了上半年网络保险索赔的 41% @ Solidot</a>》<br/>
<blockquote>
根据北美网络保险服务商 Coalition 的报告，今年上半年勒索软件占到了所有网络保险索赔的 41%。这证实了网络安全公司早先发布的报告：勒索软件是今天最为普遍且最具有破坏性的威胁。Coalition 称，勒索软件不针对某个特别行业，几乎每一个行业都看到越来越多的勒索软件攻击。最具有破坏性的勒索软件网络黑帮是 Maze 和 DoppelPaymer，这些勒索软件除了加密数据进行勒索外，还会窃取数据威胁公开数据进行二次勒索（如果第一次勒索失败的话）。Coalition 称，Maze 网络黑帮是最贪得无厌的，它索要的赎金六倍于平均水平。</blockquote>
　　<b>编程随想注：</b><br/>
　　3年前（2017）发过一篇《<a href="../../2017/05/Ransomware-Cyber-Attack.md">勒索软件是骇客攻击的新趋势，兼谈防范措施及各种误解</a>》。当年俺警告的【新趋势】，如今已经成为【主流】了。<br/>
<br/>
<h3>◇Tor 出口节点的蜜罐，及其危险性</h3>
<br/>
《<a href="https://www.solidot.org/story?sid=65203" rel="nofollow" target="_blank">恶意 Tor 出口节点如何利用用户 @ Solidot</a>》<br/>
<blockquote>
Tor 出口节点是构成 Tor 回路的三个中继的最后一跳，连接了 Tor 匿名网络与开放互联网。根据目标网站使用的是 HTTPS 还是 HTTP 协议，决定了出口节点是否能看到和操纵用户访问的内容。<br/>
研究人员报告，<a href="https://medium.com/@nusenu/how-malicious-tor-relays-are-exploiting-users-in-2020-part-i-1097575c0cac" rel="nofollow" target="_blank">恶意 Tor 出口节点的情况过去几个月恶化了</a>，恶意出口节点的比例占到了所有出口节点的 24%，这意味着 Tor 浏览器用户有很高的可能性会通过恶意出口节点访问目标网站。<br/>
恶意出口节点背后的运营者会对 Tor 用户发动中间人攻击，选择性的移除 HTTP-to-HTTPS 重定向，利用被称为 ssl stripping 的方法让目标网站通过 HTTP 而不是 HTTPS 加密连接访问，攻击者将能看到 Tor 用户访问的明文内容，并根据需要修改传输的内容。攻击者主要针对的是数字货币相关的网站，会修改 HTTP 明文流量中的钱包地址，用自己控制的钱包地址替换用户传输的地址，窃取比特币。此类的攻击并非罕见，但攻击规模如此巨大则是前所未有。</blockquote>
　　<b>编程随想注：</b><br/>
　　考虑到俺的读者中，Tor 用户的比例越来越高，再次唠叨一下“蜜罐节点”的几点注意事项。<br/>
<b>第1点</b><br/>
在 Tor 匿名网络的“三级跳”中，只有【出口节点】能看到你的【真实上网流量】。<br/>
不熟悉 Tor 的同学，请参见《<a href="../../2013/11/tor-faq.md">关于 Tor 的常见问题解答</a>》<br/>
<b>第2点</b><br/>
为了尽可能防范【蜜罐节点】，你要尽量做到【全程加密/全程 HTTPS】（如今 HTTPS 已经非常普及，做到这点不难）。<br/>
万一某个网站【不】支持 HTTPS 加密（只支持明文 HTTP 协议），当你访问该网站的时候，确保浏览器【禁用】JS 脚本。<br/>
（注：对明文的 HTTP 协议，出口节点理论上可以修改你的 HTTP 流量，并植入【恶意】的 JS 脚本）<br/>
<b>第3点</b><br/>
当你采用【全程 HTTPS】之后，接下来要注意的是——证书的风险。也就是说，你要清理操作系统和浏览器内置的那些【流氓 CA 机构】颁发的证书。<br/>
十年前（2010）俺写过一篇《<a href="../../2010/02/remove-cnnic-cert.md">CNNIC 证书的危害及各种清除方法</a>》。由于 CNNIC 的名声太臭，如今很多操作系统及浏览器已经不再内置它的根证书了。但还会有其它流氓冒出来（比如后来又出了个<a href="../../2016/09/About-WoSign.md">流氓 CA“沃通”</a>）。所以，上述这篇博文介绍的清除手段，依然值得参考。<br/>
<b>第4点</b><br/>
“恶意出口节点”可能会使用名为“ssl stripping”的招数。这招中文叫做“SSL 剥离攻击”，属于“中间人攻击”这个大类的一种。通俗地说，那些帮你中转上网流量的设备（中间人）可以利用某些机会，把“加密的 HTTPS”降级为“明文的 HTTP”。（注：大部分支持 HTTPS 加密的网站，为了向下兼容，同时也支持明文的 HTTP 协议）<br/>
为了消除“SSL 剥离攻击”，IETF（互联网工程任务组）发布了 <a href="https://zh.wikipedia.org/wiki/HTTP%E4%B8%A5%E6%A0%BC%E4%BC%A0%E8%BE%93%E5%AE%89%E5%85%A8" rel="nofollow" target="_blank">HSTS 标准</a>，可以让浏览器与网站之间【强制】采用 HTTPS 协议。<br/>
所以，你要确保你的浏览器启用了 HSTS 机制。<br/>
<br/>
<br/>
<h2>★言论审查与网络屏蔽</h2>
<br/>
<h3>◇老流氓“奇虎/360”搞了个【翻墙浏览器】——讽刺的是，出道即死亡</h3>
<br/>
《<a href="https://www.dw.com/a-55229513" rel="nofollow" target="_blank">Tuber 浏览器，自由世界的昙花一现？ @ DW/德国之声</a>》<br/>
<blockquote>
　　近日，一个叫做 Tuber 的浏览器据称是“刷爆了朋友圈”，从中文网络上的相关消息来看，这是一款可以让中国境内的用户不用安装翻墙软件，就浏览包括 YouTube、脸书、Tiwtter、Netflix 等在中国被屏蔽网站的浏览器。<br/>
　　在“新浪科技”的“自媒体综合”领域，日前原本有一篇文章题为“刷爆朋友圈的 Tuber 浏览器到底什么来头”，其中援引浏览器的出品方报道称，Tuber 已经通过相关主管部门的审核，获得上线经营许可，目前 APP 并在国内各大应用商店已经上线。名为“拾黑”的自媒体账号表示，“有备案”的拿到了许可，“未免对这个应用产生了兴趣。”<br/>
　　然而截止到10月10日，在新浪的相关网站上已经无法看到这篇文章。同时在安卓的 Goggle Play 应用商店以“Tuber”、“Tuber 浏览器”、“Tuber Browser”为关键词搜索，也无法站到下载获得该应用软件的任何信息。搜索中国腾讯公司提供的 APP 下载商店“应用宝”，也无法找到相关软件的信息。<br/>
　　路透社报道称，Tuber 的出品方是奇虎360旗下的一家企业，通过第三方安卓商店提供下载服务。而奇虎360是中国最大的网络安全技术公司，该软件曾经被下载了数百万次，但无法在苹果的 APP 引用商店中找到。<br/>
......<br/>
　　目前在360应用商店中也完全找不到这款浏览器。中国国内互联网的搜索也找不到任何有关 Tuber 浏览器的信息。<br/>
......</blockquote>
　　<b>编程随想注：</b><br/>
　　这个“Tuber 浏览器”刚公布的时候，民间就纷纷揣测——这到底是360公司自己的意图，还是真理部（或朝廷更高层）的授意？<br/>
　　既然这个浏览器才出来【一天】就被彻底和谐掉，看来是老流氓360自己的行为。<br/>
　　另外，就算这款浏览器没有死掉，俺也奉劝大伙儿【别用】。以老流氓360的德行，这玩意儿简直是钓鱼的利器——（据报道）使用该浏览器先要【实名注册】。如此一来，有关部门就可以很容易地统计出【哪些人热衷于翻墙】。<br/>
<br/>
<h3>◇“墙”与“翻墙”的技术对抗</h3>
<br/>
《<a href="https://www.solidot.org/story?sid=65185" rel="nofollow" target="_blank">防火墙（GFW）开始屏蔽 ESNI @ Solidot</a>》<br/>
<blockquote>
<a href="https://gfw.report/blog/gfw_esni_blocking/zh/" rel="nofollow" target="_blank">防火墙被发现开始屏蔽 ESNI</a>（加密服务器名称指示）。TLS 1.3 引入了 ESNI（尚未成为正式规格），用加密的 SNI 阻止中间人查看客户端要访问的特定网站。因为不知道用户使用 ESNI 访问的网站，审查者要么不封锁任何 ESNI 连接，要么封锁所有的 ESNI 连接。防火墙选择了后者。测试发现，防火墙通过丢弃从客户端到服务器的数据包来阻止 ESNI 连接。此外，ESNI 封锁不仅会发生在443端口，也会发生在1到65535的所有端口。在阻断 ESNI 握手后，防火墙会继续阻断与（源 IP，目标 IP，目标端口）3元组相关的任何连接一段时间。</blockquote>
　　<b>编程随想注：</b><br/>
　　TLS 协议中的 ESNI 规范刚刚推出不久，还不够普及。因此 GFW 可以采用“全部封杀”的策略；但等到这个标准足够普及了，GFW 再用“全部封杀 ESNI”这个策略，【副作用】就会很大。<br/>
　　总而言之，随着【加密协议】用得越来越多，加密的范围也越来越广，GFW 面临的挑战也越来越大。<br/>
　　另外，在《<a href="../../2014/11/https-ssl-tls-0.md">扫盲 HTTPS 和 SSL/TLS 协议</a>》系列教程的后续博文，俺会找机会单独聊聊 SNI ＆ ESNI 的话题。<br/>
<br/>
《<a href="https://www.solidot.org/story?sid=65344" rel="nofollow" target="_blank">揭秘防火墙（GFW）的 DNS 审查行为 @ Solidot</a>》<br/>
<blockquote>
在本月举行的 USENIX FOCI 20 会议上，研究人员<a href="https://www.usenix.org/conference/foci20/presentation/anonymous" rel="nofollow" target="_blank">报告了</a>对防火墙 DNS 包注入行为的分析（<a href="https://www.usenix.org/system/files/foci20-paper-anonymous_0.pdf" rel="nofollow" target="_blank">PDF</a>）。从2019年9月到2020年5月，研究人员调查了 Alexa 排名前一百万的域名，发现在调查期间被劫持的域名数量从23,995增加到了24,636个，其中 46% 属于“Proxy Avoidance” 类别，以 .blogspot.com 或 .tumblr.com 结尾的个人网站域名也遭到大规模劫持。<br/>
......</blockquote>
<br/>
《<a href="https://www.zdnet.com/article/def-con-new-tool-brings-back-domain-fronting-as-domain-hiding/" rel="nofollow" target="_blank">New tool brings back 'domain fronting' as 'domain hiding' @ ZDNet</a>》<br/>
<br/>
《<a href="https://www.solidot.org/story?sid=65193" rel="nofollow" target="_blank">新工具用“域隐藏”代替“域前置” @ Solidot</a>》<br/>
<blockquote>
在上周举行的 DEF CON 28 安全会议上，安全公司 SixGen 的 CTO Erik Hunstad <a href="https://www.zdnet.com/article/def-con-new-tool-brings-back-domain-fronting-as-domain-hiding/" rel="nofollow" target="_blank">发布了</a>开源工具 Noctilucent，帮助应用开发者逃避审查和绕过防火墙。源代码的不同组件采用 BSD 和 GPL 许可证，<a href="https://github.com/SixGenInc/Noctilucent" rel="nofollow" target="_blank">发布在 GitHub 上</a>。<br/>
Noctilucent 设计从某种程度上复活被众多云服务商禁止的域前置（Domain fronting）功能。域前置是一种隐藏连接真实端点来规避审查的技术，其原理为在不同通信层使用不同的域名，在明文的 DNS 请求和 TLS 服务器名称指示中使用无害的域名来初始化连接，而实际要连接的被封锁域名仅在创建加密的 HTTPS 连接后发出，使其不以明文暴露给网络审查者。新的技术被称为域隐藏，能实现域前置的隐藏真实域名的目的。它比域前置更灵活，只需要把域名 DNS 记录托管在 Cloudflare，而主机服务器可以托管在任何地方。</blockquote>
<br/>
《<a href="https://www.solidot.org/story?sid=65364" rel="nofollow" target="_blank">抵抗主动探测的代理 HTTPT @ Solidot</a>》<br/>
<blockquote>
为了探测和屏蔽代理服务器，审查者越来越多的使用主动探测攻击，即使用已知的代理协议向可疑的服务器尝试进行握手，如果服务器回应了，那么审查者将会知道它是代理服务器，然后将其屏蔽。<br/>
为了对抗主动探测攻击，Tor 等项目的开发者开发了 obfs4 等能抵抗探测的协议。但这些协议被发现存在指纹，审查者仍然能将其识别出来。此外审查者还能利用重放攻击去识别此类的代理服务器。<br/>
科罗拉多 Boulder 的研究人员<a href="https://www.usenix.org/system/files/foci20-paper-frolov.pdf" rel="nofollow" target="_blank">提出了一种新的代理原型 HTTPT</a>，基于现有的 Web 服务器和广泛使用 HTTPS 协议，能对主动探测返回标准的 TLS 响应，加大其识别的难度。他们的代码发布在 GitHub 上。</blockquote>
<br/>
<h3>◇白俄罗斯的“Telegram 革命”</h3>
<br/>
《<a href="https://www.storm.mg/article/2966665" rel="nofollow" target="_blank">全國逾1/4民眾靠它傳遞訊息！白羅斯反獨裁示威者掀起「Telegram 革命」 @ 風傳媒</a>》<br/>
<blockquote>
　　從8月9日開始，白羅斯掀起史無前例的大規模示威，9日總統大選之後，在位26年的現任總統盧卡申科（Alexander Lukashenko），以囊括8成得票的壓倒性優勢「六連霸」，但反對勢力在選前選後處處遭政府打壓，官方計票也與民間監票結果有巨大落差，徹底引燃排山倒海的民怨。<br/>
　　示威之中，警察以震撼彈、橡膠子彈對付和平示威者，超過6700人被濫捕關押，很多人被毒打、虐待並施以非人道囚禁；反對派總統候選人蒂卡諾夫斯卡婭（Svetlana Tikhanovskaya）聲稱受威脅而逃到立陶宛；當局還一度封鎖網路，讓民眾無法接觸獨立新聞網站或社群媒體，示威者似乎也頓失龍頭。<br/>
　　全球通行的軟體 Telegram 就是在此刻登場，高度隱私的加密技術，讓上面任何通訊都難以追查真實身分，早在2019年開始的香港反送中運動中，Telegram 已經爆紅，是名符其實的「抗爭神器」，如今為白羅斯人民所用。<br/>
　　美聯社（AP）報導，Telegram 有成千上萬個由普通人開設的「頻道」（群組），白羅斯抗爭者在這些頻道發布政治新聞，時時更新抗爭現場的影片、照片與其他資訊，包括重裝警察聚集地點、人權組織聯絡方式，或是直接號召新的抗議行動等等，動輒吸引數萬人參加。頻道內為抗爭者打氣的重重貼文，也不乏引述香港運動口號「Be Water！」（如水聚散）的訊息。<br/>
<br/>
......</blockquote>
<br/>
《<a href="https://www.solidot.org/story?sid=65371" rel="nofollow" target="_blank">白俄试图限制互联网访问，但失败了 @ Solidot</a>》<br/>
<blockquote>
本月初总统选举期间以及之后发生的大规模民众抗议，白俄曾尝试关闭互联网，限制流行社交平台和应用的访问，但它的策略没有获得成功。IT 可能是白俄最重要的出口行业，彻底关闭互联网对政府而言并非是一个可行的策略。至于限制流行社交平台，它使用的审查技术没有先进到能让大部分人无法访问。<br/>
消息应用 Telegram 的创始人 Pavel Durov 在8月10日称，他们在白俄启用了反审查工具，对大部分用户恢复了 Telegram 的访问。政府对互联网的限制导致 VPN 使用大幅增长。在白俄的 Google Play 应用商店，Psiphon、X-VPN、Tachyon VPN 和 VPN Proxy Master 是8月9日下载量最高的4个应用。Psiphon（注：赛风）的 Michael Hull 称，8月11日 Psiphon 在白俄的用户数突破了175万。白俄使用 DPI 去审查域名，而 Telegram 通过使用 IP 地址绕过了对域名的审查。</blockquote>
<br/>
<br/>
<h2>★密码学</h2>
<br/>
《<a href="https://www.solidot.org/story?sid=65050" rel="nofollow" target="_blank">美国制定计划，发展国家量子互联网 @ Solidot</a>》<br/>
<blockquote>
美国能源部发布了发展国家量子互联网的蓝图。能源部将与大学和行业研究人员合作，计划在十年内打造出一个原型。美国的量子互联网将是基于量子纠缠，能源部称量子传输的一大特征是它难以被窃听。采用量子互联网的早期用户可能包括金融和医疗保健行业，以及国家安全应用和航空通信。能源部的17个国家实验室将充当量子互联网的主干。<br/>
中国在2017年宣布建成了量子通信的京沪干线，<b>但这并非量子互联网，而是量子密钥分发（QKD）</b>，京沪干线全长2000公里，连接北京、济南、合肥和上海四个城市，使用 QKD 加密和解密数据。京沪干线此后很少有新闻报道，反而不时传出对其质疑的声音，认为它缺乏实用价值。</blockquote>
　　<b>编程随想注：</b><br/>
　　前一篇博文《<a href="../../2020/09/Academic-Scandals-in-China.md">二十年目睹之怪现状——中国学术界、科技界的“奇葩排行榜”</a>》发出后，有读者在评论区询问了天朝的“量子通讯”，俺在回复该读者时，已经从信息安全的角度点评了——潘建伟搞的量子通讯，存在哪些忽悠之处。<br/>
　　今天正好转贴了这篇报道，顺便也聊聊天朝的“量子通讯”。<br/>
<br/>
　　（俺已经猜到）某些潘建伟的粉丝会指责说：编程随想不懂量子力学，还想质疑“量子纠缠”。<br/>
　　所以，在吐槽潘建伟同学之前，有必要先声明一下：<br/>
俺并【不】质疑“量子纠缠”这个理论本身。恰恰相反，俺还比较看好“量子纠缠”在未来的应用。（有时间的话，可以考虑写一篇“量子力学”相关的扫盲教程，顺便扫盲“量子怪诞性、量子纠缠、量子计算”等概念）<br/>
<br/>
　　为了避免“稻草人谬误”，俺直接引述潘建伟的【原话】：<q>使用量子密钥分发技术可以帮助实现通信安全中机密性、真实性和不可否认性的<b>无条件安全</b>，也就是说，保证通信加密无法破译，保证对方身份真实可靠，保证信息无法被篡改。</q><br/>
（注：这段话的出处参见全国政协官网的“<a href="http://www.cppcc.gov.cn/zxww/2019/03/07/ARTI1551922571648232.shtml" rel="nofollow" target="_blank">这个链接</a>”，另附上“<a href="https://web.archive.org/web/20190910234634/http://www.cppcc.gov.cn/zxww/2019/03/07/ARTI1551922571648232.shtml" rel="nofollow" target="_blank">网页存档</a>”）<br/>
<br/>
　　比较熟悉“信息安全”的，看到所谓的“绝对安全 or 无条件安全”，通常都会哑然失笑。<br/>
　　潘建伟有几个值得吐槽的地方，其中一个是：他只不过搞了个“量子密钥分发”，就敢吹嘘“无条件安全”。<br/>
　　请注意：“密钥分发”只是【密码学体系】中一个很小的环节。光保证“密钥分发”的安全性，有个屁用啊？！<br/>
　　为了让密码学的菜鸟理解，俺来打个比方——<br/>
你担心小偷入室盗窃，就很仔细地藏好你的大门钥匙（让小偷无论如何都拿不到你的钥匙）。但如果你家的大门不够牢固，小偷直接踹门就进去了，根本【不需要】窃取你的钥匙。<br/>
<br/>
　　难道潘建伟同学不懂【密码学体系】？应该不至于吧。就算他本人不懂，他的团队中，总有人懂吧。但潘同学经常在公开场合故意混淆“量子密钥分发”与“量子通讯”这两个概念（注：前者只是后者的一个很小的子集）。他为啥要这么忽悠捏？因为“量子通讯”听起来更【高大上】——越高大上的术语，忽悠的效果越好（能搞来更多的国家经费）<br/>
　　如果你不信的话，可以回顾前一篇博文《<a href="../../2020/09/Academic-Scandals-in-China.md">二十年目睹之怪现状——中国学术界、科技界的“奇葩排行榜”</a>》，看看最近20年，天朝的科技界吹破了多少牛皮。<br/>
<br/>
<br/>
<h2>★安全工具</h2>
<br/>
《<a href="https://blog.torproject.org/new-release-tor-browser-100" rel="nofollow" target="_blank">New Release: Tor Browser 10 @ Tor 官方博客</a>》<br/>
<br/>
　　<b>编程随想注：</b><br/>
　　长期看本博客的，对“Tor Browser”应该都比较熟悉了。<br/>
　　9月份新出炉的 Tor Browser 10 是基于 Firefox 78.3.0 ESR 版本，Tor 版本升级为0.4.4.5，浏览器内置的 NoScript 扩展升级为11.0.44，默认禁用 TLS 1.0 ＆ TLS 1.1 协议（注：TLS 1.2 更安全，而且该标准已经发布很久了）。<br/>
　　俺已经把 Tor Browser 10.0.x 版本上传到【BTsync 网盘】。该网盘汇总了一些常见的翻墙工具，同步密钥如下：<br/>
<pre>BTLZ4A4UD3PEWKPLLWEOKH3W7OQJKFPLG</pre>
<br/>
《<a href="https://www.solidot.org/story?sid=65137" rel="nofollow" target="_blank">黑莓开源其逆向工程 PE 的工具 @ Solidot</a>》<br/>
<blockquote>
黑莓公司在 Black Hat USA 2020 大会上<a href="https://www.zdnet.com/article/blackberry-releases-new-security-tool-for-reverse-engineering-pe-files/" rel="nofollow" target="_blank">开源了</a>其逆向工程 PE 文件的工具 PE Tree，源代码采用许可证 Apache License 2.0 发布在 GitHub 上。Portable Executable（PE）文件常被恶意程序作者隐藏恶意负荷。PE Tree 基于 Python，能用于逆向工程和分析 PE 文件的内部结构。黑莓称，逆向工程是一个极端的耗费时间和劳动密集过程，需要数小时的反汇编，有时候还需要重建软件程序。</blockquote>
<br/>
<br/>
<h2>★安全编程</h2>
<br/>
<h3>◇用 Rust 开发 Linux 内核模块</h3>
<br/>
　　<b>编程随想注：</b><br/>
　　在之前的几次《近期安全动态和点评》都有聊过 Rust 的话题。关于它的特性（优缺点），这里就不重复唠叨了。<br/>
<br/>
《<a href="https://www.oschina.net/news/117139/linus-linux-rust-support-remark" rel="nofollow" target="_blank">Linus Torvalds 对 Linux 内核支持 Rust 的看法——默认可以启用 @ 开源中国</a>》<br/>
<blockquote>
　　去年就有开发者询问 Linux 内核稳定版维护者 Greg Kroah-Hartman “Linux 有没有想法拥抱 Rust”，Greg 表示愿意接受用 Rust 开发 Linux 内核的驱动程序，但前提是：<br/>
1、以可选的方式存在，而不是默认启用，这样其他开发者就不需要使用 Rust 去构建内核<br/>
2、Rust 驱动需要体现出比 C 驱动具有优势，比如针对内核 API 的安全封装器<br/>
<br/>
　　此次 Linus 关于 Linux 支持 Rust 的回应看上去正是针对这第1个条件。<br/>
　　Greg 希望 Linux 中的 Rust 支持是以可选的方式存在，而不能全面默认启用，类似于在一个大的系统配置项里还要单独开启一个针对 Rust 的小选项，但 Linus 则认为应该在默认情况下可以有效地启用支持，以确保进行广泛的测试，而不是只有某些开发者孤立地在进行疯狂/错误的使用，因为没有人关注，问题会被掩盖。<br/>
　　同时，Linus 还用 Kconfig 的使用指令举例，表示 Rust 支持需要足够简洁，类似“config RUST_IS_AVAILABLE……”，Linus 认为如果在系统上检测到 Rust 编译器，则 Kconfig 将启用 Rust 支持，并继续构建任何假定的 Rust 内核代码，以至少查看其是否正确构建。“我希望以如此简单的格式引入第一个 Rust 驱动程序（或其它任何驱动程序），以使故障显而易见且简单。”</blockquote>
<br/>
　　<b>编程随想注：</b><br/>
　　在前不久（8月）举办的 2020 Linux Plumbers 大会上，关于“内核如何支持 Rust”成为会议中最热门的话题。详细的技术报道参见如下这篇：<br/>
《<a href="https://lwn.net/Articles/829858/" rel="nofollow" target="_blank">Supporting Linux kernel development in Rust @ LWN</a>》<br/>
<br/>
<h3>◇Amazon 新鲜出炉的发行版——号称大量使用 Rust</h3>
<br/>
《<a href="https://linux.slashdot.org/story/20/09/04/2342226/" rel="nofollow" target="_blank">AWS Introduces a Rust Language-Oriented Linux for Containers @ Slashdot</a>》<br/>
<br/>
《<a href="https://www.solidot.org/story?sid=65468" rel="nofollow" target="_blank">AWS 推出用 Rust 开发的容器发行版 Bottlerocket @ Solidot</a>》<br/>
<blockquote>
Mozilla 可能终止了对 Rust 语言的资助，但有 Linux 项目的支持和加持，它的未来还是安全的。<br/>
亚马逊 Amazon Web Services（AWS）服务发布了主要用 Rust 语言开发的发行版 Bottlerocket，设计用于托管容器。<a href="https://github.com/bottlerocket-os" rel="nofollow" target="_blank">源代码</a>发布在 GitHub 上。<br/>
作为一种专注于安全、速度和并发的系统级编程语言，Rust 能避免常见的编程错误如访问无效的内存区和竞态条件。AWS 产品经理 Samartha Chandrashekar 称，Rust 帮助确保线程安全和防止内存相关的错误，如能导致安全漏洞的缓冲溢出。</blockquote>
　　<b>编程随想注：</b><br/>
　　上述文章的标题可能会引发某些歧义，稍微说明一下：<br/>
　　这个 Bottlerocket 依然算是“Linux 发行版”。到目前为止，Linux 内核依然是以【C 语言】为主（另有少量汇编）。所以，Bottlerocket 的【内核】显然是 C 语言。<br/>
　　那为啥号称“用 Rust 开发”捏？根据 <a href="https://aws.amazon.com/blogs/opensource/announcing-the-general-availability-of-bottlerocket-an-open-source-linux-distribution-purpose-built-to-run-containers/" rel="nofollow" target="_blank">Amazon 官方博客</a>的说法是：<q>Large parts of Bottlerocket are written in Rust</q><br/>
<br/>
<br/>
<h2>★硬件与物理安全</h2>
<br/>
《<a href="https://mobile.slashdot.org/story/20/08/08/180203/" rel="nofollow" target="_blank">Millions of Android Phones At Risk Due to 'Achilles' Flaw in Qualcomm Chips @ Slashdot</a>》<br/>
<br/>
《<a href="https://www.solidot.org/story?sid=65198" rel="nofollow" target="_blank">高通 DSP 芯片漏洞影响大量 Android 设备 @ Solidot</a>》<br/>
<blockquote>
安全公司 Check Point 报告在高通公司骁龙芯片的数字信号处理器（DSP）中<a href="https://arstechnica.com/information-technology/2020/08/snapdragon-chip-flaws-put-1-billion-android-phones-at-risk-of-data-theft/" rel="nofollow" target="_blank">发现了</a>400多个漏洞，它将这些漏洞统称为 Achilles。<br/>
高通的芯片占据了移动手机市场份额的四成以上，这意味着会有数以亿计的 Android 手机受到影响。Check Point 称，利用漏洞攻击者可以将手机转变成完美的间谍工具，无需用户的任何互动；攻击者可以对手机发动拒绝访问攻击，使其无法使用；恶意程序可以彻底隐藏其活动，无法移除。高通已经释出了补丁，但至今为止补丁还没有整合进 Android 操作系统或使用骁龙芯片的 Android 设备中。高通在一份声明中表示，它还没有看到有证据显示这些漏洞正被利用，它建议用户在补丁可用后尽快更新设备。</blockquote>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2019/01/Security-Guide-for-Political-Activists.md">为啥朝廷总抓不到俺——十年反党活动的安全经验汇总</a>》<br/>
《<a href="../../2013/06/privacy-protection-0.md">如何保护隐私</a>》（系列）<br/>
《<a href="../../2010/06/howto-prevent-hacker-attack-0.md">如何防止黑客入侵</a>》（系列）<br/>
《<a href="../../2010/04/howto-cover-your-tracks-0.md">如何隐藏你的踪迹，避免跨省追捕</a>》（系列）<br/>
《<a href="../../2014/11/https-ssl-tls-0.md">扫盲 HTTPS 和 SSL/TLS 协议</a>》（系列）<br/>
《<a href="../../2013/11/tor-faq.md">关于 Tor 的常见问题解答</a>》<br/>
《<a href="../../2017/05/Ransomware-Cyber-Attack.md">勒索软件是骇客攻击的新趋势，兼谈防范措施及各种误解</a>》<br/>
《<a href="../../2020/07/Security-News.md">近期安全动态和点评（2020年2季度）</a>》<br/>
《<a href="../../2020/04/Security-News.md">近期安全动态和点评（2020年1季度）</a>》<br/>
《<a href="../../2019/09/Security-News.md">近期安全动态和点评（2019年3季度）</a>》<br/>
《<a href="../../2010/02/remove-cnnic-cert.md">CNNIC 证书的危害及各种清除方法</a>》<br/>
《<a href="../../2016/09/About-WoSign.md">老流氓 CNNIC 的接班人——聊聊“沃通/WoSign”的那些破事儿</a>》<br/>
《<a href="../../2013/06/usa-vs-china.md">中美政府信息监控的差异——“棱镜门”丑闻随想</a>》<br/>
《<a href="../../2020/09/Academic-Scandals-in-China.md">二十年目睹之怪现状——中国学术界、科技界的“奇葩排行榜”</a>》
<!--BANNED
[1602503939021,1602505982687,1602520800893,1602521753340,1602527229197,1602560068730,1602584400544,1602646054057,1602665057863,1602665271532
,1602665650835,1602733933477,1602734035158,1602734102745,1602770049232,1602774100413,1602775135673,1602775224354,1602776491389,1602776891418
,1602783108576,1602821544774,1602836672096,1602836714036,1602836951383,1602845489626,1602845672402,1602849186726,1602849538981,1602850926977
,1602857042423,1602857205207,1602857263244,1602859297256,1602859860766,1602937588674,1602942208584,1602946090460,1602946318516,1602955966873
,1602956009393,1602956129355,1602962260148,1602962624323,1602962909591,1603017460227,1603017616845,1603017683349,1603017799589,1603018684257
,1603021658342,1603022368308,1603023959688,1603024007197,1603028006624,1603034532201,1603038170261,1603038231346,1603038299726,1603038601280
,1603039057880,1603039619544]
-->
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2020/10/Security-News.html
