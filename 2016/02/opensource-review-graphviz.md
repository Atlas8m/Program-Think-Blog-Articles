# 开源项目：【自动】绘图工具 Graphviz——《太子党关系网络》就是用它制作 

-----

<div class="post-body entry-content">
<h2>★先插播一个【安全通告】</h2><br/>
　　一星期前（2月16日）曝光了一个高危漏洞。该漏洞存在于广泛使用的 glibc（GNU C Library）。Linux 和 BSD 上面有非常多的软件依赖了这个库。而且出漏洞的函数是 getaddrinfo——该函数被很多软件（比如：各种脚本语言引擎、SSH、cURL ......）用于 DNS 相关的功能。<br/>
　　这个漏洞是可以被远程利用的。攻击者可以通过好几种方式来利用该漏洞，俺认为可能性比较大的方式是“中间人攻击”。具体的技术细节就不多谈了，感兴趣的同学可以参见 Google 官方的安全博客（链接在“<a href="https://googleonlinesecurity.blogspot.ca/2016/02/cve-2015-7547-glibc-getaddrinfo-stack.html" rel="nofollow" target="_blank">这里</a>”）。<br/>
　　值得一提的是：<br/>
　　这个高危漏洞，又是 Google 的研究人员披露的。为啥俺要说【又】？因为最近几年，已经有好多个影响很广泛的高危漏洞是 Google 安全研究团队曝光的（还记得前些年那个<a href="../../2014/04/openssl-heartbleed.md">“心脏出血”漏洞</a>吗）。所以，俺把博客架设在 Google 的 Blogspot 平台上还是比较放心的。虽然 Blogspot 博客平台在全球博客市场排名老二，但是份额最大的 Wordpress 平台，出了太多的安全漏洞，令人实在不敢恭维（比如说：前几天 Linux Mint 官网被入侵，就是因为 WordPress 的漏洞）。<br/>
<br/>
　　当某个高危漏洞曝光之后，到相关软件提供补丁，这中间有一个很危险的窗口期。<br/>
　　由于俺是高危险人士，所以前几天先保持静默（暂不使用“编程随想”这个身份进行网络活动）。<br/>
<br/>
<hr/><br/>
<h2>★引子</h2><br/>
　　前段时间俺承诺把《<a href="../../2015/02/Princelings.md">太子党关系网络</a>》开源到<a href="https://github.com/programthink" target="_blank">俺的 GitHub 帐号</a>下。<br/>
　　<b>对这个项目而言，“开源”只是一种手段而不是目的，开源的目的是：让更多人能够参与到其中，一起曝光天朝的权贵。</b><br/>
　　为了更好的达成此目的，今天发一篇博文，扫盲一下 Graphviz 这个牛逼的绘图工具。俺制作的《太子党关系网络》就是用它来【自动】生成各种复杂的网状关系图。<br/>
<a name="more"></a><br/>
<br/>
<h2>★Graphviz 是啥？</h2><br/>
　　Graphviz 是洋文“Graph Visualization”的缩略词，是一个开源的，跨平台的自动绘图工具，其官网在“<a href="http://www.graphviz.org/" rel="nofollow" target="_blank">这里</a>”，维基百科的介绍在“<a href="https://en.wikipedia.org/wiki/Graphviz" rel="nofollow" target="_blank">这里</a>”。<br/>
　　这玩意儿诞生于上个世纪末，来自 AT&amp;T 的实验室，属于名门正派出身。十多年来，它已经被广泛使用于各个领域。其 Mac OS 版本甚至还获得了2004年的苹果设计奖。<br/>
　　Graphviz 不但是开源软件，而且是自由软件。使用它完全【无需】付费，也【没有】任何注册码之类的恶心东西。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/fkVpNoNysQXG3Q9ZNUZPW6QwNcXa0Qu_aE0TSSHFIczPC7PLjPpu1QIOtbt04qBrTZAUlxDSvvekxE_pDQ2WDKbaufdDw0J0BDVg2WAHSA6DSBa_FnWmTAfxHyEJxxL5uSuxrkzLr48"/><br/>
（这是 UNIX 操作系统的全家福，基于 Graphviz 绘制）</center><br/>
<br/>
<h2>★Graphviz 能干啥？</h2><br/>
　　“绘图工具”有很多种，Graphviz 主要是用来绘制【关系图】。所以它更类似于微软的 Visio。但是它与 Visio 有一个【本质上】的差异：<br/>
用 Visio 画图是【手动】的——你需要动用你的肉眼和手指头。<br/>
而用 Graphviz 画图是【自动】的——你只需要告诉 Graphviz 这张图包含哪些元素，元素之间有啥关系，然后 Graphviz 可以【自动】帮你画出来。<br/>
　　那么，你如何告诉 Graphviz 你要画的图形包含哪些元素捏？这就需要用到一个名叫 DOT 的描述语言（待会儿俺会简单介绍 DOT 语言）。<br/>
<br/>
<br/>
<h2>★为啥用 Graphviz 而不用 Visio 或类似的工具？</h2><br/>
　　客观地讲，Graphviz 和 Visio 之类的工具，各有各的特长。因为本文介绍的是 Graphviz，所以下面聊一下：哪些场景是 Graphviz 胜过 Visio 类工具的。<br/>
　　简而言之，Graphviz 胜过 Visio 这类工具的关键在于【自动布局】。如果你要绘制的关系图非常复杂，这时候【手动】布局就变得极其繁琐。而 Graphviz 的自动布局功能，再复杂的关系图，也可以自动搞定。<br/>
　　请看下面几个例子（都是用 Graphviz 自动绘制的）<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/g-JE5Z-67t3lIYQ0Y5b_vdNs-x1_KZ1PKSfZXXQq19XFuwor4uzhz_1Iv0qi5LZBAUjCyLeYykQtnXEKjt78podV0NmN7va46Tf3Fd7vjFv9ffb1ANUXPP1FZzZSjmSHUCrd8IA6rAQ"/><br/>
（这是美国本土48个州的比邻关系。不含2个海外的州）</center><br/>
　　可能有读者此图不以为然，觉得48个节点不算多。这张图如果【手工】绘制，难点之一在于：如何让所有联线的交叉最少（图中只有一处交叉）。单单这点就足够伤脑筋了。<br/>
　　而 Graphviz 的自动布局功能，【无需】人为干预就可以做到“最小化连线交叉”。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/QOA8VSL2gg2BKX6kAG4K9aAptGRABJfN-5N5dNVeiu3uTOrkCvF1EAewJm7CHxiTiRyS5L52_w8QS23cyCyV8ExMXaszD5s3cpjDJVypwWgT32-h0mtd8nukaG2pdNqWx7x5pQWjyjs"/><br/>
（这是俺整理的《<a href="../../2015/02/Princelings.md">太子党关系网络</a>》其中一幅图。<br/>
注：原图太大，缩小4倍之后裁剪其中一部分）</center><br/>
　　如果你想看更复杂的关系图，可以去 Graphviz 官网。那上面收集了一些【超级复杂】的关系图（链接在“<a href="http://www.graphviz.org/gallery/" rel="nofollow" target="_blank">这里</a>”）。<br/>
<br/>
<br/>
<h2>★Graphviz 软件的使用</h2><br/>
<h3>◇下载、安装</h3><br/>
　　想下载的同学，直接上<a href="http://www.graphviz.org/download/" rel="nofollow" target="_blank">官网的这个页面</a><br/>
　　对于用 Linux 的同学，主流发行版的“软件仓库”应该都包含了 graphviz，你只需用发行版内置的软件包管理器，就可以把 graphviz 装好。<br/>
　　对于用 Mac OS 的同学，官方的 MacPorts 软件仓库已经包含 graphviz 啦。<br/>
<br/>
<h3>◇DOT 命令行的使用</h3><br/>
　　（如果你从来没有用过命令行，建议先了解“命令行”相关的基本概念，再来本看小节）<br/>
　　假设你已经用 DOT 语言写好了一个关系图的描述文件，假设这个文件名是 test.gv 那么你可以进入 test.gv 所在的目录，然后用如下命令生成【png图片】<br/>
<pre class="shell">dot -Tpng -O test.gv</pre>　　对于 Windows 用户的说明：<br/>
　　你可以把 graphviz 安装目录下的 <code>bin</code> 目录添加到 <code>PATH</code> 环境变量中，就可以在命令行中直接使用 <code>dot</code> 命令。否则的话，你需要用【全路径】方式来启动 <code>dot</code> 命令。<br/>
<br/>
<h3>◇支持的输出格式</h3><br/>
　　上述命令行中的 -Tpng 表示生成的文件类型是png图片。如果你需要生成其它格式，也可以。目前 Graphviz 支持很多种格式，<br/>
图片格式【至少】支持：png、jpg、gif、bmp、tiff、ico、svg<br/>
文档格式【至少】支持：pdf、ps/eps<br/>
　　完全的输出格式说明参见<a href="http://www.graphviz.org/doc/info/output.html" rel="nofollow" target="_blank">官网这个页面</a>。<br/>
<br/>
<h3>◇关于扩展名的说明</h3><br/>
　　DOT 的描述文件有好几种扩展名，用得比较多的就是 <code>.dot</code> 扩展名。<br/>
　　但是这个扩展名与微软的 Word 模板的扩展名冲突了。所以俺在本文的示例，用的都是 <code>.gv</code> 这个扩展名。<br/>
<br/>
<br/>
<h2>★DOT 语言入门</h2><br/>
<h3>◇概述</h3><br/>
　　前面提到，你需要通过 DOT 语言来描述一个关系图，然后 Graphviz 根据这个 DOT 语言的描述来自动生成图形。<br/>
　　很多读者一听到“语言”就先望而生畏，其实这个 DOT 并不复杂。从原则上讲，它只描述三种东西，分别是：点（node）、线（edge）、图形（graph）。你可以通过 DOT 语言定义这三种东西的属性（比如：颜色、形状）。<br/>
<br/>
<h3>◇两种图：有向图（digraph） VS 无向图（graph）</h3><br/>
　　DOT 语言支持两种图形，分别是“有向图 和 无向图”。通俗地说，“有向图”里面的连线是有箭头（比如前面给出的那张“太子党关系图”）；反之，“无向图”里面的连线是没有箭头的，比如前面那张“48州的比邻关系图”。<br/>
<br/>
　　定义一个无向图很简单，先看下面这段代码。<br/>
<div class="source"><pre><span></span><span class="n">graph</span> <span class="n">simple</span>
<span class="p">{</span>
    <span class="n">a</span> <span class="o">--</span> <span class="n">b</span> <span class="o">--</span> <span class="n">c</span><span class="p">;</span>
    <span class="n">b</span> <span class="o">--</span> <span class="n">d</span><span class="p">;</span>
<span class="p">}</span>
<span class="c1">// 这是个无向图</span>
</pre></div><br/>
　　上述代码的效果图如下：<br/>
<center><img alt="不见图 请翻墙" src="images/yvS6Vtja20XqvH8NwWAwDIZaOKoJWbcc8Z17ckNnKV_aT0CduQ3o5CAVRLHjSZoSYcAR4mXs_dJVn2aaUiTZxRopD6cxB-5WsaWYJcu_kxdzJWKhv2d-0FY-SnbtVNsrz58ncrYlYL0"/></center><br/>
　　要定义一个有向图，也很简单，代码如下：<br/>
<div class="source"><pre><span></span><span class="n">digraph</span> <span class="n">simple</span>
<span class="p">{</span>
    <span class="n">a</span> <span class="o">-&gt;</span> <span class="n">b</span> <span class="o">-&gt;</span> <span class="n">c</span><span class="p">;</span>
    <span class="n">b</span> <span class="o">-&gt;</span> <span class="n">d</span><span class="p">;</span>
<span class="p">}</span>
<span class="cm">/* 这是个有向图 */</span>
</pre></div><br/>
　　上述代码的效果图如下：<br/>
<center><img alt="不见图 请翻墙" src="images/VjYWYuSyXV7XfJQ-P97EyMaFRkmHzS8sA4VLle_327t81QDpkVPwwnJq6iswEwYpplB3uTa-i6SiUxAIeq8AjcD84AJXv3O44ArCETz7sBtfUDtEcFZ4cR6tJ-HEhDmFKoYzr0vPNkQ"/></center><br/>
　　这2段代码中，<code>graph</code> 用来表示一个无向图；<code>digraph</code> 用来表示一个有向图。<br/>
　　示例中的 <code>simple</code> 表示图的名称。图的名称可以是【英文字母、下划线、数字、中文】。最好【不要包含】其它英文的标点符号（也就是【半角符号】），可能会导致一些语法错误。但是中文标点符号（也就【全角符号】）没有关系。<br/>
　　<b>花括号/大括号</b> 里面的语句表示【图的定义】——这张图包含哪些内容。每一条语句以【分号】结尾（类似于 C、C++、Java 的语法）。<br/>
　　顺便提一下 DOT 语言的注释（其注释的语法与 C、C++、Java 类似），包括如下两种：<br/>
<b>单行注释</b><br/>
以 <code>//</code> 表示——【该行】后续的内容为注释<br/>
<b>多行注释</b><br/>
以 <code>/*</code> 和 <code>*/</code> 包含起来的内容为注释<br/>
<br/>
<h3>◇节点（node）</h3><br/>
　　通过上面两个例子，你应该已经获得了感性的认识。OK，下面来讨论“节点”（node）的概念。<br/>
　　在上面两个例子中， a b c d 都是【节点名】，分别代表节点。在图的定义中，相同名称就代表同一个节点。当 DOT 编译器碰到一个新的名称，就认为这是一个新的节点。<br/>
　　节点的命名规范类似于图的命名规范，此次不再罗嗦。如果某个节点没有设置 label 属性（关于【属性】，下面会聊到），那么图形中就用节点名作为该节点的标题——就好比前面两幅简单的示意图。<br/>
<br/>
<h3>◇节点（node）的属性</h3><br/>
　　在节点名之后可以使用 <b>方括号/中括号</b> 来定义该节点的属性，属性之间用【半角】逗号分隔。<br/>
　　属性的定义采用如下形式：<br/>
<blockquote>属性名 = 属性值</blockquote>（如果属性值包含空格，需用【半角】引号把属性值引用起来）<br/>
<br/>
　　常用的【属性名】包括如下：<br/>
<blockquote>label——标题<br/>
color——颜色<br/>
style——样式<br/>
shape——形状</blockquote>（还有更多属性，可以参见官网“<a href="http://www.graphviz.org/doc/info/attrs.html" rel="nofollow" target="_blank">这个链接</a>”）<br/>
<br/>
　　给一个示例代码及效果图，你一看就明白了：<br/>
<div class="source"><pre><span></span><span class="n">digraph</span> <span class="n">node_attr</span>
<span class="p">{</span>
    <span class="n">shape1</span> <span class="p">[</span><span class="n">shape</span><span class="o">=</span><span class="n">box</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">矩形节点"</span><span class="p">];</span>
    <span class="n">shape2</span> <span class="p">[</span><span class="n">shape</span><span class="o">=</span><span class="n">circle</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">圆形节点"</span><span class="p">];</span>
    <span class="n">shape3</span> <span class="p">[</span><span class="n">shape</span><span class="o">=</span><span class="n">ellipse</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">椭圆形节点"</span><span class="p">];</span>
    <span class="n">shape4</span> <span class="p">[</span><span class="n">shape</span><span class="o">=</span><span class="n">polygon</span><span class="p">,</span> <span class="n">sides</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span> <span class="n">skew</span><span class="o">=</span><span class="mf">0.4</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">平行四边形节点"</span><span class="p">];</span>
    <span class="n">shape5</span> <span class="p">[</span><span class="n">shape</span><span class="o">=</span><span class="n">none</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">无边框节点"</span><span class="p">];</span>
    <span class="n">shape1</span> <span class="o">-&gt;</span> <span class="n">shape2</span> <span class="o">-&gt;</span> <span class="n">shape3</span> <span class="o">-&gt;</span> <span class="n">shape4</span> <span class="o">-&gt;</span> <span class="n">shape5</span>

    <span class="n">color1</span> <span class="p">[</span><span class="n">color</span><span class="o">=</span><span class="s">"blue"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">蓝色边框"</span><span class="p">]</span>
    <span class="n">color2</span> <span class="p">[</span><span class="n">color</span><span class="o">=</span><span class="s">"green"</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">filled</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">绿色填充"</span><span class="p">]</span>
    <span class="n">color3</span> <span class="p">[</span><span class="n">color</span><span class="o">=</span><span class="s">"#ff0000"</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="n">filled</span><span class="p">,</span> <span class="n">fillcolor</span><span class="o">=</span><span class="s">"yellow"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">红色边框+黄色填充"</span><span class="p">]</span>
    <span class="n">color4</span> <span class="p">[</span><span class="n">color</span><span class="o">=</span><span class="s">"#0000FF"</span> <span class="n">style</span><span class="o">=</span><span class="n">filled</span><span class="p">,</span> <span class="n">fillcolor</span><span class="o">=</span><span class="s">"green:red"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">蓝色边框+从绿色到红色渐变填充"</span><span class="p">]</span>
    <span class="cm">/* 上面两个节点采用 HTML 的颜色语法，dot 支持 这种语法 */</span>
    <span class="n">color1</span> <span class="o">-&gt;</span> <span class="n">color2</span> <span class="o">-&gt;</span> <span class="n">color3</span> <span class="o">-&gt;</span> <span class="n">color4</span>

    <span class="n">text1</span> <span class="p">[</span><span class="n">shape</span><span class="o">=</span><span class="n">box</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">12</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">小字体"</span><span class="p">]</span>
    <span class="n">text2</span> <span class="p">[</span><span class="n">shape</span><span class="o">=</span><span class="n">box</span><span class="p">,</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">24</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">大字体"</span><span class="p">]</span>
    <span class="n">text3</span> <span class="p">[</span><span class="n">shape</span><span class="o">=</span><span class="n">box</span><span class="p">,</span> <span class="n">fontcolor</span><span class="o">=</span><span class="s">"blue"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">蓝色文字"</span><span class="p">]</span>
    <span class="n">text4</span> <span class="p">[</span><span class="n">shape</span><span class="o">=</span><span class="n">box</span><span class="p">,</span> <span class="n">label</span><span class="o">=&lt;</span><span class="s">编程随想注：&lt;br/&gt;&lt;b&gt;粗体&lt;/b&gt; &lt;i&gt;斜体&lt;/i&gt;&lt;u&gt;下划线&lt;/u&gt;</span><span class="o">&gt;</span><span class="p">]</span>
    <span class="c1">// 注意：text4 使用 HTML 风格的 label，无需引号，但必须用尖括号</span>
    <span class="n">text1</span> <span class="o">-&gt;</span> <span class="n">text2</span> <span class="o">-&gt;</span> <span class="n">text3</span> <span class="o">-&gt;</span> <span class="n">text4</span>
<span class="p">}</span>
</pre></div><center><img alt="不见图 请翻墙" src="images/jqcKVmcW45HexgH8HRoWZbrzjhr8UwPMOBVXpVyQ774a1gFkepgeSXC2XrEwfjSuocOF8x7KyR66htXNksMphq72oiRleeD3D4vho7rguBoFZUhg9cNCkJVQwJbLfmtm7r2TGy-BlbI"/></center><br/>
　　补充说明：<br/>
　　在上述示例，俺刻意用到了 HTML 的颜色语法。关于这种语法的说明可以参见维基百科的<a href="https://zh.wikipedia.org/wiki/%E7%BD%91%E9%A1%B5%E9%A2%9C%E8%89%B2" rel="nofollow" target="_blank">这个链接</a>。<br/>
<br/>
<h3>◇连线（edge）</h3><br/>
　　聊完【节点/node】，再来聊【连线/edge】。<br/>
　　如前面所示，无向图的连线用 <code>--</code> 表示，有向图的连线用 <code>-&gt;</code> 表示，非常形象。定义连线的语句也是以分号结尾。<br/>
　　连线与节点的关键差异之处在于——节点有名称而【连线没有名称】。<br/>
<br/>
<h3>◇连线（edge）的属性</h3><br/>
　　连线也可以设置属性，其属性写在定义连线的语句末尾，语法类似节点属性。<br/>
　　常用的【属性名】包括如下：<br/>
<blockquote>label——标题<br/>
color——颜色<br/>
style——线条的样式<br/>
dir——连线的方向（仅用于有向图，可设置：正向箭头、反向箭头、双向箭头）<br/>
arrowhead——前端的样式<br/>
arrowtail——末端的样式</blockquote>（还有更多属性，可以参见官网“<a href="http://www.graphviz.org/doc/info/attrs.html" rel="nofollow" target="_blank">这个链接</a>”）<br/>
<br/>
　　下面给几个示例，你自己去揣摩（以【有向图】作示范）<br/>
<div class="source"><pre><span></span><span class="n">digraph</span> <span class="n">edge_attr</span>
<span class="p">{</span>
    <span class="n">style0</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">以下是样式的示例"</span><span class="p">];</span>
    <span class="n">style1</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">]</span> <span class="n">style2</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">]</span> <span class="n">style3</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">]</span> <span class="n">style4</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">];</span>

    <span class="n">style0</span> <span class="o">-&gt;</span> <span class="n">style1</span> <span class="p">[</span><span class="n">style</span><span class="o">=</span><span class="n">solid</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"实线"</span><span class="p">];</span>
    <span class="n">style1</span> <span class="o">-&gt;</span> <span class="n">style2</span> <span class="p">[</span><span class="n">style</span><span class="o">=</span><span class="n">bold</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"粗线"</span><span class="p">];</span>
    <span class="n">style2</span> <span class="o">-&gt;</span> <span class="n">style3</span> <span class="p">[</span><span class="n">style</span><span class="o">=</span><span class="n">dashed</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"短划线"</span><span class="p">];</span>
    <span class="n">style3</span> <span class="o">-&gt;</span> <span class="n">style4</span> <span class="p">[</span><span class="n">style</span><span class="o">=</span><span class="n">dotted</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"虚线"</span><span class="p">];</span>

    <span class="n">arrow0</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">以下是箭头的示例"</span><span class="p">];</span>
    <span class="n">arrow1</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">]</span> <span class="n">arrow2</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">]</span> <span class="n">arrow3</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">]</span> <span class="n">arrow4</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">]</span> <span class="n">arrow5</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">]</span> <span class="n">arrow6</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">];</span>
    <span class="n">arrow0</span> <span class="o">-&gt;</span> <span class="n">arrow1</span> <span class="p">[</span><span class="n">dir</span><span class="o">=</span><span class="n">both</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"双向箭头"</span><span class="p">];</span>
    <span class="n">arrow1</span> <span class="o">-&gt;</span> <span class="n">arrow2</span> <span class="p">[</span><span class="n">arrowsize</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"大箭头"</span><span class="p">];</span>
    <span class="n">arrow2</span> <span class="o">-&gt;</span> <span class="n">arrow3</span> <span class="p">[</span><span class="n">arrowhead</span><span class="o">=</span><span class="s">"open"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"带倒钩的箭头"</span><span class="p">];</span>
    <span class="n">arrow3</span> <span class="o">-&gt;</span> <span class="n">arrow4</span> <span class="p">[</span><span class="n">arrowhead</span><span class="o">=</span><span class="s">"halfopen"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"单边倒钩"</span><span class="p">];</span>
    <span class="n">arrow4</span> <span class="o">-&gt;</span> <span class="n">arrow5</span> <span class="p">[</span><span class="n">arrowhead</span><span class="o">=</span><span class="s">"ediamond"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"菱形箭头"</span><span class="p">];</span>
    <span class="n">arrow5</span> <span class="o">-&gt;</span> <span class="n">arrow6</span> <span class="p">[</span><span class="n">arrowhead</span><span class="o">=</span><span class="s">"dot"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"圆形箭头"</span><span class="p">];</span>

    <span class="n">color0</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">"编程随想注：</span><span class="se">\n</span><span class="s">以下是颜色的示例"</span><span class="p">];</span>
    <span class="n">color1</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">]</span> <span class="n">color2</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">]</span> <span class="n">color3</span><span class="p">[</span><span class="n">label</span><span class="o">=</span><span class="s">""</span><span class="p">];</span>
    <span class="n">color0</span> <span class="o">-&gt;</span> <span class="n">color1</span> <span class="p">[</span><span class="n">color</span><span class="o">=</span><span class="s">"blue"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"蓝色"</span><span class="p">];</span>
    <span class="n">color1</span> <span class="o">-&gt;</span> <span class="n">color2</span> <span class="p">[</span><span class="n">color</span><span class="o">=</span><span class="s">"red:blue"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"双色"</span><span class="p">];</span>
    <span class="n">color2</span> <span class="o">-&gt;</span> <span class="n">color3</span> <span class="p">[</span><span class="n">color</span><span class="o">=</span><span class="s">"green:red;0.4:blue"</span><span class="p">,</span> <span class="n">label</span><span class="o">=</span><span class="s">"颜色分段"</span><span class="p">];</span>
