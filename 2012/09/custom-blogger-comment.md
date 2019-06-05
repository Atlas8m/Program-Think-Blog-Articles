# 博客评论功能升级（引入 BBCode 语法），顺便分享一下实现方法 

-----

<div class="post-body entry-content">
<h2>★广而告之</h2><br/>
　　最近一年来，翻墙到俺博客留言的读者日渐增多。留言多了之后， Blogger / BlogSpot 平台的评论功能就越发显得老土了。这个周末，俺痛下决心，把默认的评论功能彻底改造一下。这番改造，主要增加了如下几个功能：<a name="more"></a><br/>
<b>1. 增加嵌套评论的功能</b><br/>
通过嵌套评论，直接回复前几楼的留言就方便了。<br/>
由于 Blogger / BlogSpot 平台在功能上仅支持两层嵌套。所以，目前俺还搞不出多层嵌套。<br/>
<br/>
<b>2. 增加楼层数的显示</b><br/>
类似 BBS 论坛的效果（目前不支持 IE 8 之前的版本）。<br/>
<br/>
<b>3. 增加评论者的头像</b><br/>
如果登录过 Gmail 或 OpenID，会显示用户的头像。对于匿名用户，显示默认头像。<br/>
<br/>
<b>4. 评论支持 BBCode 语法</b><br/>
可以在评论中使用常见的几种 BBCode 语法，目前支持如下4种：<br/>
<table border="0" cellpadding="0" cellspacing="0"><tr><td>超链接</td><td>[url]网址[/url]</td></tr>
<tr><td>带标题的超链接　</td><td>[url=网址]标题[/url]</td></tr>
<tr><td>图片</td><td>[img]图片的网址[/img]</td></tr>
<tr><td>粗体文字</td><td>[b]加粗的文字[/b]</td></tr>
</table>关于 BBCode 的更多介绍，请看"<a href="https://zh.wikipedia.org/wiki/BBCode" rel="nofollow" target="_blank">这里</a>"。<br/>
<br/>
<b>5. 调整了背景颜色和边框</b><br/>
主要是为了看起来爽一点。<br/>
<br/>
　　针对上述新功能，欢迎大伙儿多提意见和建议，便于俺改进（点"<a href="http://program-think.blogspot.com/2012/09/custom-blogger-comment.html#comments">这里</a>"发表你的高见）。<br/>
　　下面是改造后的评论功能截图，如果你的浏览器看到的效果有差异，敬请告知你的浏览器版本。<br/>
<br/>
<img alt="不见图 请翻墙" border="1" src="images/jAtB5-K0PTdgslIj6TsdaGTKYSHAuHmNvvQfW0v_X4VHs6wXfZULjnV6ccLyk5k3yc6XfUHtXLoYEW5_Zxwh7AkZVGTxqZ8RTMWAs6l1vAU7BStzPQ"/><br/>
<br/>
　　接下来，俺分享一下具体的实现方式，希望对其他 Blogger / BlogSpot 上的博主有帮助。如果你没有在 Blogger / BlogSpot 上开博客，那后面的内容就无需再看了。<br/>
<br/>
================华丽的分割线================<br/>
<br/>
<h2>★如何实现"嵌套评论"？</h2><br/>
简介：<br/>
嵌套评论功能由于涉及到后端，需要 Blogger / BlogSpot 平台的支持才有可能实现。幸运的是，Blogger / BlogSpot 平台在今年开始提供"嵌套评论"的功能。<br/>
由于平台提供支持，只需要简单修改一下模板即可实现。<br/>
<br/>
步骤：<br/>
首先，进入 Blogger 的后台管理界面，点左边菜单上的 "模板" 按钮。<br/>
出现模板管理界面后，再点 "修改HTML" 按钮。<br/>
出现一个对话框，点 "继续" 按钮。<br/>
然后勾选 "扩展窗口小部件模板 "。<br/>
此时，你就可以看到模板的编辑界面了。<br/>
<b>为了保险起见，在编辑之前先备份一下模板。</b><br/>
<br/>
在模板中找到如下代码：<br/>
<blockquote style="background-color:#DDD;">&lt;b:if cond='data:blog.pageType == &amp;quot;item&amp;quot;'&gt;<br/>
&nbsp;&nbsp;&lt;b:include data='post' name='comments'/&gt;<br/>
&lt;/b:if&gt;<br/>
</blockquote><br/>
修改为如下：<br/>
<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">&lt;b:if cond='data:blog.pageType == &amp;quot;item&amp;quot;'&gt;<br/>
&nbsp;&nbsp;&lt;b:if cond='data:post.showThreadedComments'&gt;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;b:include data='post' name='threaded_comments'/&gt;<br/>
&nbsp;&nbsp;&lt;b:else/&gt;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;b:include data='post' name='comments'/&gt;<br/>
&nbsp;&nbsp;&lt;/b:if&gt;<br/>
&lt;/b:if&gt;<br/>
</blockquote><br/>
最后点 "保存" 按钮。<br/>
如果不出意外，你的博客就有嵌套评论功能了。<br/>
<br/>
<h2>★如何添加楼层数？</h2><br/>
添加评论的楼层数，有很多种方法。比较简单的有如下两种。<br/>
<br/>
<h3>◇使用 JavaScript 显示楼层号</h3><br/>
简介：<br/>
直接在模板中嵌入 JS 代码。利用模板中的 loop 循环，递增楼层号并显示。<br/>
<br/>
优点：<br/>
支持各种浏览器<br/>
<br/>
缺点，<br/>
适合用于传统的评论界面。对于新的嵌套评论界面，需要对模板进行大改，比较难搞。<br/>
<br/>
步骤：<br/>
根据刚才介绍过的步骤，进入模板编辑界面。<br/>
<b>为了保险起见，在编辑之前先备份一下模板。</b><br/>
<br/>
在模板中找到如下代码：<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">&lt;b:loop values='data:post.comments' var='comment'&gt;<br/>
</blockquote><br/>
修改为如下：<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">&lt;script type='text/javascript'&gt;nCommentIndex = 1;&lt;/script&gt;<br/>
&lt;b:loop values='data:post.comments' var='comment'&gt;<br/>
&nbsp;&nbsp;&lt;span class='comment-index'&gt;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;script type='text/javascript'&gt;document.write('第'+nCommentIndex+'楼'); nCommentIndex+=1;&lt;/script&gt;<br/>
&nbsp;&nbsp;&lt;/span&gt;<br/>
</blockquote><br/>
最后点 "保存" 按钮。<br/>
如果你想调整楼层号的显示样式，可以在模板的 CSS 代码尾部追加如下代码：<br/>
（请根据自己的喜好修改下划线部分）<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">.comment-index {<br/>
&nbsp;&nbsp;float: <u>浮动靠左还是靠右</u>;<br/>
&nbsp;&nbsp;font: <u>用啥字体</u>;<br/>
&nbsp;&nbsp;font-size: <u>字体大小</u>;<br/>
&nbsp;&nbsp;color: <u>用啥颜色</u>;<br/>
}<br/>
</blockquote><br/>
全部修改完之后，点 "保存" 按钮。<br/>
<br/>
<h3>◇使用 CSS 显示楼层号</h3><br/>
简介：<br/>
利用 CSS 的计数器功能，实现楼层号的递增及显示。<br/>
<br/>
优点：<br/>
支持嵌套评论的界面<br/>
<br/>
缺点：<br/>
浏览器兼容性不够好（比如 IE6 不支持 CSS 的 content 属性）<br/>
<br/>
步骤：<br/>
根据刚才介绍过的步骤，进入模板编辑界面。<br/>
<b>为了保险起见，在编辑之前先备份一下模板。</b><br/>
<br/>
在模板代码中，找到 CSS 的那段代码，然后在 CSS 代码的尾部追加如下代码：<br/>
（以下这2段代码就是俺博客用的，欢迎剽窃）<br/>
<br/>
这一段用来显示楼层号<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">.comment-thread ol {<br/>
&nbsp;&nbsp;counter-reset: comment_counter;<br/>
}<br/>
.comment-thread li:before {<br/>
&nbsp;&nbsp;content: counter(comment_counter,decimal) "楼";<br/>
&nbsp;&nbsp;counter-increment: comment_counter;<br/>
&nbsp;&nbsp;float: right;<br/>
&nbsp;&nbsp;position: relative;<br/>
&nbsp;&nbsp;z-index: 1;<br/>
&nbsp;&nbsp;text-align: center;<br/>
&nbsp;&nbsp;font-size: 120%;<br/>
&nbsp;&nbsp;color: $mainLinkColor;<br/>
&nbsp;&nbsp;border: none;<br/>
&nbsp;&nbsp;margin-top: 10px;<br/>
&nbsp;&nbsp;margin-right: 10px;<br/>
}</blockquote><br/>
这一段用来显示嵌套在某楼层之下的单元号<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">.comment-thread ol ol {<br/>
&nbsp;&nbsp;counter-reset: child_comment_counter;<br/>
}<br/>
.comment-thread li li:before {<br/>
&nbsp;&nbsp;content: counter(comment_counter,decimal) "楼 " counter(child_comment_counter,decimal) "单元";<br/>
&nbsp;&nbsp;counter-increment: child_comment_counter;<br/>
&nbsp;&nbsp;font-size: 100%;<br/>
}</blockquote><br/>
修改完之后，点 "保存" 按钮。<br/>
<br/>
<h2>★如何添加头像？</h2><br/>
根据刚才介绍过的步骤，进入模板编辑界面。<br/>
<b>为了保险起见，在编辑之前先备份一下模板。</b><br/>
<br/>
在模板中找到如下代码：<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">&lt;dl id='comments-block'&gt;<br/>
</blockquote><br/>
修改为如下：<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">&lt;dl expr:class='data:post.avatarIndentClass' id='comments-block'&gt;<br/>
</blockquote><br/>
还没完，就在这行代码下方2-3行的地方有如下代码：<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">&lt;a expr:name='data:comment.anchorName'/&gt;<br/>
</blockquote><br/>
修改为如下：<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">&lt;a expr:name='data:comment.anchorName'/&gt;<br/>
&lt;b:if cond='data:blog.enabledCommentProfileImages'&gt;<br/>
&nbsp;&nbsp;&lt;div expr:class='data:comment.avatarContainerClass'&gt;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&lt;data:comment.authorAvatarImage/&gt;<br/>
&nbsp;&nbsp;&lt;/div&gt;<br/>
&lt;/b:if&gt;<br/>
</blockquote><br/>
如果你想调整头像的显示尺寸，可以在模板的 CSS 代码尾部追加如下代码：<br/>
（请根据自己的喜好修改下划线部分）<br/>
<blockquote style="background-color:#DDD;font-family:Courier,monospace;">.comments .avatar-image-container img {<br/>
&nbsp;&nbsp;width: <u>图像宽度</u>;<br/>
&nbsp;&nbsp;height: <u>图像高度</u>;<br/>
&nbsp;&nbsp;border: <u>图像边界</u>;<br/>
}<br/>
</blockquote><br/>
修改完之后，点 "保存" 按钮。<br/>
<br/>
<h2>★结尾</h2><br/>
　　今天就先介绍到这里。以后如果有空，俺还会继续改进本博客的评论功能。相关的代码也会继续补充到本文中。欢迎其它博主<a href="http://program-think.blogspot.com/2012/09/custom-blogger-comment.html#comments">到本文留言</a>，交流经验。<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
<a href="../../2015/04/custom-blogger-comment.md">博客评论功能升级（智能贴图、图片代理）——兼谈“Web 图片的隐私问题及防范”</a><br/>
<a href="../../2014/12/custom-blogger-comment.md">博客评论功能升级（“未读”状态、按时间过滤）——兼谈“为啥俺不用其它博客平台”</a><br/>
<a href="../../2014/09/custom-blogger-comment.md">博客评论功能升级（增加“留言过滤”、“200条之后自动加载”等）</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2012/09/custom-blogger-comment.html
