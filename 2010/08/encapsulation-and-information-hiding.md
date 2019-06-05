# 有关封装和信息隐藏的误区 

-----

<div class="post-body entry-content">
　　上次<a href="../../2010/08/why-choose-python-3-oop.md">介绍 Python 的面对对象特性</a>，其中扯到了封装（Encapsulation）等概念。当时为了不跑题，没有深入聊这些概念。考虑到很多开发人员对这些概念，经常混淆不清。今天再专门来说一下。<a name="more"></a><br/>
<br/>
<br/>
<h2>★封装</h2><br/>
<h3>◇什么是封装？</h3><br/>
　　从字面意思来看，封装就是把一些【相关的】东西打包成一坨（看到“坨”这个量词，不要想歪了）。“封装”最广为人知的例子，就是在面向对象编程（以下简称 OOP）里面，把数据和针对该数据的操作，统一到一个 class 里。<br/>
<br/>
<h3>◇封装有啥好处？</h3><br/>
　　那封装有啥好处捏？一个主要的好处，就是增加软件代码的内聚性。通过增加内聚性，进而提高可复用性和可维护性。<br/>
<br/>
<h3>◇封装的手段</h3><br/>
　　很多人把封装的概念局限于类，认为只有 OO 中的 class 才算是封装。这实际上是片面滴！在很多不使用"类"的场合，一样能采用封装的手法。<br/>
　　下面俺随手举几个和 OO 无关的例子：<br/>
<br/>
　　<b>1. 通过文件</b><br/>
　　比如 C 和 C++ 支持对头文件的包含（#include）。因此，可以把一些相关的常量定义、类型定义、函数声明，统统<b>封装</b>到某个头文件中。<br/>
<br/>
　　<b>2. 通过 namespace / package / module</b><br/>
　　C++ 的 namespace、Java 的 package、Python 的 module，想必各自的开发人员都很熟悉。这些语法虽然称呼各不相同，但具有相同的本质。因此，也可以利用这些语法，来进行封装。<br/>
<br/>
<br/>
<h2>★信息隐藏</h2><br/>
<h3>◇什么是信息隐藏？</h3><br/>
　　“信息隐藏”——顾名思义——就是把不该暴露的信息藏起来。说到信息隐藏，很多人自然而然地，就联想到某些 OO 语言（比如 C++、Java）提供的诸如”private、protected“之类的关键字。这些关键字可以通过访问控制，来达到信息隐藏的目的。<br/>
<br/>
<h3>◇信息隐藏有啥好处？</h3><br/>
　　信息隐藏的好处，正好和“封装”的好处相呼应。封装是为了提高内聚性；而信息隐藏是为了降低耦合性。通过降低耦合，一样可以达到提高可复用性、可维护性这2个目的。<br/>
<br/>
<h3>◇信息隐藏的手段</h3><br/>
　　和封装类似，很多程序员也把信息隐藏的概念片面化——认为信息隐藏仅限于 private 和 protected 关键字。<br/>
所以，俺再随手举几个其它的信息隐藏手段。<br/>
<br/>
　　<b>1. 通过接口类</b><br/>
　　可以通过定义接口类（Java 中的 interface、C++ 中的纯虚类）来实现信息隐藏。具体实现如下：<br/>
　　定义一个接口类，仅包含一些公有的成员函数的【声明】（Java 的 abstract 函数，C++ 的纯虚函数），没有任何函数实现，也没有任何成员变量。然后把具体的实现代码放到该接口类的一个派生子类中。<br/>
　　由于调用者只看到接口类，看不到实现类。所以，同样可以达到信息隐藏。在某些情况下，使用这种手段达到的效果，会比基于访问控制（使用 private 关键字）的效果【更好】。<br/>
　　不过这种手段依赖于语言的支持。使用该手法的编程语言，至少要支持继承、虚函数等语法。<br/>
<br/>
　　<b>2. 通过 pimpl 手法</b><br/>
　　pimpl 手法也叫作“Opaque Pointer”手法。和接口类的手法不同，pimpl 手法不需要靠继承、虚函数等语法的支持，因此对诸如 C 语言来说，很有用。<br/>
　　为了省事儿，俺就不具体解释该手法的实现细节。有兴趣的同学请看“<a href="https://en.wikipedia.org/wiki/Opaque_pointer" rel="nofollow" target="_blank">这里</a>”（连不同语言的样例代码都展示给你了，要是再看不懂就只有怪自己笨了）。<br/>
<br/>
<br/>
<h2>★一些理解上的误区</h2><br/>
　　介绍完一些基本概念，再来说一下，关于封装、信息隐藏的一些常见误区。<br/>
<br/>
<h3>◇把封装等同于信息隐藏</h3><br/>
　　这是混淆最严重的一个误区——很多初学 OOP 的同学都把封装和信息隐藏混为一谈。希望经过俺前面的一番解释，有些人能搞明白其中的差异。<br/>
　　顺便提一下，有个老外写了篇小有名气的文章——《<a href="http://www.javaworld.com/javaworld/jw-05-2001/jw-0518-encapsulation.html" rel="nofollow" target="_blank">Encapsulation is not information hiding</a>》。洋文好的同学，可以去瞅一瞅。<br/>
<br/>
<h3>◇把封装看得太狭隘</h3><br/>
　　其实前面已经通过举例，驳斥了狭隘看待封装的误区。此处不再啰嗦。<br/>
<br/>
<h3>◇把信息隐藏看得太狭隘</h3><br/>
　　前面已经通过举例，驳斥了狭隘看待信息隐藏的误区。此处不再啰嗦。<br/>
<br/>
<h3>◇混淆”可访问性“和”可见性“</h3><br/>
　　考虑到某些网友可能连这两者的区别都不太清楚，先简单解释一下。所谓可访问性，就是可以对某个东西进行读/写操作；所谓可见性，就是能够感觉到某个东西的存在。<br/>
　　前面谈到信息隐藏时，我们提及了通过访问控制的关键字（private、protected）来达到信息隐藏的目的。有很多同学认为这几个关键字不光禁止了可访问性（accessibility），还禁止了可见性（visibility）。<br/>
　　其实也不尽然。不同的编程语言，对这两者的处理是不同滴。比如在 C++ 语言中，类的私有成员虽然”不可访问“，但【依然可见】。此话怎讲捏？请看下面的例子：<br/>
<div class="source"><pre><span class="kt">int</span> <span class="n">n</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span>

