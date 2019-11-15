# 扫盲 Linux：如何选择发行版 

-----

<div class="post-body entry-content">
　　Linux 的发行版实在是太多了。初次接触 Linux 的同学，面对这么的发行版，估计会有点晕。所以，在写完《<a href="http://program-think.blogspot.com/2013/10/linux-newbie-guide.html">新手如何搞定 Linux 操作系统</a>》一文之后，俺接着来扫盲一下 Linux 的发行版。<br/>
<a name="more"></a><br/>
<br/>
<h2>★“内核”与“发行版”是啥关系？</h2><br/>
　　对于新手而言，需要先搞清楚这两个概念（已经明白的同学，请跳过本章节）。<br/>
<br/>
<h3>◇操作系统内核（OS kernel）</h3><br/>
　　所谓的”操作系统内核“，通俗地说就是操作系统最核心最关键的部件。它负责一些最基本的工作，比如：管理硬件驱动、管理内存、管理文件系统、管理进程、等等。这些东西只要少了任何一样，整个操作系统就【没法】正常运转。<br/>
<br/>
<h3>◇Linux 内核（Linux kernel）</h3><br/>
　　Linux 作为操作系统，当然也有其内核。自问世以来，Linux 内核的开发工作一直是由 Linus（也就是 Linux 它爹）领导。Linus 对于 Linux 内核的意义，就如同乔布斯对于苹果的意义。<br/>
　　Linux 内核的特点是——<b>非常彻底的【开放性】</b>。所谓的【开放性】包括如下几方面：<br/>
1. 任何人都可以随意获取（可以从 <a href="https://www.kernel.org/" rel="nofollow" target="_blank">Linux Kernel 官网</a>直接下）<br/>
2. 任何人都可以免费获取（完全不用花银子）<br/>
3. 任何人都可以参与开发（阿猫阿狗都可以向 Linux 社区提交代码；只要你提交的代码符合要求，就会被合并到内核主线）<br/>
<br/>
　　内核不是今天的重点，俺就点到为止。更多详细介绍，请参见维基百科的“<a href="https://zh.wikipedia.org/wiki/Linux%E5%86%85%E6%A0%B8" rel="nofollow" target="_blank">这个词条</a>”。<br/>
<br/>
<h3>◇发行版（distribution，简称 distro）</h3><br/>
　　前面说了，操作系统都有"内核"的概念（比如 Windows 也有其内核）。但如果你使用  Windows，通常感觉不到“内核”的存在。为啥捏？原因在于：微软是把 Windows   当作一个整体来发布的。对于普通用户而言，你拿到的是一个完整的操作系统，所以你感觉不到“内核”的存在。<br/>
　　而 Linux 不同于其它操作系统的地方在于：Linus 领导的开源社区只负责开发内核，不开发其它的东西（比如：运行库、图形界面、应用软件、等）。<br/>
　　这就引出一个问题——光有一个赤裸裸的内核，用户是没法用的（就好比你光拿到一个汽车引擎，你是没法开车的）。为此，就有一大帮开源社区或商业公司，在这个裸露的内核外面，再包上一些东西（比如：运行库、应用软件）。经过这样包装之后，就成为“发行版”。<br/>
　　为啥 Linux 的发行版如此之多捏？前面俺说了，Linux 内核是彻底开放滴，随便什么阿猫阿狗都可以去 Linux 的官网下载到内核，然后自己折腾（定制）。如果定制完觉得满意，就可以拿到网上去发布（就成了一个新的发行版）。由于门槛如此之低，发行版自然就很多啦。<br/>
<br/>
<h3>◇【内核+发行版】的模式，有啥好处？</h3><br/>
　　刚才已经解释了 Linux 内核与发行版的关系。再来说说【内核+发行版】的模式，有啥好处。<br/>
　　首先表扬一下 Linus 同学，他当年作出的决定——只开发内核，其它的一概不管——真的是太有先见之明啦！<br/>
　　其一<br/>
　　在这种模式下，会有各种各样的发行版，正好可以覆盖千奇百怪的需求；<br/>
　　其二<br/>
　　【同质化】的发行版之间会产生【竞争】，最终只有优秀的发行版会存活，差劲的发行版会逐渐消亡——这就是开源生态圈的“达尔文主义”。<br/>
　　如果用一个词来形容 Linux 的优点，那就是——【<b>多元化</b>】。内核的开发是多元化滴（任何人都可以参与），发行版也是多元化滴（任何人都可以搞发行版）。<br/>
　　对比一下其它的开源操作系统——BSD系列。<br/>
　　BSD 系列中最有影响的是 <a href="https://zh.wikipedia.org/wiki/FreeBSD" rel="nofollow" target="_blank">FreeBSD</a>。说实话 FreeBSD 很优秀！但是 FreeBSD 的影响力远远小于 Linux。为啥捏？因为 FreeBSD 缺乏 Linux 这种多元化的风格。<br/>
<br/>
<br/>
<h2>★如何选择发行版？</h2><br/>
　　前面说了一通屁话，现在切入正题。<br/>
　　因为 Linux 的发行版太多，如果要逐一介绍的话，都足以写一本大部头的书了。所以俺尝试从“分类”的角度来介绍。通过介绍不同维度的分类，帮助你从不同的视角看待各种发行版。<br/>
　　对发行版的各个视角都有所了解之后，你就可以过滤掉一大批不符合你要求的发行版。过滤完之后，或许就只剩下2~3个候选者，然后再逐一尝试。<br/>
<br/>
<h2>★【通用】发行版 VS 【专用】发行版</h2><br/>
　　所谓的“通用发行版”，顾名思义就是：这个发行版可以派上各种用场；反之，“专用发行版”是为特定用途设计，只能用于某些特定场合。<br/>
　　这两种各有优缺点——通用发行版虽然用途广，但你需要自己做一些定制。专用发行版虽然用途单一，但很多软件和配置预先都帮你设置好了。<br/>
　　俺在《<a href="http://program-think.blogspot.com/2013/10/linux-newbie-guide.html">新手如何搞定 Linux 操作系统</a>》一文中强调的“成熟度”的重要性。所以，俺挑选几个成熟度比较高的通用发行版和专用发行版，大致介绍一下。<br/>
<br/>
<h3>◇【通用】发行版</h3><br/>
　　名气比较大的有如下几个：<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Debian" rel="nofollow" target="_blank">Debian</a></b><br/>
Debian 完全靠社区维护，其特点是：非常强调"自由"的开源理念。它有很多衍生的发行版（比如 Ubuntu），形成一个大家族。在 Linux 的众多家族中，Debian 家族是软件包最多的。<br/>
对于完全没有技术背景的同学，Debian 的门槛稍微有点高。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Fedora" rel="nofollow" target="_blank">Fedora</a></b><br/>
Fedora 来自 <a href="https://zh.wikipedia.org/wiki/Red_Hat_Linux" rel="nofollow" target="_blank">Red Hat Linux</a>。2003年的时候，Red Hat 公司决定不再维护面向桌面的 Red Hat Linux，改为专注于企业市场。就把原先的 Red Hat Linux 交给社区维护，成为 Fedora（原先的洋名叫”Fedora Core“）。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/OpenSUSE" rel="nofollow" target="_blank">openSUSE</a></b><br/>
这是从 Slackware 衍生出来的发行版，原先属于 SuSE 公司的商业发行版（SUSE Linux）。2004年 SuSE 被 Novell 收购之后，Novell 把它移交给社区维护，改名叫 openSUSE。<br/>
它的一个特色功能是 YaST。这玩意儿类似 Windows 的控制面板，帮你搞定一大堆系统管理的杂事（比如：硬盘分区、软件升级、用户管理、网络配置、等等）<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/ArchLinux" rel="nofollow" target="_blank">Arch Linux</a></b><br/>
这是一个白手起家的发行版（【不是】从其它发行版衍生），比较适合于 DIY。默认装出来的系统近乎全裸，然后根据你的需要，安装自己喜欢的软件包。<br/>
它的设计理念是<a href="https://zh.wikipedia.org/wiki/KISS%E5%8E%9F%E5%88%99" rel="nofollow" target="_blank">KISS 原则</a>，追求简洁主义。定位于有技术背景的熟练用户。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Gentoo_Linux" rel="nofollow" target="_blank">Gentoo Linux</a></b><br/>
它跟前面提到的 Arch Linux 很像——也是白手起家，也很适合于 DIY，也是定位于熟练用户。差别在于，它的 DIY 精神更加彻底。Gentoo 官网提供的软件包，【不是】二进制滴，全都以【源代码】形式提供。如果你要装某个软件，先从官网在线更新源代码，然后在【本地】（本机）编译成二进制的软件。你还可以根据自己的喜好，设置编译选项，以优化性能或安全性。<br/>
因为是在本地编译源代码，Gentoo 支持种类繁多的 CPU 类型。<br/>
假如你是程序员出身（尤其是 C/C++ 程序员），建议你尝试一下 Gentoo。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Slackware" rel="nofollow" target="_blank">Slackware</a></b><br/>
在依然活着的发行版中，它是最古老的（1993年问世）。它衍生出很多其它的发行版（比如前面提到的 openSUSE），形成一个大家族。<br/>
Slackware也秉承<a href="https://zh.wikipedia.org/wiki/KISS%E5%8E%9F%E5%88%99" rel="nofollow" target="_blank">KISS原则</a>，偏好命令行而不是 GUI。所以，完全没有技术背景的同学，不太适合直接上手 Slackware。<br/>
<br/>
<h3>◇面向【客户端】（桌面）的专用发行版</h3><br/>
　　这类发行版，名气较大的有如下几个（这几款的门槛都比较低。适合于没有技术背景的新手）。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Ubuntu" rel="nofollow" target="_blank">Ubuntu Desktop</a></b><br/>
衍生自 Debian，大概是影响力最大的桌面发行版了。Ubuntu 的发行版其实分“Server”和“Desktop”两种。一般说 Ubuntu 默认指的是 Ubuntu Desktop。<br/>
其美中不足之处是——Ubuntu 本身是一家【商业】公司维护的。关于商业发行版的缺点，后面会提到。<br/>
它以发布时间做版本号（比如：<code>13.10</code> 就是2013年10月发布）。每半年发布一个版本。<br/>
它的版本分两种：普通版本和长期支持版本（LTS）。LTS 会持续提供支持（补丁更新）长达几年（桌面版 3年，服务器版 5年），普通版本只支持9个月。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Linux_Mint" rel="nofollow" target="_blank">Linux Mint</a></b><br/>
衍生自 Ubuntu Desktop，由社区维护（避免了商业公司的缺点）。在 <a href="http://distrowatch.com/" rel="nofollow" target="_blank">DistroWatch</a> 的浏览量排名中，经常排在第一名。<br/>
为啥它的排名这么高捏？其中一个原因是：它很强调【傻瓜化】的用户体验，所以吸引到不少人气。<br/>
它的发布周期是半年（类似于 Ubuntu），每年的5月和11月出新版本。<br/>
它跟 Ubuntu 类似，也分普通版本和 LTS 版本。最近的一个 LTS 是 Linux Mint 13，2012年5月发布，支持到2017年4月。至于普通版本，支持6个月。<br/>
可选多种桌面环境（Cinnamon、Mate、KDE、Xfce、GNOME、LXDE、Fluxbox）<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Elementary_%28%E6%93%8D%E4%BD%9C%E7%B3%BB%E7%BB%9F%29" rel="nofollow" target="_blank">elementary OS</a></b><br/>
这款是从 Ubuntu 衍生滴，诞生于2011年。<a href="http://distrowatch.com/" rel="nofollow" target="_blank">DistroWatch</a> 的浏览量排名中，2012年还榜上无名，2013年已经排入前20位。<br/>
它的特点是：深度整合各种桌面应用。另外，因为是 Ubuntu 的衍生版，天然地兼容 Debian 家族的软件包。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Manjaro_Linux" rel="nofollow" target="_blank">Manjaro</a></b><br/>
这款是从 Arch Linux 衍生滴，诞生于2011年（与 elementary 是同龄人）。<br/>
在前面章节，俺提到了 Arch 的门槛比较高。这款发行版侧重于降低 Arch 的使用门槛，从而吸引了大量 Arch 的原有用户。<br/>
其官方默认支持的桌面是 Xfce ＆ KDE。如果你不喜欢这两个桌面，可以使用社区支持的其它桌面：Gnome、LXDE、Enlightenment、MATE、Cinnamon...<br/>
<br/>
<h3>◇面向【服务端】的专用发行版</h3><br/>
　　这类发行版，比较有影响力的是：<a href="https://zh.wikipedia.org/wiki/Red_Hat_Enterprise_Linux" rel="nofollow" target="_blank">Red Hat Enterprise Linux</a>（简称 RHEL）、<a href="https://zh.wikipedia.org/wiki/CentOS" rel="nofollow" target="_blank">CentOS</a>（从 RHEL 衍生）、<a href="https://zh.wikipedia.org/wiki/Ubuntu" rel="nofollow" target="_blank">Ubuntu Server</a>（从 Debian 衍生）、等等。<br/>
　　考虑到本文是面向【个人】用户，这方面就不多聊啦。<br/>
<br/>
<h3>◇面向【特殊用途】的发行版</h3><br/>
　　还有一些特殊用途的发行版，定位于比较小的细分市场，属于【小众的】发行版。这些小众发行版，“成熟度”不一定够。所以就不放在本章节，俺会在本文末尾统一介绍。<br/>
<br/>
<br/>
<h2>★版本发布 VS 滚动发布（无版本）</h2><br/>
　　说到发布方式，大致上有两种风格：按版本发布 or 滚动发布。<br/>
　　按版本发布，大伙儿应该比较熟悉了，Windows 和 Mac OS 都是这么干的。大部分 Linux 发行版也是这么干的。<br/>
　　但是有少部分发行版采用滚动发布，典型的代表就是前面提到的 Arch Linux 和 Gentoo Linux。对于“滚动发布”的模式，【不】存在版本号，也<b>【无需】重装系统</b>。对于这类系统，你只需要安装一次，就可以无限期地用下去（除非发行版死亡 或者 系统被你自己折腾坏了）。虽然不用重装系统，但你需要定期升级。通过定期升级来增加软件功能，并消除软件漏洞。<br/>
　　这两种发布方式，各有优缺点，很难说哪种更好。你可以根据自己的喜好，选择其中一种。<br/>
<br/>
<br/>
<h2>★保守型 VS 激进型</h2><br/>
<h3>◇【保守】的发行版</h3><br/>
　　这类发行版通常更在意系统和软件的稳定性/可靠性/安全性。为了做到这点，适当地牺牲了“新功能”。所以，它们通常都不会采用最新版本的内核或软件。而是采用不太新，但久经考验的版本。<br/>
　　一般来说，面向服务端的发行版都是“保守型”滴（比如 RHEL、CentOS）。<br/>
　　另外，在“通用发行版”中，Debian 是偏“保守”滴；而 Fedora 是偏“激进”滴。<br/>
<br/>
<h3>◇【激进】的发行版</h3><br/>
　　这类发行版优先保证“新功能”。所以它们总是第一时间升级内核版本或软件版本。<br/>
　　采用滚动方式发布的 Linux，通常都是【激进型】滴（比如 Arch Linux、Gentoo Linux）。<br/>
<br/>
<h3>◇如何权衡？</h3><br/>
　　这两种风格，也很难说谁对谁错。关键看你的需求。如果你比较关注安全性，最好选用保守型的。<br/>
<br/>
<h2>★【商业】发行版 VS 【社区】发行版</h2><br/>
　　制作发行版的组织，大体上可以分为两类——商业公司 ＆ 非营利组织。<br/>
　　说到这里，先澄清一个误区：<br/>
　　很多人有【偏见】，以为“非营利组织”的研发能力不如“商业公司”。<br/>
　　其实不然！<br/>
　　非营利组织也可以做出精品。你只需想想浏览器的例子：非营利组织开发的 Firefox 远远好于（头号软件公司）微软开发的“IE ＆ Edge”。<br/>
<br/>
　　对于这两者的选择，主要的考虑因素是：隐私。<br/>
　　商业发行版在隐私保护方面<b>不如</b>社区发行版。具体的分析请看《<a href="http://program-think.blogspot.com/2013/06/privacy-protection-1.html">如何保护隐私[1]：关于软件和服务的选择</a>》。这里就不再罗嗦了。<br/>
　　举个例子：<br/>
　　Ubuntu 属于商业发行版（其后台是 <a href="https://zh.wikipedia.org/wiki/Canonical%E5%85%AC%E5%8F%B8" rel="nofollow" target="_blank">Canonical公司</a>）。Ubuntu 曾经在去年爆了一个丑闻：其桌面搜索功能存在隐私泄露风险（相关报道在“<a href="https://www.eff.org/deeplinks/2012/10/privacy-ubuntu-1210-amazon-ads-and-data-leaks" rel="nofollow" target="_blank">这里</a>”）<br/>
　　俺的建议是：<br/>
　　<b>非常在意隐私的同学，最好用社区发行版。</b>如果你对隐私问题无所谓，那这项指标可以不考虑。<br/>
<br/>
<br/>
<h2>★一些特殊用途的发行版</h2><br/>
　　下面列举若干特殊用途的 Linux 发行版。俺的接触面有限，介绍未必全面。大伙儿如有补充，欢迎到<a href="http://program-think.blogspot.com/2013/10/linux-distributions-guide.html">俺博客留言</a>。<br/>
<br/>
<h3>◇某些【迷你】（Mini）发行版</h3><br/>
　　在《<a href="http://program-think.blogspot.com/2013/10/personal-it-infrastructure.html">磨刀不误砍柴功——聊聊个人IT基础设施的完善</a>》一文，俺提到某些 Linux 发行版可以精简到很小（只有几十兆），而且功能照样齐全。今天就来介绍一下。<br/>
　　估计有的同学会问，迷你 Linux 有啥用？用途还是不少滴。<br/>
比如：迷你型 Linux 因为很小，可以把整个系统放到内存中运行，所以速度飞快（内存的读写速度比硬盘至少快一个数量级）<br/>
比如：家中有古老的 PC，内存硬盘都很小，就可以装迷你发行版（废物利用）。<br/>
比如：早年买来的 U盘，可能只有 64兆、128兆、256兆，也可以在上面装迷你型的 Linux。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Puppy_Linux" rel="nofollow" target="_blank">Puppy Linux</a></b><br/>
这是比较老牌的迷你发行版，已有10年历史。<br/>
说说它的特色：<br/>
其它的发行版，在 LiveCD 模式下是无法实现数据保存的。每次重新启动之后，之前对文件系统的修改都会消失。<br/>
但是 Puppy 牛B的地方在于：LiveCD 模式下也可以实现数据保存。前提是：电脑具有"CD-R 或 DVD-R 光驱"。只要有这种光驱，它就可以采用多段刻录的方式，把每次运行时修改过的数据刻录到光盘上（直到刻满为止）。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/SLAX" rel="nofollow" target="_blank">SLAX</a></b><br/>
这款衍生自 Slackware。在迷你 Linux 中，这款算是比较庞大的（大约200兆）。虽然有点大，但是它具备了完善的国际化（含简体中文和繁体中文）。<br/>
它的一大特色是它的软件包管理方式【非常绿色】。你从官网下载到某个软件包之后（扩展名是 SB，别想歪了），只需要把这个 SB 文件放到某个特定目录，然后启动系统，这个软件就可以用了；下次如果觉得这个软件不想要，只需要把那个 SB 文件删除，再启动系统，这个软件就彻底消失了。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Slitaz" rel="nofollow" target="_blank">SliTaz</a></b><br/>
这款就真的是“Mini”了，目前的4.0版本只有35兆。这么小的体积，竟然还包含了不少软件（比如 Firefox、多媒体编辑、等）。<br/>
<br/>
　　<b><a href="https://zh.wikipedia.org/wiki/Tiny_Core_Linux" rel="nofollow" target="_blank">Tiny Core Linux</a></b><br/>
这款比 Slitaz 更小，包括几个不同的变种：<br/>
Micro Core——只有8兆，但是没图形界面。<br/>
Tiny Core ——12兆，带图形界面。<br/>
Core Plus——64兆，带有更多应用软件。<br/>
<br/>
<h3>◇用于安全领域的发行版</h3><br/>
　　<b><a href="https://en.wikipedia.org/wiki/BackTrack" rel="nofollow" target="_blank">BackTrack</a> / <a href="https://en.wikipedia.org/wiki/Kali_Linux" rel="nofollow" target="_blank">Kali</a></b><br/>
它衍生自 Ubuntu。在安全类的发行版中，它的名气很大。<br/>
它是面向懂安全的技术类用户，傻瓜用户不需要它。<br/>
该发行版中包含了大量的安全类工具，可以用来进行：入侵、信息收集、安全取证、安全评估、等等。<br/>
Kali 是 BackTrack 的后续发行版。它俩都出自 Offensive Security。<br/>
<br/>
　　<b><a href="https://en.wikipedia.org/wiki/The_Amnesic_Incognito_Live_System" rel="nofollow" target="_blank">Tails</a></b><br/>
Tails 是洋文”The Amnesic Incognito Live System“的缩写。它衍生自 Debian，设计目标是：保护隐私，加强上网的隐匿性。<br/>
在 Tails 里面上网，所有的流量都会经过 Tor 网络中转（没听说过 Tor 的同学，请看俺的<a href="../../2013/11/tor-faq.md">这篇博文</a>）。<br/>
它支持 LiveCD 或 LiveUSB，可以完全运行于内存中，以免在硬盘上留下你的上网痕迹。<br/>
引申阅读：对这款发行版，俺专门写过一篇教程（如下）<br/>
《<a href="../../2013/12/linux-tails-guide.md">扫盲 Tails——专门强化隐匿性的 Linux 发行版</a>》<br/>
<br/>
　　<b><a href="https://www.whonix.org/" rel="nofollow" target="_blank">Whonix</a></b><br/>
这款工具采用双虚拟机进行隔离（一台充当网关，一台用于上网），对外连接全部经过 TOR 网络中转。<br/>
上网的那个虚拟机即使遭遇入侵（比如被挂马），你的公网 IP 也不会被入侵者看到。<br/>
如果你对这种玩法有兴趣，可以看俺的博文《<a href="http://program-think.blogspot.com/2013/01/howto-cover-your-tracks-6.html">如何隐藏你的踪迹，避免跨省追捕[7]：用虚拟机隐匿公网IP（原理介绍）</a>》。<br/>
<br/>
　　<b><a href="https://en.wikipedia.org/wiki/Lightweight_Portable_Security" rel="nofollow" target="_blank">Lightweight Portable Security</a></b><br/>
这款发行版简称 LPS，是美国国防部为政府雇员量身打造的，专门用于强化安全性，防范某些国家的御用骇客。<br/>
它内置了加密工具，整个系统采用 LiveCD/LiveUSB 方式，完全运行于内存中（避免在硬盘里留下痕迹，防止泄密）<br/>
俺猜测，这款发行版很可能有美国国安局（NSA）的后门 :)<br/>
<br/>
<h3>◇用于数据恢复的发行版</h3><br/>
　　有若干发行版是专门用来做数据恢复的。比如你不小心把系统格式化了，或者不小心把硬盘分区误删了。这类发行版就可以派上用场。因为是用来做数据恢复，所以这类发行版都具备 LiveCD 的能力——数据恢复的时候，用光盘引导，可以避免对硬盘的写操作。<br/>
<br/>
　　<b><a href="https://en.wikipedia.org/wiki/SystemRescueCD" rel="nofollow" target="_blank">SystemRescueCD</a></b><br/>
这是从 Gentoo 衍生出来的，从名称就可以看出，是用来做系统应急修复的。<br/>
它内置了若干有用的系统工具，比如：分区工具、文件系统工具、数据恢复工具、Windows 注册表修改工具、等等。<br/>
它本身就提供图形界（包括浏览器），便于你在修复过程中，上网查资料。<br/>
<br/>
　　<b><a href="https://en.wikipedia.org/wiki/Trinity_Rescue_Kit" rel="nofollow" target="_blank">Trinity Rescue Kit</a></b><br/>
这款有点像 SystemRescueCD，不过只有命令行界面。但是它内置了病毒扫描工具。<br/>
这个发行版不够活跃，两年没出新版本了。<br/>
<br/>
<h3>◇用于多媒体的发行版</h3><br/>
　　<b><a href="https://en.wikipedia.org/wiki/Ubuntu_Studio" rel="nofollow" target="_blank">Ubuntu Studio</a></b><br/>
衍生自 Ubuntu，面向多媒体制作，内置了许多 图像/音频/视频 的相关软件。<br/>
它采用实时内核（real-time kernel），以提高处理视频/音频的性能。<br/>
<br/>
　　<b><a href="https://en.wikipedia.org/wiki/Mythbuntu" rel="nofollow" target="_blank">Mythbuntu</a></b><br/>
衍生自 Ubuntu，类似于 Windows Media Center<br/>
<br/>
<br/>
<h2>★总结</h2><br/>
　　Linux 发行版太杂，导致本文写得比较长。时间仓促，某些发行版没来得及介绍。欢迎大伙儿补充。有说得不对的地方，也欢迎拍砖。<br/>
　　最后，来做一下总结发言：<br/>
<br/>
<h3>◇【无】技术背景的新手</h3><br/>
　　建议先尝试那几款“面向桌面“的发行版。这几款的用户数都比较大，门槛都比较低，上手相对容易。用了一段时间之后，如果你自认为比较熟练了，想要继续”折腾“，再考虑——是否尝试那几款”通用发行版“。<br/>
<br/>
<h3>◇【有】技术背景的新手</h3><br/>
　　你可以先尝试”面向桌面“的发行版，也可以直接尝试那几款”通用发行版“。<br/>
　　在”通用发行版“中，Gentoo 和 Arch 的难度【大于】Debian、Fedora、openSUSE。喜欢折腾的，有 Geek 精神的同学，建议玩玩 Gentoo 和 Arch。折腾过这两款发行版，会让你对 Linux 系统有更深入的了解。<br/>
　　再补充一下：Gentoo 和 Arch 虽然门槛高，但是这两款发行版的文档都非常齐全。洋文不好的同学，顺便可以锻炼一下阅读能力。<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="http://program-think.blogspot.com/2013/10/linux-newbie-guide.html">扫盲 Linux：新手如何搞定 Linux 操作系统</a>》<br/>
《<a href="../../2019/11/POSIX-TUI-from-TTY-to-Shell-Programming.md">扫盲 Linux＆UNIX 命令行——从“电传打字机”聊到“shell 脚本编程”</a>》<br/>
《<a href="../../2013/12/linux-tails-guide.md">扫盲 Tails——专门强化隐匿性的 Linux 发行版</a>》<br/>
《<a href="../../2017/03/Why-Linux-Is-More-Secure-Than-Windows-and-macOS.md">为什么桌面系统装 Linux 可以做到更好的安全性（相比 Windows ＆ macOS 而言）</a>》
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2013/10/linux-distributions-guide.html
