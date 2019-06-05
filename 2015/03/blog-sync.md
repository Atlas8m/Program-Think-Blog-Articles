# 提供“博客离线浏览”和“电子书制作脚本”——用 BT Sync（Resilio Sync）【免翻墙】自动同步 

-----

<div class="post-body entry-content">
　　先提醒一下：“BT Sync”已经改名为“Resilio Sync”，但俺还是习惯于叫它原来的名字。<br/>
　　今年1月份，俺开始通过 BT Sync（Resilio Sync）自动同步俺网盘上的电子书，以取代流量受限的 Dropbox 网盘。之后，有几位热心读者建议俺把“博客打包电子书”也通过 BT Sync 进行自动同步。<br/>
　　前段时间，俺折腾了一下，已经基本搞定。今天发一篇博文通告大伙儿。<a name="more"></a><br/>
<br/>
<h2>★关于“离线浏览”</h2><br/>
<h3>◇何为“离线浏览”？</h3><br/>
　　如果你曾经使用过“离线下载工具”，应该知道俺所说的“离线浏览”是啥意思。<br/>
　　所谓的“离线下载工具”，可以把整个网站的页面内容，下载到本地——变成存储在你本机的网页。下载完成之后，你可以用浏览器浏览这些本地的页面（此时无需联网）。<br/>
　　俺这次提供的“离线浏览”功能，大致也是如此。差别在于——你无需再使用“离线下载工具”，只需使用 BT Sync 进行【自动同步】。<br/>
<pre style="font-family:Courier,monospace;"><b>“博客离线浏览页面”的 BT Sync 同步密钥是：</b>
B7P64IMWOCXWEYOXIMBX6HN5MHEULFS4V</pre>　　没用过 BT Sync 的同学，先看教程：《<a href="../../2015/01/BitTorrent-Sync.md">扫盲 BT Sync——不仅是同步利器，而且是【分布式】网盘</a>》。<br/>
<br/>
<h3>◇如何使用？</h3><br/>
　　首先，把上述密钥添加到你的 BT Sync 客户端。<br/>
　　其次，确保你的 BT Sync 已经完成同步（同步目录对应的图标变为绿色）。<br/>
　　最后，打开这个 BT Sync 同步目录，在同步目录下，找到一个名叫 <b>html</b> 的目录，然后用浏览器打开该目录下的 <b>index.html</b> 页面，就可以看了。<br/>
<br/>
<h3>◇“离线浏览”有啥好处？</h3><br/>
　　至少有如下几点：<br/>
<br/>
　　<b>1. 应对 GFW 的封杀</b><br/>
　　最近5年来，俺长期在博客上介绍翻墙教程。但是因为本博客已经被 GFW 封杀。你需要先翻墙，才能看到俺写的翻墙教程。这时候就存在一个“先有鸡还是先有蛋”两难困境。<br/>
　　而且最近一年多来，GFW 的封锁越来越严厉。万一你手头的翻墙工具全部都失效了，那么你就无法再访问俺博客了。<br/>
　　如今俺提供了离线浏览，你可以把俺博客的全部内容通过 BT Sync 同步到你自己的电脑上。一旦你手头的翻墙工具失效了，你还可以继续看俺写的翻墙教程，然后去搞定其它翻墙工具。<br/>
<br/>
　　<b>2. 无须联网</b><br/>
　　在没法联网的设备上，也可以看俺博客的内容。<br/>
<br/>
　　<b>3. 便于分享</b><br/>
　　如果你看得起俺写的东西，想要分享给周围的人。就可以把离线页面直接打包，然后通过各种方式（比如邮件）转发给你的朋友。<br/>
<br/>
<h3>◇使用 BT Sync 有啥好处？</h3><br/>
　　使用 BT Sync 至少有如下几个好处：<br/>
<br/>
　　<b>1. 免翻墙</b><br/>
　　由于俺的博客长期被 GFW 封杀。这点非常重要。<br/>
<br/>
　　<b>2. 增量同步</b><br/>
　　BT Sync 会智能地判断——哪些页面/图片更新了。然后，它只同步那些更新过的页面和图片。<br/>
<br/>
　　<b>3. 自动同步</b><br/>
　　所谓的“自动”就是说，你只需把 BT Sync 一直开着，一旦俺这边有更新，BT Sync 自动把新内容同步到你本机。<br/>
<br/>
<br/>
<h2>★关于“电子书制作脚本”</h2><br/>
<h3>◇啥是“电子书制作脚本”？</h3><br/>
　　一年前（2014年4月），<a href="../../2014/04/blog-ebook.md">俺开始提供博客内容的打包下载</a>。当时提供的电子书格式是 CHM 和 EPUB。<br/>
　　今后，俺【不再提供】这两个格式的打包下载，改为提供“电子书制作脚本”。<br/>
　　有了“电子书制作脚本”，你可以把俺博客的“离线浏览页面”制作成电子书（具体使用方法，待会儿告诉你）。<br/>
　　目前的“电子书制作脚本”支持两种格式（CHM 和 EPUB）。如果大伙儿有需要，可以考虑增加其它格式。<br/>
<br/>
<h3>◇为啥俺不再提供“博客打包电子书”的下载？</h3><br/>
　　因为俺博客的内容越来越多，因此，打包之后的 CHM 和 EPUB 也越来越大（如今已经超过 150 兆）。每次有博文更新，俺都要重新上传这两种格式的文件（加起来就是 300 MB），非常费劲。而且会增加俺的风险（被“流量分析”的风险）。<br/>
　　另外，大伙儿从微软网盘下载这两个大文件，也非常费劲（微软网盘有时候会有故障）。<br/>
　　有了电子书制作脚本，俺每次只需同步新增的博文，然后由你自己在电脑上运行制作脚本，把电子书做出来。<br/>
　　<b>别怕，俺提供的脚本是非常傻瓜化的，可以【一键式生成电子书】。</b><br/>
<br/>
<h3>◇“CHM 格式”如何制作？</h3><br/>
　　制作“CHM 格式”的具体步骤如下：<br/>
1. 确保你已经完成 BT Sync 的同步（在界面上，该同步目录的图标变为绿色）。<br/>
2. 打开对应的同步目录<br/>
3a. 使用 Windows 系统的同学，进入如下目录： <code>blog\make\chm</code> 并双击 <code>make-chm.wsf</code><br/>
3b. 使用 Linux 或苹果系统的同学，进入如下目录： <code>blog/make/chm</code> 并运行 Python 脚本 <code>make-chm.py</code>（该脚本同时兼容 Python2 和 Python3）<br/>
<br/>
　　<b>备注</b><br/>
　　因为俺目前找不到任何开源的库，能够生成 chm 格式（只有解开 chm 格式的库，没有生成的库）。所以俺不得不依赖微软的编译器（hhc）。<br/>
　　所幸这玩意儿是绿色的，只需两个文件（<code>hhc.exe</code> 和 <code>hha.dll</code>），所以俺把这两个文件放到了同步目录中。<br/>
　　因为这两个文件【没有】内置数字签名，为了让大伙儿放心，俺特地注明了这两个文件在 VirusTotal 的病毒扫描结果（<a href="https://www.virustotal.com/en/file/3e96894609819ae3d595ff6e0fbe9ce6c9ac17bdeda256b994831992f668cb99/analysis/" rel="nofollow" target="_blank">这里</a>和<a href="https://www.virustotal.com/en/file/32003df5ecd25fa39a0c410a487c8b8440758f199eb4032b4ec03cd8f1da220c/analysis/" rel="nofollow" target="_blank">这里</a>）。在这两个扫描页面上，已经注明了这两个文件都是来自微软的【可信任文件】。<br/>
　　由于要依赖微软的编译器，所以，使用 Linux/Unix 的同学，需要 <a href="https://en.wikipedia.org/wiki/Wine_(software)" rel="nofollow" target="_blank">Wine</a> 才能制作 chm 格式的电子书。并且你要把 <code>hhc.exe</code> 和 <code>hha.dll</code> 放置到 wine 的可执行文件搜索路径中。<br/>
<br/>
<h3>◇“EPUB 格式”如何制作？</h3><br/>
　　制作“EPUB 格式”的具体步骤如下：<br/>
1. 确保你已经完成 BT Sync 的同步（在界面上，该同步目录的图标变为绿色）。<br/>
2. 打开对应的同步目录<br/>
3a. 使用 Windows 系统的同学，进入如下目录： <code>blog\make\epub</code> 并双击 <code>make-epub.wsf</code><br/>
3b. 使用 Linux 或苹果系统的同学，进入如下目录： <code>blog/make/epub</code> 并运行 Python 脚本 <code>make-epub.py</code>（该脚本同时兼容 Python2 和 Python3）<br/>
<br/>
<h3>◇“CHM 格式”如何阅读？</h3><br/>
　　<b>Windows 系统</b><br/>
　　Windows 系统默认就支持 CHM 格式的阅读。你只需双击该文件，既可打开。<br/>
<br/>
　　<b>【非】Windows 系统</b><br/>
　　不使用 Windows 系统的同学，可以参考维基百科的“<a href="https://en.wikipedia.org/wiki/Microsoft_Compiled_HTML_Help" rel="nofollow" target="_blank">这个页面</a>”，列出了“【非】Windows”下的 CHM 阅读软件。<br/>
<br/>
<h3>◇“EPUB 格式”如何阅读？</h3><br/>
　　EPUB 的阅读软件很多，而且各个平台（Windows、Linux、Mac OS X、Android、iOS）都有。维基百科的<a href="https://zh.wikipedia.org/wiki/EPUB" rel="nofollow" target="_blank">这个页面</a>列出了常用的 EPUB 阅读软件。<br/>
<br/>
<br/>
<h2>★欢迎大伙儿反馈</h2><br/>
　　由于俺的时间和精力有限，上述制作脚本只在少数几种操作系统上进行测试。<br/>
　　如果在你的环境中，电子书制作脚本无法正常工作，拜托你到俺博客留言，反馈你碰到的问题。俺会尽快解决。<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
<a href="../../2015/01/BitTorrent-Sync.md">扫盲 BTSync（Resilio Sync）——不仅是同步利器，而且是【分布式】网盘</a><br/>
<a href="../../2017/08/GFW-Resilio-Sync.md">聊聊 GFW 如何封杀 Resilio Sync（BTSync）？以及如何【免翻墙】继续使用？</a><br/>
<a href="../../2014/04/blog-ebook.md">开始提供博客内容打包下载（支持 CHM 和 EPUB 格式）</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2015/03/blog-sync.html
