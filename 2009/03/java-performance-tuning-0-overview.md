# Java 性能优化[0]：概述 

-----

<div class="post-body entry-content">
　　考虑写性能优化系列，主要是因为之前看到了太多性能其烂无比的 Java 代码（有些代码看得俺口瞪目呆）。很多 Java 程序员在写程序时，由于不太了解 JVM 及语言本身的一些运作机制，从而导致了代码的性能出现【严重】问题（性能差一个数量级以上，我才称为“严重”）。<a name="more"></a><br/>
　　虽然网上也有针对 Java 性能的介绍，但是很多内容都仅仅告诉读者“该这么做”，而没有讲“为什么该这么做”。典型的例子就是关于 String 和 StringBuffer（StringBuilder），光介绍如何用，却没有说为什么这样用。这种现象导致了很多 Java 程序员只知其然，不知其所以然。所以本系列帖子会尽量介绍一些“所以然”的东东（也就是<a href="../../2009/02/study-technology-in-three-steps.md">学习技术三部曲</a>的 HOW 和 WHY），希望对 Java 程序员有所帮助。<br/>
<a name="index"> </a><br/>
　　先初步考虑聊如下几个话题：<br/>
1. <a href="../../2009/03/java-performance-tuning-1-two-types.md">基本类型 vs 引用类型</a><br/>
2. <a href="../../2009/03/java-performance-tuning-2-string.md">字符串过滤实战</a><br/>
3. <a href="../../2009/04/java-performance-tuning-3-gc.md">关于垃圾回收（GC）</a><br/>
4. <a href="../../2009/06/java-performance-tuning-4-finalize.md">finalize函数</a><br/>
5. （未完待续）<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2012/05/weekly-share-5.md">每周转载：IT 大牛谈编程语言（网文3篇）</a>》<br/>
《<a href="../../2009/01/0.md">如何成为优秀开发人员</a>》（系列）
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2009/03/java-performance-tuning-0-overview.html
