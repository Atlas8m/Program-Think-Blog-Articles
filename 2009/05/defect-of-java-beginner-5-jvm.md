# Java 新手的通病[5]：不了解 JVM 

-----

<div class="post-body entry-content">
　　<a href="../../2009/02/defect-of-java-beginner-4-exception.md">上次的帖子</a>讨论了Java异常机制的几种误用，今天咱们来说说 JVM（以及 Java 编译器）相关的话题。为啥要聊 JVM 捏？因为有很多 Java 程序员，由于对 JVM 缺乏了解，在碰到某些技术问题时无从下手；另外，由于缺乏对 JVM 的了解，可能导致写出来的代码性能巨差或者有严重的 Bug。所以俺在之前的帖子“<a href="../../2009/02/study-technology-in-three-steps.md">学习技术的三部曲：WHAT、HOW、WHY</a>”中，强调了掌握内部机制的重要性。对于一个 Java 程序员来说，你不一定要非常清楚 JVM 的细节，但是对于一些关键的运作机制，还是要掌握大致的概念。<a name="more"></a><br/>
　　按照本系列的惯例，俺会问几个和 JVM 相关的问题，你如果对这些问题不是很明白，那得考虑花点时间去了解一下了。另外，鉴于有网友批评“<a href="../../2009/01/defect-of-java-beginner-0-overview.md">本系列</a>”帖子：光诊断毛病，不开出药方。（说得很形象，也很中肯）俺会针对下面提出的问题，写一些帖子来解答。<br/>
<br/>
<br/>
<h2>★关于基本类型和引用类型</h2><br/>
很多新手不理解Java的基本类型和引用类型在本质上有什么区别。请看如下的问题：<br/>
◇这两种类型在内存存储上有什么区别？<br/>
◇这两种类型在性能上有什么区别？<br/>
◇这两种类型对于 GC 有什么区别？<br/>
　　关于前两个问题，请看之前的帖子“<a href="../../2009/03/java-performance-tuning-1-two-types.md">Java性能优化[1]：基本类型 vs 引用类型</a>”。<br/>
<br/>
<br/>
<h2>★关于垃圾回收（Garbage Collection）</h2><br/>
　　很多新手不理解 GC 的实现机制。请看如下的问题：<br/>
◇GC 是如何判断哪些对象已经失效？<br/>
◇GC 对性能会有哪些影响？<br/>
◇如何通过 JVM 的参数调优 GC 的性能？<br/>
　　关于 GC 的问题，可以参见之前的帖子“<a href="../../2009/04/java-performance-tuning-3-gc.md">Java性能优化[3]：关于垃圾回收（GC）</a>”。<br/>
<br/>
<br/>
<h2>★关于字符串</h2><br/>
　　对于 Java 提供的 String 和 StringBuilder，想必很多人都知道：String 用于常量字符串，StringBuilder 用于可变字符串。那 Java 当初为什么要这样设计捏？为啥不用一个类来统一搞定捏？<br/>
<br/>
<br/>
<h2>★关于范型（Generic Programming）</h2><br/>
　　从 JDK 1.5开始，Java 引入了一个重量级的语法：范型。不过捏，很多新手仅仅知道范型的皮毛，而对于很多本质的东东，不甚了解。<br/>
◇GP 是在编译时实现的还是在运行时实现的？为什么要这么实现？<br/>
◇GP 的类型擦除机制是咋回事？有啥优点/缺点？<br/>
◇使用范型容器（相对于传统容器）在性能上有啥影响？为什么？<br/>
<br/>
<br/>
<h2>★关于多线程</h2><br/>
　　另外，多线程也是大部分 Java 新手的短板。所以俺最后再来提几个关于多线程的问题。<br/>
◇synchronized 关键字是怎么起作用滴？<br/>
◇synchronized 的颗粒度（或者说作用域）如何？是针对某个类还是针对某个类对象实例？<br/>
◇synchronized 对性能有没有影响？为什么？<br/>
◇volatile 关键字又是派啥用滴？啥时候需要用这个关键字捏？
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2009/05/defect-of-java-beginner-5-jvm.html
