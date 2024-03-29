# 开源点评：SQLite 数据库扫盲 

-----

<div class="post-body entry-content">
　　今天注意到<a href="http://www.sqlite.org/" rel="nofollow" target="_blank">SQLite</a> 3.6.11（上个月发布的）增加了一个俺期待已久的“<a href="http://www.sqlite.org/backup.html" rel="nofollow" target="_blank">online backup</a>”接口，激动之余就顺便和大伙儿聊一下 SQLite 数据库。本帖权当是 SQLite 扫盲，如果你对 SQLite 已经很熟悉，本文就不必再看了。另外，假如你想了解 SQLite 在软件项目中的具体应用，可以看“<a href="../../2009/04/how-to-use-sqlite.md">另一篇博文</a>”。<a name="more"></a><br/>
<br/>
<br/>
<h2>★技术上的优点和特性</h2><br/>
　　SQLite 是一个轻量级、跨平台的关系型数据库。既然号称关系型数据库，支持 SQL92 标准中常用的玩意儿（比如：“视图、事务、触发器”等）就是理所当然的了，咱今天就不细说了。今天主要聊聊一些有点特色的玩意儿。<br/>
<br/>
<h3>◇轻量级</h3><br/>
　　先说它的第一个特色：轻量级。想必 SQLite 的作者很看重这个特性，连它的 Logo 都是用的“羽毛”，来显摆它的轻飘飘。<br/>
　　和 C/S 模式的数据库软件不同，SQLite 是进程内的数据库引擎，因此不存在数据库的客户端和服务器。使用 SQLite 一般只需要带上它的一个动态库，就可以享受它的全部功能。而且那个动态库的尺寸也挺小，以版本3.6.11为例，Windows 下仅仅 487KB、Linux 下仅仅 347KB。<br/>
<br/>
<h3>◇绿色软件</h3><br/>
　　SQLite 的另外一个特点是“绿色”——它的核心引擎本身不依赖第三方的软件，使用它也不需要“安装”。所以在部署的时候能够省去不少麻烦。<br/>
<br/>
<h3>◇单一文件</h3><br/>
　　所谓的“单一文件”，就是数据库中所有的信息（比如表、视图、触发器、等）都包含在一个文件内。这个文件可以 copy 到其它目录或其它机器上，也照用不误。<br/>
<br/>
<h3>◇跨平台/可移植性</h3><br/>
　　如果光支持主流操作系统，那就没啥好吹嘘的了。除了主流操作系统，SQLite 还支持了很多冷门的操作系统。我个人比较感兴趣的是它对很多嵌入式系统（比如“Android、Windows Mobile、Symbin、Palm、VxWorks”）的支持。<br/>
<br/>
<h3>◇内存数据库（in-memory database）</h3><br/>
　　这年头，内存越来越便宜，很多普通 PC 都开始以 GB 为单位来衡量内存（服务器就更甭提了）。这时候，SQLite 的内存数据库特性就越发显得好用。<br/>
　　SQLite 的 API 不区分当前操作的数据库是在内存还是在文件（对于存储介质是透明的）。所以如果你觉得 DISK I/O 有可能成为瓶颈的话，可以考虑切换为“内存数据库方式”。切换的时候，操作 SQLite 的代码基本不用大改，只要在开始时把文件从磁盘 Load 到内存，结束时把内存的数据库 Dump 回文件就 OK 了。在这种情况下，前面提到的“<a href="http://www.sqlite.org/backup.html" rel="nofollow" target="_blank">online backup API</a>”就派上用场了，聪明的同学应该明白我为啥这么期待 backup 功能了吧？<br/>
<br/>
<br/>
<h2>★技术上的缺点和不足</h2><br/>
　　前面光聊了特性和优点，为了避免枪手写软文的嫌疑，再来说说 SQLite 的一些缺点。列位看官将来如果想用它，这些缺点要权衡一下。<br/>
<br/>
<h3>◇并发访问的锁机制</h3><br/>
　　SQLite 在并发（包括多进程和多线程）读写方面的性能一直不太理想。它使用文件锁的方式，整个数据库可能会被写操作独占，从而导致其它读写操作阻塞或出错。这导致了严重的并发瓶颈。<br/>
<br/>
<h3>◇SQL标准支持不全</h3><br/>
　　在它的<a href="http://www.sqlite.org/omitted.html" rel="nofollow" target="_blank">官方网站</a>上，具体列举了不支持哪些 SQL92 标准。我个人感觉比较不爽的是不支持“外键约束”。<br/>
<br/>
<h3>◇网络文件系统（以下简称 NFS）</h3><br/>
　　有时候需要访问其它机器上的 SQLite 数据库文件，就会把数据库文件放置到网络共享目录上。这时候你就要小心了。当 SQLite 文件放置于 NFS 时，一旦出现并发读写的情况，可能会出【严重】问题（比如数据损坏）。原因据说是由于某些 NFS 文件系统对”文件锁“的实现有 Bug（不是 Sqlite 的责任）。<br/>
<br/>
<br/>
<h2>★编程语言接口</h2><br/>
　　SQLite 支持很多种语言的编程接口。这对于我这种喜欢混用多种编程语言的人来说，是很爽的。下面我大概介绍一下。<br/>
<br/>
<h3>◇C/C++</h3><br/>
　　由于 SQLite 本身是 C 写的，它<a href="http://www.sqlite.org/cintro.html" rel="nofollow" target="_blank">自带的 API</a> 也是 C 接口的。所以 C/C++ 用起来最直接了。假如你不喜欢面向过程的 C API 风格，可以另外找个 C++ 的包装库。喜欢重新发明轮子的同学，也可以自己包装一个。<br/>
<br/>
<h3>◇Java</h3><br/>
　　如果要用 Java 访问 SQLite，可以通过 SQLite 的 JDBC 驱动，或者通过专门的 SQLite 包装库。俺个人建议走 JDBC 方式，万一将来要换数据库，代码就不用大改。<br/>
<br/>
<h3>◇Python</h3><br/>
　　<a href="http://www.pysqlite.org/" rel="nofollow" target="_blank">pysqlite</a> 是 Python 操作 SQLite 的首选。从 Python 2.5 开始，它已经被整合到 Python 的标准库中（看来 Python 社区还是蛮喜欢 SQLite 嘛）。<br/>
<br/>
<h3>◇dotNet</h3><br/>
　　对于喜欢 dotNet 的同学，可以通过 SQLite 的 <a href="http://sqlite.phxsoftware.com/" rel="nofollow" target="_blank">ADO.NET</a> 驱动来访问。<br/>
<br/>
<h3>◇Ruby</h3><br/>
　　Ruby 可以通过 <a href="http://rubyforge.org/projects/sqlite-ruby/" rel="nofollow" target="_blank">SQLite-Ruby</a> 操作 SQLite 数据库，不过俺没用过。<br/>
<br/>
<h3>◇Perl</h3><br/>
　　在 CPAN 上有 <a href="http://search.cpan.org/search%3fmodule=DBD::SQLite" rel="nofollow" target="_blank">DBD::SQLite</a>，不过俺也没用过。<br/>
<br/>
<br/>
<h2>★一些非技术的参考因素</h2><br/>
　　前面讲的都是技术层面的话题，如果你考虑在公司的商业软件项目中使用 SQLite。还需要根据《<a href="http://program-think.blogspot.com/2009/02/how-to-choose-opensource-project.html">如何选择开源项目</a>》里面提到的几个参考因素，再评估一下。<br/>
<br/>
<h3>◇授权协议（License）</h3><br/>
　　SQLite 使用的是 <a href="https://en.wikipedia.org/wiki/Public_domain" rel="nofollow" target="_blank">Public Domain</a> 协议，这是最爽一种，可以放心大胆地用。<br/>
<br/>
<h3>◇用户的普及程度</h3><br/>
　　最近这几年，使用 SQLite 的人越来越多（从“<a href="https://www.google.com/trends?q=sqlite" rel="nofollow" target="_blank">Google Trends</a>”可以反应出来）。包括一些大公司也开始把它整合到产品中（比如：Mozilla 的 Firefox，Apple 的 Safari、Adobe 的 AIR）。这说明它的健壮性、稳定性等方面【不会】有太大问题。<br/>
<br/>
<h3>◇开发的活跃程度</h3><br/>
　　如果到 SQLite 的 <a href="http://www.sqlite.org/changes.html" rel="nofollow" target="_blank">Change Log</a> 上大致瞅一眼，可以看出最近5年基本上每1-2个月都会有更新。说明开发的活跃度还是非常高的。<br/>
　　从上述几个【非技术】因素来看，SQLite 用于商业公司的软件项目还是非常靠谱的。<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
<a href="../../2009/04/how-to-use-sqlite.md">开源实践：SQLite 的使用场景</a><br/>
<a href="../../2011/08/opensource-review-zeromq.md">开源点评：ZeroMQ 简介</a><br/>
<a href="../../2009/05/opensource-review-protocol-buffers.md">开源点评：Protocol Buffers 介绍</a><br/>
<a href="../../2009/02/how-to-choose-opensource-project.md">如何选择开源项目</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2009/03/opensource-review-sqlite-database.html
