# 开源实践：SQLite 的使用场景 

-----

<div class="post-body entry-content">
　　上次针对 SQLite 进行了扫盲，之后有同学在<a href="../../2009/03/opensource-review-sqlite-database.md">评论里</a>问俺：如何在项目中使用它？今天咱来聊一下这个话题。<a name="more"></a><br/>
<br/>
<br/>
<h2>★如何权衡用不用？</h2><br/>
　　当你在权衡某个场合是否应该使用 SQLite 时，（在技术层面）至少要考虑如下几点：<br/>
◇能否发挥 SQLite 的某些特长？<br/>
◇是否还有其它的替代方案？<br/>
◇是否有啥潜在的技术风险？<br/>
　　想清楚上述问题之后，再做出决策。<br/>
<br/>
<br/>
<h2>★SQLite 的特点</h2><br/>
　　关于 SQLite 的强项，在<a href="../../2009/03/opensource-review-sqlite-database.md">上次的帖子</a>中已经介绍过了。考虑到某些同学比较健忘，咱再回顾一下：<br/>
◇文件型数据库，且只有单一数据文件<br/>
◇轻量级<br/>
◇绿色（不依赖其它软件库）<br/>
◇跨平台（包括引擎和数据文件）<br/>
◇支持内存数据库<br/>
◇支持较大的数据文件（TB级别）<br/>
<br/>
<br/>
<h2>★可能的替代方案</h2><br/>
　　刚才说了，权衡 SQLite 的使用需要考虑其它的替代方案，所以俺简单介绍一下和 SQLite 用途相近的其它几种技术手段。后面讲应用场景的时候，会结合这几个替代方案来作对比。<br/>
<br/>
<h3>◇<a href="https://en.wikipedia.org/wiki/Microsoft_Access" rel="nofollow" target="_blank">Access 数据库</a></h3><br/>
　　Access 数据库也是文件型的数据库，支持的很多 SQL 特性都类似于 SQLite。自从 Windows 2000 开始，Windows 就内置了 Access 的数据库引擎（<a href="https://en.wikipedia.org/wiki/Microsoft_Jet_Database_Engine" rel="nofollow" target="_blank">Microsoft Jet Database Engine</a>）。所以，Access 数据库在 Win2000 及后续版本的系统中是可以独立运行滴（不依赖 Office）。<br/>
　　Access 数据库的缺点包括：<br/>
1. 不能跨平台<br/>
2. 文件大小有限制（最大只能到 2GB）<br/>
3. 【不】支持内存数据库。<br/>
<br/>
<h3>◇其它文件型数据库</h3><br/>
　　其实，除了 Access 之外，还有另外一些文件型数据库。但是这些文件型数据库要么名气太小，要么不支持多种编程语言（比如：<a href="https://en.wikipedia.org/wiki/HSQLDB" rel="nofollow" target="_blank">HSQLDB</a>），要么已经过时（比如：FoxPro、Paradox）。所以后面分析应用场景的时候，俺就不再提及这几个玩意儿。<br/>
<br/>
<h3>◇CSV 文件</h3><br/>
　　<a href="https://en.wikipedia.org/wiki/Comma-separated_values" rel="nofollow" target="_blank">CSV</a>（Comma Separated Values）是一种很简单的纯文本格式。它本身就是用来表示二维的数据信息的。一个 CSV 文件可以理解为数据库的一张表。<br/>
　　CSV 的缺点主要在于：<br/>
1. 【无法】直接存储非文本的数据信息（比如 BLOB 类型的信息）<br/>
2. 如果需要同时存储多张表的信息，就需要对应有多个 CSV 文件（文件一多，管理起来就嫌麻烦）<br/>
3. CSV 文件【无法】体现表之间的外键关联<br/>
<br/>
<h3>◇XML 文件</h3><br/>
　　XML 文件想必大伙儿都知道，俺就不多解释了。<br/>
　　XML 格式主要缺点包括：<br/>
1. XML 本身是树状结构，有时候不便于表示二维数据表的信息<br/>
2. 一旦数据量大（比如文件超过 10MB 或者 XML 节点层次很深）的时候，解析的开销（包括空间和时间）就不容忽视了<br/>
<br/>
<br/>
<h2>★作为数据库的应用场景</h2><br/>
　　前面说了一大通，现在开始切入正题，先说说 SQLite 作为一个轻型数据库，方便干哪些事儿？<br/>
　　在这类场景中，由于是把 SQLite 作为数据库来使的，所以基本不用考虑 CSV 和 XML 这两种替代方案。<br/>
<br/>
<h3>◇需要数据库的小型桌面软件</h3><br/>
　　如果你开发一个小型的桌面软件并且需要用到数据库功能（比如某个背单词软件），那 SQLite 是一个不错的选择。因为 SQLite 很绿色又很短小精悍。<br/>
　　不过，由于 Windows 在桌面系统的比重很大。对于那些【不考虑】跨平台的开发人员，SQLite 相对于 Access 来说，没有太大的优势。<br/>
<br/>
<h3>◇需要数据库的手机软件</h3><br/>
　　眼下手机应用的发展很迅猛，相应的开发人员也多起来了。假如你就是一个手机应用程序的开发人员，并且你开发的应用需要有数据库功能（比如某个字典工具），那 SQLite 简直是不二之选。由于手机操作系统名目繁多，同时手机的内存偏小，这时候 SQLite 跨平台和轻量级的特长就充分发挥出来了。目前几个知名的手机操作系统（比如“<a href="https://en.wikipedia.org/wiki/Google_Android" rel="nofollow" target="_blank">Android</a>、<a href="https://en.wikipedia.org/wiki/Windows_Mobile" rel="nofollow" target="_blank">Windows Mobile</a>、<a href="https://en.wikipedia.org/wiki/Symbian_OS" rel="nofollow" target="_blank">Symbin</a>、<a href="https://en.wikipedia.org/wiki/Palm_%28PDA%29" rel="nofollow" target="_blank">Palm</a>”），SQLite 都支持得不错。<br/>
　　对这类场合，Access 基本没戏。<br/>
<br/>
<br/>
<h2>★作为数据容器的应用场景</h2><br/>
　　所谓数据容器，就是把 SQLite 作为装数据的容器，充分发挥 SQLite 【单一数据文件】的优点。另外，还可以避免自己定义一套数据文件格式的麻烦。要知道，自己定义一个【完善的】数据文件格式是难度极大滴（要考虑可扩展性、要考虑向下兼容、假如跨 CPU 架构还要考虑字节序、假如数据量大还要考虑性能、还要...）。<br/>
<br/>
<h3>◇数据备份/恢复、数据导入/导出</h3><br/>
　　某些软件系统（尤其是些企业应用系统）经常会碰到数据备份/恢复的功能需求。比如说，客户会要求你把一些数据（往往是业务相关的）定期备份成一个【独立的】数据文件，然后存储在别处。一旦软件系统自身发生不测，再把备份的数据恢复回来。<br/>
　　另外，导入/导出功能也是经常碰到的。一般是某个软件安装在多个地方。然后需要把一些数据（往往是业务相关的）从 A 处导出，然后在 B 处导入。<br/>
　　针对上述这两种需求：如果牵涉的数据比较大，就不宜使用 XML 或者 Access；如果牵涉到跨平台，就【无法】使用 Access；如果牵涉到多种业务数据结构，就不宜使用 CSV（除非你能忍受多个 CSV 文件并存）。有上述条件限制的地方，都很适合用 SQLite。<br/>
<br/>
<h3>◇在线升级</h3><br/>
　　这年头不联网的单机已经很少了，提供在线升级功能的软件会多起来。一般的在线升级分为两类：升级程序（比如 Firefox 自动升级新版本）和升级业务数据（比如杀毒软件升级病毒库）。这两种类型都可以使用 SQLite 来完成。把需要要升级的内容放置到 SQLite 数据库文件中，将来升级时只需下载【单一】的升级文件即可。<br/>
　　在这种场景，不太合适用 CSV 和 XML。如果不考虑跨平台，倒也可以用 Access 来搞定。<br/>
<br/>
<br/>
<h2>★作为内存数据库的应用场景</h2><br/>
　　在这种类型的场景中，咱们要充分发挥 SQLite 内存数据库的特长。由于 SQLite 的 API 设计比较合理，操作内存数据库和操作文件数据库几乎没啥区别，所以从“文件型”切换到“内存型”，代码【无需】大改。<br/>
　　另外，从3.6.11开始，SQLite 增加了<a href="http://www.sqlite.org/backup.html" rel="nofollow" target="_blank">online backup</a>接口，便于在内存数据库和文件数据库之间进行数据的同步。<br/>
<br/>
<h3>◇降低磁盘 I/O 开销</h3><br/>
　　比如开发了某个字典工具，词库存储在 SQLite 数据库文件中。当词库越来越大的时候，你可能会发现，查词的速度越来越慢。当然啦，速度慢未必是磁盘 I/O 引起的。这时候你可以把程序略微修改一下（可能就10行左右的代码），在初始化时把词库载入内存的 SQLite 数据库中。然后再对比测试一下性能。如果发现性能有明显提升，那你以后就可以一直用这种方式了。<br/>
　　使用这个招数，要小心内存数据库对内存空间的占用。比如对于普通的 PC，占用个几兆、几十兆还行，再大的话就不爽了。另外，对于手机操作系统没必要用此招数——手机的存储介质本身已经够快了。<br/>
<br/>
<h3>◇作为临时表</h3><br/>
　　内存数据库方式，还可以用来充当临时表，存放一些临时数据。当程序的进程退出时，内存数据库就自然消失了，不会留下任何垃圾。<br/>
　　不过这种方式只适合于某个程序独占临时表的情形。如果临时表需要被多个进程共用，这招就不灵了。<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
<a href="../../2009/03/opensource-review-sqlite-database.md">开源点评：SQLite 数据库扫盲</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2009/04/how-to-use-sqlite.html
