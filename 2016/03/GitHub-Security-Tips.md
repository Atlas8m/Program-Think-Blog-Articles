# 使用 GitHub 的几种方式——兼谈安全性和隐匿性的经验 

-----

<div class="post-body entry-content">
　　先告诉大伙儿一个好消息：<br/>
　　前几天俺把《太子党关系网络》开源到 GitHub 之后，头两天就获得大量网友的关注，以至于<a href="https://github.com/programthink/zhao" target="_blank">俺这个项目</a>至少连续两天排到了 GitHub 的“每日 Trending”（这个排名汇总的是：每一天全球关注程度最高的那几个项目）<br/>
　　非常感谢捧场的 GitHub 用户！！！<br/>
<br/>
<br/>
<h2>★本文面向哪些读者？</h2><br/>
　　俺在博客上不止一次提到过，GitHub 是可以【免翻墙】使用的，而且这个网站/公司的管理层，相对来说还是比较靠谱的，不会轻易向咱们朝廷妥协。<br/>
　　因此，GitHub 非常适合用来搞一些敏感的活动（比如：提供翻墙工具、对朝廷/权贵的爆料、等等）<br/>
　　比如俺就<a href="https://github.com/programthink/zhao" target="_blank">利用 GitHub 开源了《太子党关系网络》</a>，并提供下载。<br/>
　　如果你想用 GitHub 这个平台开发翻墙工具，本文值得你参考。<br/>
　　亦或者你也想效仿俺，在 GitHub 上进行反党活动/反政府活动，那本文更加值得你参考。<br/>
<a name="more"></a><br/>
<br/>
<h2>★本文的必要性及重要性</h2><br/>
　　先举个反面教材，来说明本文的必要性及重要性。<br/>
　　前些年有一款很知名的翻墙工具叫做“Shadowsocks”。这个工具是开源在 GitHub 上的，用的人很多。<br/>
　　但是该项目的作者 clowwindy 非常缺乏安全意识，【没有】做好身份的隐匿。结果捏，大约半年前，项目作者 clowwindy 被六扇门叫去喝茶。期间估计受到相当程度威胁恐吓，以至于 clowwindy 后来把 GitHub 上的项目关闭了。<br/>
<br/>
<br/>
<h2>★阅读本文的前提——需要先了解哪些知识？</h2><br/>
　　俺假定本文的读者已经了解如下几个方面的知识：<br/>
<blockquote>版本管理系统的基本概念<br/>
Git 的基本概念<br/>
GitHub 的基本使用（至少已经注册过帐号）<br/>
Git 客户端的基本使用<br/>
Linux 或 Mac OS 命令行的基本使用<br/>
常见翻墙工具的基本使用（不懂的同学，可以看<a href="https://program-think.blogspot.com/">俺博客上</a>的各种教程）<br/>
TOR 的使用（本文会重点聊到 TOR，俺写的 FAQ 在“<a href="../../2013/11/tor-faq.md">这里</a>”）</blockquote><br/>
<br/>
<h2>★使用 GitHub 的两种方式</h2><br/>
<h3>◇B/S 方式——基于浏览器</h3><br/>
　　这是最基本的使用方式。只要你注册过 GitHub 帐号，自然就知道如何用浏览器访问它。<br/>
　　这种基于浏览器的方式，有时候也称之为“Web 方式”。<br/>
<br/>
<h3>◇C/S 方式——基于客户端软件</h3><br/>
　　除了浏览器方式，你还可以通过 Git 客户端软件来操作 GitHub 上的代码仓库。这种方式称之为“客户端软件方式”（为了打字省力，以下简称“Client 方式”）<br/>
<br/>
<h3>◇这两种方式的对比</h3><br/>
　　B/S 方式最大的好处是：无需安装额外的软件（通常而言，你的系统中已经有默认的浏览器可供使用）。<br/>
　　B/S 方式的另一个好处是：GitHub 几乎所有的功能，都可以在浏览器界面上搞定。<br/>
　　但是 B/S 方式也有如下一些缺点：<br/>
　　<b>1. 安全性</b><br/>
　　如果你经常在某个系统的某个浏览器上操作你的 GitHub 帐号。一旦该系统被入侵，很可能导致你的 GitHub 帐号也被入侵。<br/>
　　<b>2. 易用性</b><br/>
　　有些大批量的操作，在 Web 界面上不太好搞。比如俺前几天上线的项目【太子党关系网络】，里面涉及到上千个文件（包括文本文件，图片文件）。如果通过 Web 界面进行批量操作（添加、删除、改名），就会很麻烦。<br/>
<br/>
　　相比之下，“Client 方式”正好可以弥补“Web 方式”的这几个缺点。至于如何弥补，下面会聊到。<br/>
<br/>
<br/>
<h2>★Client 方式支持哪些协议？</h2><br/>
　　当你通过“client 方式”访问 GitHub 的服务器，可以走几种不同的协议。下面俺简要聊聊。<br/>
<br/>
<h3>◇Git 协议</h3><br/>
　　此种协议，顾名思义，是 Git 专有的协议。除了用于 Git 客户端与服务端之间的通讯，其它场合用不到它。<br/>
　　注意：Git 协议本身是明文的（无加密）。<br/>
<br/>
<h3>◇HTTP/HTTPS 协议</h3><br/>
　　HTTP 协议，大伙儿应该都熟悉，俺就不浪费口水了。<br/>
　　HTTPS 协议，通俗地说就是：“加密的 HTTP”。如今很多网站都开始支持 HTTPS（包括俺博客所在的 Blogspot，从去年10月也开始支持 HTTPS）。大伙儿对它应该也不陌生。<br/>
<br/>
<h3>◇SSH 协议</h3><br/>
　　这个协议，对技术菜鸟可能比较陌生。这玩意儿，早先是 Unix 系统管理员用来远程管理服务器的。<br/>
　　SSH 是“Secure Shell”的缩写。显然，这玩意儿是加密的。<br/>
<br/>
<br/>
<h2>★上述几种客户端协议的优缺点对比</h2><br/>
<h3>◇Git 协议</h3><br/>
　　前面说了，此协议【没有】加密。如果你关注安全性，不应该用它。<br/>
　　首先，明文传输的协议，很容易遭受“旁路嗅探”（sniffer）——导致你丧失数据的【保密性】；<br/>
　　其次，明文传输的协议，很容易在传输过程中被修改（恶意篡改）——导致你丧失数据的【完整性】。<br/>
<br/>
<h3>◇HTTP 协议</h3><br/>
　　明文的 HTTP 协议，同样【不】应该使用。理由同上，不再罗嗦。<br/>
<br/>
<h3>◇HTTPS 协议</h3><br/>
　　HTTPS 是加密协议，避免了前两个的弊端。<br/>
　　它还有如下几个优点：<br/>
　　<b>1. 访客身份也可以使用</b><br/>
　　即使你没有注册 GitHub 的用户，也可以通过 HTTPS 协议克隆某个项目<br/>
　　<b>2. 更容易穿透防火墙</b><br/>
　　很多公司内网的防火墙会屏蔽大部分端口，但是 HTTPS 所用的 443 端口通常是允许通过的（没有屏蔽）。<br/>
<br/>
<h3>◇SSH 协议</h3><br/>
　　与 HTTPS 类似，SSH 也是【强加密】滴。该协议提供了如下几个额外的好处：<br/>
　　<b>1. 提供了额外的认证方式</b><br/>
　　对于 SSH 协议，GitHub 支持“公钥方式”（public key）的认证。当你设置好这种认证方式，就【不再需要】用你的帐号和密码，也可以操作你代码仓库。<br/>
　　这样的好处是——万一你的系统被入侵，顶多泄露你的 key，但【不会】泄露你在 GitHub 的帐号密码。而且 key 被泄漏之后，你可以去你账户的配置界面，把已经泄露的 key 撤销掉。撤销之后，入侵者就算拿到这个 key，也无法再操作你的代码仓库了。<br/>
　　<b>2. 支持“项目级”颗粒度的控制</b><br/>
　　通俗地说就是：你可以为不同的仓库配置不同的 SSH key。如此一来，一个 key 只能操作一个代码库。一旦 key 泄露，损失就小得多了。<br/>
<br/>
<br/>
<h2>★如何用 SSH 方式操作 GitHub 的项目？</h2><br/>
　　在 Git 客户端支持的这几个协议中，俺重点来说一下 SSH 协议的配置。<br/>
　　以下配置以 Linux 环境来举例。<br/>
<br/>
<h3>◇1. 安装 openssh</h3><br/>
　　大部分知名的 Linux 发行版，其官方的软件库中都已经内置了【openssh】这个软件，你只需用该发行版提供的软件包管理器，一个命令就可以把 openssh 装好。<br/>
<br/>
<h3>◇2. 创建“公钥/私钥对”</h3><br/>
　　使用如下命令创建：<br/>
<pre style="font-family:Courier,monospace;">ssh-keygen -t rsa -b 4096 -f 文件路径 -C 邮箱地址</pre>　　稍微解释一下：<br/>
其中的 <code>-t rsa</code> 表示加密算法的类型是 RSA<br/>
其中的 <code>-b 4096</code> 表示密钥是 4096 位/比特<br/>
（请注意，不同加密算法的位数，没有可比性。对于 RSA 加密算法，如果你没有指定 -b 参数，则默认值是 1024；以目前的破解水平，2048 应该够安全了。为了保险起见，咱们这里创建 4096 比特的密钥）<br/>
<br/>
<h3>◇4. 密钥文件的存放</h3><br/>
　　上述命令中的【文件路径】表示：【私钥】文件存放的位置。然后 <code>ssh-keygen</code> 会自动在这个路径末尾附加 <code>.pub</code> 作为【公钥文件】的路径。<br/>
　　比如说：你输入的私钥文件路径是 <code>~/.ssh/xxxx</code> 那么生成之后对应的公钥文件的路径就是 <code>~/.ssh/xxxx.pub</code><br/>
　　如果你要创建不止一个“公钥私钥对”，要使用具有一定可读性的文件名，以免自己搞混了。<br/>
　　【私钥文件】非常重要，【不要】泄漏给外人。<br/>
　　（经热心读者推荐，补充一篇“保护私钥文件”文章，链接在“<a href="https://martin.kleppmann.com/2013/05/24/improving-security-of-ssh-private-keys.html" rel="nofollow" target="_blank">这里</a>”），<br/>
<br/>
<h3>◇5. 在 GitHub 上指派密钥</h3><br/>
　　GitHub 支持两种方式的 SSH key，分别是【用户级】和【项目级】。<br/>
　　所谓的【用户级】就是说，使用该 key 可以操作所有项目的代码仓库；而【项目级】的 key 只能操作所属项目的代码仓库。<br/>
<br/>
　　要设置【用户级】的 key，需要先进入“User Profile”页面，然后进入“SSH keys”页面，点击“New SSH key”按钮。<br/>
　　要设置【项目级】的 key，需要先进入该项目的“Settings”页面，然后进入“Deploy keys”页面，点击“Add deploy key”按钮。<br/>
<br/>
　　点击完上述按钮之后，你需要把【公钥文件】的内容，【<b>原封不动地</b>】 copy &amp; paste 到页面中的那个多行文本框里面。<br/>
　　注意事项：<br/>
1. 别搞错文件了，需要复制的是【公钥文件】的内容！<br/>
2. 粘贴的时候要小心，【不要】加入多余的空格或多余的回车。<br/>
<br/>
<h3>◇6. 测试 SSH 登录</h3><br/>
　　如果你当前的系统无需代理就可以访问 GitHub，那么你可以先用命令行测试一下刚才配置好的那个 SSH。<br/>
　　运行如下命令：<br/>
<pre style="font-family:Courier,monospace;">ssh -i 公钥文件路径 -T git@github.com</pre>　　运行之后，可能会出现如下提示：<br/>
<pre style="font-family:Courier,monospace;">RSA key fingerprint is nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
Are you sure you want to continue connecting (yes/no)?</pre>　　你输入 <code>yes</code> 以便继续。之后你会看到一句 <q>You've successfully authenticated</q> 就表示该 ssh key 已经通过登录认证。<br/>
<br/>
<h3>◇7. 修改 SSH 的配置文件</h3><br/>
　　测试通过之后，你可以修改 SSH 的配置文件，就不用每次都在命令行参数中指定密钥文件的路径了。如果你用 SSH 方式操作2个以上的项目，很有必要进行如下定制，可以节省很多命令行输入。<br/>
　　SSH 配置文件的路径是： <code>~/.ssh/config</code><br/>
　　如果你系统中没有这个文件，就创建一个。然后用你熟悉的文本编辑器修改这个文件。<br/>
　　下面俺给出一个示例：<br/>
你需要把示例中的“别名”改为你自己起的名字（用一个可读性好一些的名字）；<br/>
把“私钥文件路径”也同样替换为你本机所使用的文件路径。<br/>
其它部分【不要】改动。<br/>
<pre style="font-family:Courier,monospace;">Host 别名
&nbsp;&nbsp;HostName                  ssh.github.com
&nbsp;&nbsp;Port                      443
&nbsp;&nbsp;User                      git
&nbsp;&nbsp;PreferredAuthentications  publickey
&nbsp;&nbsp;IdentityFile              私钥文件路径</pre><br/>
　　所谓的“别名”，用来替换 URL 中的主机名。比如俺那个 zhao 项目，俺在 <code>~/.ssh/config</code> 中使用的别名就是 zhao<br/>
　　之后俺如果要 clone 该项目，只需用如下命令：<br/>
<pre style="font-family:Courier,monospace;">git clone ssh://<b>zhao</b>/programthink/zhao</pre>看到没？俺在 URL 中就不写 github.com 而改为 zhao，那么 openssh 就会去 <code>~/.ssh/config</code> 中找到 zhao 这个配置项，然后用对应的私钥文件进行 SSH 连接，<br/>
<br/>
<h3>◇8. 后续操作</h3><br/>
　　前面几个步骤都搞定之后，你就可以通过 ssh 协议把某个项目 clone 到本地，修改完，最后再 push 到 GitHub 上。整个过程都是通过【强加密的】 SSH 协议完成。<br/>
<br/>
<br/>
<h2>★使用代理的必要性/重要性</h2><br/>
<h3>◇为啥要使用代理？</h3><br/>
　　为啥要使用代理？简而言之就是：不让 GitHub 的服务器看到你的公网 IP。<br/>
　　看这里，估计某些同学会问了：前面不是说，GitHub 是比较靠谱的公司吗？为啥还担心被它看到（自己的）公网 IP？<br/>
　　俺来回答一下这个问题：<br/>
　　即使 GitHub 这个公司的管理层非常靠谱，丝毫不与朝廷合作，也不向朝廷妥协让步。如果让 GitHub 的服务器知道你的公网 IP，（对于高危人士）依然存在如下几种风险：<br/>
<b>风险1</b><br/>
GitHub 有一个“Session”功能，可以显示你最近几次登录时使用的【访问者IP】。<br/>
万一某天你的帐号被入侵了，那么入侵者就可以利用该功能，看你的“访问者IP”，如果你没有走代理，那么你的“访问者IP”也就是本人的“公网IP”<br/>
<b>风险2</b><br/>
即使 GitHub 公司的管理层非常有骨气，但是不保证该公司所有的员工也都是如此。万一某个服务器管理员被朝廷收买了，或许会把某些用户资料卖给朝廷。<br/>
（如果你没有走代理）然后六扇门的人就可以通过服务器上记录的“访问者IP”来定位你。<br/>
<b>风险3</b><br/>
即使 GitHub 公司的全体员工都非常有骨气，还有一个风险是：朝廷的御用骇客有可能会入侵 GitHub 的服务器。<br/>
这可不是俺耸人听闻。即使牛B如 Google，依然在2011年遭遇了天朝御用骇客的【深度渗透】。那次渗透的程度之深，据说入侵者已经接触到 Gmail 的核心服务器，并拿到了几个敏感人士（民运人士）的邮件内容。这次事件后来被称为“极光行动”，此事直接导致了 Google 高层震怒并退出大陆市场。<br/>
<br/>
　　综上所述，如果你是一个高危人士，并且通过 GitHub 进行敏感活动，访问 GitHub 的时候，一定要【全程代理】。不论你是用 B/S 方式还是 C/S 方式都要牢记这点。<br/>
<br/>
<h3>◇为啥要使用 TOR 作为代理？</h3><br/>
　　<b>代理有很多种，俺强烈建议用【基于 TOR 的双重代理】</b>。<br/>
　　为啥俺特别强调用【TOR】，并且还强调要用【双重代理】，其中的技术分析，可以参考《<a href="../../2013/11/tor-faq.md">“如何翻墙”系列：关于 TOR 的常见问题解答</a>》。<br/>
　　由于那篇 FAQ 已经说得很具体了，俺在这里就不重复罗嗦了。简而言之，这么干可以极大增加追踪者对你进行逆向追溯的难度。追踪者的难度越大，你就越安全。<br/>
　　（关于“双重代理”的扫盲教程，可以参见《<a href="../../2010/04/howto-cover-your-tracks-0.md">如何隐藏你的踪迹，避免跨省追捕</a>》系列博文的其中一篇）<br/>
<br/>
<br/>
<h2>★针对不同的 Git 使用方式，如何配置代理？</h2><br/>
<h3>◇B/S 方式（Web 方式）</h3><br/>
　　这种方式最简单——就跟你翻墙访问其它网站类似——只需要让你的浏览器通过 TOR 的线路访问 GitHub 的页面，就 OK 了。<br/>
　　没用过 TOR 的同学，先去看俺的扫盲教程《<a href="../../2009/09/break-through-gfw-with-tor.md">戴“套”翻墻的方法</a>》。<br/>
<br/>
<h3>◇C/S 方式 下的 HTTPS 协议</h3><br/>
　　对于这种方式，你需要修改 Git 的配置参数，让 Git 知道 TOR 代理的 IP 和 端口。<br/>
　　具体的配置命令如下：<br/>
<pre style="font-family:Courier,monospace;">git config --global http.proxy SOCKS5h://地址:端口号</pre>注意1：<br/>
假如你的 TOR 客户端运行在【<b>本机</b>】，那么上述命令中的“地址”就替换为： <code>127.0.0.1</code><br/>
否则就替换为：运行 TOR 客户端的主机的 IP 地址。<br/>
注意2：<br/>
如果你的 TOR 客户端用的是 <b>TOR Browser</b>，端口号必须是： <code>9150</code><br/>
如果你用的是 TOR 的其它软件包（比如：TOR Expert Bundle），则端口号使用： <code>9050</code><br/>
<br/>
<h3>◇C/S 方式下的 SSH 协议</h3><br/>
　　要让 SSH 通过 TOR 的代理，稍微麻烦一点。因为 TOR 默认提供的是 SOCKS 代理，而 OpenSSH 客户端默认又【不】支持 SOCKS 代理。<br/>
　　因此，得依靠第三方的工具，来实现“SSH through SOCKS”。<br/>
　　这里要提醒一下列位看官：<br/>
　　俺说的是“SSH through SOCKS”，而【不是】“SOCKS through SSH”（这两者完全不同）<br/>
<br/>
　　为了搞定“SSH through SOCKS”，俺选用大名鼎鼎的 nc（也就是“netcat”）。<br/>
　　由于这个 netcat 名气很大，主流 Linux 发行版的软件仓库中都有它。你只需要用发行版自带的软件包管理器，把 netcat 装上。<br/>
　　装好 netcat 之后，可以用如下命令测试“SSH through TOR SOCKS”是否成功（命令中的 nc 就是 netcat）。<br/>
<pre style="font-family:Courier,monospace;">ssh -o "ProxyCommand=nc -X 5 -x 地址:端口号 %h %p" -T ssh.github.com</pre>注意1：<br/>
假如你的 TOR 客户端运行在<b>本机</b>，那么上述命令中的“地址”就替换为： <code>127.0.0.1</code><br/>
否则就替换为：运行 TOR 客户端的主机的 IP 地址。<br/>
注意2：<br/>
如果你的 TOR 客户端用的是 <b>TOR Browser</b>，“端口号”必须是： <code>9150</code><br/>
如果你用的是 TOR 的其它软件包（比如：TOR Expert Bundle），则“端口号”使用： <code>9050</code><br/>
<br/>
　　上述测试命令如果最终显示 <q>Permession denied</q> 就说明已经通过 SOCKS 代理连接到 GitHub 了（也就是说，你的 SSH 已经能够走 SOCKS 代理联网了）。<br/>
　　如果没有显示这个信息，而是显示了其它其它信息，你再用如下命令重新试一次<br/>
<pre style="font-family:Courier,monospace;">ssh -o "ProxyCommand=nc -X 5 -x 地址:端口号 %h %p" -Tv ssh.github.com</pre>这次俺加了一个 v 选项，可以打印出详细的诊断信息（不过都是洋文）。如果你略懂洋文并略懂网络技术，或许能判断出错的原因所在。<br/>
<br/>
　　搞定之后，为了方便起见，同样可以把 SSH 的这个 <code>ProxyCommand</code> 命令行选项加入到 SSH 的配置文件。如此一来，以后每次你要连接 GitHub 的服务器，都会自动走 TOR 提供的 SOCKS 代理。<br/>
　　前面俺已经给出了 SSH 配置文件的示例，俺把之前那个示例文件，加上 ProxyCommand 选项之后，变为如下<br/>
<pre style="font-family:Courier,monospace;">Host 别名
&nbsp;&nbsp;HostName                  ssh.github.com
&nbsp;&nbsp;Port                      443
&nbsp;&nbsp;User                      git
&nbsp;&nbsp;PreferredAuthentications  publickey
&nbsp;&nbsp;IdentityFile              私钥文件路径
&nbsp;&nbsp;ProxyCommand              /usr/bin/nc -X 5 -x 地址:端口号 %h %p</pre>注意1：<br/>
假如你的 TOR 客户端运行在<b>本机</b>，那么上述命令中的“地址”就替换为： <code>127.0.0.1</code><br/>
否则就替换为： TOR 客户端的主机的 IP 地址。<br/>
注意2：<br/>
如果你的 TOR 客户端用的是 <b>TOR Browser</b>，“端口号”必须是： <code>9150</code><br/>
如果你用的是 TOR 的其它软件包，则“端口号”使用： <code>9050</code><br/>
<br/>
<h2>★其它注意事项</h2><br/>
<h3>◇GitHub 帐号的注册</h3><br/>
　　要想做到【彻底隐匿】，你需要从一开始就是隐匿的。<br/>
　　所以，当你注册 GitHub 的时候，就得用【基于 TOR 的双重代理】进行注册。俺当年注册 GitHub 就是这么干滴。<br/>
<br/>
<h3>◇邮件地址的设置</h3><br/>
　　最好不要公开你的邮箱，这样可以避免一些不必要的风险。<br/>
　　你可以在 GitHub 的用户配置界面中，设置自己的邮箱地址为“私密”。具体操作步骤参见 GitHub 官方的帮助（链接在“<a href="https://help.github.com/articles/keeping-your-email-address-private/" rel="nofollow" target="_blank">这里</a>”）<br/>
　　由于俺前面介绍了基于 SSH 客户端操作 GitHub，当你把邮箱地址设置为【私密】之后，你记得设置一下 git 客户端的 email 选项（命令如下）<br/>
<pre style="font-family:Courier,monospace;">git config --global user.email 名称@users.noreply.github.com</pre>　　把上述命令中的“名称”替换为你在 GitHub 上的帐号名。<br/>
　　经过上述命令设置之后，别人看你的提交历史，看到的是类似与 <code>xxxx@users.noreply.github.com</code> 这样的邮箱地址，看不到你真实的邮箱地址。<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
<a href="../../2010/04/howto-cover-your-tracks-0.md">如何隐藏你的踪迹，避免跨省追捕（系列）</a><br/>
<a href="../../2013/11/tor-faq.md">“如何翻墙”系列：关于 TOR 的常见问题解答</a><br/>
<a href="../../2009/09/break-through-gfw-with-tor.md">“如何翻墙”系列：戴“套”翻墻的方法</a><br/>
<a href="../../2015/03/Tor-Arm.md">扫盲 Arm——Tor 的界面前端（替代已死亡的 Vidalia）</a><br/>
<a href="../../2014/12/gfw-privoxy.md">如何用 Privoxy 辅助翻墙？</a><br/>
<a href="../../2016/02/Zhao-at-GitHub.md">《太子党关系网络》开源到 GitHub——大伙儿一起来曝光赵国权贵</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2016/03/GitHub-Security-Tips.html
