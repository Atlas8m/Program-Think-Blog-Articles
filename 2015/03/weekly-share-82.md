# 每周转载：关于 GitHub 和 GFW 的 PK（第2季） 

-----

<div class="post-body entry-content">
　　如果你是个程序员，或者比较关注翻墙的动态，或许你已经听说——最近一周，GFW 又跟 GitHub 干上了。<br/>
　　早在2年前，GitHub 已经跟 GFW PK 过一次了。当时俺还发了一篇《<a href="../../2013/02/weekly-share-39.md">每周转载：关于 GitHub 和 GFW 的 PK</a>》。所以，本次的交锋，称为“第2季”。<a name="more"></a><br/>
<br/>
<h2>★当事人以及海内外媒的报道</h2><br/>
<a href="https://github.com/blog/1981-large-scale-ddos-attack-on-github-com" rel="nofollow" target="_blank">Large Scale DDoS Attack on github.com @ GitHub Blog</a><br/>
（编程随想注：这是 GitHub 官方博客对此事的说明，俺摘录其中部分文字）<br/>
<blockquote>We are currently experiencing the largest DDoS (<a href="https://en.wikipedia.org/wiki/Denial-of-service_attack" rel="nofollow" target="_blank">distributed denial of service</a>) attack in github.com's history. The attack began around 2AM UTC on Thursday, March 26, and involves a wide combination of attack vectors. These include every vector we've seen in previous attacks as well as some sophisticated new techniques that use the web browsers of unsuspecting, uninvolved people to flood github.com with high levels of traffic. Based on reports we've received, we believe the intent of this attack is to convince us to remove a specific class of content.<br/>
We are completely focused on mitigating this attack. Our top priority is making sure github.com is available to all our users while deflecting malicious traffic. Please watch <a href="https://status.github.com/" rel="nofollow" target="_blank">our status site</a> or follow <a href="https://twitter.com/githubstatus" rel="nofollow" target="_blank">@githubstatus</a> on Twitter for real-time updates.</blockquote><br/>
<a href="https://slashdot.org/submission/4299157/chinas-national-firewall-hijacks-javascript-to-ddos-github" rel="nofollow" target="_blank">China's national firewall hijacks JavaScript to DDoS GitHub @ slashdot.org</a><br/>
（编程随想注：这是著名极客网站 Slashdot 对此事报道）<br/>
<br/>
<a href="https://cn.nytimes.com/china/20150331/c31hack/" rel="nofollow" target="_blank">中国劫持百度广告流量攻击GitHub @ 纽约时报</a><br/>
<br/>
<a href="https://news.ycombinator.com/item?id=9284226" rel="nofollow" target="_blank">GitHub under ongoing DDoS attack @ Ycombinator News</a><br/>
（编程随想注：这是老外在 Ycombinator 上的讨论，挺热烈滴。以下这段是出口转内销，介绍了朝廷对 GitHub 进行 DDOS 攻击的4个阶段）<br/>
<blockquote>I saw this on Weibo earlier, NOT from a trusted source. But the first and third rounds have been confirmed.<br/>
第一轮外域JavaScript，一个alert防住；<br/>
第二轮外域img，Referer挡外面；<br/>
第三轮GitHub Pages被D；<br/>
第四波正在进行，是TCP SYN Flood攻击。<br/>
<br/>
My translation:<br/>
The first round was cross-domain JavaScript, stopped with an "alert()".<br/>
Second round was cross-domain &lt;img&gt;, stopped with referrer.<br/>
Third was DDoS-ing GitHub Pages.<br/>
Fourth is the ongoing TCP SYN Flood attack.</blockquote><br/>
<a href="https://www.solidot.org/story?sid=43500" rel="nofollow" target="_blank">对GitHub的DDoS攻击在继续，百度否认与其有关 @ Solidot</a><br/>
<br/>
<a href="https://www.solidot.org/story?sid=43506" rel="nofollow" target="_blank">对GitHub的大规模DDoS攻击已超过80个小时 @ Solidot</a><br/>
<blockquote>对GitHub的大规模DDoS攻击已超过<a href="https://status.github.com/messages?latest" rel="nofollow" target="_blank">80个小时</a>，攻击者此举显然是为了迫使GitHub<a href="http://weibo.com/5488749285/CaGZLsvc0?from=page_1006065488749285_profile&amp;wvr=6&amp;mod=weibotime" rel="nofollow" target="_blank">移除</a>反审查项目Greatfire。DDoS攻击产生的史翠珊效应（Streisand effect）反而让更多人知道了Greatfire。攻击者先后使用了四种DDoS技术<a href="https://news.ycombinator.com/item?id=9284226" rel="nofollow" target="_blank">攻击</a>GitHub（未完全确认）：第一波是创造性的劫持百度JS文件利用中国海外用户的浏览器每2秒向托管在GitHub上的两个反审查项目发出请求，这一手段被GitHub用弹出JS警告alert()防住；第二轮是跨域 &lt;img&gt; <img/> 攻击，被GitHub检查Referer挡住；第三波是DDoS攻击GitHub Pages；第四波是正在进行中的TCP SYN洪水攻击，利用TCP协议缺陷发送大量伪造的TCP连接请求，让GitHub耗尽资源。对于Greatfire所实现的<a href="https://openitp.org/pdfs/CollateralFreedom.pdf" rel="nofollow" target="_blank">collateral freedom</a>（PDF），也有许多人对此表达了不满，Greatfire的做法让一些CDN服务商遭到了封杀，而GitHub是最新的受害者。</blockquote><br/>
<a href="https://www.solidot.org/story?sid=43530" rel="nofollow" target="_blank">中国对GitHub发动的是Man-on-the-side攻击 @ Solidot</a><br/>
<br/>
<a href="https://www.solidot.org/story?sid=43569" rel="nofollow" target="_blank">寻找DDoS攻击GitHub的幕后组织 @ Solidot</a><br/>
<blockquote>为了防止数据在网络中无限循环，名为<a href="https://en.wikipedia.org/wiki/Time_to_live" rel="nofollow" target="_blank">存活时间（Time to live，TTL）</a>或跳数限制（hop limit）的机制限定了数据包的寿命。当TTL=0，数据包将被丢弃。大多数系统发送IP包时都是从TTL=64开始，如果该数据包抵达你时TTL=46，那么你和发送者之间经过了18跳（64-18=46）。在对GitHub发动大规模DDoS攻击时，攻击者劫持了百度的JS文件。如图所示，百度服务器所发送数据包的TTL=64，第一次抵达用户浏览器时TTL=42（不同位置这一数字会有所不同），经过了22跳，用户发回的请求包的TTL值也是64，但接下来的响应包的TTL值非常怪异，显然有个中间人设备注入了伪造包。如何识别这个中间人设备的IP？你可以借助Traceroute工具。利用该工具发送TTL=1，2，3....的请求包，因为TTL的值很小，在到达目的地前跳数就会变为零被沿路的路由器抛弃，而此时路由器会使用其IP地址发回时间超时的报文，如果某两跳之间发现了伪造包，那么注入设备应该就藏在其中。一位研究人员用定制Traceroute工具测试发现，注入设备位于第11跳和第12跳之间，通过查询第12跳设备的IP地址，作者发现它<a href="http://blog.erratasec.com/2015/04/pin-pointing-chinas-attack-against.html" rel="nofollow" target="_blank">位于中国联通骨干网</a>，因此得出了中国政府与此有关的结论。</blockquote><br/>
上述几篇，是国内极客网站 Solidot 对此事的报道。<br/>
<br/>
<a href="https://pao-pao.net/article/404" rel="nofollow" target="_blank">中国翻墙者被劫持为黑客 Github遭史上最大攻击 @ 泡泡网</a><br/>
<br/>
<br/>
<h2>★DDOS 是谁干的？</h2><br/>
　　很显然，是咱们天朝大名鼎鼎的 GFW 干的。<br/>
　　这可【不是】冤枉它——从前面转载的几篇，已经能看出是 GFW 所为。另外，你还可以看文本的后续章节——★对“攻击手段”的技术分析——里面有各路网友的分析。<br/>
<br/>
<br/>
<h2>★GFW 的动机何在？</h2><br/>
　　那么，对 GitHub 进行 DDOS 的动机何在捏？<br/>
　　此次攻击针对的页面是 https://github.com/greatfire。该页面是 GreatFire 在 GitHub 上的主页。攻击者这么做，就是为了让 GitHub 的服务器不堪重负，从而逼迫 GitHub 移除 GreatFire 的相关内容（甚至注销该帐号）。<br/>
　　为啥 GreatFire 会跟 GFW 结仇捏？最大的一个原因是：GreatFire 最近几年开始提供墙外知名网站的【免翻墙镜像】（很多读者应该知道，俺博客的镜像也是其中之一）<br/>
　　以下是 GreatFire 目前提供镜像的网站列表：<br/>
<blockquote>Google 搜索<br/>
纽约时报<br/>
BBC<br/>
德国之声<br/>
自由微博<br/>
中国数字时代<br/>
博讯网<br/>
泡泡网<br/>
编程随想<br/>
人民监督网</blockquote><br/>
　　以下是 GreatFire 发出的呼吁：<br/>
<blockquote>GreatFire.org：<br/>
既然GFW想让全球的中文用户DDOS我们的网页 https://github.com/greatfire/wiki 大家把这个转给朋友访问吧。</blockquote><br/>
<br/>
<h2>★GFW 的攻击是否得手？</h2><br/>
　　到目前为止，GitHub 并没有删除 GreatFire 帐号的内容。所以，朝廷的企图，暂时还没有得逞。<br/>
　　在接下来的几天，咱们还要继续关注，看看 GitHub 的骨气，到底有多硬？<br/>
<br/>
　　虽然 GitHub 暂时还没有向朝廷妥协，但是 DDOS 攻击，已经给 GitHub 造成了一些影响。最近几天，你如果访问 GreatFire 在 GitHub 的主页（https://github.com/greatfire），会看到如下报错信息：<br/>
<blockquote><center><img alt="不见图 请翻墙" src="images/jkC-9LMR98na1gzs80ylDHF4P_LbUkUhqUTrcRKCugBrmziblg_05fQbutM_-Rd_k0dSqzSOE6OhEEA7JNPfOtPm7pzvo6KKM7hWSRhWgXS0kNRRoYEUOPiOZ4hLRfrEZLBIs-3y-A"/></center>Something went wrong and we cannot service your request.<br/>
<br/>
Sorry about that. Please try refreshing and contact us if the problem persists.</blockquote><br/>
　　另外还有墙内读者给出了 GitHub 访问速度受到的影响。<br/>
<blockquote>比特客栈的寻行数墨：<br/>
再次强调，Github没有因为DDoS封中国的IP。<br/>
但由于攻击，整个线路的访问速度受到很大影响，某程度上GFW做到了它们想做的事情。<br/>
而且这次，没有李开复来救火。 <br/>
<center><img alt="不见图 请翻墙" src="images/8hCPo4cNgjhFxZ8ObP-zCj_qCEWAFRNV-nVYcrgCt1zpoVfnQ4oxukxQZPvnaixMvwu7u3cMj53mEDfz-9CseNMUiNJ5UOOKeAWc7gK0vAn0gpqPWCW8aM5KiOtwh0jsW3zXgSAGyg"/></center></blockquote><br/>
　　如果拿 GitHub 跟全球顶级的 IT 公司作一下对比，会发现它在对抗 DDOS 方面，还是有欠缺。以下是某知名博主的评论，谈及“朝廷御用骇客”攻击 Google 和 Facebook 遭遇的尴尬挫败。<br/>
<blockquote>Eric Xu, PhD (徐宥)：<br/>
硅谷小道消息。某国政府不是没 DDoS 过G和F。<br/>
这两家公司的 CDN, EdgePOP 和负载均衡做得很好，以至于某国政府无法伤害。<br/>
话说某国政府上次搞的时候，搞完好久G才发现，因为流量还没凯特王妃结婚直播时候高。<br/>
这种没回应的攻击好伤人家感情的，从此没脸再搞这些大鳄。<br/>
<br/>
Eric Xu, PhD (徐宥)：<br/>
依然小道消息。搞 F 的时候也是不疼不痒，负载均衡系统直接吸收了流量。<br/>
相比之下有次 Facebook 客户端程序员出了个大Bug, 自家客户端不断访问某资源以至于自己 DDoS 自己。<br/>
除此外其他攻击都没达到类似量级，也就无所谓了。</blockquote><br/>
　　曾经有好几个读者问俺：为啥要选择 Google 的 Blogger/blogspot 作为博客平台？为啥不用 WordPress 或者干脆自己在 VPS 上搭建博客。<br/>
　　通过这次事件，你或许就能体会到——俺选择 Blogger 搭建博客的优势（基本不用担心朝廷的 DDOS 攻击）。像俺这种长期抹黑朝廷的反党分子，对 DDOS 攻击还是需要防范于未然。<br/>
<br/>
<br/>
<h2>★对“攻击事件”的网民评论</h2><br/>
推倒柏林墙：<br/>
自从GitHub反击之后我上国内网站就老是跳出恶意脚本警告，忍无可忍只好把百度的JS给屏蔽了（我之前从来不用广告屏蔽软件）。<br/>
上GitHub看了一眼貌似人家屁事都没有，根本没给GFW击沉，百度就这么白白做了炮灰，真是凄凉。<br/>
<br/>
Shippo7：<br/>
百度网盘的页面有脚本正在ddos github，录了一段视频<br/>
https://www.youtube.com/watch?v=l6eAtcwT5Pc<br/>
<br/>
比特客栈的寻行数墨：<br/>
如果你没能测出这次基于百度CDN劫持的Github DDoS，别担心，这有个视频演示。<br/>
https://www.youtube.com/watch?v=l6eAtcwT5Pc<br/>
<br/>
比特客栈的寻行数墨：<br/>
值得一提，这个视频也演示了Github对策攻击的高明之处——<br/>
在你点击确认alert或无视alert之前，浏览器的js会block，不再执行，也就有效降低了自动发请求的次数。<br/>
<br/>
Tianran Ding：<br/>
访问新浪网的某些JS也被劫持夹带代码去攻击 Github<br/>
http://news.sina.com.cn/w/2015-03-29/133631657611.shtml … @GreatFireChina <br/>
<center><img alt="不见图 请翻墙" src="images/fScD4D9uWaQ1RUUjH2qS3ZKt6x4l3UdFPVm_on75FUXfxzytIRDfoQofHz4gEqHCS9XwHTJ3hkF8YFSpZa6NCGvGaMSn7-ZcJSM6oJBVDgVW9jUwBLwvhA4WRnbS50uDfxDkh7j3EA"/></center><br/>
xxoo：<br/>
@dingtianran @iaskfq @GreatFireChina RT @bitinn: 建议将“DDoS attack has shifted again...”翻译为“强奸犯又换了一个姿势”。<br/>
<br/>
余晟：<br/>
GFW本着“利用和破坏正常信任关系”的精神，突破了恶心下作的底线<br/>
<br/>
wzyboy：<br/>
GFW 利用百度 CDN 来 DDoS GitHub，这「创意」 -_-<br/>
<br/>
<br/>
<h2>★对“攻击手段”的技术分析</h2><br/>
陈少举：<br/>
@cxqn @yegle @Arctosia @wenyunchao<br/>
https://twitter.com/mac_zhou/status/581321375773667328<br/>
从TTL的变动来看，极高的可能性是GFW引起的。相同IP的通信不可能发生剧烈的TTL变化。<br/>
<br/>
Mac_Zhou：<br/>
@chenshaoju @cxqn @yegle @Arctosia @wenyunchao 不排除百度的可能性。<br/>
TTL只相差了3，这说明百度服务器和这台中间设备可能靠得很近。<br/>
当然更有可能不是伪造报文，而是直接在线路中插入的。<br/>
<br/>
Mac_Zhou：<br/>
对@yegle 发现的百度JS被植入greatfire的现象进行了抓包跟踪，正常百度服务器返回给我日本VPS的TTL为51， RESP返回HTTP 200 OK的报文的TTL是 47，可以确定的是有中间设备对VPS发了伪造报文。 <br/>
<center><img alt="不见图 请翻墙" src="images/rw8AwvSQbbhCi5cvyYjDRRSH_LkYlE-A02GXOTuWo9QsH2jvxUgWARRCvWsqkkOBIw5GBfibGWzoL23_M3LX3WM7O3YLaX4o1ZLkqeW444QGNDHohJKsffrFXHeL1BqW2m5CdfNUTQ"/></center><br/>
Danny Chen：<br/>
@yegle @Arctosia @chenshaoju @wenyunchao 可以直接说是操纵众多浏览器向github发起请求，因而造成DDoS。还不能确认是Gfw所为，要仔细实验排除百度公司所为的可能。<br/>
<br/>
北风（温云超, Yunchao Wen）：<br/>
@mac_zhou @chenshaoju @cxqn @yegle @Arctosia 百度自己出面干这种事的可能性不大。<br/>
<br/>
陈少举：<br/>
@wenyunchao @mac_zhou @cxqn @yegle @Arctosia 劫持和被劫持的时候，HTTP返回的头部信息里的Server字段是完全不一样的。被劫持的时候是Apache，正常的时候是JSP3/2.0.6。 <br/>
<center><img alt="不见图 请翻墙" src="images/fZbYFggN-n3WM8meI766SsSGRqEi-cgInMyGkGJ2aKHchz-_xK3QCLQ2vsejkPBTs8bJvO3BcyNxRybfZsbcwYRLEbEPpyEfZ9CiKxHI-UXZkFku2VacnvBkaeQZJbn3hr8tiBqaWw"/></center><br/>
九条凛：<br/>
牆外訪問百度時確實可以在m.js中發現github，greatfire和cn-nytimes等字樣，有理由相信中國本次針對github的國家級攻擊是真實可信的。 <br/>
<center><img alt="不见图 请翻墙" src="images/4LxQCn6R9WtkSctcPhwfD-ZfWxuxcwd-A2q3Cm83wC-L7ZoWLIMVmbfZl3Nf2MbQFCsBgn4zYD-pBBgn12u40tVzVEoCwyvFSHvHi_qbhg2DWvUYAoE2RgKzTwUyeeqW8h8Q-Lg1Og"/></center><br/>
28小盆友：<br/>
这次的事情其实也不复杂……<br/>
就是 GFW 利用很多网站都有百毒的广告联盟之类，发假包，给他们的 JS 插了个攻击代码，用户读取之后就去攻击 GitHub 了。<br/>
因为国内用户访问百毒不用过墙，所有只有国外的访问才会有效……贱格<br/>
<br/>
C.A. Yeung：<br/>
为何要劫持百度来攻击GITHUB：<br/>
1. 这方式的优点是可以无需劫持大量电脑，也可以让网站访客在不自觉的情况下成了攻击行动的帮凶<br/>
2. 让人产生攻击是来自中国境外的错觉<br/>
3. 希望透过服务供应商向外国媒体施压，删除中共官方不喜欢的内容。<br/>
https://thenanfang.com/why-baidu-was-hijacked-to-attack-github/<br/>
<br/>
一阁：<br/>
看起来似乎是这样的：<br/>
国内好多网站上嵌入的某个js会自动载入 http://github.com/greatfire/  和 http://githu.com/cn-nytimes/ ，达到DDoS效果。<br/>
GitHub看到大量流量和referer信息后决定这两个URL返回javascript<br/>
<br/>
<br/>
<h2>★关于“GFW”的相关评论</h2><br/>
Jian Alan Huang：<br/>
GFW之所以越来越忙，因为<br/>
最开始只需要封锁敌对势力网站，<br/>
接着发现还要封锁提供翻墙软件登录敌对网站的网站，<br/>
后来连曝光封锁敌对势力网站和曝光封锁提供翻墙软件网站的网站都需要封锁，<br/>
随后连提供资源、提供平台的网站都被当作潜在的敌对势力需要封锁……<br/>
反正最后肯定是：只要不舔菊的都需要封锁。<br/>
<br/>
青萝卜：<br/>
自由在哪，GFW 就去哪，Google 到哪，GFW 也到哪。<br/>
GitHub 有无数个知名或不知名的翻墙工具，还有很多研究 GFW 的项目，加上近期 Google code 项目开始迁移到 GitHub，对于作恶多端的 GFW 来说，GitHub 就是眼中钉，肉中刺，不灭不消气。<br/>
<br/>
clowwindy：<br/>
今天是个值得纪念的日子，墙的角色已经不再只是一个保护主义的工具。<br/>
墨守于长城内几千年的伟大民族终于穿过长城走向世界，开始挑战西方价值和规则。<br/>
不管你是翻墙也好，肉翻也好，你都躲不开这个民族不断扩张的世界影响力。<br/>
中国第一份电子邮件里的那句话一语成谶。<br/>
<br/>
人生露点服务中心：<br/>
咦，这么来看，GFW已经成了码农界的ISIS了<br/>
<br/>
lovegoodbest：<br/>
HTTP 协议<br/>
#GFW 说：我们有能力让全世界范围内，访问了中国大陆网站的人（主要是海外华人），在不知情的情况下对全世界内任何网站发动 #DDOS 攻击。<br/>
HTTPS 协议<br/>
#GFW 说：我们有顶级CA可以签任意证书哦~~<br/>
<br/>
北风（温云超, Yunchao Wen）：<br/>
GFW劫持百度来攻击GITHUB，不过是提醒大家，访问中国网站，就有可能成为网络攻击的帮凶。<br/>
想不做帮凶，最好不要碰中国网站。<br/>
（利用JS在客户端执行的特性，让攻击显示来自四面八方，这种攻击真的很聪明，可惜当局的聪明都用在了这种无耻的地方。）<br/>
<br/>
28小盆友：<br/>
听说 GFW 对 GitHub 发动了 DDoS 核打击……<br/>
那也是，自从上次想封掉谁知引发激烈反弹后被迫解封，就一直耿耿于怀了吧？<br/>
<br/>
比特客栈的寻行数墨：<br/>
利用平民上网的正常流量进行DDoS已经成为中国全新的政治武器。<br/>
新的被害者是：GitHub。<br/>
换而言之，我们已经从Defensive变为Offensive了。<br/>
<br/>
东先生：<br/>
GFW调用民间流量攻击境外网站，这是挟持中国网民对抗整个文明世界，是一种流氓行径。<br/>
不是百度流氓，也不是GFW流氓，而是这个国家真的很流氓。 #你国<br/>
<br/>
lovegoodbest：<br/>
以前<br/>
“Across the Great Wall, we can reach every corner in the world”<br/>
现在<br/>
“Reinforcing the Great Wall, we can attack every corner in the world”<br/>
<br/>
Velaciela：<br/>
较量无声：全球最大成人搜索网站正在攻击全球最大同性交友网站<br/>
<br/>
zmt：<br/>
说句公道话，GFW的领导真的没兴趣ddos一个同性交友网站。<br/>
我觉得应该是GFW里的码农和github上的码农因基生恨，将怒火发泄在github上了。。。<br/>
归根到底，还是码农内部矛盾<br/>
<br/>
clowwindy：<br/>
GitHub 其实可以在这个弹框里写点吓人的话，对国内网站的声誉造成足够恶劣的影响和不可挽回的损失。<br/>
<br/>
nekoworkshop：<br/>
要我说github应该把那个alert换成：<br/>
“天灭共产党 退党保平安 1·发表三退声明的其他途径：(1)电子邮件: tuidang@epochtimes.com(2)美国热线电话:001-7…………”<br/>
#然后看好戏<br/>
<br/>
lovegoodbest：<br/>
话说如果现在 #Github 把那个alert信息改为google ads，那么它不就是可以坐着收钱了么....<br/>
<br/>
东哥：<br/>
github要不是alert，直接再重定向到我朝的任意一个gov站点，那会是什么效果？<br/>
<br/>
东哥：<br/>
这次对github的攻击刷新了肉鸡的概念，从此没人敢NB哄哄的说自己的电脑不可能成为肉鸡了。<br/>
<br/>
流觴：<br/>
看GFW这种二逼机制，以及国企式的维护水平，如果哪一天被牛逼黑客利用，搞出个全球网络大灾难来，千万不要奇怪。<br/>
GFW这次搞GitHub等于在全球程序员中给自己打了个广告，感觉丫正在慢慢走向那一步。<br/>
<br/>
Ukyoi (右京样一)：<br/>
GFW这次做得好下流……<br/>
千万别说是井外敌对势力故意栽赃陷害。<br/>
<center><img alt="不见图 请翻墙" src="images/cHr2Z8IdpMGPYgwsALs0r_DaCDMReeV2zvndMzYoXLm3Ctr11eJqiiwws6hzFjXqpQ1ezrXGtGI96EzmQ-A4M31M0OhtQNGuTwK17DsbMbyTp2f5xyKsmYWaFRnc7_ElhA9Um1i-TQ"/></center><br/>
Arctosia：<br/>
如果程序员不管在哪里工作都是所谓讨碗饭吃求生计，“只是执行命令而已”。<br/>
那这么有创意的手法，也一定是五六十岁的领导们想出来的了，绝对和程序员们没关系。<br/>
<br/>
小果汁：<br/>
被GFW刷屏从昨晚现在了…环境似乎越来越糟了呢。<br/>
我一直说，一个Google Scholar都打不开的国度，有什么资格谈学术？！<br/>
<br/>
老杨：<br/>
全世界程序员的切磋之地被我天朝端了，这算扬我国威壮我国魂么？<br/>
换一句话说，全世界程序员都没想出来怎么把墙搞死？<br/>
<br/>
Shell.E.Xu：<br/>
GFW的新思路看来是利用全中国人的流量在国外揍人。这样就算GFW不封你们，也没有啥外国网站敢放行中国IP了。。。<br/>
<br/>
<br/>
<h2>★关于“GitHub”的相关评论</h2><br/>
Shippo7：<br/>
这次gfw攻击github，最逗之处在于选择了一个程序员网站。<br/>
这相当于一个平时劫财劫色的猖狂流氓去武术学校里找教练打架，把全校师生都被吸引过来了。<br/>
就看github见招拆招从来没完全中断过服务，gfw有匕首没人能一下制服他，但是衣服已经被众人扒光了...<br/>
就看他是继续表演下去还是默默离开<br/>
<br/>
青萝卜：<br/>
这几天 GitHub 在其官网上不断公告受到超大流量的持续性 DDoS 攻击，但网站在数天内一直保持正常。<br/>
通过安全研究员 宫一鸣 提供的信息，这背后是一家名为 Prolexic 的公司帮助 GitHub 抵御 DDoS 攻击。<br/>
http://36kr.com/p/531307.html<br/>
<br/>
Get：<br/>
逼人删项目自我审查，干脆让github被封掉算了吧。<br/>
影响中国IT业的发展水平？切，老子现在才不关心这个！<br/>
翻个墙都搞不定说明缺乏做程序员好奇心，筛掉一大部分滥用者以及低水平码农，合格的程序员自然供不应求，工资水涨船高，这明显是好事。<br/>
<br/>
zmt：<br/>
要是封了github，下一届“国家自然科学一等奖”从哪抄？<br/>
<br/>
<br/>
<h2>★关于墙内那些“奇葩的程序员”</h2><br/>
（编程随想注：<br/>
咱们天朝有些奇葩的程序员。当 GitHub 被 GFW 骚扰了之后，他们不去责怪 GFW，却抱怨 GitHub 没有把那些“不和谐的内容”清理掉。<br/>
这就好比——有歹徒持刀行凶，不去责怪歹徒，反而去责怪那些卖刀的。<br/>
抱有这种观点的人，很多已经深陷于“斯德哥尔摩综合症”。如果你没听说过这种病症，请看俺之前的博文《<a href="http://program-think.blogspot.com/2012/06/stockholm-syndrome.html">天朝民众的心理分析：斯德哥尔摩综合症</a>》。）<br/>
<br/>
☂XiaoLan：<br/>
跪久了,站不起来了...<br/>
<center><img alt="不见图 请翻墙" src="images/pwpHvXubSzAl0dHRaNksuZogRgV1FRAi1v234aBB_JtnXVMJrSk2CcVV3JxcllyXZHrPj2-5zutOvdW_r61RbUrxhFezp4aaVuZoTtkN1U2dgorDiT97HADhZSwnNQSRLuXqpjTm8g"/></center>（编程随想注：上述这些，就是墙内奇葩程序员在 GitHub 上的留言，要求 GreatFire 撤出 GitHub）<br/>
<br/>
青萝卜：<br/>
GitHub 被攻击，<br/>
网络墙国的程序员说 @GreatFireChina 在作恶。<br/>
来自自由世界的程序员说 CNGov 在作恶。<br/>
同一个计算机世界，不同的程序员。<br/>
<br/>
（匿名网友）：<br/>
这是光明程序员和黑暗程序员的斗争！<br/>
<br/>
Chunlin Zhang：<br/>
你们觉得那些技术人员无骨，他们觉得"扬我国威！"<br/>
大家思考的基准根本就不一样。<br/>
//China's national firewall hijacks JavaScript to DDoS GitHub - Slashdot http://t.cn/RAy86Fu<br/>
<br/>
Jian Alan Huang：<br/>
你国的程序员长期以来一直以技术小清新居多，不过最近几年确实有很大长进。<br/>
标榜自己技术中立、不碰政治、不反共的，以前很常见，现在基本上已经属于恐龙了。<br/>
没办法，都是被逼的，每天上网都被政治糊一脸屎，再怎么装小清新都是要爆发的。<br/>
在残酷的现实面前，任何启蒙都是多余的！<br/>
<br/>
Hsiaoming Yang：<br/>
每次发生什么网站被封，就会有一大群国人跑过去让别人删内容，仿佛接到了省政府新闻办的删帖令。<br/>
你们什么时候才能醒悟，作恶的是你们政府，而不是几篇文章几个项目。<br/>
而且你永远也抓不住政府的G点，你以为删掉这删掉那就没事了？想的美。<br/>
<br/>
qubicllj：<br/>
GitHub用戶taogogo（bio顯示為百度職員）發文讓Greatefire項目離開Github，這個國家沒有救<br/>
（编程随想注：这位taogogo用户，不光“自我阉割”，还想让别人也“自我阉割”）<br/>
<br/>
御宅暴君：<br/>
谁说 GitHub 本身就不适合 GreatFire 这「政治组织」活动？<br/>
GitHub 来打你们脸了：https://government.github.com/<br/>
别国政府都用 GitHub 为公民服务了，中国政府就会 DDoS; 更还有人作伥地叫 GreatFire 滚。<br/>
差距令人悲哀！<br/>
<br/>
御宅暴君：<br/>
@akar1nchan 前几天有个新闻，某男性强暴了女性，还振振有词地说，要怪就怪她「晚上乱外出」。你这归因法和他一致。<br/>
什么叫晚上外出？现代公民天生就应该有在公共场所活动的自由，并享有人身安全受到保障的权利。<br/>
同理，GitHub 的 ToS 上也没有禁止 GreatFire.<br/>
<br/>
土木坛子：<br/>
知乎的自我阉割是不是越来越厉害了？——<br/>
如何评价百度广告代码和统计代码被劫持攻击GitHub 的事件<br/>
https://www.zhihu.com/question/29086378<br/>
<br/>
<br/>
<h2>★又见“真理部”</h2><br/>
数字时代“真理部指令”项目：<br/>
[真理部指令]<br/>
Github遭遇大规模ddos攻击: 对Github遭遇大规模ddos攻击一事，在权威媒体没有报道之前不要自行揣测和评论，也不要转载境外信息。<br/>
http://bit.ly/1MiaNAg  [中国数字时代]<br/>
<br/>
陈少举：<br/>
@CasperYang 如何评价知乎删除《如何评价知乎删除《如何评价知乎删除《如何评价知乎删除《如何评价知乎删除《如何评价知乎删除《如何评价知乎删除《如何评价知乎删除《如何评价知乎删除《如何评价知乎删除百度统计代码被用于攻击GitHub的事件？》》》》》》》》》<br/>
<br/>
<br/>
<h2>★关于“习包子”的调侃</h2><br/>
无名☂：<br/>
刁呆呆：“中国一不输出革命，二不输出饥饿和贫困，三不去折腾你们，还有什么好说的。”<br/>
话音刚落，GFW分分钟扇刁呆呆的老肉脸。<br/>
<br/>
Jian Alan Huang：<br/>
小组长上台以后，尽管网络管制思路跟之前一致，但路子毕竟野了很多。<br/>
CNNIC颁发官方假证书进行中间人攻击、GFW劫持全球网络流量发动DDoS攻击、强调网络主权等等的事...<br/>
如果从积极方面看的话，那就是在当局看来，单纯的砌墙防御已经不够用了，翻墙途经越来越多，不主动出击就是等死。<br/>
<br/>
<br/>
<h2>★关于“天朝外交部的回应”</h2><br/>
（编程随想注：就在昨天，朝廷外交部已经郑重声明，彻底撇清和此次事件的关系。对这种耍赖，俺毫不意外。）<br/>
<br/>
Kgen Bao：<br/>
外叫部否认攻击 Github 了，其实这种掩饰毫无意义。<br/>
因为能在中国网络出入口处，劫持百度的JS脚本的，除了墙，还有谁呢？<br/>
可是中国说自己没有墙的，要是承认了这次攻击，就等于承认了墙的存在。<br/>
所以撒了一个谎，就要用另一个谎来圆场，发炎人不好当。<br/>
<br/>
九条凛：<br/>
為什麼中國政府能一邊聲稱自己是網路犯罪受害國，在外交部發言中否認一切攻擊的行為。<br/>
然後還一邊明目張膽肆無忌憚的進行偽造證書，中間人攻擊竊取國民資料，DDoS攻擊他國的行為。<br/>
因為謊言是專制政權的根基，這和宇宙真理邪教的本質是一脈相承的。<br/>
<br/>
<br/>
<h2>★其它的一些评论</h2><br/>
比特客栈的寻行数墨：<br/>
Github DDoS进入第三天（超过72小时），已不对Github服务造成多大影响。<br/>
我不知道GFW的人作何感想。他们只剩下砍掉Github这个选项。<br/>
但正如中国政治：一刀切，恰恰体现了管理者的愚昧和失败。<br/>
<br/>
Eric Xu, PhD (徐宥)：<br/>
号召大家趁这个机会花点钱买 GitHub 的服务。你交给流氓政府的每一块钱税都可能成为攻击人类文明的子弹。<br/>
<br/>
九条凛：<br/>
你國建GFW和搞DDoS都是用納稅人的錢唉，人民不投票也就罷了，人大代表也沒舉手表決一下就開搞了嗎？<br/>
<br/>
heely：<br/>
别一惊一乍的，或许是我党想考验一下网络作战部队的真实水准，于是某领导在喝醉了之后，对部下悄悄说了一番话。<br/>
拿Github练练手而已，主要目的是为了进一步防止美帝窥探我国网络隐私而采取的演习。<br/>
<br/>
*っぽい*：<br/>
我国仍处于并将长期处于社会主义初级阶段，我们现阶段所面临的主要矛盾是：<br/>
人民日益增长的智商同落后的洗脑教材之间的矛盾。<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
<a href="../../2013/02/weekly-share-39.md">每周转载：关于 GitHub 和 GFW 的 PK（第1季）</a><br/>
<a href="../../2014/12/weekly-share-78.md">每周转载：关于“Gmail 彻底被墙”的网友评论</a><br/>
<a href="../../2012/06/stockholm-syndrome.md">天朝民众的心理分析：斯德哥尔摩综合症</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2015/03/weekly-share-82.html
