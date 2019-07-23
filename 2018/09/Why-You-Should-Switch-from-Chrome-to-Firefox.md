# 弃用 Chrome 改用 Firefox 的几点理由——关于 Chrome 69 隐私丑闻的随想 

-----

<div class="post-body entry-content">
<center><img alt="不见图 请翻墙" src="images/-vAXPYeJpJsOLYj4tHEGwRMtJzdFwRgQ1eDkDQrvj5URXalNJ-m8WQRKYc3VTa8bx6r1DpTzRejxGkTR-d9e2GNVTtFt_WUQz3VDWsp0EgJL4gnMvJeHw6H9PZMdG7--FdTxXpD31IE"/></center><br/>
<h2>★引子</h2><br/>
　　本文要聊的这个话题，俺在5年前的那个《<a href="../../2013/06/privacy-protection-0.md">如何保护隐私</a>》系列博文中，已经聊过一次（参见那个系列的第2篇《<a href="../../2013/06/privacy-protection-2.md">关于浏览器的基本防范（上）</a>》）。<br/>
　　为啥今天又要老调重谈捏？主要是因为本月初（2018年9月）发布的 Chrome 69 版本出了一个严重的隐私丑闻。这个丑闻如此雷人，俺觉得有必要老调重谈：劝大伙儿弃用 Chrome。<br/>
　　虽然 Google 官方已经承诺在 Chrome 70 版本解决此问题，但俺认为：Chrome 浏览器在隐私方面【根本不值得信任】（下面会聊到这点）。<br/>
<a name="more"></a><br/>
<br/>
<h2>★名词解释</h2><br/>
<h3>◇Chrome &amp; Chromium</h3><br/>
　　这两者都是由 Google 主导进行开发的。简而言之：Chromium 是一个开源项目，Chrome 是在 Chromium 的基础上又增加了一些【闭源】的模块（比如一些闭源的视频解码器）。<br/>
　　为了打字省力，本文后续部分凡是提到 Chrome，除非有特别说明，否则都是泛指 Chrome 与 Chromium 的总称。<br/>
<br/>
<h3>◇Firefox Quantum</h3><br/>
　　Firefox Quantum 实际上是 Firefox 57 版本，于2017年11月正式发布（参见“<a href="https://blog.mozilla.org/blog/2017/11/14/introducing-firefox-quantum/" rel="nofollow" target="_blank">这个链接</a>”）。<br/>
　　之所以专门给 57 版本起了一个代号，因为这是个【全新】的 Firefox 版本，内部采用了基于 Rust 编程语言开发的 <a href="https://en.wikipedia.org/wiki/Servo_(software)" rel="nofollow" target="_blank">Servo 引擎</a>。另外，其网络模块和 UI 外观的代码也是重写的。<br/>
<br/>
<h3>◇Firefox 的快速迭代版本和 ESR 版本</h3><br/>
　　Firefox 从 5.0 开始效仿 Chrome，进行大版本的快速迭代，每6~7星期发一个新版本（大版本号加一）。出了新版本之后，老版本就不维护了（也就不再有安全补丁）<br/>
　　而 Firefox 的 ESR 版本是【长期支持版本】（洋文叫做“Extended Support Release”），ESR 版本提供长达一年的维护。一般来说，每隔7到8个快速迭代版本，就会有一个 ESR 版本。最近的几个 ESR 版本分别是：“38.0 和 45.0 和 52.0 和 60.0”。<br/>
　　Firefox ESR 版本的官方下载页面是：<br/>
<a href="https://www.mozilla.org/firefox/organizations/" rel="nofollow" target="_blank">https://www.mozilla.org/firefox/organizations/</a><br/>
<br/>
<h3>◇Tor</h3><br/>
　　Tor 是洋文 （The Onion Router）的缩写，中文又称“洋葱网络/洋葱路由”。简单而言，这是一款老牌的安全工具，专门设计用于隐匿上网身份。<br/>
　　大名鼎鼎的【斯诺登】同学（曝光美国政府棱镜丑闻的那位）就是 Tor 的用户，他还专门向公众推荐过 Tor 这款工具。这从另一个侧面说明了 Tor 在隐私保护方面的地位与口碑。<br/>
　　关于 Tor，俺博客上已经写了好几篇教程，如下：<br/>
《<a href="../../2014/10/gfw-tor-meek.md">“如何翻墙”系列：Tor 已复活——meek 流量混淆插件的安装、优化、原理</a>》<br/>
《<a href="../../2013/11/tor-faq.md">“如何翻墙”系列：关于 Tor 的常见问题解答</a>》<br/>
<br/>
<br/>
<h2>★为啥 Firefox 在【隐私保护】方面会优于 Chrome？</h2><br/>
<h3>◇非营利机构（Mozilla） VS 商业公司（Google）</h3><br/>
　　首先要指出的是：开发 Firefox 的 Mozilla 是一个【非营利组织】；而开发 Chrome 的 Google 是一家【商业公司】。<br/>
　　为啥 Firefox 在隐私保护方面比 Chrome 好？这是最根本的原因。<br/>
<br/>
<h3>◇Google 的商业模式——注定了它收集隐私的偏好</h3><br/>
　　Google 的利润，90% 以上是来自于广告收入。Google 的【客户】，其实并【不是】全球那几十亿使用 Google 产品的网民。那么，谁才是 Google 真正的客户捏？是那些投放广告的商家（广告主），他们付钱给 Google，他们才是甲方，他们才是 Google 真正的客户。<br/>
　　广告主最关心的是啥捏？他们关心：广告能否被展示给【有效的】目标受众，用行话来说就是【精准投放广告】。<br/>
　　对 Google 而言，广告投放得越精准，就可以从广告主手中赚到越多的钱。那如何才能实现【精准投放】捏？关键在于 Google 要了解每一个网民的特性，要知道他们从事啥行业，有啥偏好，有啥生活习惯，诸如此类。为了达到这个目的，Google 就必须尽可能地收集一切网民的隐私。<br/>
　　以上这些，就是 Google 商业模式的本质。<br/>
<br/>
<h3>◇顺便抹黑一下百度</h3><br/>
　　（批评完 Google 的商业模式，请允许俺稍微跑题，顺便抹黑一下百度）<br/>
　　百度同样是一家搜索引擎公司，但是百度比 Google 更恶心百倍。Google 虽然喜欢收集用户隐私，但最起码人家 Google 的搜索结果是【客观的】。而百度的搜索结果是可以花钱买滴（还美其名曰“竞价排名”）。这么说吧，如果你针对某个关键词向百度出了高价，那么网民在百度上搜索该关键词的时候，你的网站就会排在搜索结果的前面。<br/>
　　就是靠着“竞价排名”，莆田系与百度这两个大流氓完美地勾搭在一起。<b>如果说莆田系医院是垃圾，那百度这家公司就是垃圾中的垃圾；如果说莆田系的老板是人渣，那百度的老板李彦宏就是人渣中的人渣。</b><br/>
　　莆田系加上百度，不知毁掉了多少家庭，不知让多少病患人财两空。李彦宏的百亿身家，就是靠人血馒头堆出来的。当年的魏则西事件，只不过是碰巧被曝光的沧海一粟。下面是俺当年发的《每周转载》。<br/>
《<a href="../../2016/05/weekly-share-101.md">每周转载：魏则西事件、百度广告、莆田系、军队医院（各方报道及网友评论）</a>》<br/>
<br/>
<h3>◇Chrome 缺乏【网站中立性】</h3><br/>
　　（跑题结束，言归正传）<br/>
　　现在咱们开始来讨论 Chrome 69 版本那个严重的隐私漏洞。这事儿简直可以称为【隐私丑闻】，已经在网络上引发大量吐槽。下面列出若干链接，是某些知名网站对此事的报道和讨论。<br/>
《<a href="https://news.ycombinator.com/item?id=18064537" rel="nofollow" target="_blank">Chrome 69 will keep Google Cookies when you tell it to delete all cookies @ Hacker News</a>》<br/>
《<a href="https://www.solidot.org/story?sid=58064" rel="nofollow" target="_blank">Chrome 69 清空 Cookies 会保留 Google 的 Cookies @ Solidot</a>》<br/>
《<a href="https://www.extremetech.com/internet/277609-chrome-69-is-a-full-fledged-assault-on-user-privacy" rel="nofollow" target="_blank">Chrome 69 Is a Full-Fledged Assault on User Privacy @ ExtremeTech</a>》<br/>
<br/>
　　这个丑闻是这样滴：<br/>
　　当你在 Chrome 69 版本上使用【清空所有 cookie】这个功能的时候，其它网站下的 cookie 确实被清空了；但是，Google 域名下的 cookie 被悄悄地保留了下来。<br/>
　　俺要强调一下：这绝对不是一个意外引入的 bug；恰恰相反，这是一个【有意实现】的功能。<br/>
　　由于 Chrome 悄悄地保留了 Google 相关域名的 cookie，这就意味着——即使在你清空了所有 cookie 之后，一旦你通过 Chrome 使用 Google 的服务，Google 的服务器依然知道你是谁（依然可以把“你之后的行为”与“你之前的身份”关联起来）。<br/>
　　Chrome 的这个隐私丑闻，说白了就是——Chrome 缺乏【网站的中立性】。<br/>
　　【网站的中立性】理应是任何一个浏览器最起码的要求——通俗地说，浏览器对所有的网站都应该是一视同仁的。<br/>
　　但由于 Chrome 本身是 Google 开发的，而 Google 本身又提供了大量的网络服务。在这种情况下，Chrome 就很难再做到【网站中立性】了。<br/>
<br/>
<h3>◇Chrome 可能会与 Google 的服务暗中勾搭，以收集隐私</h3><br/>
　　比【缺乏中立性】更严重的是：Chrome 有可能会悄悄收集你本机的信息，然后上传到 Google 的服务器。<br/>
　　（请注意：这种风险目前【尚未】被证实，但要始终保持警惕性）<br/>
　　为了加深印象，咱们来对比一下 Firefox 与 Chrome。<br/>
其一，<br/>
Mozilla 这个非营利组织几乎【没有】提供啥网络服务（大概也就只有一个“自动同步数据”的服务）。如果 Firefox 与 Mozilla 网站有频繁的网络通讯，很容易引发用户（尤其是极客用户）的怀疑。<br/>
相比之下，大部分 Chrome 用户同时也是 Google 服务的用户。因此，Chrome 本来就需要经常与 Google 的服务器通讯。如果 Chrome 在这些网络通讯中夹带私活，很难被发现。<br/>
其二，<br/>
Firefox 是完全开源的，而 Chrome 是基于 Chromium 增加了一些闭源模块（换句话说，Chrome【不是】完全开源的）。<br/>
如果 Firefox 偷偷摸摸干了坏事，会被代码审计曝光；相反，Chrome 的【闭源】模块干了些啥，大伙儿并不太清楚。<br/>
<br/>
<h3>◇换“网络服务”难，换“浏览器”容易</h3><br/>
　　要防止上述所说的——浏览器配合网络服务收集隐私。最彻底的解决之道是：<b>不要使用同一家公司的网络服务与浏览器</b>。<br/>
　　不得不承认，Google 的很多网络服务做得相当好，甚至是世界第一。比如 Gmail、Google Translate、Blogger 都很难找到称心的替代品。如果你已经是一个 Google 服务的重度用户，要想舍弃这些服务是挺难滴。<br/>
　　相比之下，换一个浏览器会容易得多。<br/>
<br/>
<br/>
<h2>★为啥 Firefox 在【防范入侵】方面会优于 Chrome？</h2><br/>
　　在对比这两款浏览器的安全性时，Firefox 粉丝总可以找到一些 Chrome 有而 Firefox 没有的漏洞；反之，Chrome 粉丝也可以找出一些 Firefox 有而 Chrome 没有的漏洞。<br/>
　　俺个人觉得：对比个别的漏洞，意义不太大。俺想在更【宏观】的层面讨论一下安全漏洞的问题。<br/>
<br/>
<h3>◇小众 VS 大众</h3><br/>
　　如今 Chrome 已经占据浏览器市场份额的【第一名】。很显然，Chrome 是一款【大众】的浏览器；相比之下，Firefox 是一款【小众】的浏览器。<br/>
　　除了这两者的份额，还要考虑到众多的【国产浏览器】是基于 Chromium 进行定制开发的，他们与 Chrome 使用【相同的引擎】，名叫“<a href="https://en.wikipedia.org/wiki/Blink_(web_engine)" rel="nofollow" target="_blank">Blink</a>”（这玩意儿衍生自 WebKit 引擎）。如果以 Blink 内核来算的话，其市场份额还会更高。<br/>
　　更高的市场份额意味着——对攻击者而言具有更高的诱惑力。说得更直白一点：Chrome 的安全漏洞（尤其是 Blink 引擎的漏洞），在地下黑市能卖得更值钱。<br/>
　　试想一下：如果某个安全研究人员发现了一个 Blink 引擎的漏洞，他/她是会把漏洞公布出来捏，还是会拿到黑市上去卖捏？<br/>
　　Firefox 当然也会有安全漏洞，但 Firefox 的市场份额比 Chrome 低很多倍，（相比 Chrome）它的漏洞就没有这么吃香。<br/>
<br/>
<h3>◇Rust VS C++</h3><br/>
　　前面俺提到了 Firefox Quantum（Firefox 57）版本是一个全新的版本，引入了一个新的 <a href="https://en.wikipedia.org/wiki/Servo_(software)" rel="nofollow" target="_blank">Servo 引擎</a>。这个引擎是用 Rust 编程语言开发的。<br/>
　　在 Firefox Quantum 之前，Firefox 的 Gecko 引擎是用 C++ 开发的；而 Chrome 的 Blink 引擎也是用 C++ 写的。C++ 语言如同 C 语言，很容易因为内存使用方面的问题而导致安全漏洞（比如：缓冲区溢出、野指针...）。这个缺点是编程语言本身导致的。<br/>
　　最近20年，主流浏览器（IE、Firefox、Chrome）曝光的很多【高危漏洞】（远程执行漏洞、提权漏洞）都是因为 Web 引擎的 C++ 代码有安全方面的 bug。<br/>
　　而 Rust 作为一门新的编程语言，它一方面可以达到与 C/C++ 相同的性能，另一方面又避免 C/C++ 在内存和多线程方面的弊端。这个话题如果要深入谈下去，会涉及到太多编程语言的细节，俺就不展开了。<br/>
　　简而言之，当 Firefox 开始改用 Rust 语言来开发 Web 渲染引擎，会大大降低某些类型的安全漏洞。这是 Firefox 在安全方面相比 Chrome 的另一个优势。<br/>
<br/>
<h3>◇“自带 CA 证书” VS “使用系统 CA 证书”</h3><br/>
　　首先要强调一下：在信息安全体系中，CA 证书是很重要滴！具体的概念可以参见俺8年前写的《<a href="../../2010/02/introduce-digital-certificate-and-ca.md">数字证书及 CA 的扫盲介绍</a>》。<br/>
　　对于 CA 证书，Firefox 与 Chrome 采用【完全不同】的处理方式。<br/>
　　Firefox 使用【自带的】CA 证书；而 Chrome 使用【操作系统提供的】CA 证书。换个说法就是：Mozilla 自己维护一套可信任的 CA 证书列表；而 Chrome 使用操作系统厂商维护的可信任 CA 证书列表。<br/>
　　考虑到大多数读者是 Windows 用户，而 Windows 这款操作系统的厂商是【微软】。现在咱们来考虑一个问题：是微软更可信还是 Mozilla 更可信？假设有一天，朝廷的【有关部门】分别找到微软和 Mozilla，向他俩提出无理要求。谁更容易屈服于咱们的朝廷？当然是微软（M$）。为啥捏？因为微软在咱们天朝有着庞大的商业利益。这些商业利益自然成为朝廷威胁 M$ 的筹码。相比之下，Mozilla 只是一家【非盈利】组织。朝廷拿什么威胁 Mozilla？<br/>
　　考虑到还有很多同学使用苹果的 Mac OS，同样的问题，你自己思考一下：当面对朝廷的无理要求和威胁，是苹果公司先屈服还是 Mozilla 先屈服？答案是显然的。<br/>
　　通过上述的对比你就能体会到：Firefox【自带】CA 证书的好处——自带的 CA 证书【不会】受到操作系统及其厂商的影响。<br/>
<br/>
<br/>
<h2>★Tor 社区对 Firefox 的加持</h2><br/>
　　关于 Tor，本文开头部分的“名词解释”已经介绍过了。<br/>
<br/>
<h3>◇基于 Firefox 定制的 Tor Browser</h3><br/>
　　Tor 官方推出的 Tor Browser 就是在 Firefox ESR（长期支持版本）的基础上进行定制。<br/>
　　俺再重复唠叨一下：Tor 开源社区的宗旨就是为了提升安全性（尤其是隐私保护）。<br/>
　　大伙儿不妨想一想：为啥 Tor Browser 要在 Firefox 的基础上定制，而不在 Chromium 的基础上定制？这不正好说明 Firefox 在安全方面比 Chromium 更强吗！<br/>
<br/>
　　关于 Tor Browser，俺写过如下教程：<br/>
《<a href="../../2018/04/gfw-tor-browser-7.5-meek.md">“如何翻墙”系列：扫盲 Tor Browser 7.5——关于 meek 插件的配置、优化、原理</a>》<br/>
<br/>
<h3>◇Tor 项目组对 Firefox 的回馈</h3><br/>
　　由于 Tor 开源社区多年来在 Firefox ESR 的基础上定制开发 Tor Browser，Tor 社区也会把一些安全防御及隐私保护的功能回馈给 Mozilla 社区。比如在2017年，Tor 社区就回馈了两项重要的隐私保护功能给 Firefox 团队，分别是：<br/>
【<b>第一方隔离</b>】<br/>
洋文叫做“First Party Isolation”，相关介绍看“<a href="https://www.solidot.org/story?sid=54573" rel="nofollow" target="_blank">这个链接</a>”。<br/>
【<b>防范指纹追踪</b>】<br/>
洋文叫“Fingerprinting Resistance”，相关介绍看“<a href="https://www.solidot.org/story?sid=50921" rel="nofollow" target="_blank">这个链接</a>”。<br/>
<br/>
<h3>◇未来的展望——Firefox 直接整合 Tor</h3><br/>
　　就在今年（2018），Mozilla 启动了一个 Fusion 项目（Fusion 是“Firefox USIng ONions”的缩写），进一步把 Tor 的安全防御和隐私保护技术整合到 Firefox 中。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/2z8PL15f1ug4b_kKyqHRZV7I2QjgZYUh00mi5nnjNBwwC6z0HVVfEgPEi7ficiQ9HP9q-OeGhDbdNQ2jIMGh4cKLHvYRpTaJShbshYypnKivuVeefLCA4rJ37lxTllXBzkiEYUpqFlg"/><br/>
（Fusion 的 logo——狐狸抱着洋葱）</center><br/>
　　该项目的介绍页面在“<a href="https://wiki.mozilla.org/Security/Fusion" rel="nofollow" target="_blank">这里</a>”，其中提到：<q>We will determine how best to integrate the Tor proxy into Firefox</q><br/>
　　或许在不远的将来，Firefox 用户就可以直接体验 Tor 代理的匿名网上冲浪。<br/>
<br/>
<br/>
<h2>★最后来谈谈 Firefox 的性能问题</h2><br/>
　　很多 Chrome 用户之所以不愿意切换到 Firefox 是担心它的性能太差。当年 Chrome 刚刚问世那会儿，就是靠突出的性能优势抢了很多 IE 和 Firefox 的用户。在很多 Chrome 用户的【印象】中，Firefox 速度很慢。<br/>
　　但如今，世道变了。在本文开头部分，俺提到了去年（2017年11月）发布的 Firefox Quantum（Firefox 57）是一个重大的版本更新，替换了渲染引擎、UI 框架、网络模块。从 57 版本之后，Firefox 的性能相比以前有大幅提升。<br/>
　　这可不是俺一家之言，连《纽约时报》这种全球知名的媒体今年6月还专门发了一篇文章（如下），谈到 Firefox 的强势回归。<br/>
《<a href="https://www.nytimes.com/2018/06/20/technology/personaltech/firefox-chrome-browser-privacy.html" rel="nofollow" target="_blank">Firefox Is Back. It's Time to Give It a Try. @ NYTimes</a>》<br/>
<br/>
　　57 版本之后的 Firefox 能否在性能上超过 Chrome 捏？这个俺不好说。针对不同的测评标准，这两家各有优劣。但至少，<b>两者的性能已经相差不大了</b>。<br/>
<br/>
<br/>
<h2>★总结</h2><br/>
　　当性能相差不大，而 Firefox 在“保护隐私”和“安全防御”方面会有更多优势——假如你是 Chrome 用户，就该考虑“是否要切换”了。即使你现在还无法作出“换浏览器”的决定，至少可以先装个 Firefox 体验一下。<br/>
　　看了读者评论之后，补充一下：<br/>
　　【不要】使用【中国版】的 Firefox（具体的分析参见“<a href="../../2018/10/How-to-Choose-Firefox-Version.md">这篇博文</a>”），要从 Mozilla 官网下载【国际版】。国际版支持多语种，其中也包括中文。最新版的网址如下：<br/>
<a href="https://www.mozilla.org/en-US/firefox/all/" rel="nofollow" target="_blank">https://www.mozilla.org/en-US/firefox/all/</a><br/>
　　另外，下面的网址可以下载到 Firefox 历史上的【所有版本】（都是【国际版】）<br/>
<a href="https://ftp.mozilla.org/pub/firefox/releases/" rel="nofollow" target="_blank">https://ftp.mozilla.org/pub/firefox/releases/</a><br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2018/10/How-to-Choose-Firefox-Version.md">基于安全考虑，如何选择及切换 Firefox 版本？</a>》<br/>
《<a href="../../2013/06/privacy-protection-0.md">如何保护隐私</a>》（系列）<br/>
《<a href="../../2010/06/howto-prevent-hacker-attack-0.md">如何防止黑客入侵</a>》（系列）<br/>
《<a href="../../2010/04/howto-cover-your-tracks-0.md">如何隐藏你的踪迹，避免跨省追捕</a>》（系列）<br/>
《<a href="../../2013/11/tor-faq.md">“如何翻墙”系列：关于 Tor 的常见问题解答</a>》<br/>
《<a href="../../2018/04/gfw-tor-browser-7.5-meek.md">“如何翻墙”系列：扫盲 Tor Browser 7.5——关于 meek 插件的配置、优化、原理</a>》<br/>
《<a href="../../2010/02/introduce-digital-certificate-and-ca.md">数字证书及 CA 的扫盲介绍</a>》<br/>
《<a href="../../2013/12/linux-tails-guide.md">扫盲 Tails——专门强化隐匿性的 Linux 发行版</a>》<br/>
《<a href="../../2019/07/Customize-Firefox.md">扫盲 Firefox 定制——从“user.js”到“omni.ja”</a>》<br/>
《<a href="../../2016/10/custom-firefox-theme-without-extension.md">无需任何插件或扩展，定制 Firefox 外观</a>》
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2018/09/Why-You-Should-Switch-from-Chrome-to-Firefox.html
