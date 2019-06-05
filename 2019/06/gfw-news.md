# 2019年6月翻墙快报（兼谈用 I2P 突破封锁） 

-----

<div class="post-body entry-content">
　　很久没有发过《翻墙快报》了。前一篇还是在“十九大期间”（2017年10月）。<br/>
　　最近几年，翻墙工具越来越多，翻墙也越来越方便，所以《翻墙快报》的“需求量”和“必要性”也下降了。<br/>
　　这次是因为赶上了“六四事件30周年”，看到很多读者在抱怨，所以特地再发一篇。<br/>
<a name="more"></a><br/>
<br/>
<h2>★近期翻墙动态</h2><br/>
　　最近一段时间（尤其是6月的开头几天），一些翻墙工具纷纷失效。<br/>
　　这其实是意料之中。<br/>
　　在上个月（5月份）的几篇博文中，俺不止一次警告过大伙儿：六四事件30周年，GFW 肯定会发飙，请读者们提前做好准备。<br/>
　　有经验的读者，看了俺的警告之后，应该提前安装好 I2P，然后做好【补种】，并在接下来这段时间，偶尔让 I2P 运行一下，以确保其始终【可用】。（注：时常运行 I2P，以确保它始终保存了【新鲜的】P2P 节点信息）。<br/>
　　为啥俺特别强调 I2P 捏？根据最近十年的经验，I2P 的坚挺程度始终令人放心。所以在封锁很严重的时期，手头备一个【可用的】I2P，可以用来【应急】。<br/>
<br/>
　　上述这些经验之谈，俺已经唠叨过多次了，包括<a href="../../2017/10/gfw-news.md">上一篇《翻墙快报》</a>也提到过。可惜很多读者不太愿意去翻看旧博文，害得俺又要重复一遍。<br/>
<br/>
<br/>
<h2>★常见翻墙工具的状况</h2><br/>
　　俺测试了几款常用翻墙工具，把情况分享给大伙儿。<br/>
　　<b>先提醒一下：</b>根据这几年的经验，不同省份或者不同 ISP，翻墙工具的效果可能会有差异。所以俺个人的测试，仅供参考。<br/>
　　由于存在上述差异，所以也欢迎列位看官在博客留言，反馈自己的翻墙情况。<br/>
　　<a href="../../2019/05/share-books.md">【前一篇】博文</a>已经有很多读者反馈了自己的翻墙情况，俺也挑选了一些，转贴在下面（按照翻墙工具归类）。<br/>
<br/>
<h3>◇Tor + meek</h3><br/>
　　Tor 在多年前就被 GFW 封杀了（GFW 屏蔽了全球的 Tor 中继节点和网桥）。后来（2014）Tor 官方提供了一个 meek 插件，可以让 Tor 客户端通过墙外的云计算平台，间接地连入 Tor 网络。<br/>
<br/>
　　根据俺的测试，“Tor + meek”的方式【依然可用】，但速度比5月份慢很多。而且俺观察到针对 meek 的 HTTPS 连接的干扰。干扰有两种：<br/>
其一是，启动 Tor 后，meek 的初始连接就连不上。<br/>
其二是，连接一段时间后突然断线（6月之前，meek 的连接很稳定，没有出现频繁断线）<br/>
　　如果你碰到第一种情况（初始连接就失败了），可以尝试【切换一下自己的公网 IP】，然后再重试，【运气好的话】就又能联网了。<br/>
　　（对于家用宽带，只需要关闭一下宽带拨号设备，隔一会儿再开，就可以切换自己的“公网 IP”）<br/>
<br/>
　　关于 Tor + Meek 的使用教程，请参见：《<a href="../../2018/04/gfw-tor-browser-7.5-meek.md">“如何翻墙”系列：扫盲 Tor Browser 7.5——关于 meek 插件的配置、优化、原理</a>》<br/>
<br/>
　　<b>以下是热心读者的反馈：</b><br/>
<br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
问题1：你的 Tor 是否用了 meek 插件？是否走微软的云平台？<br/>
是的，用了meek插件，走了微软的云平台。<br/>
速度还可以，要等一会，浏览网页没问题，不看视频的话。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
为何微软如此牛逼？在谷歌和亚马逊纷纷屈服于俄罗斯压力而禁止域名前置以后，微软Azure云坚挺至今，任然允许域名前置（从而保证meek可以继续正常运作）。<br/>
微软真实太牛逼了！在这里不得不为微软严重滴点个赞！！！</blockquote><br/>
<h3>◇I2P</h3><br/>
　　从来没用过 I2P 的同学，请先看这篇《<a href="../../2012/06/gfw-i2p.md">简单扫盲 I2P 的使用</a>》。<br/>
　　（对 I2P 的夸奖，前面已经说过，此处不再重复）<br/>
　　经俺本人测试，I2P 一直可用！<br/>
<br/>
　　<b>提醒一下：</b><br/>
　　有些同学的 I2P 已经联网成功，但却无法通过 I2P 翻墙，可能有以下几个原因：<br/>
1. 上网软件的代理设置有误（I2P 对“HTTP 代理”和“HTTPS 代理”提供两个不同端口；在浏览器的界面上要分开设置）<br/>
2. I2P 要运行一段时间之后，获取了足够多节点信息，才能建立“本地隧道”（local tunnel）。你的浏览器才能通过 I2P 的“local tunnel”翻墙。<br/>
<br/>
　　I2P 虽然坚挺，但是【速度慢】。所以它适合于：<b>在其它翻墙工具都失效的情况下，进行应急。</b><br/>
　　如果你是【第一次】运行 I2P，需要先进行【补种】（洋文叫做“reseed”）。补种之后，I2P 才能够接入 P2P 网络。现在封锁很严重，【如何补种】是一门艺术。本文后续有一个章节专门聊“补种”的话题。<br/>
<br/>
<br/>
<h3>◇无界</h3><br/>
　　经俺本人测试，无界最新的 19.02 版本还可以用，但要很久才能连通。<br/>
　　有些读者反馈说无界“完全正常”，还有些读者反馈说无界“完全失效”。这就是前面提到的“地区差异”或“运营商差异”导致的。<br/>
<br/>
　　<b>以下是热心读者的反馈：</b><br/>
<br/>
<blockquote style="background-color:#DDD;">三二一：<br/>
我反馈一下，我发现一件很有趣的事，白天翻墙比较容易，晚上就难得多了。<br/>
然后我平常用的赛风，蓝灯，现在已经不怎么好用了，我改用vpngate，无界，三月，四月翻墙比较难，到了5月，容易了不少，不知道是不是因为换了翻墙软件，<br/>
现在主要用无界，奇葩的是三月时还连不上，五月直接可以看视频了，无语。绝妙的感觉。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
赛风、vpngate、蓝灯、ssr统统挂了。抱着死马当活马治的态度，试了一下无界。乖乖。。好顺畅啊。。哈哈。</blockquote><br/>
<blockquote style="background-color:#DDD;">金三胖得了精神病：<br/>
反馈 南方某地 （俺的坐标）6.5<br/>
1赛风、蓝灯、自由门基本废了 vpngate几年前就死透了<br/>
2tor加meek绝大部分时间失效 I2P间歇性抽风<br/>
3无界过一段时间需要重启一次  算是唯一一个还凑合的<br/>
4无界似乎在所有插件不启动的无痕模式中比在普通模式中稳定</blockquote><br/>
<blockquote style="background-color:#DDD;">正經拆尼斯：<br/>
東北地區，無界進入六月後速度下降，而且需要間歇地重連服務器，不然就撲街。<br/>
自由瀏覽APP不受影響，然而是手機端。</blockquote><br/>
<h3>◇VPN Gate</h3><br/>
　　经俺本人测试，最近一段时间，VPN gate 的“server list”总是无法刷新。<br/>
　　为了判断它是否完全失效，俺特意去看了 <a href="https://www.vpngate.net/" rel="nofollow" target="_blank">VPN gate 的官网</a>。发现天朝（china）在“国别排名”中排在【第5名】。排名虽然下降了，但 china 的总流量（截止俺写本文时）【每分钟】都在增加，这说明：某些地区还是可以用 VPNgate。<br/>
<br/>
　　<b>刷新“server list”的【技巧】</b><br/>
　　由于 VPN gate 的客户端软件，可以使用别的翻墙工具作为【前置代理】。因此，你可以用另一个【可用】的翻墙工具（比如 I2P）【临时】辅助 VPN gate 刷新“server list”。等到“server list”刷新完之后，再把 VPN gate 客户端的“前置代理”【去掉】。<br/>
<br/>
<br/>
<h3>◇自由门</h3><br/>
　　很多读者抱怨自由门最新的 7.6.7 版本已经失效了；但某些读者表示：自由门依然可用。<br/>
<br/>
　　<b>以下是热心读者的反馈：</b><br/>
<br/>
<blockquote style="background-color:#DDD;">土豆妮：<br/>
感叹一下，自由门真是稳定，在一众梯子倒下的时候，竟然仍然屹立不倒。<br/>
同时也很后怕，同时准备这么多翻墙方式避免单点故障，几乎已经是普通人的极限，但是这一次仍然被打击到只剩下一种方式，这意味着自由门已经成为未来的单点故障。</blockquote><br/>
<h3>◇蓝灯（lantern）</h3><br/>
　　在前两年，据说蓝灯用了【阿里云】来提供翻墙服务。考虑到俺本人是【高危人士】，为了保险起见，俺后来就没再它翻墙了。所以这次也没有亲自测试它。<br/>
　　从其它人的反馈来看，蓝灯应该失效了。<br/>
<br/>
　　<b>以下是热心读者的反馈：</b><br/>
<br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
蓝灯付费版本,在6月3号,4号不能使用.5号恢复正常.<br/>
蓝灯付费版本.用来好几个月,大部分时间可用.应该说还是比较满意的.</blockquote><br/>
<blockquote style="background-color:#DDD;">土豆妮：<br/>
同意39单元反馈的“有趣的事”，白天翻墙更容易，晚上难得多。<br/>
具体表现为，能用的SS和自由门在晚上变慢，不能用的蓝灯在白天偶尔能够连上。</blockquote><br/>
<h3>◇赛风（psiphon）</h3><br/>
　　最近两年，赛风很疲软，所以俺对它没抱啥希望。<br/>
　　在俺的环境中，它在5月份就不行了。<br/>
<br/>
　　<b>以下是热心读者的反馈：</b><br/>
<br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
赛风五月大部分时间连上就断，五月末至今变得稳定、快速(昨天竟然没有断过连接)。<br/>
我发现一个规律，在凌晨x点后，GFW就不会抽风断你连接。</blockquote><br/>
<h3>◇SS（ShadowSocks）及其衍生工具 SSR</h3><br/>
　　俺一直没有购买 VPS 用于翻墙，所以就没法亲自测试 SS 的情况。<br/>
　　（注：基于【隐匿性】的考虑，俺尽量避免各种在线支付）<br/>
<br/>
　　<b>以下是热心读者的反馈：</b><br/>
<br/>
<blockquote style="background-color:#DDD;">九头鸟：<br/>
shadowsocks最近好像彻底没法用了，基本上只要试图连接就会被以秒级的速度检出并切断。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
我的搬瓦工VPS在6月1号被封锁IP，于是启用另外一个备用的（其他VPS提供商），结果在6月2号也被封锁IP。<br/>
两个VPS上面安装的都是shadowsocks，我第二个帐号最近2个月没有使用，刚一使用第二天就被封锁了。<br/>
还好第二个帐号可以更换IP地址，换了IP地址后就就正常了，但是也不太稳定。现在都不敢24小时运行了，需要的时候才连一下，有时候半天也连接不上，但是不显示timeout。<br/>
<br/>
我用shaodowsocks已经3年多了，还没遇到过这样严重的情况，看来六四事件30周年真不是开玩笑的。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
给大家反馈一下我的情况。<br/>
<br/>
看了22单元网友回复，我查了CDN翻墙，发现比较适合我这种情况（我的搬瓦工VPS因为使用SS被封锁了IP）。我采用了Goflyway+CDN的方式成功续命，现在看速度没有下降很多，是否稳定还有待观察。<br/>
<br/>
我另外一个SS架设在AWS上面，这两天也是经常被封，还好AWS可以使用弹性IP（Elastic IP），可以更换IP地址，但也是坚持不了一会就会被封。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
TO ALL<br/>
裸SS【不能】再用了！！！必须把裸SS封装在HTTPS加密通讯管道了。选用一个不被墙知道的SNI域名！</blockquote><br/>
<blockquote style="background-color:#DDD;">土豆妮：<br/>
借楼分享一下我这边的翻墙情况。北方某城市，联通。<br/>
<br/>
平常用自己在谷歌云搭建的Shadowsocks和锐速加速，没有用混淆插件。只有两三个亲友用，半年来断过一次，换端口解决了。同时有蓝灯专业版、自由门、Tor作为备用。<br/>
<br/>
6月2日发现SS、Tor、蓝灯都失效。自由门7.66、7.67均有效。手机端安卓的自由浏览有效，但手机端浏览器无法用来开发新梯子，因此没有太大的帮助。<br/>
<br/>
尤其与以前不同的是，这次SS的出错方式，我以前没有见过————<br/>
--PAC模式下，墙内能正常浏览，墙外无法连接。<br/>
--log没有显示超时。<br/>
--可以ping通服务器IP.<br/>
--tracert IP有严重延迟，但也是通的。<br/>
--用在线工具检查IP地址，显示国内国外的ICMP和TCP都是通的（技术小白，照猫画虎地排查，其实并不太明白这意味着什么）。<br/>
--设法临时翻墙后在谷歌云检查服务器登录历史，并没有其他用户登录的记录。<br/>
<br/>
另外，我看到谷歌服务宕机的新闻，但据新闻报道，受影响的服务主要在北美和欧洲部分地区。那么亚洲机房并不应该受影响，而且即使受到宕机影响，也应该在谷歌修复后恢复正常。<br/>
<br/>
今天（6月4日）刚刚趁翻墙稳定一会儿，登上谷歌云换了端口，可以重新翻墙了。<br/>
同时建了一个新的SS服务器，用了一键部署的BBR魔改加速，加了simple-obfs混淆插件，安装fail2ban保护服务器（摸着石头过河，也不知道设置的会不会有啥问题）。作为备用。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
强烈建议把ss封装在HTTPS的加密通信道里使用。</blockquote><br/>
<blockquote style="background-color:#DDD;">（编程随想注：这条是对上一条留言的补充说明）<br/>
匿名：<br/>
现在的墙草木皆兵，如果看到你发起的TCP连接用的不是HTTPS协议，就会封杀连接。所以你翻墙建立的连接必须是使用HTTPS为协议的。<br/>
【但是】（我要说【但是】了）用HTTPS建立起来的加密信道【里面】输送的内容【不一定】是HTTP，可以是Tor、SS、SSR、V2Ray、BTSync。<br/>
但是这些不同的协议一经HTTPS加密就都变的一样了，墙无法识别出来。如果你想象HTTPS是一个管道，这个管道外表写着“我是HTTPS”，但是这个管道里面流的水不一定是HTTPS，可能是如Tor、SS、SSR、V2Ray、BTSync。但是这些水都在HTTPS这跟管道里流，管道外面（墙）看不到管道里流的是什么水，所以只能让水流出墙。也就是说水在管道的保护下流出墙。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
自用的两个Virmach垃圾vps，位置是水牛城和洛杉矶，都配置了v2ray，用的ws+tls+web的配置，一直很稳。另外有用搬瓦工的官方机场JMS，仅用于家人晚高峰看4K视频，6月1日中午的时候测试了一下掉线了，晚上使用的时候又正常了，到现在都一直很稳。不懂技术，不清楚是否针对SS或SSR，但是大家讨论的时候没有没考虑过幸存者偏差，毕竟SS系的VPS翻墙工具在机场的推广下，现在是主流，跑流量也大，被封的时候SS系死得多也很正常。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
说一下我这里的情况，华北地区某城市，联通，ssr和Vray一直能正常使用，IP也没有被封，可能与我一直配合tor使用有关。传输速率和平常一样，昨晚看香港六四纪念活动的直播没有一点压力。</blockquote><br/>
<h3>◇V2Ray</h3><br/>
　　V2Ray 依赖于 VPS，基于前面提到原因，俺没有尝试过“基于 VPS 的翻墙”，因此也就没有亲自测试 V2Ray 的情况。<br/>
<br/>
　　<b>以下是热心读者的反馈：</b><br/>
<br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
我的经验是，除非使用CDN，否则不要用V2Ray的Vmess协议。我在两台电脑上测试Vmess协议，第一次连通了，不过大约几分钟之后就会达到100%的丢包率。换成shadowsocks之后丢包率下降到了10%（这个是正常值）。然后我重复实验，又换到Vmess协议，又是丢包100%（这里的丢包是指所有数据包，不仅仅包含由V2Ray发送的数据包；意思就是说其他不走翻墙软件的包也会被丢弃）<br/>
<br/>
至于CDN翻墙，据我所知，GFW本身看不到你在使用Vmess协议，GFW只能看到的是由CDN颁发的HTTPS证书下的加密流量。理论上换其他协议也行，不过我没有试过。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
vmess协议设计上没看出有什么大问题，和shadowsocks（增加AEAD之后）一样都是预享密钥，不需要握手过程，协议header本身不可识别（除非检测流量特征），在GFW看来就是未知应用层协议的tcp/udp（如果你用kcp）包</blockquote><br/>
<blockquote style="background-color:#DDD;">（编程随想注：这条是回复上一条）<br/>
匿名：<br/>
关键问题就在这儿：现在墙是草木皆兵了，墙会封杀【所有】未知应用层协议的tcp/udp包。当今墙【只】放行HTTPS连接，而且还得要是那种IP和SNI均未被封杀的HTTPS连接。（DNS污染可以依靠HOSTS修改解决）。</blockquote><br/>
<blockquote style="background-color:#DDD;">Unknown：<br/>
我用自建V2ray翻墙，kcp传输协议。今日两个节点都被强，好伤心。直接封了Ip,我现在用SSH都远程登不了主机</blockquote><br/>
<blockquote style="background-color:#DDD;">Len Kagamine：<br/>
1. 坏消息：6月5日中午，移动宽带，包括I2P、赛风、V2Ray(mKCP, ws+TLS)的翻墙手段全部失效:(<br/>
2. 同一时间段，V2Ray(ws+TLS)在中国电信正常工作。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
敏感时期，除了用WS+tls套CDN加速防封VPS的IP强力翻墙方式之外，取消HTTP及HTTPS混淆也是一个很好的办法，这些混淆还是有一些流量指纹的，容易被DPI检查出来，<br/>
最后一定得启用AEAD加密算法，这是关键中的关键。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
南方城市，电信和联通目前都很稳。v2ray采用的是ws+tls+web+cdn的方式。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
V2ray非常稳啊就，ss这次是真滴不行了</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
V2Ray用ws+TLS+nginx完全无压力，没有用cdn中转</blockquote><br/>
<h3>◇关于 VPS（Virtual Private Server）的补充说明</h3><br/>
　　除了 SS，还有其它一些翻墙方法（比如自建 SSH）也依赖 VPS，所以再顺便提一下 VPS。<br/>
　　每当 GFW 加强封锁，都会把很多 VPS 提供商的【整个网段】屏蔽掉。（按照以往经验）名气越大的提供商，被封杀的可能性越大。<br/>
　　假如你付费的 VPS 提供商，其网段已经被 GFW 加入“IP 黑名单”，那你的 VPS 就废了（无论怎么折腾都没戏）。<br/>
<br/>
　　<b>以下是热心读者的反馈：</b><br/>
<br/>
<blockquote style="background-color:#DDD;">copycat：<br/>
博主<br/>
昨天vultr等vps的ip一批批都挂了……几乎什么翻墙工具都不能用了……我用了一个不知名的vpn才翻到这里</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
其实如果自己使用国外云的话，有大把的选择：Cloudflare，AWS，Azure，Akamai，Citrix，IBM，HP，甲骨文。虽然最近很多云都禁止了域名前置，但是请注意如果是自己使用的私家梯子，则不需要搞域名前置，因为墙是不会知道私家梯子使用的域名的。当然，如果使用私家梯子，则必须注意：<br/>
1.不要告诉别人自己的私家梯子在云上所使用的SNI域名。<br/>
2.不要用私家梯子看YouTube等容易产生引起墙的注意的流量的活动。</blockquote><br/>
<h3>◇读者的其它反馈</h3><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
白天 Psiphon、自由門、無界三款老牌的工具都可以用，晚上干擾比較明顯，但總有一兩款可以用。我的使用經驗，一次啟動所有翻牆工具比單獨啟動有更高的成功率。用 Tor over proxy 比單獨 proxy 效果更好。</blockquote><br/>
<blockquote style="background-color:#DDD;">卢比扬卡大酒店：<br/>
使用OpenVPN协议的传统VPN（如世界第一的ExpressVPN）毫无疑问地被GFW干烂了，因为OpenVPN不是用来隐藏流量的。<br/>
本人使用的12VPN支持WEB/Shadowsocks/V2Ray/Wireguard等多种可隐藏流量的协议，应对六四这波封锁稳如狗。<br/>
各位一定要买支持新型协议的VPN服务，不建议自己用VPS搭，一旦封了IP段就会束手无策。</blockquote><br/>
<blockquote style="background-color:#DDD;">匿名：<br/>
请博主把这个工具补录进去吧，trojan-gfw，开源页面在这里：https://github.com/trojan-gfw/trojan<br/>
它是完全模拟HTTPS客户端的，现在用的人很少，但是在这一波封杀里面很稳的活着。</blockquote><br/>
<blockquote style="background-color:#DDD;">Unknown：<br/>
IPv6无所畏惧</blockquote><br/>
<h2>★非常时期，关于翻墙的注意事项</h2><br/>
　　下面是一些经验介绍，供大伙儿参考。<br/>
<br/>
<h3>◇【不要】在一棵树上吊死</h3><br/>
　　在严重封锁的非常时期，你手头要多准备几个翻墙的梯子。<br/>
　　有些缺乏经验的同学只依赖一个梯子，万一这个仅有的梯子失效了，就傻眼了。<br/>
<br/>
<h3>◇确保有一个【可用的】I2P（“补种”的几个招数）</h3><br/>
　　考虑到 I2P 比较坚挺，可以在非常时期用来【救急】。当 GFW 加大封锁导致很多翻墙工具失效，这些翻墙工具也会更频繁地发布新版本，尝试突破封锁。而 I2P 的【救急】作用就体现在——用来下载其它翻墙工具的新版本。<br/>
　　如果你是第一次运行 I2P，或者你很久没有运行 I2P，要先进行【补种】。I2P 的补种大致有三招，分别如下：<br/>
<br/>
　　<b>第1招：用其它翻墙工具给 I2P 补种</b><br/>
　　I2P 内置了一批“补种服务器”（洋文叫“reseed server”）。很显然，这些“补种服务器”早就被 GFW 封杀了。要想通过这些“种子服务器”进行补种，需要让 I2P 通过其它翻墙工具联网。假如你手头有其它的翻墙工具，【并且还能用】，赶紧用这个工具给 I2P 补种。<br/>
　　启动 I2P 之后，用浏览器中访问如下网址，就可以进入【I2P 的补种界面】。<br/>
<pre style="background-color:#DDD;">http://127.0.0.1:7657/configreseed</pre>　　在这个界面上勾选“Enable HTTP Proxy”，并填写相应的“Proxy Host”和“Proxy Port”（具体填啥，取决于另一个翻墙工具提供的代理）。填写完记得点保存按钮，然后 I2P 就可以通过其它翻墙工具联网并补种。<br/>
　　补种完成之后，当 I2P 已经找到其它节点（界面上的 Peers 大于零），你就可以把“Enable HTTP Proxy”选项去掉——让 I2P【独立联网】。<br/>
<br/>
　　<b>第2招：找其它人帮忙获取 I2P 的【种子文件】</b><br/>
　　假设你有一个朋友手头有【可用的】I2P，那么你让这个朋友生成 I2P 的种子文件，并把种子文件发给你；然后你在自己的 I2P 补种界面上，导入这个种子文件，就可以成功补种。<br/>
　　【生成种子文件】的方法如下：<br/>
　　进入“I2P 的补种界面”，界面上有一项是【Create reseed file】。如果 I2P 已经联网，就可以通过这个功能，创建一个种子文件（文件中会包含可用的 I2P 节点的信息）。这个种子文件可以分享给其他 I2P 的使用者。<br/>
　　【导入种子文件】的方法如下：<br/>
　　进入“I2P 的补种界面”，界面上有一项是【Reseed from file】，用来导入种子文件。只要导入的种子文件【足够新鲜】，就可以让无法联网的 I2P 重新联网。<br/>
<br/>
　　补充说明：<br/>
　　种子文件是有【时效性】滴。越久以前创建的种子文件，时效性越差。因为 I2P 网络的节点是在不断变化的——很早以前创建的种子文件，其中包含的节点信息可能已经过时了。一般来说，一两天之内的种子文件，是“新鲜”的；而超过一周的种子文件，就“不新鲜”了。<br/>
<br/>
　　<b>第3招：通过 BT sync（Resilio Sync）获得 I2P 的【种子文件】</b><br/>
　　如果你既没有其它可用的翻墙工具，也没有其它朋友可以帮你生成种子文件，那么你还有第三个选择——利用俺提供的 BTsync（Resilio Sync）网盘获取种子文件。<br/>
　　熟悉俺博客的读者应该都知道：俺提供了一个 BTsync 网盘用来分享翻墙工具。该网盘的【同步密钥】如下：<br/>
<pre style="background-color:#DDD;">BTLZ4A4UD3PEWKPLLWEOKH3W7OQJKFPLG</pre>　　俺已经在这个网盘上放了 I2P 的【安装包】（位于 <code>I2P</code> 目录下），还放了若干“种子文件”（位于 <code>I2P</code> 目录下的 <code>seeds</code> 子目录）。<br/>
　　在翻墙困难的时期，俺会尽量多更新网盘上的这批种子文件。就在昨天（6月4日），俺刚更新了一批种子。<br/>
<br/>
　　补充说明：<br/>
　　如果俺从自己的 I2P 界面上创建种子文件，这些种子文件可能会包含一些跟俺本人的网络环境相关的信息。<br/>
　　所以，【为了保护自己的隐匿性】，俺分享的“种子文件”是从一些【公开的】“补种服务器”下载的。为了确保种子文件的可靠性，俺使用了 I2P 界面【内置的】“补种服务器”（在“I2P 补种界面”上有这些 server 的列表）。<br/>
<br/>
<h3>◇经常运行 I2P 和 BTsync</h3><br/>
　　I2P 和 BT sync（Resilio Sync）都是基于 Kad（Kademlia）技术进行 P2P 联网。它们的客户端会缓存当前联网的节点信息。如果你只是【短暂关闭】它们的客户端，下次运行时，它们的客户端依然可以根据缓存的节点信息，找到互联网上的其它节点，于是就可以正常联网。<br/>
　　但如果你【长时间没有运行】I2P 或 BTsync，那么它们客户端缓存的节点信息就过时了（不够新鲜了），于是下次再运行时，客户端就找不到其它节点。这种情况下，就需要【重新补种】！<br/>
　　那么，怎样才算【长时间不运行】？根据经验，超过一周就算“长时间”。为了保险起见，至少一两天就得运行一次，以便让 I2P 或 BTsync 的客户端更新 P2P 网络的节点信息。如果有条件的话，可以让 I2P 或 BTsync 的客户端一直开着。<br/>
<br/>
<h3>◇电脑上保留一份【本博客的离线浏览】</h3><br/>
　　多年前，俺就通过 BT sync 网盘分享博客的离线浏览。<br/>
　　在封锁很严重的时期，如果你手头保留一份【博客的离线浏览】，那么你【无需联网】就可以看俺写的那些【翻墙教程】。<br/>
　　要获取【本博客的离线浏览】，请使用如下【同步密钥】：<br/>
<pre style="background-color:#DDD;">B7P64IMWOCXWEYOXIMBX6HN5MHEULFS4V</pre><br/>
<br/>
<h2>★翻墙教程汇总</h2><br/>
　　下面这些教程都在俺博客上（需翻墙）。<br/>
　　再次唠叨：如果你已经用 BT sync（Resilio Sync）自动同步了【本博客的离线浏览】，无需联网就可以看这些教程。<br/>
<br/>
<h3>◇基础教程</h3><br/>
<a href="../../2009/05/how-to-break-through-gfw.md">如何翻墙</a>（这是全方位扫盲介绍，写给新手的入门教程）<br/>
<a href="../../2011/03/how-to-get-gfw-tools.md">获取翻墙软件方法大全</a>（教你在无法翻墙的情况下拿到翻墙软件）<br/>
<a href="../../2013/01/cross-host-use-gfw-tool.md">多台电脑如何【共享】翻墙通道——兼谈【端口转发】的几种方法</a><br/>
<a href="../../2019/04/Proxy-Tricks.md">如何让【不支持】代理的网络软件，通过代理进行联网（不同平台的 N 种方法）</a><br/>
<a href="../../2017/08/GFW-Resilio-Sync.md">聊聊 GFW 如何封杀 Resilio Sync（BTSync）？以及如何【免翻墙】继续使用？</a><br/>
<a href="../../2015/01/BitTorrent-Sync.md">扫盲 BT Sync——不仅是同步利器，而且是【分布式】网盘</a><br/>
<br/>
<h3>◇各种翻墙软件使用教程</h3><br/>
<a href="../../2012/06/gfw-i2p.md">简单扫盲 I2P 的使用</a><br/>
<a href="../../2013/11/tor-faq.md">关于 TOR 的常见问题解答</a><br/>
<a href="../../2013/04/gfw-vpngate.md">扫盲 VPN Gate——分布式的 VPN 服务器</a><br/>
<a href="../../2011/12/gfw-wujie.md">新版本无界——赛风3失效后的另一个选择</a><br/>
<a href="../../2011/10/gfw-psiphon.md">双管齐下的赛风3</a><br/>
<a href="../../2014/10/gfw-tor-meek.md">“如何翻墙”系列：TOR 已复活——meek 流量混淆插件的安装、优化、原理</a><br/>
<a href="../../2014/07/gfw-fqrouter.md">fqrouter——安卓系统翻墙利器（免 ROOT）</a><br/>
<a href="../../2010/03/choose-free-gate.md">自由門——TOR 被封之后的另一个选择</a><br/>
<a href="../../2009/09/break-through-gfw-with-tor.md">戴“套”翻墻的方法</a><br/>
<a href="../../2011/09/gfw-vpn-hotspot-shield.md">扫盲 VPN 翻墙——以 Hotspot Shield 为例</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2019/06/gfw-news.html
