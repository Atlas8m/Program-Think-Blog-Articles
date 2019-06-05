# 开源点评：cURL——优秀的应用层网络协议库 

-----

<div class="post-body entry-content">
　　今天来点评一下 <a href="https://curl.haxx.se/" rel="nofollow" target="_blank">cURL</a>，这是一个老资格的开源项目，使用它可以基于多种应用层网络协议进行数据传输（包括上传和下载）。它的特点是：支持的协议多、跨平台、支持多种编程语言接口。后面我会针对这些特点作一些简单的介绍。<a name="more"></a><br/>
　　cURL 项目实际上包含两个部分：命令行工具和编程用的库（<a href="https://curl.haxx.se/libcurl/" rel="nofollow" target="_blank">libcurl</a>）。两者支持的功能基本相同。由于开发人员更多地是和 libcurl 打交道，所以后面我会主要介绍 libcurl。<br/>
<br/>
<br/>
<h2>★支持多种应用层协议</h2><br/>
　　多种网络协议支持是 cURL 的主要卖点。截至到（写本文时）最新的7.19.4版本，它支持的网络协议至少有：FTP、FTPS、HTTP、HTTPS、<a href="https://en.wikipedia.org/wiki/Secure_copy" rel="nofollow" target="_blank">SCP</a>（secure copy）、<a href="https://en.wikipedia.org/wiki/SSH_file_transfer_protocol" rel="nofollow" target="_blank">SFTP</a>（SSH FTP）、<a href="https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol" rel="nofollow" target="_blank">TFTP</a>（trivial FTP）、TELNET、<a href="https://en.wikipedia.org/wiki/DICT" rel="nofollow" target="_blank">DICT</a>、<a href="https://en.wikipedia.org/wiki/Lightweight_Directory_Access_Protocol" rel="nofollow" target="_blank">LDAP</a>、LDAPS、<a href="https://en.wikipedia.org/wiki/File:URL" rel="nofollow" target="_blank">FILE</a>，够全的吧？<br/>
<br/>
<h3>◇HTTP</h3><br/>
　　HTTP 估计是最常用的一种协议，俺简单说一下 cURL 对 HTTP 支持的程度。<br/>
对于协议版本：cURL 支持 HTTP 1.0 和 HTTP 1.1。<br/>
对于请求方式：cURL 支持 GET、POST、PUT、File Upload POST。<br/>
对于代理（Proxy）类型：包括 HTTP Proxy、<a href="https://en.wikipedia.org/wiki/SOCKS#SOCKS_4_protocol" rel="nofollow" target="_blank">SOCKS4</a> Proxy、<a href="https://en.wikipedia.org/wiki/SOCKS#SOCKS_5_protocol" rel="nofollow" target="_blank">SOCKS5</a> Proxy。<br/>
　　另外，还可以设定 HTTP 认证的用户名口令，cookies，referer 等许多杂七杂八的东东。<br/>
<br/>
<h3>◇SSL 加密</h3><br/>
　　假如你要支持某些依赖 <a href="https://en.wikipedia.org/wiki/Secure_Sockets_Layer" rel="nofollow" target="_blank">SSL</a>/<a href="https://en.wikipedia.org/wiki/Transport_Layer_Security" rel="nofollow" target="_blank">TLS</a>的协议（比如 HTTPS、FTPS），则需要用到 <a href="https://en.wikipedia.org/wiki/OpenSSL" rel="nofollow" target="_blank">OpenSSL</a> 库。在 cURL 的<a href="https://curl.haxx.se/download.html" rel="nofollow" target="_blank">下载页面</a>上标注有 SSL 标志的压缩包，都内置了 <a href="https://en.wikipedia.org/wiki/OpenSSL" rel="nofollow" target="_blank">OpenSSL</a> 的动态库。另外，在cURL 配置 SSL 证书的相关说明，可以参见“<a href="https://curl.haxx.se/docs/sslcerts.html" rel="nofollow" target="_blank">这里</a>”。<br/>
<br/>
<br/>
<h2>★跨平台</h2><br/>
　　cURL 支持的平台是相当多的。即使是一些冷门的操作系统（比如：DOS、OS/2），它也支持得很好。<br/>
　　另外，cURL 官方网站的<a href="https://curl.haxx.se/download.html" rel="nofollow" target="_blank">下载页面</a>提供了基于不同平台的、编译好的、二进制文件供大伙儿直接使用。对于 Linux，它还根据不同厂商、不同发行版本，分别提供二进制文件，考虑相当周到。相比某些开源项目只提供源代码（使用者需要自己动手编译），cURL 算是很方便的一个。<br/>
<br/>
<br/>
<h2>★多种编程语言支持</h2><br/>
　　和上次 <a href="../../2009/03/opensource-review-sqlite-database.md">点评的SQLite</a>一样，libcurl 也支持多种编程语言的绑定，而且 cURL 整合的编程语言比 <a href="https://en.wikipedia.org/wiki/SQLite" rel="nofollow" target="_blank">SQLite</a> 还要多。下面列了一些比较常见的编程语言和平台提供的cURL接口。<br/>
<br/>
<h3>◇C/C++</h3><br/>
　　cURL 本身是 C 写的，因此 C 和 C++ 都可以直接调用它的 C 接口 API。在 cURL 的源码包中带有很多 C 的示例，大伙儿可以依样画葫芦。<br/>
喜欢OO的同学，可以使用 <a href="http://curlpp.org/" rel="nofollow" target="_blank">cURLpp</a> 提供的 C++ 包装类。这玩意儿使用 MIT 许可协议。<br/>
<br/>
<h3>◇Java</h3><br/>
　　cURL 和 Java 的整合通过 JNI 实现。可以在“<a href="https://curl.haxx.se/libcurl/java/" rel="nofollow" target="_blank">这里</a>”下载压缩包，然后自己编译出相关的动态库和 class 文件。那些懒惰的同学可以到“<a href="http://www.gknw.de/mirror/curl/curl_java/" rel="nofollow" target="_blank">这里</a>”捡现成。<br/>
<br/>
<h3>◇Python</h3><br/>
　　<a href="http://pycurl.sourceforge.net/" rel="nofollow" target="_blank">pycurl</a> 是 cURL 的 Python 包装库。如果你觉得 Python 内置的 <a href="https://docs.python.org/library/urllib.html" rel="nofollow" target="_blank">urllib</a> 功能不够，可以考虑用它。（这玩意儿使用双重许可协议：LGPL  和MIT/X）<br/>
<br/>
<h3>◇dotNET</h3><br/>
　　cURL 和 dotNET 的绑定 <a href="http://libcurl-net.sourceforge.net/" rel="nofollow" target="_blank">libcurl.NET</a>。这玩意儿只支持 Win32 操作系统。不过不要紧，对于非 Windows 系统，可以使用 cURL 的 <a href="https://en.wikipedia.org/wiki/Mono_%28software%29" rel="nofollow" target="_blank">Mono</a> 绑定 <a href="http://forge.novell.com/modules/xfmod/project/?libcurl-mono" rel="nofollow" target="_blank">libcurl.mono</a>。<br/>
<br/>
<h3>◇Visual Basic</h3><br/>
　　cURL 和 VB 的绑定 <a href="http://libcurl-vb.sourceforge.net/" rel="nofollow" target="_blank">libcurl.vb</a>。这个项目和上述的 <a href="http://libcurl-net.sourceforge.net/" rel="nofollow" target="_blank">libcurl.NET</a> 都是由同一个作者维护的。（也都使用MIT许可协议）<br/>
<br/>
<h3>◇PHP</h3><br/>
　　PHP 要支持 cURL 相对简单多了。在 <a href="http://cn.php.net/curl" rel="nofollow" target="_blank">PHP 官方网站</a>上有相关的安装/配置说明。<br/>
<br/>
<h3>◇Ruby</h3><br/>
　　cURL 的 Ruby 的绑定 <a href="http://curb.rubyforge.org/" rel="nofollow" target="_blank">Curb</a>。（这玩意儿使用 Ruby 许可协议）<br/>
<br/>
<h3>◇Perl</h3><br/>
　　cURL 和 Perl 的绑定 <a href="http://search.cpan.org/%7Ecrisb/WWW-Curl/Easy.pm.in" rel="nofollow" target="_blank">WWW::Curl::Easy</a>。（这玩意儿使用 MPL 或 MIT/X 许可协议）<br/>
<br/>
<br/>
<h2>★应用场景举例</h2><br/>
　　前面说了很多 cURL 的特点，下面来随手举几个应用的例子。<br/>
<br/>
<h3>◇传输文件</h3><br/>
　　如果你需要在程序中进行文件的上传、下载，使用 libcurl 会非常方便。由于它支持的协议很多。一旦将来你的应用程序发生需求变更，改用其它协议，你的代码也不用大改。<br/>
<br/>
<h3>◇调用 Web 接口</h3><br/>
　　随着 SOA 风格的流行，很多比较复杂的系统都会提供很多 Web API 接口。如果你要在程序中调用 Web API 接口，可以考虑使用 libcurl 来实现。<br/>
<br/>
<h3>◇Web 测试</h3><br/>
　　还记得之前<a href="../../2009/02/7.md">善用自动化</a>的帖子里提到自动测试的好处吗？由于 cURL 对 HTTP 的支持很全。在 HTTP 协议方面，浏览器能干的活它基本上也能干。再加上它可以和很多脚本语言绑定（除了前面提到的，还可以支持 Lua、Tcl、Lisp 等脚本）。所以你可以用“脚本语言 + cURL”的方式，来进行某些自动化的 Web 测试。<br/>
　　比如测试某 Web 站点的安全性（是否有 SQL 注入、XSS 跨站脚本等安全漏洞）或者测试某 Web 接口是否符合文档的约定或者测试某些 Web 接口的性能或者......<br/>
<br/>
<br/>
<h2>★其它一些补充说明</h2><br/>
　　如果你想定期了解 cURL 的新版本、新特性、新 Bug，可以订阅<a href="https://curl.haxx.se/mail/" rel="nofollow" target="_blank">相关的邮件列表</a>。<br/>
　　另外，cURL 使用 MIT/X 衍生协议，可以用于商业软件中。<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
<a href="../../2009/03/opensource-review-sqlite-database.md">开源点评：SQLite 数据库扫盲</a><br/>
<a href="../../2011/08/opensource-review-zeromq.md">开源点评：ZeroMQ 简介</a><br/>
<a href="../../2009/05/opensource-review-protocol-buffers.md">开源点评：Protocol Buffers 介绍</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2009/03/opensource-review-curl-library.html
