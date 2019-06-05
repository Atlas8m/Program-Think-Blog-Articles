# 为啥俺推荐 Python[5]：作为瑞士军刀的 Python——顺便分享俺整理的 Python 开源库 

-----

<div class="post-body entry-content">
　　本系列几乎变成年度系列了——<a href="../../2012/02/why-choose-python-4-fp.md">上一篇帖子</a>是去年元宵节发的。这几天正值春节假期，赶紧抽空补上本系列新的一篇，免得大伙儿以为本系列“烂尾”了。<br/>
　　“瑞士军刀”，大伙儿应该很熟悉，俺就不解释了。拿“瑞士军刀”来比喻 Python 就是想说明：Python 不但短小精悍，而且功能强大。今天就来介绍一下 Python 的这两个特点（尤其是后者）。<a name="more"></a><br/>
<br/>
<br/>
<h2>★短小精悍</h2><br/>
<h3>◇轻量级的的代码</h3><br/>
　　要吹嘘 Python 的轻量级，首先要吹嘘的，自然是它简洁的代码。为了让大伙儿有个初步的印象，举几个例子。<br/>
<br/>
　　举例1<br/>
　　要得到100-200之间所有奇数的3次方，只需如下一行<br/>
<div class="source"><pre><span></span><span class="p">[</span><span class="n">x</span><span class="o">**</span><span class="mi">3</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">100</span><span class="p">,</span> <span class="mi">200</span><span class="p">)</span> <span class="k">if</span> <span class="p">(</span><span class="n">x</span><span class="o">%</span><span class="mi">2</span><span class="p">)</span><span class="o">==</span><span class="mi">1</span><span class="p">]</span>
</pre></div><br/>
　　举例2<br/>
　　如果要把上述结果拼成一个逗号分隔的字符串，还是只要一行<br/>
<div class="source"><pre><span></span><span class="s1">','</span><span class="o">.</span><span class="n">join</span><span class="p">([</span><span class="nb">str</span><span class="p">(</span><span class="n">x</span><span class="o">**</span><span class="mi">3</span><span class="p">)</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">100</span><span class="p">,</span> <span class="mi">200</span><span class="p">)</span> <span class="k">if</span> <span class="p">(</span><span class="n">x</span><span class="o">%</span><span class="mi">2</span><span class="p">)</span><span class="o">==</span><span class="mi">1</span><span class="p">])</span>
</pre></div><br/>
　　举例3<br/>
　　可能有人觉得上面2个例子是小儿科，再来举一个稍微复杂点的。只需一行代码，即可实现网络扫描（用的是第三方的 <a href="http://www.secdev.org/projects/scapy/" rel="nofollow" target="_blank">Scapy</a> 工具）。<br/>
<div class="source"><pre><span></span><span class="c1"># 传统的 ping 扫描，基于 ICMP 协议</span>
<span class="n">ans</span><span class="p">,</span><span class="n">unans</span> <span class="o">=</span> <span class="n">sr</span><span class="p">(</span><span class="n">IP</span><span class="p">(</span><span class="n">dst</span><span class="o">=</span><span class="s2">"192.168.1.1-254"</span><span class="p">)</span><span class="o">/</span><span class="n">ICMP</span><span class="p">())</span>
<span class="c1"># 局域网扫描，基于 ARP 协议</span>
<span class="n">ans</span><span class="p">,</span><span class="n">unans</span> <span class="o">=</span> <span class="n">srp</span><span class="p">(</span><span class="n">Ether</span><span class="p">(</span><span class="n">dst</span><span class="o">=</span><span class="s2">"ff:ff:ff:ff:ff:ff"</span><span class="p">)</span><span class="o">/</span><span class="n">ARP</span><span class="p">(</span><span class="n">pdst</span><span class="o">=</span><span class="s2">"192.168.1.0/24"</span><span class="p">),</span> <span class="n">timeout</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
</pre></div><br/>
<h3>◇轻量级的安装环境</h3><br/>
　　比如 Python 的安装包只有十几兆，而 Java 的 JDK 安装包动辄接近100兆。<br/>
<br/>
<h3>◇轻量级的运行环境</h3><br/>
　　同样是运行一个“Hello World”，用 Python 写的进程，占用的内存会更小（相比大多数其它编程语言）。而且 Python 的运行环境（Python 虚拟机）可以很方便地嵌入到 C/C++ 程序中，只需额外带一个动态库即可。<br/>
<br/>
<br/>
<h2>★功能强大之1——跟非常多的语言整合</h2><br/>
　　很多程序员喜欢“在一棵树上吊死”——始终只用一种编程语言。俺非常反对这种倾向。要想成为一个优秀的程序员，有必要掌握【不同风格/不同范式】的编程语言。编程语言多样化的好处在于，你可以利用不同语言的特色，以取长补短。<br/>
　　而 Python 在跨语言整合方面，堪称佼佼者——你很难找到哪个语言，能像 Python 这样，跟如此多的语言进行整合。<br/>
　　下面简单举几个例子：<br/>
<br/>
<h3>◇跟 C/C++ 整合</h3><br/>
　　咱们常用的 Python 运行环境也称为 CPython，是用 C 语言写的。所以 Python 天生就具有跟 C/C++ 整合的能力。而且这种整合是双向的——也就是说，既可以在 Python 模块调用 C/C++ 模块，也可以在 C/C++ 模块调用 Python 模块。<br/>
　　Python 跟 C/C++ 整合，可以有如下三个优点：<br/>
<br/>
　　<b>1. 丰富的第三方资源</b><br/>
　　因为 C/C++ 具有非常丰富的第三方模块（包括开源和闭源），其丰富程度超过 Java。所以 Python 可以利用这种整合能力，直接调用各种 C/C++ 的模块，来丰富自己的功能。<br/>
　　举个例子<br/>
　　比如 cURL 是一个C语言编写的应用层网络工具，功能非常强。而 Python 可以通过整合 cURL 直接获得 cURL 的强大功能。<br/>
<br/>
　　<b>2. 性能的提升</b><br/>
　　除了第三方模块丰富，C/C++ 开发的模块还有一个优点——性能好。所以，Python 整合了 C/C++ 模块之后，还能趁机获得性能提升。<br/>
　　举个例子<br/>
　　比方说你要写一个 3D 游戏，其中的 3D 渲染引擎是性能瓶颈。那么你可以用 Python 整合一个 C/C++ 的 3D 渲染引擎。而 Python 只用来实现跟游戏高层应用逻辑相关的部分。这样可以一举两得：性能不差，代码不多。<br/>
　　顺便说一下：如今有不少游戏都走这个开发思路——底层引擎用【重型的】C 或 C++ 实现，以确保高性能；而高层的业务逻辑则用【轻型的】脚本语言来开发。<br/>
<br/>
　　<b>3. 跟操作系统整合</b><br/>
　　地球上的操作系统，只要是有点名气的，内核都是 C 语言写的；除了操作系统内核，大部分操作系统的运行库也都是 C/C++ 编写的。所以，Python 跟 C/C++ 整合，可以带来第三个好处——跟操作系统的整合。关于这点，待会儿俺还会专门聊。<br/>
<br/>
<h3>◇跟 JVM（Java） 整合</h3><br/>
　　通过 <a href="http://www.jython.org/" rel="nofollow" target="_blank">Jython</a> 这个开源项目，Python 可以无缝整合到 JVM 环境中。如此一来，Python 能直接调用所有 JVM 标准库（比如 JDBC）和第三方库（比如 Lucene），还可以跟各种 JVM 语言（比如“Java、Scale、Groovy”等）进行互操作。<br/>
<br/>
<h3>◇跟 dotNet 整合</h3><br/>
　　通过 <a href="http://ironpython.net/" rel="nofollow" target="_blank">IronPython</a> 这个开源项目，Python 可以无缝整合到 dotNet 环境中。如此一来，Python 能直接调用所有 dotNet 的标准库（比如 ADO.NET）和第三方库，还可以跟各种 dotNet 语言（比如“C#、F#”等）进行互操作。<br/>
　　顺便说一下：Jython 跟 IronPython 貌似同一个作者，牛人啊！<br/>
<br/>
<br/>
<h2>★功能强大之2——既可以跨平台，又可以跟操作系统深度整合</h2><br/>
<h3>◇Python 语言如何体现“跨平台性”？</h3><br/>
　　说到跨平台这个话题，俺给编程语言分一下类：<br/>
1. 可以跨平台，但无法跟操作系统深度耦合（比如 JavaScript、PHP）<br/>
2. 可以跟操作系统深度耦合，但无法跨平台（比如 VB、VBScript）<br/>
3. 既可以跨平台，又可以跟操作系统深度耦合（比如 C C++ Python）<br/>
<br/>
　　为啥第三类语言能做到两者兼得？因为这类语言把选择权留给了程序猿——<br/>
一方面，如果程序猿遵循跨平台的开发规范，那么写出来的代码就是跨平台的；<br/>
另一方面，程序猿也可以写出跟系统耦合很紧密的代码——这样的代码虽然不能跨平台，但可以发挥特定平台的强项。<br/>
　　显然俺喜欢第三类编程语言，因为这类语言给了程序猿自由。<br/>
<br/>
<h3>◇Python 语言如何“与操作系统深度整合”？</h3><br/>
　　Python 的跨平台特性，懂 Python 的同学估计都晓得了。所以俺单独说一下 Python 如何跟操作系统深度整合。为了照顾到大多数人，俺拿 Windows 来说事儿。<br/>
　　在 Python 社区有一个很有名气的库，叫做 <a href="http://sourceforge.net/projects/pywin32/" rel="nofollow" target="_blank">PyWin32</a>。通过这个库，可以让 Python 代码很容易地调用 Windows 的 API 以及 COM 组件。<br/>
比方说，可以用 Python 代码直接操作 Windows 注册表<br/>
比方说，可以用 Python 代码直接读写 Windows 的系统日志<br/>
比方说，可以用 Python 代码直接操作某个窗口句柄<br/>
比方说，可以利用 COM 组件，直接调用 Word 来处理 doc 格式的文档<br/>
......<br/>
<br/>
<br/>
<h2>★功能强大之3——具有很丰富的第三方模块</h2><br/>
　　最后一个方面，也是最重要的一个方面，就是 Python 社区具有非常非常丰富的资源（第三方库），而且几乎都是开源的。形形色色的编程领域几乎都可以看到 Python 的身影。<br/>
　　<b>为了让众多程序员读者领略 Python 的丰富资源，俺特地整理了一个 wiki 页面</b>（请用鼠标猛击“<a href="https://github.com/programthink/opensource/blob/master/libs/python.wiki" target="_blank">这里</a>”），放上 Python 在各个编程领域的常用模块。为了显示出 Python 代码的简洁，某些模块还放上示例代码。<br/>
　　最后感叹一下：<br/>
　　写这篇博文只花了不到一小时，而整理这个 wiki 页面累计超过10个小时。不过这时间没白花——整理的时候顺便对某些领域有了更多的了解。这也就是写博客的好处，既可以帮助别人，又可以帮助自己。<br/>
　　大伙儿如果觉得俺整理的清单有遗漏，欢迎到<a href="../../2013/02/why-choose-python-5-tools.md">本页面</a>留言补充。<br/>
<br/>
<br/>
<a href="../../2009/08/why-choose-python-0-overview.md">回到本系列的目录</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2013/02/why-choose-python-5-tools.html