<span class="k">class</span> <span class="nc">Parent</span>
<span class="p">{</span>
<span class="k">public</span><span class="o">:</span>
    <span class="n">Parent</span><span class="p">()</span>
    <span class="p">{</span>
        <span class="n">n</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span>
    <span class="p">}</span>

<span class="k">private</span><span class="o">:</span>
    <span class="kt">int</span> <span class="n">n</span><span class="p">;</span>
<span class="p">};</span>

<span class="k">class</span> <span class="nc">Child</span> <span class="o">:</span> <span class="k">public</span> <span class="n">Parent</span>
<span class="p">{</span>
<span class="k">public</span><span class="o">:</span>
    <span class="n">Child</span><span class="p">()</span>
    <span class="p">{</span>
    <span class="p">}</span>

    <span class="kt">void</span> <span class="n">Func</span><span class="p">()</span>
    <span class="p">{</span>
        <span class="o">::</span><span class="n">printf</span><span class="p">(</span><span class="s">"%d"</span><span class="p">,</span> <span class="n">n</span><span class="p">);</span>
    <span class="p">}</span>
<span class="p">};</span>

<span class="kt">int</span> <span class="nf">main</span><span class="p">()</span>
<span class="p">{</span>
    <span class="n">Child</span> <span class="n">c</span><span class="p">;</span>
    <span class="n">c</span><span class="p">.</span><span class="n">Func</span><span class="p">();</span>

    <span class="k">return</span> <span class="mi">0</span><span class="p">;</span>
<span class="p">}</span>
</pre></div><br/>
　　现在俺问列位看官：程序执行后会打印出啥？相信一多半的同学会回答：“打印0”。<br/>
　　如果你也这么想，很遗憾，你答错了。<br/>
　　答错的同学，不要急着看答案。<br/>
<br/>
建<br/>
<br/>
议<br/>
<br/>
你<br/>
<br/>
再<br/>
<br/>
思<br/>
<br/>
考<br/>
<br/>
一<br/>
<br/>
柱<br/>
<br/>
香<br/>
<br/>
的<br/>
<br/>
功<br/>
<br/>
夫<br/>
<br/>
。<br/>
<br/>
<br/>
　　真相是：<b>该程序根本在编译时就报错了</b>。<br/>
　　问题在于，父类的私有成员变量 n 虽然对子类是无法访问的，但依然是可见的（可感知的）。所以，对于那个 printf 语句，编译器会认为是企图访问父类的私有成员，故而报错。<br/>
　　悄悄跟大伙儿说一下：这例子是俺从 C++ 它爹所写的《The Design and Evolution of C++》里面剽窃来滴 :)<br/>
<br/>
<br/>
<h2>★结尾</h2><br/>
　　今天的话题，基本上到此结束了。最后，俺想提醒列位看官注意一下：象封装和信息隐藏，都属于编程的基本功，为啥很多开发人员都没有想透彻捏？<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
<a href="../../2009/08/why-choose-python-0-overview.md">为什么俺推荐 Python（系列）</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2010/08/encapsulation-and-information-hiding.html