<span class="p">}</span>
</pre></div><center><img alt="不见图 请翻墙" src="images/IoAD-JfXRYNSY7m9Foa5lZxEpRSTgtob1vAeoqq1a4M97W4tUA3SXr615dcwwGAygk1OISxwDt65Z-CR1c2x51ajxD3dNmrWJTn3gmcnJeF11C8rh4dV-eyT_xEhAateELjfciklwXM"/></center><br/>
<h3>◇图的属性</h3><br/>
　　说完了“节点”和“连线”，最后稍微聊一下“图”本身的属性。<br/>
　　常用的【属性名】包括如下：<br/>
<blockquote>label——标题<br/>
bgcolor——颜色<br/>
fontname——字体名称（【不】影响节点和连线）<br/>
fontsize——字体大小（【不】影响节点和连线）<br/>
fontcolor——字体颜色（【不】影响节点和连线）<br/>
center——是否居中绘制</blockquote>（还有更多属性，可以参见官网“<a href="http://www.graphviz.org/doc/info/attrs.html" rel="nofollow" target="_blank">这个链接</a>”）<br/>
<br/>
<div class="source"><pre><span></span><span class="n">digraph</span> <span class="n">graph_attr</span>
<span class="p">{</span>
    <span class="n">graph</span><span class="p">[</span><span class="n">bgcolor</span><span class="o">=</span><span class="s">"cadetblue"</span> <span class="n">label</span><span class="o">=</span><span class="s">"图的标题"</span> <span class="n">fontsize</span><span class="o">=</span><span class="mi">24</span> <span class="n">fontcolor</span><span class="o">=</span><span class="s">"green"</span><span class="p">];</span>

    <span class="n">node0</span> <span class="o">-&gt;</span> <span class="n">node1</span><span class="p">;</span>
    <span class="n">node0</span> <span class="o">-&gt;</span> <span class="n">node2</span><span class="p">;</span>
<span class="p">}</span>
</pre></div><center><img alt="不见图 请翻墙" src="images/FngPZ5V84luUwXNc-ctY9SI3FyBfdgYwuOa9tjd88fMJIxoHGZo3Ir1-OL5_3dGRomzuoMFYW9CDFdZRB-oaurXF7DQYVg_sQ1jlbQetW3eZVOWM2mrZbBHuDxysHG_Ofi53pIYDe7M"/></center><br/>
<h3>◇进阶</h3><br/>
　　前面俺讲的都是 DOT 最基本的概念和使用。DOT 语言还有一些更高级的用法，感兴趣的同学可以参考下一个章节（★相关资源）给出的“dotguide.pdf”。<br/>
<br/>
<br/>
<h2>★相关资源</h2><br/>
<h3>◇官网的资源</h3><br/>
以下是官网上的若干在线文档：<br/>
<a href="http://www.graphviz.org/doc/Dot.ref" rel="nofollow" target="_blank">http://www.graphviz.org/doc/Dot.ref</a><br/>
<a href="http://www.graphviz.org/doc/info/attrs.html" rel="nofollow" target="_blank">http://www.graphviz.org/doc/info/attrs.html</a><br/>
<a href="http://www.graphviz.org/doc/info/shapes.html" rel="nofollow" target="_blank">http://www.graphviz.org/doc/info/shapes.html</a><br/>
<a href="http://www.graphviz.org/doc/info/arrows.html" rel="nofollow" target="_blank">http://www.graphviz.org/doc/info/arrows.html</a><br/>
<a href="http://www.graphviz.org/doc/info/colors.html" rel="nofollow" target="_blank">http://www.graphviz.org/doc/info/colors.html</a><br/>
<br/>
<a href="http://www.graphviz.org/pdf/dotguide.pdf" rel="nofollow" target="_blank">官方提供的 DOT 语言完整的指南（dotguide.pdf）</a><br/>
<br/>
<a href="https://github.com/ellson/graphviz" rel="nofollow" target="_blank">Graphviz 官方的 GitHub 帐号</a><br/>
<br/>
<h3>◇编辑器</h3><br/>
　　<b>自带的编辑器</b><br/>
<br/>
Graphviz 软件包中自带了 gvedit 和 vimdot。<br/>
<br/>
　　<b>Emacs 的 mode</b><br/>
<br/>
<a href="https://github.com/ppareit/graphviz-dot-mode" rel="nofollow" target="_blank">https://github.com/ppareit/graphviz-dot-mode</a><br/>
俺平时用这个 mode 来编辑 dot 数据文件。它可以实现“所见即所得”——每次修改完，直接在 Emacs 另一个窗口预览图片。<br/>
其作者提供的效果图如下：<br/>
<center><img alt="不见图 请翻墙" src="images/KkoTguhEwfxEDsiDhFeD2xmpdxc-lObNT1yqMw9P5rnRRUfqnz0iLO-Dlm7BgKXlD-K88RTKFjeDboaZOezm1IoYXYjlQkhbBN42KsB-PGgWCRFvpdues-32L5P4uVckUPN1QWpUwpw"/></center><br/>
　　<b>VI/VIM 的插件</b><br/>
<br/>
<a href="https://github.com/wannesm/wmgraphviz.vim" rel="nofollow" target="_blank">https://github.com/wannesm/wmgraphviz.vim</a><br/>
<br/>
<h3>◇编程语言的整合</h3><br/>
　　<b>JavaScript</b><br/>
<br/>
<a href="https://github.com/mdaines/viz.js" rel="nofollow" target="_blank">https://github.com/mdaines/viz.js</a><br/>
<br/>
<a href="https://github.com/gyuque/livizjs" rel="nofollow" target="_blank">https://github.com/gyuque/livizjs</a><br/>
<br/>
　　<b>Python</b><br/>
<br/>
<a href="https://pypi.python.org/pypi/graphviz" rel="nofollow" target="_blank">https://pypi.python.org/pypi/graphviz</a><br/>
<br/>
　　<b>Ruby</b><br/>
<br/>
<a href="https://github.com/glejeune/Ruby-Graphviz" rel="nofollow" target="_blank">https://github.com/glejeune/Ruby-Graphviz</a><br/>
<br/>
　　<b>Java</b><br/>
<br/>
<a href="http://jgraphviz.sourceforge.net/" rel="nofollow" target="_blank">http://jgraphviz.sourceforge.net/</a><br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2009/02/how-to-choose-opensource-project.md">如何选择开源项目</a>》<br/>
《<a href="../../2015/02/Princelings.md">曝光天朝权贵——《太子党关系网络》2.2 版本发布</a>》
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2016/02/opensource-review-graphviz.html
