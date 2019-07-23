# 如何保护隐私[4]：关于浏览器的基本防范（下） 

-----

<div class="post-body entry-content">
　　本系列的上一篇介绍了 Cookie 相关的知识。今天这篇把浏览器剩余的几个常见话题聊一下。<br/>
<a name="more"></a><br/>
<br/>
<h2>★如何隔离浏览器？</h2><br/>
<h3>◇为啥要隔离浏览器？</h3><br/>
　　举例1<br/>
　　你经常使用 Gmail，并且依赖于 Gmail 的自动登录功能。这种情况下，你就【不能】禁用 <code>google.com</code> 域名对应的 cookie（禁用了就无法自动登录）。但是，如果你不禁用 <code>google.com</code> 域名对应的 cookie，当你使用 Google 的搜索功能时，Google 会知道你的搜索偏好（这涉及到隐私）。<br/>
<br/>
　　举例2<br/>
　　虽然浏览器插件会导致隐私问题（本系列<a href="../../2013/06/privacy-protection-2.md">前面的博文</a>有提到），但有些浏览器插件是你不得不安装的。比如你想看在线视频，不得不装 Flash 插件；比如你使用网银，不得不安装某些登录的控件。<br/>
<br/>
　　当你学会了【浏览器隔离】这个招数，就可以搞定上述难题，鱼和熊掌兼得。下面，俺分别介绍几种不同的隔离方法。<br/>
<br/>
<h3>◇多浏览器</h3><br/>
　　这是最简单的隔离方法——使用不同类型的浏览器（比如同时 Firefox 和 Chrome）。<br/>
　　对于刚才的第一个例子。你可以在“A浏览器”里面登录 Gmail，并允许“A浏览器”存储 <code>google.com</code> 域名的 cookie；然后你用“B浏览器”进行 Google 搜索。<br/>
　　只要你能确保——从来不在“B浏览器”中登录任何 Google 帐号，那么“B浏览器”的 cookie 中就【不会有】你的用户标识。所以你用“B浏览器”进行 Google 搜索的时候，Google 不知道你是谁。<br/>
<br/>
<h3>◇多实例</h3><br/>
　　但是有些用户就喜欢某款浏览器，不喜欢混用。那就可以考虑“多实例”的招数。目前的三大浏览器中，Firefox 和 Chrome 支持多实例，IE 不支持。啥是多实例捏？稍微解释一下。<br/>
　　所谓的浏览器多实例，洋文称之为“Multiple Profiles”。<br/>
　　不论是 Firefox 还是 Chrome，默认安装的时候，只有一个实例（Profile）。和浏览器相关的各种信息，包括：插件、扩展、外观（皮肤）、页面缓存、cookie、等等，都存储在这个实例中。<br/>
　　反之，如果使用多实例，每个实例都具有独立的插件、独立的扩展、独立的外观（皮肤）、独立的页面缓存、独立的 cookie、等等。不同实例之间是相对隔离的，不会互相影响。<br/>
　　对于 Chrome，要特别提醒一下：<br/>
　　Chrome 同时支持“Multiple Profiles”和“Multiple Accounts”。千万别把这两者搞混了。即使你配置了多个 Accounts，依然在同一个实例里（有兴趣的同学可以看 chromium 官网的“<a href="https://www.chromium.org/developers/creating-and-using-profiles" rel="nofollow" target="_blank">这个链接</a>”）<br/>
<br/>
　　关于多实例的配置，一年前写《<a href="../../2010/06/howto-prevent-hacker-attack-0.md">如何防止黑客入侵</a>》系列的时候，已经介绍过了（请翻墙看“<a href="../../2012/09/howto-prevent-hacker-attack-6.md">这里</a>”），今天就不再浪费口水了。<br/>
<br/>
<h3>◇多用户</h3><br/>
　　万一你喜欢的浏览器是 IE，而 IE 又不支持“多实例”，咋办捏？招数还是有滴，那就是【多用户】。<br/>
　　你可以创建多个操作系统用户，然后在不同的操作系统用户中分别运行同一款浏览器。所有主流的操作系统都会对系统用户的资源进行隔离。所以，你在不同的操作系统用户中运行的浏览器，也是互相隔离的（包括“插件、扩展、书签、浏览历史、cookie、缓存”，都不会互相影响）。<br/>
<br/>
　　如果你用的是 Windows 操作系统，可以使用“快速用户切换”的功能，在不同用户的桌面之间切换。但是有个缺点：一次只能看到某一个用户运行的桌面，其它用户运行的软件看不到。其实有一个小技巧，可以在同一个桌面运行多个用户的软件。具体请看<a href="../../2012/09/howto-prevent-hacker-attack-6.md">这篇博文</a>中的“多用户浏览器共享同一个桌面的技巧”。<br/>
<br/>
<h3>◇多虚拟机</h3><br/>
　　大部分场合用上述三招基本就能搞定了。但有捏，有时你会碰到一些比较变态的网银控件，一定要用系统管理员才能安装，有的控件甚至做到了“驱动级”。对于这种变态的控件，即使用“多用户”的隔离方案，也行不通了。这时候只能用【多虚拟机】来隔离。<br/>
<br/>
　　“多虚拟机”的方案，说起来挺简单——就是安装多个操作系统虚拟机，把浏览器安装到虚拟机中。利用虚拟机来进行隔离，每个虚拟机就如同一台单独的电脑，这种隔离性，比前面三个方案更加彻底。如果你不熟悉操作系统虚拟机，请先看俺写的《<a href="../../2012/10/system-vm-0.md">扫盲操作系统虚拟机</a>》系列博文。<br/>
<br/>
<br/>
<a name="dnt"> </a><br/>
<h2>★DNT（Do Not Track）</h2><br/>
　　说完了浏览器的隔离，再来说几个杂项。首先说说 DNT 这玩意儿。<br/>
<br/>
<h3>◇DNT 是啥？</h3><br/>
　　DNT 是洋文 Do Not Track 的缩写，中文译作“请勿追踪”。它最早是由 Mozilla 的一个工程师在 2009 发明的，如今已经成为 W3C 的标准。截至2012年底，所有主流的浏览器都已支持 DNT 标准。<br/>
<br/>
<h3>◇DNT 的原理</h3><br/>
　　这玩意儿说白了没啥技术含量，其原理大致如下：<br/>
　　如果你在浏览器中启用了 DNT，那么浏览器每次访问网站的时候，会在 HTTP 请求的 header 部分加入一个 DNT 的标识。网站的服务器接收到这个 HTTP 请求，看到此标识，就知道该用户不希望被追踪。<br/>
　　如果这个网站遵循 W3C 的规范——当它看到这个 DNT 标识，就【不】应该使用 cookie 或诸如此类的手段来追踪用户的行为；反之，如果这个网站【不】遵循 DNT 规范，它就会直接无视 HTTP 请求中的 DNT 标识。<br/>
<br/>
<h3>◇DNT 有用吗？</h3><br/>
　　通过上述介绍你应该可以看出：DNT 技术并不是一项很保险的防范措施。DNT 要起作用需要靠网站方面【自觉配合】。如果你访问的网站比较流氓，不愿意配合这个规范，那你的 DNT 设置就形同虚设。<br/>
　　所以，DNT 是一个有点鸡肋的功能，不能全指望它，但“启用”总比“不启用”要好（至少没啥坏处）。虽然遵循该规范的“老实”网站很少，但如果你访问的网站正好是“老实”的，启用 DNT 就能禁止该网站对你的追踪。<br/>
<br/>
<br/>
<a name="user_agent"> </a><br/>
<h2>★User Agent</h2><br/>
<h3>◇“User Agent”是啥？</h3><br/>
　　浏览器方面还有一个涉及到隐私的因素，而且不太为人所知，那就是“User Agent”。<br/>
　　浏览器的 UserAgent 是用来标识客户端的信息（包括 浏览器的类型和版本、操作系统类型和版本、等等）。浏览器向网站发起 HTTP 请求时，会在 HTTP header 中加入 User Agent 信息。<br/>
<br/>
<h3>◇“User Agent”有啥用？</h3><br/>
　　因为 User Agent 标识了浏览器客户端的信息，网站拿到这些信息之后，就可以针对客户端的不同，发送针对性的网页。比方说，如果客户端是移动设备（屏幕较小），就发送针对小尺寸屏幕的网页。<br/>
　　从这里的介绍可以看出，User Agent 本身是有用的。<br/>
<br/>
<h3>◇“User Agent”有啥隐私问题？</h3><br/>
　　但是，有些浏览器的 User Agent 写得太详细了。这就导致：很多额外的客户端信息也通过 User Agent 提交到 Web 服务端。网站拿到这么详细的信息，就可以知道你操作系统和浏览器的很多细节。另外，User Agent 越详细，“独特性”就越明显。那么网站就可以利用 User Agent，【<b>大致猜测</b>】某些页面访问是否来自同一个人。<br/>
<br/>
　　放几个比较详细的 User Agent 给大伙儿瞻仰一下：<br/>
（某个 IE）<br/>
<blockquote>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; Zune 4.0; Tablet PC 2.0; InfoPath.3; .NET4.0C; .NET4.0E)</blockquote>（某个 Opera）<br/>
<blockquote>Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.13) Gecko/20101213 Opera/9.80 (Windows NT 6.1; U; zh-tw) Presto/2.7.62 Version/11.01</blockquote>（某个腾讯浏览器）<br/>
<blockquote>Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; QQPinyin 686; QQDownload 661; GTB6.6; TencentTraveler 4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506）</blockquote>　　想知道自己浏览器的 User Agent 长啥样？猛击下面这个网址就可以看到了。<br/>
<a href="http://www.useragentstring.com/" rel="nofollow" target="_blank">http://www.useragentstring.com/</a><br/>
<br/>
<h3>◇要不要修改“User Agent”？</h3><br/>
　　对于大部分网友而言，如果对隐私方面的要求不高，没必要修改 User Agent。目前为止，User Agent 的隐私问题不如 cookie 严重。所以隐私要求不高的网友，先学会清除 cookie 的招数。<br/>
　　但如果你对隐私的要求比较高，可以考虑修改自己浏览的默认 User Agent，伪造一个假的。<br/>
<br/>
<h3>◇如何修改“User Agent”？</h3><br/>
　　要想避免 User Agent 泄漏隐私，简单的办法就是修改浏览器的“默认 User Agent”<br/>
　　俺简单说一下三大浏览器如何修改默认的 User Agent：<br/>
<br/>
　　<b>Firefox</b><br/>
　　通过定制 Firefox，创建一个新的配置项，其“名称”是 <code>general.useragent.override</code>，其“值”就是“新的 User Agent”。<br/>
　　定制 Firefox 的方法参见博文：《<a href="../../2019/07/Customize-Firefox.md">扫盲 Firefox 定制——从“user.js”到“omni.ja”</a>》。<br/>
<br/>
　　<b>Chrome</b><br/>
　　在 Chrome 的启动参数中加上 <code>--user-agent="XXX"</code><br/>
　　这个 XXX 就是新的 User Agent。（可以在快捷方式中追加命令行的启动参数）<br/>
<br/>
　　<b>IE</b><br/>
　　用 regedit 打开注册表，编辑键值 <code>HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings\User Agent</code><br/>
　　输入新的 User Agent<br/>
<br/>
<h3>◇“User Agent”改成啥样比较好？</h3><br/>
　　用上述方式，可以伪造你浏览器的 User Agent。那么，伪装的 User Agent 该如何写捏？<br/>
　　前面俺说了：“User Agent”越【独特】就越容易被追踪。所以，当你要伪造自己的“User Agent”，当然是改成比较【大众化】的。下面这3个链接包含了三大浏览器【常见的】User Agent，供大伙儿参考。<br/>
<a href="http://www.useragentstring.com/pages/useragentstring.php?name=Firefox" rel="nofollow" target="_blank">Firefox 的 User Agent</a><br/>
<a href="http://www.useragentstring.com/pages/useragentstring.php?name=Chrome" rel="nofollow" target="_blank">Chrome 的 User Agent</a><br/>
<a href="http://www.useragentstring.com/pages/useragentstring.php?name=Internet+Explorer" rel="nofollow" target="_blank">IE 的 User Agent</a><br/>
　　你可以把自己浏览器的 User Agent 伪装成另外的两种之一。<br/>
<br/>
<br/>
<h2>★结尾</h2><br/>
　　用了三篇博文，大致把浏览器【常见的】隐私问题介绍了一遍。大伙儿如果还有其它补充，或者有其它疑问，欢迎到本文留言。俺会尽量给予解答。<br/>
　　本系列的下一篇，俺来<a href="../../2014/01/privacy-protection-5.md">扫盲一下“浏览器指纹”</a>。<br/>
<br/>
<br/>
<a href="../../2013/06/privacy-protection-0.md" target="_blank">回到本系列的目录</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2013/07/privacy-protection-4.html
