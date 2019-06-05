# 为啥俺推荐 Python[3]：作为面向对象语言的 Python 

-----

<div class="post-body entry-content">
　　<a href="../../2009/08/why-choose-python-0-overview.md">本系列</a>已经中断了很长时间 :( 直到最近一个读者来信问俺，为啥不继续写，俺才突然想起这个被遗忘的系列，实在是抱歉！前一个帖子介绍了<a href="../../2009/08/why-choose-python-2-dynamic.md">作为动态语言的 Python</a>，今天来聊一聊 Python 在面向对象编程（OOP）方面的特色。<br/>
　　本文主要针对那些熟悉 OOP，但还不熟悉 Python 的同学。为了让大伙儿有一个直观的认识，俺会拿 C++/Java 来进行语法上的对比。（这俩语言的名气够大，且号称支持 OO，也算有些可比性）<a name="more"></a><br/>
　　强调一下：本文虽然拿了某些语言来作对比，但丝毫没有贬低这些语言的意思，请这些语言的粉丝们，不要对号入座 :)<br/>
<br/>
<br/>
<h2>★抽象（Abstraction）</h2><br/>
　　但凡介绍 OOP，自然会提到抽象。因为抽象，是 OO 的第一要素，也是其它要素的基础。而提到抽象，又不免提到对象（Object）。所以，俺首先来聊一下，Python 语言是如何体现“对象”这个思想的。<br/>
<br/>
<h3>◇Python的对象</h3><br/>
　　如果要问俺，什么是 Python 中的对象，还真不好下一个严密又通俗易懂的定义。为了敷衍大伙儿，俺只好用一句话来概括，那就是 Python 语言中，【<b>一切皆对象</b>】。这句话该如何理解捏？简单来说，就是你在 Python 语言中涉及到的各种东东，都是“对象”。比如，函数是对象、各种数值（比如整数值、浮点数值、布尔值）是对象、模块（类似于 Java 的 package）是对象、None（类似于 Java 的空引用 null、C++ 的空指针 NULL）也是对象、甚至连类（class）也是对象......<br/>
　　对比一下 C++ 和 Java 的语法：只有【类的实例】才能算得上是对象。这2个语言的基本类型（比如“int、char、float”等）不是对象，至于函数，就更算不上了。<br/>
　　既然是一切皆对象，俺有必要稍微总结一下，Python 对象的共性，否则初学 Python 的同学还是会一头雾水。<br/>
<br/>
<h3>◇对象的属性</h3><br/>
　　首先，所有的 Python 的对象，都具有若干个属性。你可以通过内置的 dir() 函数进行反射，从而了解到某个对象分别都包含哪些属性。熟悉 Java 的同学，应该明白啥是“反射”。光懂 C/C++ 的同学，如果理解上有困难，可以先参考“<a href="https://en.wikipedia.org/wiki/Reflection_%28computer_science%29" rel="nofollow" target="_blank">维基百科的解释</a>”。<br/>
　　另外，Python 还提供了若干内置的函数，用于在【运行时】操作指定对象的属性。具体如下：<br/>
<div class="source"><pre><span></span><span class="nb">hasattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span>  <span class="c1">#判断obj对象是否具有名为name的属性</span>
<span class="nb">setattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span>  <span class="c1">#设置obj对象的名为name的属性值为value</span>
<span class="nb">getattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span>  <span class="c1">#获取obj对象的名为name的属性值</span>
<span class="nb">delattr</span><span class="p">(</span><span class="n">obj</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span>  <span class="c1">#删除obj对象的名为name的属性</span>
</pre></div><br/>
<h3>◇对象的类型</h3><br/>
　　所有的 Python 对象，都可以通过内置的 type() 函数获取该对象的类型。这实际上就是 Python 的 <a href="https://en.wikipedia.org/wiki/Run-time_type_information" rel="nofollow" target="_blank">RTTI</a> 机制的体现。懂 C++ 的同学，可以回忆一下 C++ 的 typeid 关键字；懂 Java 的同学，可以想一想 Java 的 instanceof 关键字。<br/>
<br/>
<h3>◇对象的标示</h3><br/>
　　所有的 Python 对象，都可以通过内置的 id() 函数获取该对象的【唯一】标示。而且当一个对象创建之后，这个唯一标示就会始终保持不变。对于学过 C/C++ 的同学，不妨把这个“唯一标示”想象成该对象在内存的地址。这或许有助于你的理解 :)<br/>
<br/>
　　Python 对象还有其它一些共性，考虑到本文的扫盲性质，就不再费口水了。有兴趣的同学，可以自己找些入门书研读一番。<br/>
<br/>
<h3>◇【一切皆对象】的好处？</h3><br/>
　　可能有同学会问，“一切皆对象”有啥好处捏？俺窃以为：当一切皆为对象，就可以把很多概念、操作、惯用手法统一起来，在语法层面体现出美感。<br/>
下面俺举几个例子，并拿 Java 来对比一下。<br/>
　　在 Java 里面，由于基本类型不是继承自 Object 类，引出不少麻烦。当初 Java 它爹刚开始设计容器类（比如 Vector、ArrayList ...）的时候，颇费了一番功夫。因为容器里面放置的东东必须是 Object，为了让容器能适应基本类型，只好给每一种基本类型分别对应一个派生自 Object 的包装类（Integer 类对应 int、Float 类对应 float ...）；后来又平添了自动装箱/拆箱的概念；搞来稿去，产生了 N 多复杂性。<br/>
　　而 Python 就没有这方面的困扰。<br/>
　　再拿刚才提及的“反射”来说事儿。虽然 Java 语言支持对象的反射，但是 Java 的 package 不是 Object，所以也就无法对 package 进行反射。反观 Python，任何一个 module（相当于 Java 的 package）import 之后，都可以直接通过前面提到的 dir() 函数进行反射，得知该 module 包含了哪些东东。仅仅需要2行代码：<br/>
<div class="source"><pre><span></span><span class="kn">import</span> <span class="nn">xxx</span>
<span class="nb">dir</span><span class="p">(</span><span class="n">xxx</span><span class="p">)</span>
</pre></div><br/>
<br/>
<h2>★封装（Encapsulation）</h2><br/>
　　为了避免歧义，首先要明确一下：什么是“封装”？为了叙述方便，俺把【OOP 的封装】，分为“狭义”和“广义”两种。（关于“封装”的深入讨论，可以参见“<a href="../../2010/08/encapsulation-and-information-hiding.md" target="_blank">另一篇博文</a>”）<br/>
<br/>
<h3>◇广义封装</h3><br/>
　　OOP 很强调以数据为中心。所以 OOP 的广义封装，就是把数据和操作数据的行为，打包到一起。比如 C++/Java 里的 class，可以同时包含数据成员和函数成员，就算是满足“广义的封装”了。对于 Python 而言，其 class 关键字类似于 C++ 和 Java，也已经具有“广义的封装性”了。<br/>
<br/>
<h3>◇狭义封装</h3><br/>
　　而 OOP 的狭义封装，则更进一步，增加了信息隐藏（Information Hiding）。比如 C++ 和 Java 的“public、protected、private”等关键字，就是通过访问控制来达到信息隐藏的效果。Python 虽然没有针对访问控制的关键字来修饰类成员，但是 Python 采用了另外一套机制——根据命名来约定。在 Python 的对象中，如果某个属性以双下划线开头来命名（比如 <code>__name</code>），就能起到类似于 C++/Java 的 <code>private</code> 关键字的效果。<br/>
<br/>
<h3>◇对访问控制的偏见</h3><br/>
　　俺曾经在某技术论坛看到有人质疑 Python 的访问控制机制，说 Python 的私有属性，可以通过反射机制绕过，因此形同虚设。在此，俺想举 C++ 和 Java 来进行反驳。<br/>
　　在 Java 中，同样可以通过反射机制，来访问类的私有成员。至于 C++，得益于指针的强大，只要能访问某个对象（的 this 指针），通过计算该对象成员变量在内存中的偏移，一样可轻易对私有成员变量进行读写。虽然这么干挺变态滴，但技术上是可行滴。<br/>
<br/>
<br/>
<h2>★继承（Inheritance）</h2><br/>
　　紧接着，咱再来说一下继承的话题。<br/>
<br/>
<h3>◇Python 的继承</h3><br/>
　　Python 没有像 Java 那样，区分出“类继承”（OO 的术语中也叫“实现继承”）和“接口继承”；也没有像 C++ 那样，区分出“公有继承、私有继承、保护继承”这么花哨的玩意儿。Python 就只有一种继承方式。<br/>
<br/>
<h3>◇继承的语法</h3><br/>
　　Python 的继承语法，相比 C++/Java 而言，更加简洁。比如子类 Child 需要继承父类 Parent，代码只需如下：<br/>
<div class="source"><pre><span></span><span class="k">class</span> <span class="nc">Child</span><span class="p">(</span><span class="n">Parent</span><span class="p">)</span> <span class="p">:</span>
    <span class="c1"># xxxx</span>
