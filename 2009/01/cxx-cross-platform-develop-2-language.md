# C++ 的可移植性和跨平台开发[2]：语法 

-----

<div class="post-body entry-content">
　　目前还有相当一部分开发人员在使用老式编译器干活，这些老式编译器可能对C++98支持不够。因此，当你的代码移植到这些老式的编译器上时，可能会碰到一些稀奇古怪的问题（包括编译出错和运行时错误）。下面这些注意事项有助于你绕过这些问题。<br/>
强调一下，后面提到的好几个条款都是通过回避C++的新语法来保证移植性。如果你用的是新式编译器，那么你可以不理会这些条款。<a name="more"></a><br/>
<br/>
<br/>
<h2>★小心 for 循环变量的作用域（不支持新标准）</h2><br/>
　　在 C++ 98 标准中，for 循环变量的作用域局限在循环体内。但某些老的编译器（例如Visual C++ 6）认为 for 循环变量的作用域在循环体外。所以如下的代码可能导致移植问题。<br/>
<div class="source"><pre><span></span><span class="p">{</span>
    <span class="k">for</span><span class="p">(</span><span class="kt">int</span> <span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span> <span class="n">i</span><span class="o">&lt;</span><span class="n">XX</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span>
    <span class="p">{</span>
        <span class="c1">// ...</span>
    <span class="p">}</span>

    <span class="k">for</span><span class="p">(</span><span class="kt">int</span> <span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span> <span class="n">i</span><span class="o">&lt;</span><span class="n">XXX</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span>
    <span class="p">{</span>
        <span class="c1">// ...</span>
    <span class="p">}</span>
<span class="p">}</span>
</pre></div><br/>
　　建议修改为【不同的】循环变量名，如下所示：<br/>
<div class="source"><pre><span></span><span class="p">{</span>
    <span class="k">for</span><span class="p">(</span><span class="kt">int</span> <span class="n">i</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span> <span class="n">i</span><span class="o">&lt;</span><span class="n">XX</span><span class="p">;</span> <span class="n">i</span><span class="o">++</span><span class="p">)</span>
    <span class="p">{</span>
        <span class="c1">// ...</span>
    <span class="p">}</span>

    <span class="k">for</span><span class="p">(</span><span class="kt">int</span> <span class="n">j</span><span class="o">=</span><span class="mi">0</span><span class="p">;</span> <span class="n">j</span><span class="o">&lt;</span><span class="n">XXX</span><span class="p">;</span> <span class="n">j</span><span class="o">++</span><span class="p">)</span>
    <span class="p">{</span>
        <span class="c1">// ...</span>
    <span class="p">}</span>
<span class="p">}</span>
</pre></div><br/>
<br/>
<h2>★不要使用全局类对象，改用单键（标准未定义）</h2><br/>
　　全局类对象的构造函数先于 main() 函数执行，如果某个模块中同时包含若干个全局类对象，则它们的构造函数的调用顺序是【不确定】的。而单键是在第一次调用时被初始化，能避免此问题。另外，单键虽然解决了构造问题，但是析构依然有隐患。更多介绍请看《<a href="../../2009/02/cxx-object-destroy-overview.md">C++ 对象是怎么死的？</a>》系列博文。<br/>
<br/>
<br/>
<h2>★保持 inline 函数尽量简单</h2><br/>
　　【不要】在 inline 函数内部使用局部静态变量，【不要】在 inline 函数使用可变参数。<br/>
　　因为这些做法有可能导致可移植性的问题。<br/>
<br/>
<br/>
<h2>★不要依赖函数参数的求值顺序（标准未定义）</h2><br/>
　　C++ 标准【没有】明确规定函数参数的求值顺序。因此，如下的代码行为是不确定的。<br/>
<div class="source"><pre><span></span><span class="kt">void</span> <span class="nf">Foo</span><span class="p">(</span><span class="kt">int</span> <span class="n">a</span><span class="p">,</span> <span class="kt">int</span> <span class="n">b</span><span class="p">);</span>
<span class="kt">int</span> <span class="n">n</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span>
<span class="n">foo</span><span class="p">(</span><span class="o">++</span><span class="n">n</span><span class="p">,</span> <span class="o">++</span><span class="n">n</span><span class="p">);</span>
</pre></div><br/>
<br/>
<h2>★慎用模板特化（不支持新标准）</h2><br/>
　　某些【老式】编译器对“模板偏特化”或“模板全特化”支持不够。<br/>
　　举例：VC6 不支持“模板偏特化”。<br/>
<br/>
<br/>
<h2>★模板继承中，引用基类成员要小心（不支持新标准）</h2><br/>
　　为了直观，给出如下例子：<br/>
<div class="source"><pre><span></span><span class="k">template</span> <span class="o">&lt;</span><span class="k">typename</span> <span class="n">T</span><span class="o">&gt;</span>
<span class="k">class</span> <span class="nc">TBase</span>
<span class="p">{</span>
<span class="k">protected</span><span class="o">:</span>
    <span class="k">typedef</span> <span class="n">std</span><span class="o">::</span><span class="n">vector</span><span class="o">&lt;</span><span class="n">T</span><span class="o">&gt;</span> <span class="n">Container</span><span class="p">;</span>
    <span class="n">Container</span> <span class="n">m_container</span><span class="p">;</span>
<span class="p">};</span>

<span class="k">template</span> <span class="o">&lt;</span><span class="k">typename</span> <span class="n">T</span><span class="o">&gt;</span>
<span class="k">class</span> <span class="nc">TDerived</span> <span class="o">:</span> <span class="k">public</span> <span class="n">TBase</span><span class="o">&lt;</span><span class="n">T</span><span class="o">&gt;</span>
<span class="p">{</span>
    <span class="k">typedef</span> <span class="n">TBase</span><span class="o">&lt;</span><span class="n">T</span><span class="o">&gt;</span> <span class="n">BaseClass</span><span class="p">;</span>

<span class="k">public</span><span class="o">:</span>
    <span class="kt">void</span> <span class="n">Func</span><span class="p">()</span>
    <span class="p">{</span>
        <span class="k">typename</span> <span class="n">BaseClass</span><span class="o">::</span><span class="n">Container</span> <span class="n">foo</span><span class="p">;</span>  <span class="c1">// 可移植</span>
        <span class="n">Container</span> <span class="n">foo</span><span class="p">;</span>  <span class="c1">// 【不】可移植</span>
        <span class="k">this</span><span class="o">-&gt;</span><span class="n">m_container</span><span class="p">.</span><span class="n">clear</span><span class="p">();</span> <span class="c1">// 可移植</span>
        <span class="n">m_container</span><span class="p">.</span><span class="n">clear</span><span class="p">();</span> <span class="c1">// 【不】可移植</span>
    <span class="p">}</span>
<span class="p">};</span>
</pre></div><br/>
<br/>
<h2>★慎用 RTTI（不支持新标准、标准未定义）</h2><br/>
　　（先声明一下，俺这里说的 RTTI 主要是指 typeid 操作符和 type_info 类型）<br/>
　　首先，由于某些老式编译器可能不支持 typeid 操作符和 type_info 类型，会导致移植性的问题，这是慎用 RTTI 的一个原因。（如果你用的是新式编译器，不用考虑这个因素）<br/>
　　其次，由于标准对于 type_info 类型的约束比较简单。这导致了不同的编译器对 type_info 的实现有较大差异。如果你确实要使用 type_info 类型，建议仅仅使用它的 operator== 和 operator!= 这两个成员函数（只有这两个函数是明确定义的）<br/>
　　所以，如果你确实需要在运行时确定类型，又不想碰到上述问题，可以考虑在自己的类体系中加入类型信息来实现。例如：MFC 和 <a href="http://www.wxwidgets.org/" rel="nofollow" target="_blank">wxWidgets</a> 都是这么干的。<br/>
<br/>
<br/>
<h2>★慎用嵌套类（不支持新标准）</h2><br/>
　　如果在内部类访问外部类的非公有成员，要把内部类声明为外部类的friend。<br/>
　　如下代码存在移植问题。<br/>
<div class="source"><pre><span></span><span class="k">class</span> <span class="nc">COuter</span>
<span class="p">{</span>
<span class="k">private</span><span class="o">:</span>
    <span class="kt">char</span><span class="o">*</span> <span class="n">m_name</span><span class="p">;</span>

<span class="k">public</span><span class="o">:</span>
    <span class="k">class</span> <span class="nc">CInner</span>
    <span class="p">{</span>
        <span class="kt">void</span> <span class="n">Print</span><span class="p">(</span><span class="n">COuter</span><span class="o">*</span> <span class="n">outer</span><span class="p">)</span>
        <span class="p">{</span>
            <span class="n">cout</span> <span class="o">&lt;&lt;</span> <span class="n">outer</span><span class="o">-&gt;</span><span class="n">m_name</span><span class="p">;</span>
        <span class="p">}</span>
    <span class="p">};</span>
<span class="p">};</span>
</pre></div><br/>
应该改为如下代码：<br/>
<div class="source"><pre><span></span><span class="k">class</span> <span class="nc">COuter</span>
<span class="p">{</span>
<span class="k">private</span><span class="o">:</span>
    <span class="kt">char</span><span class="o">*</span> <span class="n">m_name</span><span class="p">;</span>

<span class="k">public</span><span class="o">:</span>
    <span class="k">class</span> <span class="nc">CInner</span><span class="p">;</span>  <span class="c1">// 前置声明</span>
    <span class="k">friend</span> <span class="k">class</span> <span class="nc">CInner</span><span class="p">;</span>

    <span class="k">class</span> <span class="nc">CInner</span>
    <span class="p">{</span>
        <span class="kt">void</span> <span class="n">Print</span><span class="p">(</span><span class="n">COuter</span><span class="o">*</span> <span class="n">outer</span><span class="p">)</span>
        <span class="p">{</span>
            <span class="n">cout</span> <span class="o">&lt;&lt;</span> <span class="n">outer</span><span class="o">-&gt;</span><span class="n">m_name</span><span class="p">;</span>
        <span class="p">}</span>
    <span class="p">};</span>
<span class="p">};</span>
</pre></div><br/>
<br/>
<h2>★不要定义参数类型相近的函数（标准未定义）</h2><br/>
　　先看如下代码：<br/>
<div class="source"><pre><span></span><span class="kt">void</span> <span class="nf">Foo</span><span class="p">(</span><span class="kt">short</span> <span class="n">n</span><span class="p">)</span>
<span class="p">{</span>
    <span class="c1">// ....</span>
<span class="p">}</span>
  
<span class="kt">void</span> <span class="nf">Foo</span><span class="p">(</span><span class="kt">long</span> <span class="n">n</span><span class="p">);</span>
<span class="p">{</span>
    <span class="c1">// ....</span>
<span class="p">}</span>

<span class="n">Foo</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span> <span class="c1">// 会导致二义性错误</span>
</pre></div>　　假如没有出现最后一行的那个调用，光编译前面两个重载的 Foo 函数是【不会】出错的。这反而增加了该问题的隐蔽性。<br/>
　　下面俺来解释一下：<br/>
　　万一这两个 Foo 函数存在于某个公共函数库中，编译这个库都很正常。但是使用这个库的某个程序调用了 Foo(0); 结果就编译失败了。<br/>
<br/>
<br/>
<h2>★不要依赖标准类型的字长（标准未定义）</h2><br/>
　　某些标准类型（例如 int、wchar_t）的字长会随着具体的平台而改变。<br/>
<br/>
<br/>
<h2>★用枚举代替类的静态成员常量（不支持新标准）</h2><br/>
　　某些【老式】的编译器不支持类的静态成员常量，可以用枚举来代替。<br/>
<div class="source"><pre><span></span><span class="k">class</span> <span class="nc">CFoo</span>
<span class="p">{</span>
    <span class="k">static</span> <span class="k">const</span> <span class="kt">int</span> <span class="n">MIN</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span>  <span class="c1">// 【不】可移植</span>
    <span class="k">enum</span> <span class="p">{</span> <span class="n">MAX</span> <span class="o">=</span> <span class="mi">64</span> <span class="p">};</span>  <span class="c1">// 可移植</span>
<span class="p">};</span>
</pre></div><br/>
<br/>
<h2>★结尾</h2><br/>
　　今天说了这么一大堆，都比较琐碎，估计会有遗漏的。日后如果大伙儿发现有补充的，欢迎在本帖的评论中指教一二。<br/>
　　由于篇幅有限，和异常相关的内容留到<a href="../../2009/01/cxx-cross-platform-develop-3-exception.md">下一个话题</a>来聊。<br/>
<br/>
<br/>
<a href="../../2009/01/cxx-cross-platform-develop-0-overview.md">回到本系列的目录</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2009/01/cxx-cross-platform-develop-2-language.html
