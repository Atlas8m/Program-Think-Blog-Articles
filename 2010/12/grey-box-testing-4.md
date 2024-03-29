# 如何开展灰盒测试[4]：接口测试实战——测试跨主机的模块接口 

-----

<div class="post-body entry-content">
　　跨主机的交互方式，必然涉及到网络（为了防止爱抬杠的同学挑刺，事先声明：本节提及的网络，均是基于 TCP/IP 网络）。在 TCP/IP 协议栈的4个层次中（参见<a href="https://zh.wikipedia.org/wiki/TCP/IP%E5%8D%8F%E8%AE%AE" rel="nofollow" target="_blank">这里</a>），模块间的交互方式主要是位于上面两层（传输层、应用层）。<br/>
　　有些软件系统，直接采用某种现成的应用层协议（比如 HTTP）来进行跨主机的通讯。这时候，测试人员就只需关心该应用层协议，不用操心传输层是如何实现的。<br/>
　　还有一些软件系统，自己实现了某种专有的应用层协议。这种情况下，对测试人员的要求就比较高了——测试人员需要大致了解传输层的知识以及该专有应用协议的格式。（具体请看本帖的 Socket 这一节）<a name="more"></a><br/>
<br/>
<br/>
<h2>★基于 Web 接口的交互（HTTP 协议）</h2><br/>
　　由于这几年 B/S 系统大行其道，而B/S系统，总是离不开HTTP协议，所以俺首先来介绍它。<br/>
　　在 B/S 系统中，服务端（也叫后端）总是会提供一些 Web 接口给客户端（前端）进行调用。这种调用总是基于 HTTP 协议来进行（HTTP 协议的介绍，请看维基百科的<a href="https://zh.wikipedia.org/wiki/%E8%B6%85%E6%96%87%E6%9C%AC%E4%BC%A0%E8%BE%93%E5%8D%8F%E8%AE%AE" rel="nofollow" target="_blank">这里</a>）。当你针对服务端进行灰盒测试，你需要模拟客户端的各种 HTTP 请求（既要包括合法的请求，也要包括各种非法的、无效的请求），然后再检验服务端返回的响应（Response）内容。如果响应内容不符合接口文档的约定，就表明该服务端模块出 Bug 了。<br/>
　　HTTP 请求（Request）的类型，常用的主要是 GET 和 POST。这两者的用途及区别，维基百科上已有，俺就不浪费口水了，直接说如何进行脚本编程。<br/>
<br/>
<h3>◇使用内置的标准模块</h3><br/>
　　在 Python 脚本中，内置了完善的模块（urllib 和 urllib2），以便于你操作 HTTP 协议。对于简单的使用，urllib 就足够了。<br/>
<br/>
　　比如俺想用 GET 方式抓取 Google 的主页，只需如下3行代码：<br/>
<pre style="background-color:#DDD;font-family:Courier,monospace;">import urllib
f = urllib.urlopen("http://www.google.com/")
print f.read()</pre><br/>
　　如果想往某个 Web 接口 POST 数据，并得到服务端的返回内容，只需再增加1行代码（构造 POST 参数）：<br/>
<pre style="background-color:#DDD;font-family:Courier,monospace;">import urllib
params = urllib.urlencode({name1:value1, name2:value2})
f = urllib.urlopen("http://xxxx/xxxx", params)
print f.read()</pre><br/>
　　如果需要一些复杂点的功能（比如 cookie；比如 proxy），urllib2 就可以派上用场了。更多的使用细节，请看洋文的官方文档（<a href="https://docs.python.org/2/library/urllib.html" rel="nofollow" target="_blank">这里</a>和<a href="https://docs.python.org/3/library/urllib.html" rel="nofollow" target="_blank">这里</a>）。<br/>
<br/>
<h3>◇使用 cURL</h3><br/>
　　俺博客的老读者，或许记得俺在2009年初写过的一个帖子：《<a href="http://program-think.blogspot.com/2009/03/opensource-review-curl-library.html">开源点评：cURL——优秀的应用层网络协议库</a>》。看完这个帖子，你就能领会到：cURL 是一个非常牛X的网络协议库，支持很多种网络协议（显然也包括HTTP）。这么牛X的一个开源库，自然会有不少编程语言对其进行包裹。下面俺把其它脚本语言针对 cURL 的封装列举如下。如果你不喜欢用 Python，或许可以改用俺列举的其它脚本语言（以下列举的都是开源项目）。<br/>
<blockquote style="background-color:#DDD;">Python　<a href="http://pycurl.sourceforge.net/" rel="nofollow" target="_blank">pycurl</a><br/>
Ruby　　<a href="http://curb.rubyforge.org/" rel="nofollow" target="_blank">Curb</a><br/>
Perl　　<a href="http://search.cpan.org/%7Ecrisb/WWW-Curl/Easy.pm.in" rel="nofollow" target="_blank">WWW::Curl::Easy</a><br/>
dotNet　<a href="http://libcurl-net.sourceforge.net/" rel="nofollow" target="_blank">libcurl.NET</a></blockquote><br/>
<h2>★基于数据库的交互</h2><br/>
　　在现有软件系统的开发过程中，操作数据库也属于家常便饭。因此，聊完 HTTP 协议之后，就得来聊一下数据库的操作。眼下，大部分程序员都是远程操作数据库，所以俺把数据库的操作也归入“跨主机”交互方式。（其实本节的内容也适用于操作本机数据库）<br/>
　　在很多软件系统中，软件模块需要从数据库中读取数据或者把自己生成的数据存储到数据库中。因此，测试人员需要通过一些测试脚本，在数据库中制造测试数据，以作为软件模块的输入；或者在软件模块把数据保存到数据库之后，验证其输出的数据是否符合接口文档的约定。<br/>
<br/>
<h3>◇跨数据库的接口</h3><br/>
　　所谓的“跨数据库的接口”，顾名思义，就是这种编程接口可以支持多种数据库产品。如果你没有其它特殊的要求（比如性能），俺建议尽量用这种方式操作数据库。这样的好处是，万一哪天数据库平台换了，你的测试脚本可以不用大改（甚至不改）。<br/>
<br/>
　　<b>1、ODBC</b><br/>
　　ODBC 是一种三跨（跨数据库、跨操作系统、跨编程语言）的数据库接口。大部分知名的数据库软件都支持ODBC方式访问。<br/>
　　Python 社区提供了不止一个的 ODBC 编程库，可以考虑用<a href="https://github.com/mkleehammer/pyodbc" rel="nofollow" target="_blank">PyODBC</a>或<a href="http://ceodbc.sourceforge.net/" rel="nofollow" target="_blank">ceODBC</a>。<br/>
<br/>
　　<b>2、JDBC</b><br/>
　　对于搞 Java 开发的同学，应该很熟悉 JDBC。不过很多人有一个【误解】，以为只有 Java 才可以进行 JDBC 编程。其实不然！自从前几年 JVM 开始效仿 DotNet，支持多种编程语言之后，很多脚本语言也可以在 JVM 上跑起来了。比如 Python（JVM 上叫 <a href="https://zh.wikipedia.org/wiki/Jython" rel="nofollow" target="_blank">Jython</a>）、Ruby（JVM 上叫 <a href="https://zh.wikipedia.org/wiki/JRuby" rel="nofollow" target="_blank">JRuby</a>）、<a href="https://zh.wikipedia.org/wiki/Groovy" rel="nofollow" target="_blank">Groovy</a>。<br/>
　　作为测试人员，你也可以利用上述脚本语言，编写基于JDBC的数据库测试脚本。<br/>
<br/>
　　<b>3、ADO / ADO.Net</b><br/>
　　ADO / ADO.Net（以下简称ADO）是微软设计的跨数据库编程接口。既然是微软搞得，秉承其一贯风格，自然是不跨操作系统的。如果你所有的测试工作都在 Windows 平台上，也可以考虑用 ADO 来访问数据库。<br/>
　　如果要用 Python 进行 ADO 编程，可以考虑用 PyWin32 开源项目（官网在“<a href="http://sourceforge.net/projects/pywin32/" rel="nofollow" target="_blank">这里</a>”）。它是专门针对 Windows 平台的 Python 扩展，让 Python 可以很方便地调用各种 Win32 的 API（包括ADO 的 API）。<br/>
　　你还可以使用基于 dotNet 平台之上脚本语言。比如 <a href="https://zh.wikipedia.org/wiki/IronPython" rel="nofollow" target="_blank">IronPython</a>、<a href="https://zh.wikipedia.org/wiki/IronRuby" rel="nofollow" target="_blank">IronRuby</a>等。这些运行于 DotNet 之上的脚本语言，自然也就具有操作 ADO 的能力。<br/>
<br/>
<h3>◇特定数据库的接口</h3><br/>
　　前面已经提到“跨数据库的接口”有种种好处，那啥时候需要用特定数据库的接口捏？有时候，你需要使用某个数据库专有的某个特色功能，这时候，通用的数据库接口可能就搞不定了，你就需要用该数据库特定的编程接口来写脚本。当然，这种情况不是很多见。<br/>
下面，俺把几种常见数据库及其对应的 Python 开源项目列在如下表格中。<br/>
<blockquote style="background-color:#DDD;">Oracle　　　　<a href="http://cx-oracle.sourceforge.net/" rel="nofollow" target="_blank">cx_Oracle</a><br/>
SQL Server　　<a href="http://pymssql.org/" rel="nofollow" target="_blank">pymssql</a><br/>
DB2　　　　　　<a href="http://sourceforge.net/projects/pydb2/" rel="nofollow" target="_blank">pydb2</a><br/>
MySQL　　　　　<a href="http://mysql-python.sourceforge.net/" rel="nofollow" target="_blank">MySQL-Python</a><br/>
PostgreSQL　　<a href="http://initd.org/psycopg/" rel="nofollow" target="_blank">psycopg2</a><br/>
SQLite　　　　<a href="https://docs.python.org/library/sqlite3.html" rel="nofollow" target="_blank">（Python 内置）</a></blockquote><br/>
<h3>◇关于 Python 操作数据库的补充说明</h3><br/>
　　刚才介绍了多个操作数据库的 Python 开源项目。俺顺便补充一下：Python 社区制定了一个<a href="https://www.python.org/dev/peps/pep-0249/" rel="nofollow" target="_blank">数据库操作的规范</a>。那些比较靠谱的数据库操作的模块，都会遵循该规范。因此，你只要熟悉了某一个模块，也就很容易熟悉其它模块。<br/>
<br/>
<br/>
<h2>★基于网络文件系统的交互（NFS）</h2><br/>
　　网络文件系统存在的目的，就是把跨主机的文件操作，伪装成本机的文件操作。所以，对 NFS 的灰盒测试，放到后面的帖子（主机内的跨进程交互方式）一起聊。<br/>
<br/>
<br/>
<h2>★基于其它应用层协议的交互</h2><br/>
　　还有另外一些应用层的网络协议，其应用范围没有 HTTP 协议那么广，因此，Python 没有把它纳入到内置的标准模块中。这时候，前面提到的 PycURL 就可以派上用场了。你只要安装一个 PycURL，就可以搞定十几种应用层协议（FTP, FTPS, Gopher, SCP, SFTP, TFTP, TELNET, LDAP, LDAPS, IMAP, POP3, SMTP），非常之爽！<br/>
<br/>
<br/>
<h2>★基于 Socket 的交互</h2><br/>
　　前面提到，如果软件系统自己实现了专有的应用层协议，那测试人员进行灰盒测试时，就必须了解该专有协议的格式以及传输层的知识。在这种情况下，测试人员可能需要直接和 Socket 打交道。<br/>
　　Python 内置了对 socket 的支持，Python 官方的洋文介绍在<a href="https://docs.python.org/howto/sockets.html" rel="nofollow" target="_blank">这里</a>。Python 的 socket API 和传统的伯克利套接字 API 很像，如果你之前写过 C 语言的 socket 程序，那搞定 Python 的 socket 程序肯定是不在话下滴。<br/>
　　但你千万别高兴得太早。用脚本来模拟软件模块之间的 socket 通讯，主要难点往往不在于socket，而在于专有协议本身。有些专有的通讯协议格式多变且复杂，有些虽然格式不太复杂，但是通讯双方交互的逻辑很复杂。因此，在 socket 层面进行灰盒测试，测试人员要多花精力在这方面。<br/>
<br/>
对“跨主机的模块接口”该如何进行灰盒测试，就介绍到这里。下一个帖子介绍“主机内跨进程的模块接口”该如何搞。<br/>
<br/>
<br/>
<a href="../../2010/11/grey-box-testing-0.md">回到本系列的目录</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2010/12/grey-box-testing-4.html