</pre></div><br/>
　　如果是多继承，代码大同小异：<br/>
<div class="source"><pre><span></span><span class="k">class</span> <span class="nc">Child</span><span class="p">(</span><span class="n">Parent1</span><span class="p">,</span> <span class="n">Parent2</span><span class="p">,</span> <span class="n">Parent3</span><span class="p">)</span> <span class="p">:</span>
    <span class="c1"># xxxx</span>
</pre></div><br/>
　　假如你想知道某个类有哪些父类（基类），只需要通过 <span "="" style="font-family:Courier,monospace;">Child.__bases__</span> 便可知晓。<br/>
<br/>
<h3>◇继承的动态性</h3><br/>
　　其实<a href="../../2009/08/why-choose-python-2-dynamic.md">上一个帖子</a>已经介绍了动态改变继承关系的例子。但是考虑到上一个帖子年代久远（距本文将近1年），想必很多同学没看过或者看过又忘了。俺不妨再啰嗦一下：作为一种动态语言，Python 可以在【运行时】修改类的继承关系。这个特性比较酷，是 C++/Java 所望尘莫及滴。请看下面的例子：<br/>
<div class="source"><pre><span></span><span class="k">class</span> <span class="nc">Parent1</span> <span class="p">:</span>
    <span class="k">def</span> <span class="nf">dump</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="p">:</span>
        <span class="k">print</span><span class="p">(</span><span class="s2">"parent1"</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Parent2</span> <span class="p">:</span>
    <span class="k">def</span> <span class="nf">dump</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="p">:</span>
        <span class="k">print</span><span class="p">(</span><span class="s2">"parent2"</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">Child</span> <span class="p">:</span>
    <span class="k">def</span> <span class="nf">dump</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="p">:</span>
        <span class="k">print</span><span class="p">(</span><span class="s2">"child"</span><span class="p">)</span>

<span class="k">print</span><span class="p">(</span><span class="n">Child</span><span class="o">.</span><span class="n">__bases__</span><span class="p">)</span>
<span class="n">Child</span><span class="o">.</span><span class="n">__bases__</span> <span class="o">+=</span> <span class="p">(</span><span class="n">Parent1</span><span class="p">,</span> <span class="n">Parent2</span><span class="p">)</span>  <span class="c1"># 动态追加了2个父类</span>
<span class="k">print</span><span class="p">(</span><span class="n">Child</span><span class="o">.</span><span class="n">__bases__</span><span class="p">)</span>  <span class="c1"># 此处打印出的父类信息中，已经包含 Parent1、Parent2</span>
</pre></div><br/>
<br/>
<h2>★多态（Polymorphism）</h2><br/>
　　至于 Python 的多态，和传统的 OO 语言差不多，似乎没有太多值得说道的地方。俺简单举个代码作例子。为了省打字，直接复用上述的3个类，并增加一个 test() 函数如下：<br/>
<div class="source"><pre><span></span><span class="k">def</span> <span class="nf">test</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="p">:</span>
    <span class="n">obj</span><span class="o">.</span><span class="n">dump</span><span class="p">()</span>
</pre></div><br/>
　　然后对 test() 函数分别传入不同的类型的对象，输出结果俺就无需多说了吧？<br/>
<div class="source"><pre><span></span><span class="n">c</span> <span class="o">=</span> <span class="n">Child</span><span class="p">()</span>
<span class="n">test</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>  <span class="c1"># 打印出 child</span>
<span class="n">p1</span> <span class="o">=</span> <span class="n">Parent1</span><span class="p">()</span>
<span class="n">test</span><span class="p">(</span><span class="n">p1</span><span class="p">)</span>  <span class="c1"># 打印出 parent1</span>
</pre></div><br/>
<br/>
<h2>★结尾</h2><br/>
　　今天的话题，主要是让不熟悉 Python 的网友，对 Python 在面向对象方面的特性，有一个粗浅、感性的认识。聊完了 OOP，下一个帖子会聊一下<a href="../../2012/02/why-choose-python-4-fp.md">关于 FP（函数式编程）的话题</a>。<br/>
<br/>
<br/>
<a href="../../2009/08/why-choose-python-0-overview.md#index">回到本系列的目录</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2010/08/why-choose-python-3-oop.html
