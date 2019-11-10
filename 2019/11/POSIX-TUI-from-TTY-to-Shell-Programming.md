# 扫盲 Linux＆UNIX 命令行——从“电传打字机”聊到“shell 脚本编程” 

-----

<div class="post-body entry-content">
<h2>★引子</h2><br/>
　　首先，<br/>
　　这篇是为了补前几年的“欠债”。这些年，俺写了好多篇 Linux 相关的技术教程。但还从来没有【系统性】地介绍 Linux 命令行相关的基本概念和基本知识。几年来，已经有不少读者催俺填上这个大坑，但俺比较懒，一直拖到现在，惭愧 :(<br/>
　　其次，<br/>
　　一个多月前（9月份）写了一篇 <a href="../../2019/09/Netcat-Tricks.md">netcat 的扫盲教程</a>，其中涉及了很多命令行相关的知识。很多菜鸟读者，如果缺乏这些基础知识，恐怕看不懂那篇 netcat 教程。再加上<a href="../../2019/10/Systematic-Learning.md">前几天的博文</a>谈到了【系统性学习】相关的方法论，并且还聊了【费曼学习法】的各种好处。<br/>
　　今天这篇，算是俺第 N 次践行“费曼学习法”——无论对俺还是读者，这都是【双赢】滴 :)<br/>
<a name="more"></a><br/>
<br/>
<h2>★本文目标读者</h2><br/>
　　虽然本文的标题号称是【扫盲】，但俺相信：<b>即使是一些 POSIX 系统的命令行【老手】，对本文中介绍的某些概念，可能也会有【欠缺】。</b><br/>
　　因此，这篇教程既适合于命令行的新手，也值得某些【老手】看一看。<br/>
<br/>
　　由于本文介绍的是 POSIX 系统中【通用的】概念与知识。因此，包括 Linux、BSD 家族、Mac OS 等各种系统的用户，应该都能从中受益。<br/>
　　（注：<a href="https://en.wikipedia.org/wiki/POSIX" rel="nofollow" target="_blank">POSIX</a> 是某种操作系统的标准/规范。各种 Linux 发行版以及所有的 UNIX 变种，包括 Mac OS，都属于“POSIX 系统”）<br/>
<br/>
　　如果你是这方面的菜鸟，并且想要掌握这个领域。【不要】企图只看一遍就完全理解本文的内容。可能需要看好几遍，并且要一边看，一边拿命令行的环境【实践】一下。<br/>
<br/>
<a name="teletype"> </a><br/>
<h2>★一切都从【电传打字机】开始说起</h2><br/>
　　（说完了“引子”与“目标读者”，开始切入正题）<br/>
　　可能有些读者会纳闷——“聊命令行的基本概念”，为啥要扯到“电传打字机”？是不是扯得太远了？<br/>
　　俺来解释一下：<br/>
　　IT 行业的很多基本概念都来自于【历史遗迹】。有时候你觉得某些东西很奇怪（并纳闷“为啥会设计成这样”）；而当你搞清楚历史的演变过程之后，自然就明白其中的原因。<br/>
<br/>
<h3>◇在那遥远的【电报时代】</h3><br/>
　　在计算机诞生之前（二战前），【电报】属于高科技的玩意儿——它能够瞬间把信息传送到另一个城市（甚至传送到大洋彼岸）。<br/>
　　当年的电报线路，是以【字符】为单位发送信息。在线路两端使用【电传打字机】，就可以自动地把对方发过来的字符打印出来。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/SO-SrkxjARZ0k4dADyEbtp9vYYHbv37f1R_iYFZzit2KJjjmeRjLqrXb0gRlHebYTYz1QeT9KzkiJaCneNrhmuBQZaXhlpt2QVDB1N0_3eigwXAZuDmQGq6wmUYjA7zIsyRgxRejW5c"/><br/>
（上世纪40年代的电传打字机——用于电报网）</center><br/>
<h3>◇“回车/换行”的来历</h3><br/>
　　稍微懂点 IT 的同学，应该都听说过“回车/换行”，洋文分别称之为“carriage return”＆“line feed”。在编程领域，这两个字符简称为 <code>\r</code> ＆ <code>\n</code>。<br/>
　　为啥会有这么两个玩意儿捏？<br/>
　　因为在电传打字机时代，当打印完一行之后，需要用一个控制命令把“打印头”复位（移到打印纸的左边），然后再用另一个控制命令把“打印头”往下移动一行。很自然地，这俩动作就对应了两个控制字符（CR ＆ LF），也就是所谓的“回车 ＆ 换行”。<br/>
<br/>
<h3>◇其它控制字符</h3><br/>
　　如果你去留意一下 ASCII 字符表的开头部分，前面那32个字符都是控制字符，很多都源于遥远的【电报时代】。<br/>
　　在本文后续的介绍中，还会再聊到这些“控制字符”。<br/>
<br/>
<br/>
<a name="tty"> </a><br/>
<h2>★终端（terminal/TTY）</h2><br/>
<h3>◇历史演变</h3><br/>
　　“终端”一词，洋文称之为“<a href="https://en.wikipedia.org/wiki/Computer_terminal" rel="nofollow" target="_blank">terminal</a>”。有时候又被称作 TTY，而 TTY 这个简写就来自刚才介绍的【电传打字机】（teletype printer）。<br/>
　　因为早期的大型机，其“终端”就是【电传打字机】。那时候的终端，也称作【硬件终端】。<br/>
<br/>
　　为啥会有“终端”这个概念捏？你依然需要了解历史的变迁。<br/>
　　最早期的计算机（大型机）是【单任务】滴——也就是说，每次只能干一件事情。<br/>
　　到了60年代，出现了一个【革命性】的飞跃——发明了【多任务】系统，当时叫做“<a href="https://en.wikipedia.org/wiki/Time-sharing" rel="nofollow" target="_blank">time-sharing</a>”（分时系统）。有了“分时系统”，就可以让多个人同时使用一台大型机。而为了让多个人同时操作这台大型机，就引入了【终端】的概念。每一台大型机安装多个终端，每个操作员都在各自的终端上进行操作，互不干扰。<br/>
<br/>
<h3>◇（跑题）“约翰·麦卡锡”其人</h3><br/>
　　聊到这里，稍微跑题一下：<br/>
　　最早的“分时系统”由 IT 超级大牛“约翰·麦卡锡”（<a href="https://en.wikipedia.org/wiki/John_McCarthy_(computer_scientist)" rel="nofollow" target="_blank">John McCarthy</a>）设计。此人不仅仅是“分时系统它爹”，还是“Lisp 语言它爹”，另外还参与设计了编程语言“ALGOL 60”。而这个“ALGOL 60”编程语言虽然知道的人不多，但该语言深刻影响了后续的 Ada、BCPL、C、Pascal......<br/>
　　为了让你体会这只大牛到底有多牛。俺引用另一个牛人保罗·格雷汉姆（《<a href="https://docs.google.com/document/d/17i49-SpeKz1wRG5S-HPonO-lXJHD99h62gDsQ64NWXo/" target="_blank">黑客与画家</a>》作者）的观点——他认为在所有编程语言中， Lisp 与 C 是两座无法超越的高峰。而“约翰·麦卡锡”亲自发明 Lisp 语言，然后又深刻影响了 C 语言。<br/>
　　另外，麦卡锡这只大牛还参与创立了“MIT 人工智能实验室”与“斯坦福人工智能实验室”。前者涌现出一大批早期的黑客，其中包括大名鼎鼎的 <a href="https://en.wikipedia.org/wiki/Richard_Stallman" rel="nofollow" target="_blank">Richard Stallman</a>（此人开创了：自由软件运动、GNU 社区、GCC、GDB、GNU Emacs ......）。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/0Yiucax8D7skki_Z5csmfmOhFXAc6nUnQfHik6WDoNRMPX4OJeqjq7GZcuHrjYFrBiPmqOunexkfby3c0NI7blTa1d_yDoELrPfIVVYFIHqJLHlQM8X94Ql4IKSyGsKuesGRYbJZKgU"/><br/>
（超级大牛约翰·麦卡锡）</center><br/>
<h3>◇【远程】终端</h3><br/>
　　跑题结束，言归正传。<br/>
　　“终端”的好处不光是“多任务”，而且还可以让用户在【远程】进行操作。这种情况下，“终端”通过 modem（调制解调器）与“主机”相连。这种玩法很类似于——互联网普及初期的拨号上网。示意图如下：<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/iUIOjl4GY8O419YJ45c1BN4ri4U2eLJThOEq_Ff_6_gdfGwz76imgEqf6kHp0pgs1iGr0544VL5bTcRGkKaw42mz25Z0vYqEWXhbWwOKS9Y4Nh2UDfN_6LuM-PK1jhtDUtkGbHgV27k"/><br/>
（通过 modem 实现的【远程】终端）</center><br/>
　　最早的“终端”，本质上就是“电传打字机”——以“打字机”作为输入；以“打印纸”作为输出。这类终端，比较经典的是如下这款：<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/3tqr5yVvG9QF7vW_J45SWY8aMmGekLQZZNKOP48Vvi9V71qz9v45vbTs25tN6stF13qotXRkyuC_o76FLzYYAbDKzRXFNcSiKnoy5H-6BpRzQ2ZdR9ON1vjdfYYpThUHpthIYv9MoL0"/><br/>
（Teletype Model 33 ASR）</center><br/>
　　到了上世纪70年初，终于有了带【屏幕】的远程终端。<a href="https://en.wikipedia.org/wiki/Digital_Equipment_Corporation" rel="nofollow" target="_blank">DEC 公司</a>的 VT05 是第一款基于 CRT 显示器的远程终端。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/SDvmTqKHE5lh3PPbrTUGvuX7V8Ux4fv3TdWvB7Ga8BbAVMKUJ8mwn9qp0UqI_6YEDYwhbrEqOWa2M3ifzrTTT5zrpzS-kJwijICRVQDldIfl2W3ra3WQuPxPzWD7I9u8d45z84l04dM"/><br/>
（VT05 终端）</center><br/>
<h3>◇内部结构示意图</h3><br/>
　　下面这张是大型机时代，“终端”与“进程”通讯的示意图。<br/>
　　图中的 <code>UART</code> 是洋文“Universal Asynchronous Receiver and Transmitter”的缩写（相关维基百科链接在“<a href="https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter" rel="nofollow" target="_blank">这里</a>”）。LDISC 是洋文“line discipline”的简写（相关维基百科链接在“<a href="https://en.wikipedia.org/wiki/Line_discipline" rel="nofollow" target="_blank">这里</a>”）。<br/>
　　通俗地说，UART 用来处理物理线路的字符传输（比如：“错误校验”、“流控”、等）；LDISC 用来撮合底层的“硬件驱动”与上层的“系统调用”，并完成某些“控制字符”的处理与翻译。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/wzvdclkzzYDah1LxS_lTCQqAbxdePKSr-w1XT7c91axw-_CuT7aATNsEuHxbWBYIOvhbifp8hrwLDkBpOXVQajgX5ZSDfcjvoqjjIpiQVV0EVbaldvA1geO_FHxMe40DMFZ9RfG7iSA"/><br/>
（TTY 示意图1：使用【硬件终端】的大型机内部结构图）</center><br/>
<h3>◇如今的含义</h3><br/>
　　如今，“终端”一词的含义已经扩大了——<b>用来指：基于【文本】的输入输出机制。</b><br/>
　　在本文后续的章节中， terminal 与 TTY 这两个术语基本上是同义词。<br/>
<br/>
<a name="tty-mode"> </a><br/>
<h2>★终端的3种【缓冲模式】——字符模式、行模式、屏模式</h2><br/>
<h3>◇字符模式（character mode）</h3><br/>
　　又要说回到【电传打字机】。<br/>
　　在本文开头，已经聊过这个玩意儿，并且提到——它是基于【字符】传输滴。也就是说，操作员每次在“电传打字机”上按键，对应的字符会立即通过线路发送给对方。这就是最传统的【字符模式】<br/>
　　通俗地说，“字符模式”也就是【无缓冲】的模式。<br/>
<br/>
<h3>◇行模式（line mode）</h3><br/>
　　不客气地说，“字符模式”是非常傻逼滴！因为如果你不小心按错键，这个错误也会立即发送出去。<br/>
　　比如说，你在输入一串很长的命令，结果输到半当中，敲错一个按键，整个命令就废了——要重新再输入一遍。<br/>
　　所以，当早期的程序员对“字符模式”实在忍无可忍之后，终于发明了【行模式】。<br/>
　　【行模式】也叫做“行缓冲”。也就是说，终端会把你当前输入的这行先缓冲在本地。只有当你最终按了【回车键】，才会把这一整行发送出去。如果你不小心敲错了一个字符，可以赶紧用“退格键”删掉重输这个字符。<br/>
　　因此，这种模式称之为【行缓冲】。<br/>
<br/>
　　顺便说一下：<br/>
　　早期的标准键盘，【没有】方向键（“上下左右”这4个键）。不信的话，可以去看本文前面贴的那张“Teletype Model 33 ASR”的照片。<br/>
　　因为无论是“字符模式”还是“行模式”，都没这个需求。<br/>
<br/>
<h3>◇屏模式（screen mode/block mode）</h3><br/>
　　“行模式”进一步的发展就是【屏模式】。这个玩意儿也叫“全屏缓冲”，顾名思义，终端会缓冲当前屏幕的内容。<br/>
　　在这种模式下，用户可以利用方向键，操纵光标（cursor）在屏幕上四处游走。<br/>
　　开发这种类型的软件，比较复杂——程序员至少需要做如下工作：<br/>
1. 保存整个屏幕的状态<br/>
2. 根据键盘输入，操纵光标（cursor）移动<br/>
3. 控制屏幕的哪些区域是光标可达，哪些是不可达；<br/>
4. 对于光标可达的部分，控制哪些是“可编辑”，哪些是“只读”；<br/>
5. 根据“光标移动”以及某些“特定的按键”（比如“翻页键”），重新绘制屏幕<br/>
......<br/>
　　后来，为了简化”屏模式“的编程，专门搞了一个叫做 curses 的编程库。如今的“ncurses 库”就是从 curses 衍生出来滴（前面加了一个 n 表示 new）。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/nPGfx1VIMvI26G-L4q9jqaw-RYqRLkHIj3vjgOMHzxAFQMHgOEry2YyN4mXFPAxqvNPl4EwqJr0Q34Z9sMl_8HPNmm1eT-FAkJyU8FCJcSPovg8wb3UZJT5CIbdKz-zmeNdX0J2pFvk"/><br/>
（“重编译 Linux 内核”的配置界面，基于 ncurses 实现）</center><br/>
　　前面说了——早期的键盘【没】方向键。有了这个【屏模式】之后，键盘上才开始增加了“方向键”（所以“方向键”位于键盘的扩展区）<br/>
<br/>
<h3>◇小结</h3><br/>
　　上述这三种模式，第1种基本淘汰（仅限于极少数场景）；第3种用得也不多。与本文关系比较密切的，其实是【第2种】——行模式。<br/>
　　为了加深你的印象，用 <code>cat</code> 命令来举例（注：这个命令其实与“猫”【无关】，而是 concatenate 的简写）<br/>
　　大部分情况下，都是用它来显示某个文件的内容，比如说：<code>cat 文件名</code> 。但如果你运行 <code>cat</code>【没】加任何参数，那么它就会尝试读取你在终端的输入，然后把读到的文本再原样输出到终端。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/PPet_RllllnSmYALmxV56ohy5NZz1kj76GzbmcvM9HJDrqY6h74otCFL1E0rG_lEKnALViM8zv2E4BOj4bUUTixzD_QTTXsmoh0-U3dxJROpiAfvW2vHZ69s2vpYlq88-6FBngqgzSQ"/><br/>
（动画：演示“行模式”的效果）</center><br/>
　　在上述动画中，你的输入并【没有】直接传递给 <code>cat</code> 进程。要一直等到你按下【回车键】，<code>cat</code> 进程才收到你的输入，并立即打印了输出。<br/>
<br/>
<a name="tty-echo"> </a><br/>
<h2>★终端的【回显】</h2><br/>
<h3>◇“回显”是啥？</h3><br/>
　　在刚才那个 gif 动画中，当俺逐个输入 <code>test</code> 的每个字母，这些字母也会逐个显示在屏幕上。这种做法叫做【回显】。<br/>
<br/>
<h3>◇“回显”的打开与关闭（启用/禁用）</h3><br/>
　　虽然“回显”很人性化，但某些特殊的场合是【不想】“回显”滴，比如当你输入密码/口令的时候。<br/>
　　因此，终端提供了某种机制，使得程序能够控制“回显”的启用/禁用。<br/>
　　对于大多数终端，可以用【<code>Ctrl + S</code>】禁用“回显”，然后用【<code>Ctrl + Q</code>】启用“回显”。<br/>
　　如果你在禁用“回显”的情况下输入一些文本，当你重新启用“回显”的瞬间，这些文本会一起出现在屏幕上。<br/>
<br/>
　　顺便说一下：<br/>
　　由于【<code>Ctrl + S</code>】在 Windows 上是很常见的组合键。某些菜鸟刚开始玩 Linux 命令行的时候，会习惯性地按这个组合键，结果就禁用了回显。这时候，任何键盘输入都没有反应。菜鸟就以为终端死掉了。<br/>
<br/>
<h3>◇历史演变</h3><br/>
　　对于 Windows 用户来说，【<code>Ctrl + S</code>】实在太常用了，很容易误按。肯定有大量的用户吐槽过 POSIX 终端的这个快捷键。<br/>
　　那么，为啥要用这两个快捷键来控制“回显”捏？俺又要第 N 次说到【电传打字机】了。<br/>
　　由于这玩意儿的输出是【打印纸】，其速率比较【慢】。一旦“对方发送字符的速率”高于“自己这边的打印速率”，就需要向对方发一个控制信号，让对方暂停发送；等到自己这边打印完了，再发送另一个控制字符，通知对方继续。<br/>
　　（注：上述这种玩法，通信领域行话称之为“流量控制/流控”）<br/>
　　当年用来表示“暂停发送”的控制字符，对应的就是【<code>Ctrl + S</code>】；用来“恢复发送”的控制字符，也正是【<code>Ctrl + Q</code>】。<br/>
<br/>
<a name="system-console"> </a><br/>
<h2>★（早期的）系统控制台/物理控制台（system console）</h2><br/>
　　（前面说了）在【没】发明“分时系统”之前，当时的计算机只能执行【单任务】。因此，那时候的大型机只有【一个】操作界面，称之为【控制台】。<br/>
　　话说那时的“控制台”，真的是一个台子（参见下图）。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/vc0kCy3x_3ds8LNeFUpgcE7HljoCBVAD1T-857bjeMUGIBweBrX32gZ27A5c7I2ChXLOljlh3h8_1iIYp39EvlNSn9w5x5zu5CTxWlO6W1aBV6qilF9pt0aq7MXCcZkq2SHMKS_5pt8"/><br/>
（上世纪50年代，IBM 公司 704 大型机的控制台）</center><br/>
　　后来发明了“分时系统”。如刚才所说——“分时系统”使得大型机可以具备多个终端。在这种情况下，你可以把“控制台”通俗地理解为“本地终端”，而【不】是“控制台”的那些终端，称之为“远程终端”。<br/>
　　在那个年代，计算机属于【非常非常稀缺】的资源。于是拥有大型机的公司，就可以【出租计算资源】，获得一笔相当可观的收入。他们把大型机的某个“远程终端”租给外来人员使用，然后根据“时间/空间”收取费用。由于资源的稀缺性，当年的 CPU 是按【秒】计费，而内存是按【KB】计费。<br/>
　　由于“远程终端”可能会被【外人】使用，因此对“远程终端”的【权限】要进行一些限制。如果要进行一些高级别的操作（比如“关闭整个系统”），就只能限制在【控制台】（本地终端）进行。有些公司为了安全起见，还会把“控制台”单独锁在某个“secured room”里面。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/5AlRxQhR00CvQ3DSO-idsyShNRJAOMIGL1J5I3b1UE1kW1dZVE5gU8mBenZUF_DMxwi0nHYd6ju7J6JsdApfarb3E_1_jBJQ2fL4SMm60k34xVToDm41jWoHfZOY32nZEhJW247zx3U"/><br/>
（上世纪60年代，DEC 公司 PDP-7 小型机的控制台）</center><br/>
<a name="virtual-console"> </a><br/>
<h2>★（如今的）虚拟控制台（virtual console）</h2><br/>
　　到了 PC 时代，传统意义上的【控制台】已经看不到了。但 console 这个术语保留了下来。<br/>
<br/>
<h3>◇从“物理 console”到“虚拟 console”</h3><br/>
　　早期大型机的 console 是【独占】硬件滴——“键盘/显示器”固定用于某个 console 滴。<br/>
　　【现代】的 POSIX 系统，衍生出“virtual console”的概念——可以让几个不同的 console【共用】一套硬件（键盘/显示器）。“virtual”一词就是这么来滴。<br/>
　　再重复唠叨一下：不论是早期的“物理控制台”还是后来的“虚拟控制台”，都属于广义上的“终端”。<br/>
<br/>
<h3>◇举例：Linux 的 virtual console</h3><br/>
　　假设你的 Linux 系统没安装图形界面（或者默认不启用图形界面），当系统启动完成之后，你会在屏幕上看到一个文本模式的登录提示。这个界面就是 virtual console 的界面。<br/>
　　在默认情况下，Linux 内置了【6个】virtual console 用于命令行操作，然后把第7个 virtual console 预留给图形系统。你可以使用 <code>Alt + Fn</code> 或 <code>Ctrl + Alt + Fn</code> 在这几个 console 之间切换（注：上述所说的 <code>Fn</code> 指的是 F1、F2... 之类的功能键）。<br/>
<br/>
<h3>◇虚拟控制台的【内部结构】</h3><br/>
<center><img alt="不见图 请翻墙" src="images/8rNRQNmIjTgBgt2N9RQQuzPJ4FP-03PcZfURXegbfEWowJ2XpAVNm3beOKXEVOJIbFmrDUQi3EqylMhxr2igKvHVp95rP1cyKgtl8He00YemHrCUAtOzjZSE48C6bkWibmun8pJFOEI"/><br/>
（TTY 示意图2：【虚拟控制台】的内部结构图）</center><br/>
<a name="terminal-emulator"> </a><br/>
<h2>★终端模拟器（terminal emulator）</h2><br/>
　　请注意上面那张示意图，图中出现了一个【终端模拟器】，这就是本章节要说的东东。<br/>
　　如果你对比前面的【TTY 示意图1】与【TTY 示意图2】的变化，会发现——“UART ＆ UART 驱动”没了，然后多了这个【终端模拟器】。<br/>
　　多出来的这个玩意儿相当于加了一个【抽象层】，模拟出早期硬件终端的效果，因此就【无需改动】系统内核中的其它部分，比如：LDISC（<a href="https://en.wikipedia.org/wiki/Line_discipline" rel="nofollow" target="_blank">line discipline</a>）<br/>
　　请注意，这个场景下的“终端模拟器”位于操作系统【内核】。换句话说，它属于【内核态】的模拟器。正是因为它处于这个地位，所以能够在“驱动”＆“LDISC”之间进行协调。<br/>
<br/>
<a name="pty"> </a><br/>
<h2>★伪终端（PTY/pseudotty/pseudoterminal）</h2><br/>
<h3>◇从“文本模式”到“图形模式”</h3><br/>
　　前面讲的那些，都是【文本模式】（文本界面）。<br/>
　　话说到了上世纪80年代，随着【图形界面】的兴起，就出现某种需求——想在图形界面下使用“【文本】终端”。于是就出现了“<a href="https://en.wikipedia.org/wiki/Pseudoterminal" rel="nofollow" target="_blank">伪终端</a>”的概念。<br/>
　　通俗地说，“伪终端”就是用某个图形界面的软件来模拟传统的“文本终端”的各种行为。前面说了，TTY 这个缩写相当于“终端”的同义词；因此“pseudotty” 就衍生出 PTY 这个缩写。<br/>
<br/>
<h3>◇从“【内核态】终端模拟器”到“【用户态】终端模拟器”</h3><br/>
　　在上一个章节中，emulator 运行在系统内核中，因此是“内核态模拟器”；<br/>
　　等到后来搞“伪终端”的时候，就直接把这个玩意儿从【内核态】转到【用户态】——让它直接运行在【桌面环境】。如此一来，用户就可以直接在桌面环境中使用“终端模拟器”。<br/>
　　当“终端模拟器”变为【用户态】，它就【无法】直接与“键盘驱动 or 显卡驱动”打交道。在这种情况下，由“GUI 系统”（比如：X11）负责与这些驱动打交道，然后再把用户的输入输出转交给“终端模拟器”。<br/>
<br/>
　　下面这张示意图是 <a href="https://en.wikipedia.org/wiki/Xterm" rel="nofollow" target="_blank">xterm</a>。别看它长得丑，它的出现也算是“里程碑”了。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/2GRHQZetZPor718nRQB0D4JPscPyssaw4c2ufUOa-EF73PWb-SmTFNJYjILwZ5znmpzX6qEdHrT5-1R83TmZAKUVzr4IhfdRMYmpZQmZC16qqIcaaJOESrJUX798-qtrtUSIE9lEUH4"/><br/>
（xterm——“图形化终端模拟器”的祖师爷）</center><br/>
<h3>◇内部结构示意图</h3><br/>
　　很多人把“emulator”与“PTY”混为一谈。实际上两者处于【不同】层次。<br/>
　　在操作系统内部（内核），PTY 分为两部分实现，分别叫做“PTY master” ＆ “PTY slave”。master 负责与“terminal emulator”打交道；而用户通过 emulator 里面的 shell 启动的其它进程，则与 slave 打交道。<br/>
　　在这个环节中，“PTY slave”又进一步缩写为“PTS”。如果你用 <code>ps</code> 命令查看系统中的所有进程，经常会看到 PTS 之类的字样，指的就是这个玩意儿。<br/>
　　对普通用户而言，看到的是“终端模拟器”的界面，至于 PTY 内部的 master ＆ slave，通常是感觉不到滴。<br/>
<br/>
　　为了让大伙儿更加直观，再放一张 PTY 的结构示意图。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/KMWA2czF8HbdkSj0_H0bqVxaTdJB2yUGg46vvvAlCxGf0kwUEKH4Kn5_yr6NyFrEbOdlJTxRTt63lczZw3YsIgMrusiCn_I22jDnE2S1NMMJdhDPTDks1XwgZbkI-YFdqxw4N2Lmdz4"/><br/>
（TTY 示意图3：【伪终端】的内部结构图）</center><br/>
<a name="shell"> </a><br/>
<h2>★shell——命令行解释器</h2><br/>
　　费了好多口水，咱们终于聊到 shell 了。<br/>
　　顺便吐槽一下：<br/>
　　扫盲命令行的教程，很少会像俺这样，从最基本的概念说起。其导致的后果就是——很多人（甚至包括很多 Linux 程序员）都搞不清“shell、terminal、console、TTY、PTY、PTS”这些概念到底有啥区别。<br/>
　　在《<a href="../../2019/10/Systematic-Learning.md">如何【系统性学习】——从“媒介形态”聊到“DIKW 模型”</a>》一文中，俺特别强调了【基本概念/基础知识】的重要性。这也就是俺为啥前面要费这么多口水的原因。<br/>
<br/>
<h3>◇shell VS terminal</h3><br/>
　　前面所说的“终端”（terminal），本质上是：<b>基于【文本】的输入输出机制</b>。它并【不】理解具体的命令及其语法。<br/>
　　于是就需要引入 shell 这个玩意儿——shell 负责解释你输入的命令，并根据你输入的命令，执行某些动作（包括：启动其它进程）。<br/>
<br/>
<h3>◇常见 shell 举例</h3><br/>
　　常见的 shell 包括如下这些（为避免排名纠纷，按字母序列出）：<br/>
<blockquote style="background-color:#DDD;">bash<br/>
csh<br/>
fish<br/>
ksh<br/>
zsh</blockquote><br/>
　　在维基百科的“<a href="https://en.wikipedia.org/wiki/Comparison_of_command_shells" rel="nofollow" target="_blank">这个页面</a>”，列出了各种各样的 shell 及其功能特性的对照表。<br/>
　　如今影响力最大的 shell 是 <a href="https://en.wikipedia.org/wiki/Bash_(Unix_shell)" rel="nofollow" target="_blank">bash</a>（没有之一）。其名称源自“Bourne-again shell”，是 GNU 社区对 <a href="https://en.wikipedia.org/wiki/Bourne_shell" rel="nofollow" target="_blank">Bourne shell</a> 的重写，使之符合自由软件（GPL 协议）。<br/>
　　本文后续章节对 shell 的举例，如果没有做特殊说明，均指 bash 这个 shell。<br/>
<br/>
<br/>
<h2>★shell 的基本功能</h2><br/>
<h3>◇显示【命令行提示符】</h3><br/>
　　当你打开一个 shell，会看闪烁的光标左侧显示一个东东，那个玩意儿就是【命令行提示符】（参见下图）<br/>
<center><img alt="不见图 请翻墙" src="images/q5gzYkmF9TWwGKHNRJKXgE2EhnVrHdCuKSb_bij_33qGNGlHgLCg-FUmFqTGG0ySOa2r7ftvwcW8H1p1CwnGt_9F9q1Kb2PeeZlACYUk5B540yV0AxoLDcfaeSjjT62NeuEGh2hlYi8"/><br/>
（截图中的“命令行提示符”包含了：用户名、当前路径、$分隔符）</center><br/>
　　很多 shell 的“命令行提示符”都会包含【当前路径】。当你用 <code>cd</code> 命令切换目录，提示符也会随之改变。这有助于你搞清楚当前在哪个目录下，<b>可以有效避免误操作</b>。<br/>
　　下面这张图演示了——“命令行提示符”随着当前目录的变化而变化。<br/>
<center><img alt="不见图 请翻墙" src="images/RY0bVcLsYb8NFwMCu2XFeYEtaNopq9mI-XHZguPCFF7ojalynKSebm1LWVrENzZk_8msixbqyzGae8y5MxysSu2Q_GNl7N9l8AGt9ltXwsr5nUt-XWIuQH0l-scWPyO0qkm-y_D1oJs"/></center><br/>
　　大部分 shell 都可以让你自定义这个【命令行提示符】，使之显示更多的信息量。<br/>
　　比如说，可以让它显示：当前的时间、主机名、上一个命令的退出码......<br/>
　　（注：如果你需要开多个【远程】终端，去操作多个【不同】的系统，“主机名”就蛮有用）<br/>
<br/>
<h3>◇解析用户输入的【命令行】</h3><br/>
　　假设你想看一下 <code>/home</code> 这个目录下有哪些子目录，可以在 shell 中运行了如下命令：<br/>
<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">ls /home
</pre><br/>
　　当你输入这串命令并敲回车键，shell 会拿到这一行，然后它会分析出，空格前面的 <code>ls</code> 是一个外部命令，空格后面的 <code>/home</code> 是该命令的参数。<br/>
　　然后 shell 会启动这个外部命令对应的进程，并把上述参数作为该进程的启动参数。<br/>
<br/>
<h3>◇内部命令 VS 外部命令</h3><br/>
　　（刚才提到了【外部命令】这个词汇，顺便解释一下）<br/>
　　通俗地说，“内部命令”就是内置在 shell 中的命令；而“外部命令”则对应了某个具体的【可执行文件】。<br/>
　　当你在 shell 中执行“外部命令”，shell 会启动对应的可执行文件，从而创建出一个“子进程”；而如果是“内部命令”，就【不】产生子进程。<br/>
　　那么，如何判断某个命令是否为“外部命令”捏？<br/>
　　比较简单的方法是——用如下方式来帮你查找。如果某个命令能找到对应的可执行文件，就是“外部命令”；反之则是“内部命令”。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">whereis 命令名称
</pre><br/>
<h3>◇翻译【通配符】</h3><br/>
　　玩过命令行的同学，应该都知道：“星号”（<code>*</code>）与“问号”（<code>?</code>）可以作为通配符，用来模糊匹配文件名。<br/>
　　当你在 shell 中执行的命令包含了上述两个通配符，实际上是 shell 先把”通配符“翻译成具体的文件名，然后再传给相应命令。<br/>
<br/>
<h3>◇翻译某些【特殊符号】</h3><br/>
　　比如说：在 POSIX 系统中，通常用 <code>~</code> 来表示当前用户的【主目录】（home 目录）。<br/>
　　如果你在 shell 中用到了 <code>~</code> 这个符号，shell 会先把该符号翻译成“home 目录的【全路径】”，然后再传给相应命令。<br/>
<br/>
<h3>◇翻译【别名】</h3><br/>
　　很多 POSIX 的 shell 都支持用 <code>alias</code> 命令设置别名（把一个较长的命令串，用一个较短的别名来表示）。<br/>
　　设置了别名之后，当你在 shell 中使用“别名”，由 shell 帮你翻译成原先的命令串。<br/>
<br/>
　　举例：<br/>
　　在《<a href="../../2019/09/Netcat-Tricks.md">扫盲 netcat（网猫）的 N 种用法——从“网络诊断”到“系统入侵”</a>》一文中，俺使用如下命令创建了 <code>nc-tor</code> 这个别名。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">alias nc-tor='nc -X 5 -x 127.0.0.1:9050'
</pre>　　设置完之后，当你在 shell 中执行了这个 <code>nc-tor</code> 命令，shell 会把它自动翻译成 <code>nc -X 5 -x 127.0.0.1:9050</code><br/>
<br/>
<h3>◇历史命令</h3><br/>
　　大部分 shell 都会记录历史命令。你可以使用某些设定的快捷键（通常是【向上】的方向键），重新运行之前执行过的命令。<br/>
<br/>
<h3>◇自动补全</h3><br/>
　　很多 shell 都具备自动补全的功能。<br/>
　　该功能不仅指“命令”本身的自动补全，还包括对“命令的参数”进行自动补全。<br/>
<br/>
<h3>◇操作“环境变量”</h3><br/>
　　关于这部分，在下面的“环境变量”章节单独聊。<br/>
<br/>
<h3>◇“管道”与“重定向”</h3><br/>
　　关于这部分，在下面的“管道”章节单独聊。<br/>
<br/>
<h3>◇“进程控制”与“作业控制”</h3><br/>
　　关于这部分，在下面的“进程控制”与“作业控制”章节单独聊。<br/>
<br/>
<a name="process"> </a><br/>
<h2>★进程的启动与退出</h2><br/>
<h3>◇进程的【启动】及其【父子关系】</h3><br/>
　　一般来说，每个“进程”都是又另一个进程启动滴。如果“进程A”创建了“进程B”，则 A 是【父进程】，B 是【子进程】（这个“父子关系”很好理解——因为完全符合直觉）<br/>
　　有些同学会问，那最早的【第一个】进程是谁启动滴？<br/>
　　一般来说，第一个进程由【操作系统内核】（kernel）亲自操刀运行起来；而 kernel 又是由“引导扇区”中的“boot loader”加载。<br/>
<br/>
<h3>◇进程树</h3><br/>
　　在 POSIX 系统（Linux ＆ UNIX），所有的进程构成一个【单根树】的层次关系。进程之间的“父子关系”，体现在“进程树”就是树上的【父子节点】。<br/>
　　你可以使用如下命令，查看当前系统的“进程树”。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">pstree
</pre><br/>
<center><img alt="不见图 请翻墙" src="images/oyi3HQTSxSr8Jyov0B1gGtwvQrjuWsScmpmZamLS8KfpLAIUzUZ5AaZem5fcOnYsAGewJoVKviqGMirk8QVRFfPFC3YYe-Dbh_-czN3M0M_HHgOQh0BvxrGMVPnj6g4wrlmiJZwPVBM"/><br/>
（“进程树”的效果图。注：为了避免暴露俺的系统信息，特意【不】用自己系统的截图）</center><br/>
<h3>◇初始进程</h3><br/>
　　一般情况下，POSIX 系统的“进程树”的【根节点】就是系统开机之后【第一个】创建的进程，并且其进程编号（PID）通常是 1。这个进程称之为“初始进程”。<br/>
　　（注：上述这句话并【不够】严密——因为某些 UNIX 衍生系统的“进程树”，位于根节点的进程【不是】“初始化进程”。因为这种情况与本文的主题没太大关系，俺不打算展开讨论）<br/>
　　对于“大部分 UNIX 衍生系统”以及“2010年之前的 Linux 发行版”，系统中的“初始进程”名叫 <code>init</code>；<br/>
　　如今越来越多的 Linux 发行版采用 <a href="https://en.wikipedia.org/wiki/Systemd" rel="nofollow" target="_blank">systemd</a> 来完成系统引导之后的初始化工作。在这些发行版中，“初始进程”名叫 <code>systemd</code>。<br/>
<br/>
　　你可以用如下命令显示“进程树”中每个节点的“进程编号”（PID），然后就能看到编号为 1 的“初始进程”。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">pstree -p
</pre><br/>
<h3>◇进程的三种死法</h3><br/>
　　关于进程如何死亡，大致有如下三种情况：<br/>
<br/>
　　<b>自然死亡</b><br/>
　　如果某个进程把它该干的事情都干完了，自然就会退出。<br/>
　　这种是最常见的情况，也是最优雅的死法。俺习惯称作【自然死亡】。<br/>
<br/>
　　<b>自杀</b><br/>
　　如果某个进程的工作干到半当中，突然收到某个通知，让它立即退出。<br/>
　　这时候，进程会赶紧处理一些善后工作，然后自行了断——这就是【自杀】。<br/>
<br/>
　　<b>它杀</b><br/>
　　比“自杀”更粗暴的方式称之为【它杀】。也就是让“操作系统内核”直接把进程干掉。<br/>
　　在这种情况下，进程【不会】收到任何通知，因此也【不】可能进行任何善后事宜。<br/>
<br/>
　　（注：上述三种死法纯属比喻，以加深大伙儿的印象；不必太较真。十年前俺刚开博客，写过几篇帖子谈“<a href="../../2009/02/cxx-object-destroy-overview.md">C++ 对象之死</a>”，也用过类似比喻）<br/>
　　关于“自杀＆它杀”的方式，会涉及到【信号】。在下一个章节，俺会单独讨论【进程控制】，并会详细介绍“信号”的机制。<br/>
<br/>
<h3>◇“孤儿进程”及其“领养”</h3><br/>
　　如果某个进程死了（退出了），而它的子进程还【没】死，那么这些子进程就被形象地称之为“孤儿”，然后会被上述提到的【初始进程】“领养”——“初始进程”作为“孤儿进程”的父进程。<br/>
　　对应到“进程树”——“孤儿进程”会被重新调整到“进程树根节点”的【直接下级】。<br/>
<br/>
<a name="signal"> </a><br/>
<h2>★“进程控制”与“信号”</h2><br/>
<h3>◇用【Ctrl + C】杀进程</h3><br/>
　　为了演示这个效果，你可以执行如下命令：<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">ping 127.0.0.1
</pre><br/>
　　如果是 Windows 系统里的 <code>ping</code> 命令，它只会进行4次“乒操作”，然后就自己退出了；<br/>
　　但对于 POSIX 系统里面的 <code>ping</code> 命令，它会永远运行下去（直到被杀掉）。<br/>
　　当 ping 在运行的时候，如果你按下 <code>Ctrl + C</code> 这个组合键，就可以立即干掉这个 <code>ping</code> 进程。<br/>
<br/>
<h3>◇“Ctrl + C”背后的原理——【信号】（signal）</h3><br/>
　　当你按下了 <code>Ctrl + C</code> 这个组合键，当前正在执行的进程会收到一个叫做【SIGINT】的信号。<br/>
　　如果进程内部定义了针对该信号的处理函数，那么就会去执行这个函数，完成该函数定义的一些动作。一般而言，该函数会进行一些善后工作，然后进程退出。<br/>
　　如果进程【没有】定义相应的处理函数，则会执行一个【默认动作】。对于 SIGINT 这个信号而言，默认动作就是“进程退出”。<br/>
　　上述这2种情况，都属于前面所说的自杀。这2种属于【常规情况】。<br/>
<br/>
　　下面再来说【特殊情况】——有时候 <code>Ctrl + C</code>【无法】让进程退出。为啥会这样捏？<br/>
　　假如说，编写某个进程的程序员，定义了该信号的处理函数，但在这个函数内部，并【没有】执行“进程退出”这个动作。那么当该进程收到 SIGINT 信号之后，自然就【不会】退出。这种情况称之为——<b>信号被该进程【屏蔽】了</b>。<br/>
<br/>
<h3>◇【谁】发出“Ctrl + C”对应的信号？</h3><br/>
　　很多人（包括很多玩命令行的老手）都有一个【误解】——他们误以为是 shell 发送了 SIGINT 信号给当前进程。<b>其实不然！</b><br/>
　　在上述 ping 的例子中，当 ping 进程在持续运行之时，你的键盘输入是关联到 ping 进程的“标准输入”（stdin）。在这种情况下，shell 根本【无法】获取你的按键信息。<br/>
　　实际上，是【终端】获取了你的 <code>Ctrl + C</code> 组合键信息，并发送了 SIGINT 信号。因为【终端】处于更底层，它负责承载你所有的输入输出。因此，它当然可以截获用户的某个特殊的组合键（比如：<code>Ctrl + C</code>），并执行某些特定的动作。<br/>
　　聊到这里，大伙儿会发现——<br/>
如果没有正确理解“终端”与“shell”这两者的关系，就会犯很多错误（造成很多误解）。<br/>
<br/>
　　有的读者可能会问：“终端”如何知道【当前进程】是哪一个？（能想到这点，通常是比较爱思考滴）<br/>
　　俺来解答一下：<br/>
　　当 shell 启动了某个进程，它当然可以拿到这个进程的编号（pid），于是 shell 会调用某个系统 API（比如 <code>tcsetpgrp</code>）把“进程编号”与 shell 所属的“终端”关联起来。<br/>
　　当“终端”需要发送 SIGINT 信号时，再调用另一个系统 API（比如 <code>tcgetpgrp</code>），就可以知道当前进程的编号。<br/>
<br/>
<h3>◇对比杀进程的几个信号：SIGINT、SIGTERM、SIGQUIT、SIGKILL</h3><br/>
　　<b>SIGINT</b><br/>
　　在大部分 POSIX 系统的各种终端上，<code>Ctrl + C</code> 组合键触发的就是这个信号。<br/>
　　通常情况下，进程收到这个信号后，做完相关的善后工作，就自行了断（自杀）。<br/>
<br/>
　　<b>SIGTERM</b><br/>
　　这个信号基本类似于 SIGINT。<br/>
　　它是 <code>kill</code> ＆ <code>killall</code> 这两个命令【默认】使用的信号。<br/>
　　也就是说，当你用这俩命令杀进程，并且【没有】指定信号类型，那么 <code>kill</code> 或 <code>killall</code> 用的就是这个 SIGTERM 信号。<br/>
<br/>
　　<b>SIGQUIT</b><br/>
　　这个信号类似于前两个（SIGINT ＆ SIGINT），差别在于——进程在退出前会执行“<a href="https://en.wikipedia.org/wiki/Core_dump" rel="nofollow" target="_blank">core dump</a>”操作。<br/>
　　一般而言，只有程序员才会去关心“core dump”这个玩意儿，所以这里就不细聊了。<br/>
<br/>
　　<b>SIGKILL</b><br/>
　　在杀进程的几个信号中，这个信号是是最牛逼的（也是最粗暴的）。<br/>
　　前面三个信号都是【可屏蔽】滴，而这个信号是【不可屏蔽】滴。<br/>
　　当某个进程收到了【SIGKILL】信号，该进程自己【完全没有】处理信号的机会，而是由操作系统内核直接把这个进程干掉。<br/>
　　此种行为可以形象地称之为“它杀”。<br/>
　　当你用下列这些命令杀进程，本质上就是在发送这个信号进行【它杀】。【SIGKILL】这个信号的编号是 <code>9</code>，下列这些命令中的 <code>-9</code> 参数就是这么来滴。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">kill -9 进程号
kill -KILL 进程号

