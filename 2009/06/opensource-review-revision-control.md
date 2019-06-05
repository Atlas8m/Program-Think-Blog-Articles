# 开源点评：源代码版本控制系统介绍 

-----

<div class="post-body entry-content">
　　本文是“<a href="../../2009/06/daily-build-4-tools.md">每日构建[4]：相关工具介绍</a>”的第一部分。<br/>
　　由于源代码版本控制系统（Revision Control System，以下简称“RCS”）属于“<a href="../../2009/02/daily-build-3-proces.md">每日构建流程</a>”的头一个环节，所以俺在介绍每日构建的相关工具时，先来聊一聊 RCS 类的软件。<a name="more"></a><br/>
<br/>
<br/>
<h2>★老派的 RCS</h2><br/>
　　在整个软件开发的生命周期中，RCS 处于一个很基础的位置。很多软件工程的环节都会依赖于它。所以，RCS 对于整个软件开发过程而言，是非常重要的。但是却有很多软件公司仍然在使用一些比较陈旧落后的 RCS。因此，有必要先抨击一下这些老古董的弊端。<br/>
<br/>
<h3>◇VSS</h3><br/>
　　要说老派的 RCS，当仁不让的就是微软的 Visual Source Safe（简称“VSS”）。VSS 的设计是相当的老土，对源代码库的访问是基于局域网的共享文件夹方式。共享文件夹的方式那是要多土有多土：不光效率低下，而且容易产生安全隐患。<br/>
　　光是设计老土也就算了，毕竟人家是九十年代早期设计的，那会儿 TCP/IP 还没流行呢！VSS 还有更严重的问题，那就是：【误导】了开发人员的对于源代码管理的观念（比如它对文件的锁定模式）。估计有很多开发的新手就是这样被带到沟里去的，以至于长期以来，一直有人在为 VSS 的“锁定模式”进行辩护。<br/>
　　当然，VSS 还是有少量优点的，比如：捆绑在 Visual Studio 中，和 VS 的其它套件整合得比较好。但是这少数优点远远不能抵消它那些严重的缺点。因此俺强烈建议：那些还在用 VSS 的同学，<b>赶紧换掉吧</b>！万一让别人知道你还在用 VSS，以后上街都没脸跟人打招呼。如果大伙儿觉得俺说得太夸张，可以去看看牛人 Coding Horror 写的帖子（在“<a href="http://www.codinghorror.com/blog/archives/000660.html" rel="nofollow" target="_blank">这里</a>”）。<br/>
<br/>
<h3>◇CVS</h3><br/>
　　骂完 VSS，再稍微说一下曾经广为流行的 CVS，（官方站点在“<a href="http://www.nongnu.org/cvs" rel="nofollow" target="_blank">这里</a>”）。<br/>
　　CVS 的优点显然比 VSS 多多了。曾几何时，CVS 几乎成了源代码版本管理的代名词。那会儿，大部分的开源项目都使用 CVS 进行代码管理。不过，用的人多了之后，大家开始发现 CVS 的一些弊端（比如不能改名文件/目录、比如不支持对目录的版本控制、比如对 Unicode/UTF8 支持不够好、比如版本提交的原子性、比如......）。<br/>
　　有些人受不了 CVS 的某些缺点，开发了一个改良版的 <a href="http://cvsnt.org/" rel="nofollow" target="_blank">CVSNT</a>。这玩意儿俺曾经用过几年，比 CVS 好些，不过几个致命的缺点还在（比如上述提到的改名问题）；还有些人更加激进，干脆另起炉灶，搞出全新的 RCS（比如后面提到的 SVN，就是为了取代 CVS 而设计的）。<br/>
　　据俺的观察，目前 RCS 市场的趋势已经比较明显了：很多后来居上的 RCS 正在逐步侵占 CVS 的市场份额。长此以往，CVS 的人气和份额将会逐年下降。不过它暂时还不会消亡，毕竟还有很多老用户还在用它。<br/>
　　所以，俺对 CVS 的观点是：还在用 CVS 的同学也可以考虑换一换了。不过捏，假如你暂时不想换，问题也不算太大（至少CVS的问题没VSS那么严重<b>:-</b>）。<br/>
<br/>
<h2>★新潮的集中式 RCS</h2><br/>
　　批完老派的 RCS，接着来说说近几年比较时髦的 RCS。为了循序渐进，俺先从集中式的 RCS 说起。<br/>
　　在新潮的集中式 RCS 软件中，SVN（全名叫“subversion”）是比较有代表性的（官方站点在"<a href="http://subversion.tigris.org/" rel="nofollow" target="_blank">这里</a>"）。俺就重点来说说它。<br/>
<br/>
<h3>◇SVN 的优点</h3><br/>
　　其实 SVN 相对于 CVS 的优点很多，限于篇幅，俺只挑主要的优点介绍。<br/>
<br/>
　　<b>1、能够导入多种 RCS 的代码库</b><br/>
　　稍微懂行的人都知道，RCS 迁移是一项很严肃的事情，不可等闲视之。如果新的 RCS 不能很好地导入原有 RCS 的代码库，那你肯定会死得很难看滴。<br/>
　　SVN 在这点上是比较成功的：由于它的影响力比较大，自然会有一些第三方的工具提供代码库的导入功能。比如<a href="http://www.subversionary.org/projects/svnimporter" rel="nofollow" target="_blank">SVN Importer</a>，可以把其它很多种 RCS（比如：CVS、PVCS、MKS、ClearCase、SourceSafe）的代码库迁移到 SVN。另外还有<a href="http://cvs2svn.tigris.org/" rel="nofollow" target="_blank">cvs2svn</a>，专门用来导入 CVS 代码库。通过这些工具，你可以完整地保留原有代码库的所有历史版本。<br/>
<br/>
　　<b>2、和 CVS 的使用类似</b><br/>
　　另外，SVN 的一些常用命令、概念、操作习惯都比较类似于 CVS（当然，差别还是有的）。比如俺在 CVS 下经常使用的 <a href="http://www.tortoisecvs.org/" rel="nofollow" target="_blank">TortoiseCVS</a>，也有对应的 SVN 版本（<a href="http://tortoisesvn.tigris.org/" rel="nofollow" target="_blank">TortoiseSVN</a>）。两者就像双胞胎，连界面风格都很像。所以，开发人员从CVS切换到SVN的学习周期会很短，阻力也会很小。<br/>
<br/>
　　<b>3、支持文件/目录改名</b><br/>
　　这个问题一直是 CVS 的致命伤，SVN 没理由不搞定。<br/>
　　有了这个功能之后，就可以直接在客户端进行文件的改名操作。拥有新名称的文件，会继承原有文件的版本历史。<br/>
<br/>
　　<b>4、和Web密切整合</b><br/>
　　这年头，Web越来越成为主流、B/S 的操作方式也开始深入人心。SVN 迎合了这种趋势，和 Apache 绑定在一起。由于深度整合了 Web，很多版本管理的操作都可以直接在浏览器上搞定，巨简单的说。另外，Apache 作为头号 Web Server，功能、性能、安全性自然无可挑剔。<br/>
<br/>
　　<b>5、能很好地整合其它的开发工具</b><br/>
得益于 SVN 的设计理念和开源社区的人气，有越来越多的开发工具都可以和 SVN 无缝整合。比如在 Bug 管理方面，有：<a href="http://trac.edgewall.org/" rel="nofollow" target="_blank">Trac</a>、<a href="http://www.bugzilla.org/" rel="nofollow" target="_blank">Bugzilla</a>、<a href="http://www.mantisbt.org/" rel="nofollow" target="_blank">Mantis</a>；至于各种编辑器或 IDE 的 SVN 插件，那就更多啦，俺就不一一列举了。<br/>
<br/>
<h3>◇SVN 有些啥缺点</h3><br/>
　　<b>1、不支持分布式</b><br/>
　　这是比较明显的缺点。俺后面会提到，集中式相对于分布式具体有哪些缺点。<br/>
<br/>
　　<b>2、性能</b><br/>
　　感觉 SVN 在性能方面不咋滴，包括操作速度和存储空间，都不太理想。如果和后面提到的分布式 RCS 相比，这个缺点会更加明显（尤其是在代码 commit 的时候）。<br/>
<br/>
　　<b>3、到处散落 .svn 目录</b><br/>
　　其实这个问题倒不是什么大问题（CVS 也有此毛病）。或许某些有洁癖的人看着那么多 <b>.svn</b> 会很不爽。俺自己倒是无所谓。<br/>
<br/>
<h2>★新潮的分布式 RCS</h2><br/>
<h3>◇集中式和分布式的区别</h3><br/>
　　分布式 RCS 和集中式的主要区别在于：<br/>
　　对于集中式 RCS，只有一个中央代码仓库，每个开发人员自己机器上维护一个工作拷贝（working copy）。开发人员本地的代码在没有提交之前，是无法被RCS管理的，因此就无法进行各种操作（比如创建分支）。一旦你的开发机器和中央代码仓库的网络连接断掉（比如你把笔记本带回家写代码），你就只好干瞪眼，无法进行后续工作。<br/>
　　对于分布式 RCS，每一个开发人员的机器上都有一个代码仓库。你随时都可以提交到本地的代码仓库中。分布式 RCS 可以在网络连通的时候，再进行各个代码仓库之间的数据同步。<br/>
　　为啥这几年，分布式的 RCS 多起来捏？一个主要的推动力来自于开源社区。大部分开源项目的开发人员都分布在世界各地，有些人受限于网络因素，不能很流畅地和代码仓库交换数据。在这种情况下，分布式 RCS 的优点就体现出来了。<br/>
<br/>
<h3>◇哪些公司适合分布式的 RCS</h3><br/>
　　俺个人认为，一般的软件公司，使用分布式 RCS 的优点不如开源团队那么明显。但是在如下几种情况，你可以考虑采用分布式 RCS。<br/>
　　1、开发团队的地域性分隔<br/>
　　比如公司的开发团队分散在不同的城市，而且互相之间的网络连接不稳定。这有点类似于开源项目的团队，因此可以考虑采用分布式 RCS。<br/>
　　2、在公司之外开发<br/>
　　所谓的“在公司之外开发”，主要有如下几种情况：比如开发人员喜欢在回家之后干活、比如开发人员经常去客户现场干活、比如公司雇佣兼职人员在家干活。<br/>
　　不过这些情况都有一个前提条件，那就是：公司既没有搭建 VPN，而 RCS 又无法从公网上访问。在这种情况下，才值得用分布式 RCS。<br/>
<br/>
<h3>◇几个常见的分布式 RCS</h3><br/>
　　分布式的 RCS，名气比较大的有：Git、Mercurial、Monotone、Bazaar。下面俺大致说一下头两个。<br/>
　　<b>1、Git</b><br/>
　　（官方站点在“<a href="http://git-scm.com/" rel="nofollow" target="_blank">这里</a>”）<br/>
　　俺个人感觉，Git 的最大亮点和卖点就是：它的创始人是 Linus。单凭 Linus 这块金字招牌，Git 就吸引到很多人气。而且 Git 在各方面的功能还是比较齐全的。<br/>
　　它的主要缺点就是：对 Windows 系统支持不太好（想想也是，Linus 本人是 Linux 它爹，对 Windows 支持不好也在情理之中啊）。不过现在情况略有好转：Windows 下的 GUI 客户端 <a href="http://code.google.com/p/tortoisegit/" rel="nofollow" target="_blank">TortoiseGit</a> 才刚出来不久，将来如果能做到像 <a href="http://tortoisesvn.tigris.org/" rel="nofollow" target="_blank">TortoiseSVN</a> 那么成功，那 Git 在 Windows 下就前途光明了。<br/>
　　Git 的成功应用案例，俺不说大伙儿应该猜得到是：Linux Kernel。光这一个就足够说明问题了。<br/>
<br/>
　　<b>2、Mercurial</b><br/>
　　（官方站点在“<a href="http://www.selenic.com/mercurial/" rel="nofollow" target="_blank">这里</a>”）<br/>
　　Mercurial 是另一个比较牛的分布式 RCS。它还有一个绰号叫 Hg。化学比较好的同学，应该会立马联想到：Hg 是元素周期表中“水银”的缩写。<br/>
　　Mercurial 的特色是基于 Python 开发，所以它在跨平台方面，会比较有优势。另外，它在 Windows 上的 GUI 客户端 <a href="http://tortoisehg.sourceforge.net/" rel="nofollow" target="_blank">TortoiseHg</a> 也比 <a href="http://code.google.com/p/tortoisegit/" rel="nofollow" target="_blank">TortoiseGit</a>要成熟一些。<br/>
　　Mercurial 相对于 Git 的缺点是性能不够好。没准和基于 Python 开发有关，不过也有可能是 Git 的性能太过优秀。<br/>
　　Mercurial 的成功应用案例有：Mozilla、OpenSolaris、NetBeans。这几个也都是重量级的项目。
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2009/06/opensource-review-revision-control.html
