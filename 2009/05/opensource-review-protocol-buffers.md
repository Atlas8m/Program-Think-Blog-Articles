# 开源点评：Protocol Buffers 介绍 

-----

<div class="post-body entry-content">
　　今天来介绍一下“Protocol Buffers”（以下简称 protobuf）这个玩意儿。本来俺在构思“<a href="../../2009/03/producer-consumer-pattern-0-overview.md">生产者/消费者模式</a>”系列的下一个帖子：《生产者/消费者之间的数据传输格式》。由于里面扯到了 protobuf，想想干脆单独开一个帖子算了。<br/>
<a name="more"></a><br/>
<br/>
<br/>
<h2>★protobuf 是啥玩意儿？</h2>
<br/>
　　为了照顾从没听说过的同学，照例先来扫盲一把。<br/>
　　首先，protobuf 是一个开源项目（其官方站点在“<a href="https://developers.google.com/protocol-buffers/" rel="nofollow" target="_blank">这里</a>”），而且是后台很硬的开源项目。网上现有的大部分（至少80%）开源项目，要么是某人单干、要么是几个闲杂人等合伙搞。而 protobuf 则不然，它是鼎鼎大名的 Google 公司开发出来，并且是在 Google 内部久经考验的一个东东。由此可见，它的作者绝非一般闲杂人等可比。<br/>
　　那这个听起来牛逼的东东到底有啥用处捏？简单地说，这个东东干的事儿其实和 XML 差不多——也就是把某种结构化的信息，以某种格式保存起来。主要用于“数据存储、传输协议格式”等场合。有同学可能心理犯嘀咕了：放着好好的 XML 不用，干嘛重新发明轮子啊？！先别急，后面俺自然会有说道。<br/>
　　话说到了去年（大约是2008年7月），Google 突然大发慈悲，把这个好东西贡献给了开源社区。这下，像俺这种喜欢捡现成的家伙可就有福啦！貌似喜欢捡现成的家伙还蛮多滴，再加上 Google 的号召力，开源后不到一年，protobuf 的人气就已经很旺了。俺为了与时俱进，就单独开个帖子来忽悠一把。<br/>
<br/>
<br/>
<h2>★protobuf 有啥特色？</h2>
<br/>
　　扫盲完了之后，就该聊一下技术方面的话题了。<br/>
　　由于这玩意儿发布的时间较短（尚未满周岁），所以俺接触的时间也不长。今天在此是现学现卖，列位看官多多包涵 :-)<br/>
<br/>
<h3>◇性能好/效率高</h3>
<br/>
　　现在，俺就来说说 Google 公司为啥放着好端端的 XML 不用，非要另起炉灶，重新造轮子。一个根本的原因是：【XML 性能不够好】。<br/>
　　先说时间开销：XML 格式化（序列化）的开销倒还好；但是 XML 解析（反序列化）的开销就不敢恭维啦。俺之前经常碰到一些时间性能很敏感的场合，由于不堪忍受 XML 解析的速度，弃之如敝履。<br/>
　　再来看空间开销：熟悉 XML 语法的同学应该知道，XML 格式为了有较好的可读性，引入了一些冗余的文本信息。所以空间开销也不是太好（不过这点缺点，俺不常碰到）。<br/>
　　由于 Google 公司赖以吹嘘的就是它的海量数据和海量处理能力。对于几十万、上百万机器的集群，动不动就是 PB 级的数据量，哪怕性能稍微提高 0.1% 也是相当滴可观。所以 Google 自然无法容忍 XML 在性能上的明显缺点。再加上 Google 从来就不缺造轮子的牛人，所以 protobuf 也就应运而生了。<br/>
　　Google 对于性能的偏执，那可是出了名的。所以，俺对于 Google 搞出来 protobuf 是非常滴放心，性能上不敢说是最好，但肯定不会差。<br/>
<br/>
<h3>◇代码生成机制</h3>
<br/>
　　除了性能好，“代码生成机制”是主要吸引俺的地方。为了说明这个代码生成机制，俺举个例子。<br/>
　　比如说：有个电子商务的系统（假设用 C++ 实现），其中的模块 A 需要发送大量的订单信息给模块 B，通讯的方式使用 socket。<br/>
假设订单包括如下属性：<br/>
<blockquote>时间：time（用整数表示）<br/>
客户id：userid（用整数表示）<br/>
交易金额：price（用浮点数表示）<br/>
交易的描述：desc（用字符串表示）</blockquote>
<br/>
　　如果使用 protobuf 实现，首先要写一个 proto 文件（不妨叫 Order.proto），在该文件中添加一个名为 Order 的 message 结构，用来描述通讯协议中的结构化数据。该文件的内容大致如下：<br/>
<div class="source"><pre><span class="kd">message</span> <span class="nc">Order</span>
<span class="p">{</span>
    <span class="k">required</span> <span class="kt">int32</span> <span class="na">time</span> <span class="o">=</span> <span class="mi">1</span><span class="p">;</span>
    <span class="k">required</span> <span class="kt">int32</span> <span class="na">userid</span> <span class="o">=</span> <span class="mi">2</span><span class="p">;</span>
    <span class="k">required</span> <span class="kt">float</span> <span class="na">price</span> <span class="o">=</span> <span class="mi">3</span><span class="p">;</span>
    <span class="k">optional</span> <span class="kt">string</span> <span class="na">desc</span> <span class="o">=</span> <span class="mi">4</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
<br/>
　　然后，使用 protobuf 内置的编译器【编译】该proto。由于本例子的模块是 C++，你可以通过 protobuf 编译器的命令行参数（看“<a href="https://developers.google.com/protocol-buffers/docs/proto#generating" rel="nofollow" target="_blank">这里</a>”），指定它生成 C++ 语言的“订单包装类”。（一般来说，一个 message 结构会生成一个包装类）<br/>
　　然后你使用类似下面的代码来序列化/解析该订单包装类：<br/>
<br/>
　　<b>发送方代码示例</b><br/>
<div class="source"><pre><span class="n">Order</span> <span class="n">order</span><span class="p">;</span>
<span class="n">order</span><span class="p">.</span><span class="n">set_time</span><span class="p">(</span><span class="n">XXXX</span><span class="p">);</span>
<span class="n">order</span><span class="p">.</span><span class="n">set_userid</span><span class="p">(</span><span class="mi">123</span><span class="p">);</span>
<span class="n">order</span><span class="p">.</span><span class="n">set_price</span><span class="p">(</span><span class="mf">100.0f</span><span class="p">);</span>
<span class="n">order</span><span class="p">.</span><span class="n">set_desc</span><span class="p">(</span><span class="s">"a test order"</span><span class="p">);</span>

<span class="n">string</span> <span class="n">sOrder</span><span class="p">;</span>
<span class="n">order</span><span class="p">.</span><span class="n">SerailzeToString</span><span class="p">(</span><span class="o">&amp;</span><span class="n">sOrder</span><span class="p">);</span>
<span class="c1">// 然后调用某种 socket 通讯库把序列化之后的字符串发送出去</span>
<span class="c1">// ......</span>
</pre></div>
<br/>
　　<b>接收方代码示例</b><br/>
<div class="source"><pre><span class="n">string</span> <span class="n">sOrder</span><span class="p">;</span>
<span class="c1">// 先通过网络通讯库接收到数据，存放到某字符串 sOrder</span>
<span class="c1">// ......</span>

<span class="n">Order</span> <span class="n">order</span><span class="p">;</span>
<span class="k">if</span><span class="p">(</span><span class="n">order</span><span class="p">.</span><span class="n">ParseFromString</span><span class="p">(</span><span class="n">sOrder</span><span class="p">))</span>  <span class="c1">// 解析该字符串</span>
<span class="p">{</span>
    <span class="n">cout</span> <span class="o">&lt;&lt;</span> <span class="s">"userid:"</span> <span class="o">&lt;&lt;</span> <span class="n">order</span><span class="p">.</span><span class="n">userid</span><span class="p">()</span> <span class="o">&lt;&lt;</span> <span class="n">endl</span>
         <span class="o">&lt;&lt;</span> <span class="s">"desc:"</span> <span class="o">&lt;&lt;</span> <span class="n">order</span><span class="p">.</span><span class="n">desc</span><span class="p">()</span> <span class="o">&lt;&lt;</span> <span class="n">endl</span><span class="p">;</span>
<span class="p">}</span>
<span class="k">else</span>
<span class="p">{</span>
    <span class="n">cerr</span> <span class="o">&lt;&lt;</span> <span class="s">"parse error!"</span> <span class="o">&lt;&lt;</span> <span class="n">endl</span><span class="p">;</span>
<span class="p">}</span>
</pre></div>
<br/>
　　有了这种代码生成机制，开发人员再也不用吭哧吭哧地编写那些“协议解析代码”啦（干这种活是典型的吃力不讨好）。<br/>
　　万一将来需求发生变更，要求给订单再增加一个“状态”的属性，那只需要在 <code>Order.proto</code> 文件中增加一行代码。对于发送方（模块 A），只要增加一行设置状态的代码；对于接收方（模块 B）只要增加一行读取状态的代码。哇塞，简直太轻松了！<br/>
　　另外，如果通讯双方使用不同的编程语言来实现，使用这种机制可以有效确保两边的模块对于协议的处理是一致的。<br/>
　　顺便跑题一下。<br/>
　　从某种意义上讲，可以把 proto 文件看成是描述通讯协议的规格说明书（或者叫接口规范）。这种伎俩其实老早就有了，搞过微软的 COM 编程或者接触过 CORBA 的同学，应该都能从中看到 <a href="https://en.wikipedia.org/wiki/IDL_specification_language" rel="nofollow" target="_blank">IDL</a> 的影子。它们的思想是相通滴。<br/>
<br/>
<h3>◇支持“向后兼容”和“向前兼容”</h3>
<br/>
　　还是拿刚才的例子来说事儿。为了叙述方便，俺把增加了“状态”属性的订单协议成为“新版本”；之前的叫“老版本”。<br/>
　　所谓的【向后兼容】（backward compatible），就是说，当模块 B 升级了之后，它能够正确识别模块 A 发出的【老】版本的协议。由于老版本没有“状态”这个属性，在扩充协议时，可以考虑把“状态”属性设置成【<b>非必填</b>】的，或者给“状态”属性设置一个缺省值（如何设置缺省值，参见“<a href="https://developers.google.com/protocol-buffers/docs/proto#optional" rel="nofollow" target="_blank">这里</a>”）。<br/>
　　所谓的【向前兼容】（forward compatible），就是说，当模块 A 升级了之后，模块 B 能够正常识别模块 A 发出的【新】版本的协议。这时候，新增加的“状态”属性会被忽略。<br/>
　　“向后兼容”和“向前兼容”有啥用捏？俺举个例子：<br/>
　　当你维护一个很庞大的分布式系统时，由于你无法【同时】升级【所有】模块，为了保证在升级过程中，整个系统不受影响（继续运转），就需要尽量保证通讯协议的“向后兼容”或“向前兼容”。<br/>
<br/>
<h3>◇支持多种编程语言</h3>
<br/>
　　俺开博以来点评的几个开源项目（比如“<a href="../../2009/03/opensource-review-sqlite-database.md" target="_blank">Sqlite</a>”、“<a href="../../2009/03/opensource-review-curl-library.md" target="_blank">cURL</a>”），都是支持【多种编程语言】滴，这次的 protobuf 也不例外。在 Google 官方发布的源代码中包含了 C++、Java、Python 三种语言（正好也是俺最常用的三种，真爽）。如果你平时用的就是这三种语言之一，那就好办了。<br/>
　　（注：本文发布几年后，Google 官方又增加了 Go 和 C# 的支持）<br/>
　　假如你想把 protobuf 用于其它语言，咋办捏？由于 Google 一呼百应的号召力，开源社区对 protobuf 响应踊跃，近期冒出很多其它编程语言的版本（比如：ActionScript、C#、Lisp、Erlang、Perl、PHP、Ruby ......），有些语言还同时搞出了多个开源的项目。<br/>
　　不过俺有义务提醒一下在座的各位同学：如果你考虑把 protobuf 用于上述这些语言，一定认真评估对应的开源库。因为这些开源库【不是】Google 官方提供的、而且出来的时间还不长。所以，它们的质量、性能等方面可能还有欠缺。<br/>
　　（说到“评估开源项目”，可以参考另一篇博文《<a href="../../2009/02/how-to-choose-opensource-project.md">如何选择开源项目</a>》）<br/>
<br/>
<br/>
<h2>★protobuf 有啥缺陷？</h2>
<br/>
　　前几天刚刚在“<a href="../../2009/05/halo-effect.md">光环效应</a>”的帖子里强调了“要同时评估优点和缺点”。所以俺最后再来批判一下这玩意儿的缺点。<br/>
<br/>
<h3>◇应用不够广</h3>
<br/>
　　俺写此文时，protobuf 刚公布没多久。相比 XML 而言，protobuf 还属于初出茅庐的新生代。因此，在“知名度 ＆ 应用广度”等方面都远不如 XML。由于这个原因，假如你设计的系统需要提供若干对外的接口给第三方系统调用，俺奉劝你暂时不要考虑 protobuf 格式。<br/>
<br/>
<h3>◇二进制格式导致可读性差</h3>
<br/>
　　为了提高性能，protobuf 采用了二进制格式进行编码。这直接导致了可读性差的问题（严格地说，是“没有可读性”）。虽然 protobuf 提供了 TextFormat 这个工具类（文档在“<a href="https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.text_format" rel="nofollow" target="_blank">这里</a>”），但终究无法彻底解决此问题。<br/>
　　“可读性差”的危害，俺再来举个例子。比如通讯双方如果出现问题，极易导致扯皮（都不承认自己有问题，都说是对方的错）。俺对付扯皮的一个简单方法就是直接抓包并 dump 到日志文件，能比较容易地看出错误在哪一方。但是 protobuf 的二进制格式，导致你抓包并直接 dump 出来的 log 难以看懂。<br/>
<br/>
<h3>◇缺乏自描述</h3>
<br/>
　　一般来说，XML 是自描述的，而 protobuf 格式则不是。给你一段二进制格式的协议内容，如果不配合相应的 proto 文件，那简直就像天书一般。<br/>
　　由于“缺乏自描述”，再加上“二进制格式导致可读性差”。所以在“配置文件”方面，protobuf 是肯定无法取代 XML 的地位滴。<br/>
<br/>
<br/>
<h2>★为啥俺要选用 protobuf？</h2>
<br/>
　　俺自从前段时间接触了 protobuf 之后，就着手把俺负责的产品中的【某些】数据传输协议替换成 protobuf。可能有同学会问，和 protobuf 类似的东东也有不少，为啥独独相中 protobuf 捏？由于今天写的篇幅已经蛮长了，俺卖个关子，把这个话题留到“生产者/消费者模式[5]：如何选择传输协议及格式？”。俺会在后续的这个帖子里对比各种五花八门的协议格式，并谈谈俺的浅见。<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2021/03/Computer-Networks-Overview.md">计算机网络通讯的【系统性】扫盲——从“基本概念”到“OSI 模型”</a>》<br/>
《<a href="../../2009/03/producer-consumer-pattern-0-overview.md">架构设计：生产者/消费者模式</a>》（系列）<br/>
《<a href="../../2009/03/opensource-review-curl-library.md">开源点评：cURL——优秀的应用层网络协议库</a>》<br/>
《<a href="../../2011/08/opensource-review-zeromq.md">开源点评：ZeroMQ 简介</a>》<br/>
《<a href="../../2009/03/opensource-review-sqlite-database.md">开源点评：SQLite 数据库扫盲</a>》<br/>
《<a href="../../2019/03/Misunderstand-Free-and-Open-Source-Software.md">澄清“自由软件、开源软件”相关概念及许可证的误解</a>》<br/>
《<a href="../../2009/02/how-to-choose-opensource-project.md">如何选择开源项目</a>》
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2009/05/opensource-review-protocol-buffers.html