killall -9 进程名称
killall -KILL 进程名称
killall -SIGKILL 进程名称
</pre><br/>
　　请注意：<br/>
　　<b>【它杀】是一种比较危险的做法，可能导致一些副作用。</b>只有当你用其它各种方式都无法干掉某个进程，才考虑用这招。<br/>
<br/>
　　为了方便对照上述这4种，俺放一个表格如下：<br/>
<center><table border="1" cellpadding="3" cellspacing="0"><tbody>
<tr style="background:lightgrey;"><th>信号名称</th><th>编号</th><th>能否屏蔽</th><th>默认动作</th><th>俗称</th></tr>
<tr><td>SIGINT</td><td>2</td><td>YES</td><td>进程自己退出</td><td>自杀</td></tr>
<tr><td>SIGTERM</td><td>15</td><td>YES</td><td>进程自己退出</td><td>自杀</td></tr>
<tr><td>SIGQUIT</td><td>3</td><td>YES</td><td>执行 core dump<br/>进程自己退出</td><td>自杀</td></tr>
<tr><td>SIGKILL</td><td>9</td><td>NO</td><td>进程被内核干掉</td><td>它杀</td></tr>
</tbody></table></center><br/>
<h3>◇kill VS killall</h3><br/>
　　这两个的差别在于——前者用“进程号”，后者用”进程名“（也就是可执行文件名）。<br/>
　　对于新手而言，<br/>
如果用 <code>kill</code> 命令，你需要先用 <code>ps</code> 命令打印出当前进程清单，然后找到你要杀的进程的编号；而如果要用 <code>killall</code> 命令，就比较省事（比较傻瓜化）。但万一碰到有多个【同名】进程在运行，而你只想干掉其中一个，那么就得老老实实用 <code>kill</code> 了。<br/>
<br/>
<h3>◇进程退出码</h3><br/>
　　任何一个进程退出的时候，都对应某个【整数类型】的“退出码”。<br/>
　　按照 POSIX 系统（UNIX ＆ Linux）的传统惯例——<br/>
当“退出码”为【零】，表示“成功 or 正常状态”；<br/>
当“退出码”【非零】，表示“失败 or 异常状态”。<br/>
<br/>
<h3>◇暂停进程</h3><br/>
　　刚才聊“杀进程”的时候提到了“自杀 VS 它杀”。前者比较“温柔”；而后者比较“粗暴”。<br/>
　　对于暂停进程，也有“温柔 ＆ 野蛮”两种玩法。而且也是用 <code>kill</code> 命令发信号。<br/>
<br/>
　　<b>【温柔】式暂停（SIGTSTP）</b><br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">kill -TSTP 进程编号
</pre>　　这个【SIGTSTP】信号类似前面提及的【SIGINT】——<br/>
1. 两者默认都绑定到组合键（【SIGINT】默认绑定到组合键【<code>Ctrl + C</code>】；【SIGTSTP】默认绑定到组合键【<code>Ctrl + Z</code>】）<br/>
2. 两者都是【可】屏蔽的信号。也就是说，如果某个进程屏蔽了【SIGTSTP】信号，你就【无法】用该方式暂停它。这时候你就得改用【粗暴】的方式（如下）。<br/>
<br/>
　　<b>【粗暴】式暂停（SIGSTOP）</b><br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">kill -STOP 进程编号
</pre>　　这个【SIGSTOP】信号与前面提及的【SIGKILL】有某种相同之处——这两个信号都属于【不可屏蔽】的信号。也就是说，收到【SIGSTOP】信号的进程【无法】抗拒被暂停（suspend）的命运。<br/>
<br/>
　　与“杀进程”的风格类似——当你想要暂停某进程，应该先尝试“温柔”的方法，搞不定再用“粗暴”的方法（套用咱们天朝的老话叫“先礼后兵”）。<br/>
<br/>
<h3>◇恢复进程</h3><br/>
　　当你想要重新恢复（resume）被暂停的进程，就用如下命令（该命令发送信号【SIGCONT】）<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">kill -CONT 进程编号
</pre><br/>
<h3>◇引申阅读</h3><br/>
　　除了前面几个小节提到的信号，POSIX 系统还支持其它一些信号，具体参见维基百科的“<a href="https://en.wikipedia.org/wiki/Signal_(IPC)" rel="nofollow" target="_blank">这个页面</a>”。<br/>
<br/>
<a name="job"> </a><br/>
<h2>★作业控制（job）</h2><br/>
　　聊完了“进程控制”，再来聊“作业控制”。<br/>
　　（注：这里所说的“作业”是从洋文 job 翻译过来滴）<br/>
<br/>
<h3>◇同步执行（前台执行） VS 异步执行（后台执行）</h3><br/>
　　大部分情况下，你在 shell 中执行的命令都是“同步执行”（或者叫“前台执行”）。对于这种方式，只有当命令运行完毕，你才会重新看到 shell 的“命令行提示符”。<br/>
　　如果你以“异步执行”的方式启动某个外部命令，在这个命令还没有执行完的时候，你就可以重新看到“命令行提示符”。<br/>
<br/>
　　请注意：<br/>
　　对于【短】寿命的外部命令（耗时很短的外部命令），“同步/异步”两种方式其实【没】啥区别。比如 <code>ls</code> 命令通常很快就执行完毕，你就感觉不到上述两种方式的差异。<br/>
　　只有当你执行了某个【长】寿命的外部命令（其执行时间至少达到若干秒），上述这两种方式才会体现出差别。<br/>
<br/>
　　到目前为止，本文之前聊的命令执行方式，都属于“同步执行”；如果想用【异步】，需要在整个命令的最末尾追加一个半角的 <code>&amp;</code> 符号。<br/>
<br/>
　　<b>【同步】方式举例</b><br/>
　　下列命令以【同步】的方式启动火狐浏览器，只有当你关闭了火狐，才会重新看到 shell 的命令行提示符。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">firefox
</pre><br/>
　　<b>【异步】方式举例</b><br/>
　　下列命令以【异步】的方式启动火狐浏览器。你刚敲完回车，就会重新看到 shell 的“命令行提示符”（此时火狐依然在运行）<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">firefox &amp;
</pre><br/>
　　以“同步”方式启动的进程，称作“【前台】进程”；反之，以“异步”方式启动的进程，称作“【后台】进程”。<br/>
<br/>
<h3>◇“前台”切换到“后台”</h3><br/>
　　假设当前的 shell 正在执行某个长寿命的【前台】进程，你可以按【<code>Ctrl + Z</code>】，就可以让该进程变为【后台】进程——此时你立即可以看到“命令提示符”。<br/>
　　只要你不是太健忘，应该记得前一个章节有提到过【<code>Ctrl + Z</code>】这个组合键——它用来实现”【温柔】式暂停“，其原理是：向目标进程发送【SIGTSTP】信号。<br/>
<br/>
<h3>◇“后台”切换到“前台”</h3><br/>
　　假设当前 shell 正在执行某个后台进程。由于该进程在【后台】执行，此时有“命令提示符”，然后你在 shell 中执行 <code>fg</code> 命令，就可以把该后台进程切换到【前台】。<br/>
<br/>
　　某些爱思考的同学会问了——如果同时启动了【多个】“后台进程”，<code>fg</code> 命令会切换哪一个捏？<br/>
　　在这种情况下，<code>fg</code> 命令切换的是【最后启动】的那个。<br/>
<br/>
　　如果你有 N 个“后台进程”，你想把其中的某个切换为“前台进程”，这时候就需要用到 <code>jobs</code> 命令。该命令与乔布斯同名 :)<br/>
　　举例：<br/>
　　假设俺同时启动了 vim 与 emacs 作为后台进程，先用 <code>jobs</code> 命令列出所有的后台进程。假设该命令的输出是如下这个样子。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">$ jobs
[1] running    vim
[2] running    emacs
</pre>　　在上述的终端窗口，中括号里面的数字称作“job id”。你可以用 <code>fg</code> 命令搭配“job id”，把某个后台进程切换到前台。<br/>
　　（在本例中）如果你想切换 emacs 到前台，就运行 <code>fg %2</code>，如果想切换 vim 就运行 <code>fg %1</code>（以此类推）<br/>
<br/>
<h3>◇引申阅读</h3><br/>
　　想进一步了解“作业控制”，可以参考维基百科（<a href="https://en.wikipedia.org/wiki/Job_control_(Unix)" rel="nofollow" target="_blank">这个链接</a>）。<br/>
<br/>
<a name="environment-variable"> </a><br/>
<h2>★环境变量（environment variable）</h2><br/>
<h3>◇“环境变量”是啥？</h3><br/>
　　所谓的“环境变量”，你可以通俗理解为某种【名值对】——每个“环境变量”都有自己的【名称】和【值】。并且名称必须是【唯一】滴。<br/>
<br/>
<h3>◇如何设置/修改“环境变量”？</h3><br/>
　　在 bash（或兼容 bash 的其它 shell），你可以用 export 设置环境变量。比如下面这个命令设置了一个“环境变量”，其名称是 <code>abc</code>，其值是 <code>xyz</code><br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">export abc=xyz
</pre><br/>
　　假如你要设置的【值】包含空格，记得用双引号引用该值（示例如下）。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">export abc="program think"
</pre><br/>
<h3>◇如何查看“环境变量”？</h3><br/>
　　设置完之后，你可以用 <code>env</code> 命令查看。该命令会列出【当前 shell】中的【全部】“环境变量”。<br/>
<br/>
<h3>◇“环境变量”的【可见性】和【可继承性】</h3><br/>
　　某个进程设置的“环境变量”，其【可见性】仅限于该进程及其子进程（也就是“进程树”中，该进程所在的那个枝节）。<br/>
　　基于上述的【可见性】原则，你在某个 shell 中设置的“环境变量”，只在“该 shell 进程本身”，以及通过该 shell 进程启动的“其它子进程”，才能看到。<br/>
<br/>
　　另外，如果系统关机，所有进程都会退出，那么你采用上一个小节（export 方式）设置的“环境变量”也就随之消失了。<br/>
　　为了让某个“环境变量”永久生效，需要把相应的 <code>export</code> 命令添加到该 shell 的初始化配置文件中。对于 bash 而言，也就是 <code>~/.bashrc</code> 或者 <code>~/.profile</code><br/>
　　估计有些同学会问：上述这两个初始化配置文件，有啥差别捏？<br/>
　　俺如果有空，会单独写一篇关于 bash 的定制教程，到时候再聊这个话题。<br/>
<br/>
<h3>◇“环境变量”有啥用？</h3><br/>
　　通俗地说，“环境变量”是某种比较简单的 IPC 机制（进程通讯机制）。可以让两个进程共享某个简单的文本信息。<br/>
　　举例：<br/>
　　很多知名的软件（比如：curl、emacs）都支持“以环境变量设置代理”。<br/>
　　如果你按照它的约定，在 shell 中设置了约定名称和格式的“环境变量”，然后在【同一个】shell 中启动这个软件，（由于环境变量的【可继承性】）该软件就会看到这个“环境变量”，并根据“环境变量”包含的信息，设置代理。<br/>
<br/>
<a name="standard-stream"> </a><br/>
<h2>★“标准流”（standard stream）与“重定向”（redirection）</h2><br/>
<h3>◇进程的3个“标准流”</h3><br/>
　　在 POSIX 系统（Linux ＆ UNIX）中，每个进程都内置了三个“标准流”（<a href="https://en.wikipedia.org/wiki/Standard_streams" rel="nofollow" target="_blank">standard stream</a>），分别称作：“标准输入流”（stdin），“标准输出流”（stdout），“标准错误输出流”（stderr）。<br/>
　　当进程启动后，在默认情况下，stdin 对接到终端的【输入】；stdout ＆ stderr 对接到终端的【输出】。示意图如下：<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/JEfAB2UXDSRwczojJZOXEDAK5xH4E6YdksxZuIqq_5Tfe6xjwHrbeYX5EETlsHxQYk1Wm_wXg-ajpjIu3lHzYLeYJML5xxQQgsuhnZodUcC5jbtdLQ7_AflDdUkEfAthqHqBly3CQPo"/><br/>
（三个【标准流】的示意图）</center><br/>
　　如果你是程序员，俺补充一下：<br/>
　　当你在程序中打开某个文件，会得到一个“文件描述符”（洋文叫“<a href="https://en.wikipedia.org/wiki/File_descriptor" rel="nofollow" target="_blank">file descriptor</a>”，简称 fd）。可以用 fd 对该文件进行读写。fd 本身是个整数。<br/>
　　而进程的三个【标准流】，就相当于是三个特殊的 fd。当进程启动时，操作系统就已经把这三个 fd 准备好了。<br/>
　　由于这三个玩意儿是特殊滴，所以它们的数值分别是：0、1、2（参见上图中 # 后面的数字）。<br/>
<br/>
<h3>◇演示“标准流”的实际效果</h3><br/>
　　在本文前面的某个章节，俺已经用 gif 动画演示了终端的“行模式”。<br/>
　　动画中的 <code>cat</code> 命令同样可以用来演示“标准输入输出”。俺把那个动画再贴一次。<br/>
<br/>
<center><img alt="不见图 请翻墙" src="images/PPet_RllllnSmYALmxV56ohy5NZz1kj76GzbmcvM9HJDrqY6h74otCFL1E0rG_lEKnALViM8zv2E4BOj4bUUTixzD_QTTXsmoh0-U3dxJROpiAfvW2vHZ69s2vpYlq88-6FBngqgzSQ"/><br/>
（动画：“标准输入输出”的效果）</center><br/>
　　请注意，第1行 <code>test</code> 是针对 <code>cat</code> 进程的【输入】，对应于【stdin】（你之所以能看到这行，是因为前面所说的【终端回显】）<br/>
　　第2行 <code>test</code> 是 <code>cat</code> 进程拿到输入文本之后的原样输出，对应于【stdout】。<br/>
<br/>
<h3>◇“标准流”的【<a href="https://en.wikipedia.org/wiki/Redirection_(computing)" rel="nofollow" target="_blank">重定向</a>】</h3><br/>
　　所谓的【重定向】大体上分两种：<br/>
<br/>
　　<b>1. 【输入流】重定向</b><br/>
　　把某个文件重定向为 stdin；此时进程通过 stdin 读取的是该文件的内容。<br/>
　　这种玩法使用小于号（<code>&lt;</code>）<br/>
<br/>
　　<b>2. 【输出流】重定向</b><br/>
　　把 stdout 重定向到某个文件；此时进程写入 stdout 的内容会【覆盖 or 追加】到这个文件。<br/>
　　这种玩法使用【单个】大于号（<code>&gt;</code>）或【两个】大于号（<code>&gt;&gt;</code>）。前者用于【覆盖】文件内容，后者用于【追加】文件内容。<br/>
<br/>
　　另外，有时候你会看到 <code>2&gt;&amp;1</code> 这种写法。它表示：把 stderr 合并到 stdout。<br/>
　　（注：前面俺提到过——stdout 是“数值为 1 的文件描述符”；stderr 是“数值为 2 的文件描述符”）<br/>
<br/>
<br/>
<h3>◇【重定向】举例</h3><br/>
　　<b>cat 的例子</b><br/>
　　下面这个命令把某个文件重定向到 <code>cat</code> 的 stdin。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">cat &lt; 文件名
</pre><br/>
　　很多菜鸟容易把上面的命令与下面的命令搞混淆。<br/>
　　请注意：上面的命令用的是【输入重定向】，而下面的命令用的是【命令行参数】。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">cat 文件名
</pre><br/>
　　<code>cat</code> 命令还可以起到类似“文件复制”的效果。<br/>
　　比如你已经有个 <code>文件1</code>，用下面这种玩法，会创建出一个内容完全一样的 <code>文件2</code>。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">cat &lt; 文件1 &gt; 文件2
</pre>　　某些同学会问了：既然可以这么玩，为啥还需要用 <code>cp</code> 命令进行文件复制捏？<br/>
　　原因在于：<code>cat</code> 的玩法，只保证内容一样，其它的不管；而 <code>cp</code> 除了复制文件内容，还会确保“目标文件”与“源文件”具有相同的属性（比如 mode）。<br/>
<br/>
　　<b>更多的例子</b><br/>
　　在之前那篇《<a href="../../2019/09/Netcat-Tricks.md">扫盲 netcat（网猫）的 N 种用法——从“网络诊断”到“系统入侵”</a>》，里面介绍了十多种 nc 的玩法。很多都用到了【重定向】。<br/>
<br/>
<a name="anonymous-pipe"> </a><br/>
<h2>★“匿名管道”（anonymous pipe）</h2><br/>
<h3>◇“匿名管道”的【原理】</h3><br/>
　　在大部分 shell 中，使用竖线符号（<code>|</code>）来表示【管道符】。用它来创建一个【<a href="https://en.wikipedia.org/wiki/Anonymous_pipe" rel="nofollow" target="_blank">匿名管道</a>】，使得前一个命令（进程）的“标准输出”关联到后一个命令（进程）的“标准输入”。<br/>
<br/>
<h3>◇举例</h3><br/>
　　俺曾经在“<a href="../../2013/01/cross-host-use-gfw-tool.md">这篇博文</a>”中介绍过——如何用 <code>netstat</code> 查看当前系统的监听端口。<br/>
　　对于 Windows 系统，可以用如下命令：<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">netstat -an | find "LISTEN"
</pre>　　对于 POSIX 系统，可以用如下命令：<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">netstat -an | grep "LISTEN"
</pre><br/>
　　在上述两个例子中，都用到了【管道符】。因为 <code>netstat -an</code> 这个命令的输出可能会很多，先把它的输出通过【匿名管道】丢给某个专门负责过滤的命令（比如：POSIX 的 grep 或 Windows 的find）。当这个过滤命令拿到 <code>netstat</code> 的输出内容，再根据你在命令行参数中指定的【关键字】（也就是上述例子中的 <code>LISTEN</code>），过滤出包含【关键字】的那些【行】。<br/>
　　最终，你看到的是“过滤命令”（grep 或 find）的输出。<br/>
<br/>
<h3>◇【串联的】匿名管道（chained pipeline）</h3><br/>
　　前面的例子，可以用来列出当前系统中所有的监听端口。<br/>
　　现在，假设你运行了 Tor Browser，然后想看看它到底有没有开启 <code>9150</code> 这个监听端口，那么你就可以在上述命令中进行【二次过滤】（具体命令大致如下）。这就是所谓的【串联】。<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">netstat -an | grep "LISTEN" | grep "9150"
</pre><br/>
<a name="batch"> </a><br/>
<h2>★批处理（batch）</h2><br/>
<h3>◇啥是“批处理”？</h3><br/>
　　通俗地说就是：同时执行多个命令。<br/>
　　为了支持“批处理”，shell 需要提供若干语法规则。而且不同类型的 shell，用来搞“批处理”的语法规则也存在差异。<br/>
　　在本章节中，俺以 bash 来举例。<br/>
<br/>
<h3>◇【无】条件的“批处理”</h3><br/>
　　如果你把多个命令写在同一行，并且命令之间用半角分号隔开，这种玩法就属于【无条件】的批处理执行。<br/>
　　举例：<br/>
　　假设当前目录下有一个 <code>abc.txt</code> 文件，然后要在当前目录下创建一个名为 <code>xxx</code> 的子目录，并把 <code>abc.txt</code> 移动到这个新创建的子目录中。你可以用如下方式搞定（只用【一行】命令）<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">mkdir ./xxx/; mv abc.txt ./xxx/
</pre><br/>
　　为啥这种方式叫做“【无条件】批处理”捏？因为不管前一个“子命令”是否成功，都会继续执行下一个“子命令”。<br/>
<br/>
　　请注意：<br/>
　　虽然俺上述举例只使用了两个“子命令”，但实际上这种玩法可以把 N 个“子命令”串起来。<br/>
<br/>
<h3>◇【有】条件的“批处理”</h3><br/>
　　与“无条件”相对应的，当然是“有条件”啦。<br/>
　　这种玩法的意思是——后一个“子命令”是否执行，取决于【前一个】“子命令”的结果（成功 or 失败）。<br/>
　　（注：如何界定“成功/失败”，请参见前面某个章节聊到的【进程退出码】）<br/>
　　【有】条件的批处理，常见的方式有两种，分别是【逻辑与】、【逻辑或】。<br/>
<br/>
　　<b>逻辑与（语法：<code>&amp;&amp;</code>）</b><br/>
　　只要前面的某个“子命令”【失败】了，就【不再】执行后续的“子命令”。<br/>
　　举例：<br/>
　　还是拿前一个小节的例子。如下方式使用了“逻辑与”。如果创建子目录失败，就【不再】执行“移动文件”的操作<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">mkdir ./xxx/ &amp;&amp; mv abc.txt ./xxx/
</pre><br/>
　　<b>逻辑或（语法：<code>||</code>）</b><br/>
　　只要前面的某个“子命令”【成功】了，就【不再】执行后续的“子命令”。<br/>
　　举例：<br/>
　　把上述例子进一步扩充，变为如下：<br/>
<pre class="shell" style="background-color:Black;color:LawnGreen;">mkdir ./xxx/ &amp;&amp; mv abc.txt ./xxx/ || echo "FAILED!!!"
</pre><br/>
　　这个有点复杂，俺稍微解释一下：<br/>
　　你把前面两句看作一个【整体】。其执行的逻辑参见前面所说的“逻辑与”。然后这个“整体”与后面的那句 <code>echo</code> 再组合成【逻辑或】的关系。<br/>
　　也就是说，如果前面的“整体”成功了，那么就【不】执行 <code>echo</code>（【不】打印错误信息）。反之，如果前面的“整体”失败了，就会打印错误信息。<br/>
<br/>
<br/>
<h2>★shell 脚本</h2><br/>
　　虽然前一个章节拿 bash 来举例。但其实有很多其它类型的 shell 都支持类似的“批处理”机制。<br/>
　　只要某个 shell 支持刚才所说的【有条件批处理】的机制，它就已经很接近【编程语言】了。<br/>
　　于是很自然地，那些 shell 的作者就会把 shell 逐步发展成某种【脚本语言】的解释器。然后就有了如今的“shell script”（shell 脚本）和“shell 编程”。<br/>
　　由于“shell 编程”这个话题比较大。哪怕俺只聊 bash 这个 shell 的编程，也足够写上几万字的博文。考虑到本文已经很长了，这个话题就不再展开。<br/>
　　对此感兴趣的同学，可以参考俺分享的电子书。具体参见<a href="https://github.com/programthink/books" target="_blank">电子书清单</a>的如下几本（这几本都位于【IT类 / 操作系统 / 使用教程】分类目录下）<br/>
《<a href="https://docs.google.com/document/d/1Zw8XD56F6rCi899UxIE-0sKoXWr2WGqiUNcRl70kIYk/" target="_blank">Shell 脚本学习指南</a>》（Classic Shell Scripting）<br/>
《<a href="https://docs.google.com/document/d/1Nk83xAbRUdcgqUBSfDCwozA3-EUFeBz-nrpf1G7x-j0/" target="_blank">Linux 与 UNIX Shell 编程指南</a>》（Linux and UNIX Shell Programming）<br/>
《<a href="https://docs.google.com/document/d/1BYSgrSViVZyDTQcuhWEFAc_uc0YZvkIoQYLmv0yWo_A/" target="_blank">高级 Bash 脚本编程指南</a>》（Advanced Bash-Scripting Guide）<br/>
　　上述这几本，都属于俺在《<a href="../../2019/10/Systematic-Learning.md">如何【系统性学习】——从“媒介形态”聊到“DIKW 模型”</a>》中提到的【入门性读物】。最后一本书的名称中虽然有”高级“字样，但别担心——其内容的5个部分，有4部分都是在讲基础的东西，只有最后一部分才稍微有一点点深度。<br/>
<br/>
<br/>
<h2>★结尾</h2><br/>
　　由于这篇涉及的内容比较杂，跨度也比较大。可能会有一些俺没覆盖到的地方。欢迎在博客留言中补充。<br/>
　　如果你发现本文的错误之处，也欢迎批评指正 :)<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2013/10/linux-newbie-guide.md">扫盲 Linux：新手如何搞定 Linux 操作系统</a>》<br/>
《<a href="../../2013/10/linux-distributions-guide.md">扫盲 Linux：如何选择发行版</a>》<br/>
《<a href="../../2019/09/Netcat-Tricks.md">扫盲 netcat（网猫）的 N 种用法——从“网络诊断”到“系统入侵”</a>》<br/>
《<a href="../../2013/01/cross-host-use-gfw-tool.md">多台电脑如何【共享】翻墙通道——兼谈【端口转发】的几种方法</a>》<br/>
《<a href="../../2019/04/Proxy-Tricks.md">如何让【不支持】代理的网络软件，通过代理进行联网（不同平台的 N 种方法）</a>》<br/>
《<a href="../../2012/10/system-vm-0.md">扫盲操作系统虚拟机</a>》（系列）<br/>
《<a href="../../2019/10/Systematic-Learning.md">如何【系统性学习】——从“媒介形态”聊到“DIKW 模型”</a>》
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2019/11/POSIX-TUI-from-TTY-to-Shell-Programming.html
