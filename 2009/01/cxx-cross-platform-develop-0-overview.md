# C++ 的可移植性和跨平台开发[0]：概述 

-----

<div class="post-body entry-content">
　　今天聊聊 C++ 的可移植性问题。如果你平时使用 C++ 进行开发，并且你对 C++ 的可移植性问题不是非常清楚，那么建议你看看这个系列。即使你目前没有跨平台开发的需要，了解可移植性方面的知识对你还是很有帮助的。<a name="more"></a><br/>
　　C++ 的可移植性这个话题很大，包括了编译器、操作系统、硬件体系等很多方面，每一个方面都有很多内容。鉴于本人能力、精力都有限，只能介绍每一个方面最容易碰到的问题，供大伙儿参考。<br/>
　　后面我会分别从编译器、C++ 语法、操作系统、第三方库、辅助工具、开发流程等方面进行介绍。<br/>
<br/>
<a name="index"> </a><br/>
为了方便阅读，把本系列帖子的目录整理如下：<br/>
1. <a href="../../2009/01/cxx-cross-platform-develop-1-compiler.md">编译器</a><br/>
2. <a href="../../2009/01/cxx-cross-platform-develop-2-language.md">语法</a><br/>
3. <a href="../../2009/01/cxx-cross-platform-develop-3-exception.md">异常处理</a><br/>
4. <a href="../../2009/01/cxx-cross-platform-develop-4-hardware.md">硬件体系</a><br/>
5. <a href="../../2009/02/cxx-cross-platform-develop-5-os.md">操作系统</a><br/>
6. <a href="../../2009/04/cxx-cross-platform-develop-6-thread.md">多线程</a><br/>
7. （未完待续）<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2012/05/weekly-share-5.md">每周转载：IT 大牛谈编程语言（网文3篇）</a>》<br/>
《<a href="../../2009/01/0.md">如何成为优秀开发人员</a>》（系列）
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2009/01/cxx-cross-platform-develop-0-overview.html
