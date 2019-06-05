# 澄清“自由软件、开源软件”相关概念及许可证的误解 

-----

<div class="post-body entry-content">
<h2>★引子</h2><br/>
　　长期以来，一直有很多读者不太明白“自由软件”与“开源软件”的差异。除此之外，还经常会有其它的一些误解。<br/>
　　昨天正好在<a href="https://github.com/programthink/books" target="_blank">俺的网盘</a>上分享了《若为自由故——自由软件之父理查德·斯托曼传》一书的中文版，所以顺便来聊聊相关的话题。<br/>
<a name="more"></a><br/>
<br/>
<h2>★误解1——“提供源代码的软件”就是“开源软件”</h2><br/>
　　这可能是最常见的误解，所以俺把这条放在本文第一条。<br/>
　　“提供源代码”只是“开源软件”的【必要条件】，但【不是】充分条件。换句话说：不提供源码的一定不是开源软件，提供源码的不一定是开源软件（有点像绕口令）<br/>
　　所谓的“开源软件”，是有严格定义滴！目前业界的共识是采用“<a href="https://zh.wikipedia.org/wiki/%E5%BC%80%E6%94%BE%E6%BA%90%E4%BB%A3%E7%A0%81%E4%BF%83%E8%BF%9B%E4%BC%9A" rel="nofollow" target="_blank">开放源代码促进会</a>”（洋文叫“Open Source Initiative”，缩写是 OSI）给出的定义。<br/>
　　其定义很长，包含很多项，俺就不全文列出啦。想看的同学，请猛击 OSI【官网】的“<a href="https://opensource.org/osd" rel="nofollow" target="_blank">这个链接</a>”。不懂洋文的同学，请看中文维基百科的“<a href="https://zh.wikipedia.org/wiki/%E5%BC%80%E6%BA%90%E8%BD%AF%E4%BB%B6" rel="nofollow" target="_blank">这个页面</a>”。<br/>
<br/>
　　为了让大伙儿加深印象，举 UNIX 的例子。<br/>
　　说到 UNIX，在计算机史上那可是大名鼎鼎滴。其背景，俺就不多说啦。当年（上世纪70年代）UNIX 隶属于商业公司 <a href="https://en.wikipedia.org/wiki/AT%26T" rel="nofollow" target="_blank">AT&amp;T</a>。那年头，AT&amp;T 销售 UNIX 的时候都会附送【全部源代码】。但即使这样，（以如今的标准来看）UNIX 也【不能】算是开源软件。因为用户拿到源代码之后，受限于保密条款，【无法】随意分发源代码。<br/>
<br/>
<br/>
<h2>★误解2——把“开源软件”等同于“自由软件”（混淆这两者）</h2><br/>
　　“开源软件”与“自由软件”这两个概念有很大的重叠，导致很多人混淆这两者（误以为这俩概念可以互换）。<br/>
　　但其实这两者在理念上有【很大】差异。考虑到本文是面向普通读者，俺尽可能用通俗的大白话来说一下两者的共性和差异。<br/>
<br/>
<h3>◇“开源软件”与“自由软件”的【共性】</h3><br/>
　　共性大致有如下几条：<br/>
1. 两者都要求——源代码要【公开】<br/>
2. 两者都要求——公开的源代码必须具备【完整性】（换句话说，用公开的源码必须能重新生成该软件）<br/>
3. 两者都要求——公开的源代码要允许【随意分发】<br/>
4. 两者都要求——公开的源代码要允许【随意修改】<br/>
5. 两者都要求——【不能】限制商业使用<br/>
......<br/>
（还有其它一些共同点，考虑到篇幅，就不再列举啦）<br/>
<br/>
<h3>◇“开源软件”与“自由软件”在【理念】方面的【差异】</h3><br/>
　　“开源软件”的立足点更加侧重于——源代码的【开放性】。<br/>
　　“自由软件”的立足点更加侧重于——软件用户的【自由度】。<br/>
<br/>
　　考虑到很多人不太清楚“用户的自由”，俺来介绍一下——<br/>
　　FSF 的创始人 <a href="https://zh.wikipedia.org/wiki/%E7%90%86%E6%9F%A5%E5%BE%B7%C2%B7%E6%96%AF%E6%89%98%E6%9B%BC" rel="nofollow" target="_blank">理查德·斯托曼</a>（Richard Matthew Stallman，人称 RMS）给出了【用户的四大自由】：<br/>
<blockquote style="background-color:#DDD;">自由度0：<br/>
无论用户出于何种目的，必须可以按照用户意愿，自由地运行该软件。<br/>
<br/>
自由度1：<br/>
用户可以自由地学习并修改该软件，以此来帮助用户完成用户自己的计算。<br/>
（作为前提，用户必须可以访问到该软件的源代码）<br/>
<br/>
自由度2：<br/>
用户可以自由地分发该软件的拷贝，这样就可以助人。<br/>
<br/>
自由度3：<br/>
用户可以自由地分发该软件修改后的拷贝。借此，用户可以把改进后的软件分享给整个社区令他人也从中受益。<br/>
（作为前提，用户必须可以访问到该软件的源代码）</blockquote><br/>
　　更详细的介绍可以参见 FSF（<a href="https://zh.wikipedia.org/wiki/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6%E5%9F%BA%E9%87%91%E4%BC%9A" rel="nofollow" target="_blank">自由软件基金会</a>）【官网】的文章（如下）：<br/>
《<a href="https://www.gnu.org/philosophy/free-sw.html" rel="nofollow" target="_blank">What is free software?</a>》（原文）<br/>
《<a href="https://www.gnu.org/philosophy/free-sw.zh-cn.html" rel="nofollow" target="_blank">什么是自由软件？</a>》（上述的中文翻译）<br/>
<br/>
　　引申阅读：<br/>
　　<a href="https://github.com/programthink/books" target="_blank">俺的网盘</a>上分享了【自由软件运动创始人】理查德·斯托曼（RMS）的“选集”和“传记”，分别如下：<br/>
《<a href="https://docs.google.com/document/d/1kTL8VE6AoUZCJY2OJ3qv39nJpFn7zj6EacAHXyNXfEY/" target="_blank">自由软件，自由社会——理查德·斯托曼选集</a>》<br/>
《<a href="https://docs.google.com/document/d/1J6AfA8Z4uUiMS7-Or9WchCuiDEc-G6Ar5D3600jxYSQ/" target="_blank">若为自由故——自由软件之父理查德·斯托曼传</a>》<br/>
<br/>
<h3>◇“开源软件”与“自由软件”在【许可证】方面的【差异】</h3><br/>
　　（注：本文后续部分提到的“许可证、许可协议、license”三者指同一个东东）<br/>
　　刚才俺聊到了“自由软件”与“开源软件”在理念上的差异。这些差异自然也会反应到 license 的条款上。比如有些 license 立足于“开源”，还有些 license 立足于“自由”。<br/>
　　为了方便大伙儿，给出一个维基百科链接（在“<a href="https://zh.wikipedia.org/wiki/%E8%87%AA%E7%94%B1%E5%8F%8A%E9%96%8B%E6%94%BE%E5%8E%9F%E5%A7%8B%E7%A2%BC%E8%BB%9F%E9%AB%94%E8%A8%B1%E5%8F%AF%E8%AD%89%E6%AF%94%E8%BC%83" rel="nofollow" target="_blank">这里</a>”）。该页面对比了各种不同的软件许可协议。在【第二个】表格中，有一栏是“FSF 认可”——<b>凡是被 FSF 认可的，都可以算是【自由软件】许可证</b>；另外还有一栏是“OSI 认证”——<b>凡是被 OSI 认证的，都可以算是【开源软件】许可证</b>。<br/>
<br/>
<br/>
<h2>★误解3——以为“自由软件”排斥商业公司</h2><br/>
　　长期以来，很多商业公司对“自由软件”进行【污名化/妖魔化】。比如微软前任 CEO 巴尔默曾经污蔑说——Linux 以及相关的（GPL）许可证是“癌症”（以下是他原话）：<br/>
<blockquote style="background-color:#DDD;">Linux is a cancer that attaches itself in an intellectual property sense to everything it touches.<br/>
That's the way that the license works.</blockquote>　　长期的妖魔化，让很多人【误以为】“自由软件与商业公司水火不容”。但其实不然！<br/>
　　商业公司也能基于“自由软件许可协议”去开发“自由软件”并提供给用户。该过程可以是“免费的”，也可以是“付费的”。<br/>
　　所谓的“付费”，也就是说——商业公司也可以通过“销售自由软件”来获得利润（关于这点，下一条会详细介绍）。<br/>
<br/>
<br/>
<h2>★误解4——以为“自由软件 or 开源软件”必定是免费的</h2><br/>
　　（注：为了打字省力，本文以下部分以 <a href="https://en.wikipedia.org/wiki/Free_and_open-source_software" rel="nofollow" target="_blank">FOSS</a> 作为“自由软件 or 开源软件”的总称）<br/>
　　关于这个误解，俺把“自由软件”和“开源软件”分开来阐述。<br/>
<br/>
<h3>◇对于“自由软件”</h3><br/>
　　在前一条，俺提到：（从理论上讲）商业公司也可以销售自由软件（拿自由软件卖钱）。<br/>
　　说到这，可能很多人还不信。下面俺给出 FSF（<a href="https://zh.wikipedia.org/wiki/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6%E5%9F%BA%E9%87%91%E4%BC%9A" rel="nofollow" target="_blank">自由软件基金会</a>）【官网】的文章。<br/>
《<a href="https://www.gnu.org/philosophy/selling.html" rel="nofollow" target="_blank">Selling Free Software</a>》（原文）<br/>
《<a href="https://www.gnu.org/philosophy/selling.zh-cn.html" rel="nofollow" target="_blank">销售自由软件</a>》（上述的中文翻译）<br/>
<br/>
<h3>◇对于“开源软件”</h3><br/>
　　如果你理解了“为啥商业公司也允许销售自由软件”，也就比较能理解“为啥商业公司允许销售开源软件”了。<br/>
　　OSI（<a href="https://zh.wikipedia.org/wiki/%E5%BC%80%E6%94%BE%E6%BA%90%E4%BB%A3%E7%A0%81%E4%BF%83%E8%BF%9B%E4%BC%9A" rel="nofollow" target="_blank">开放源代码促进会</a>）对“开源软件”的定义（前面已经提到），并【没有】对“销售或付费”做任何限制。<br/>
　　也就是说，如果你开发了一套“开源软件”，并拿去卖，并且有人愿意买。这个（销售/购买）行为并【不】违背 OSI 的精神和条款。<br/>
<br/>
<h3>◇实际案例</h3><br/>
　　不要以为俺在本章节提到的只是【理论上的可能性】。在现实生活中已经有商业公司（在遵守 FOSS 许可的前提下）利用自由软件盈利，甚至还上市了——这就是大名鼎鼎的【<a href="https://zh.wikipedia.org/wiki/%E7%B4%85%E5%B8%BD%E5%85%AC%E5%8F%B8" rel="nofollow" target="_blank">红帽公司</a>】（洋文是：Red Hat）。该公司发布的“Red Hat Enterprise Linux”（简称 RHEL），在 Linux 社区很有影响。<br/>
　　关于“红帽公司”的规模，以下摘自维基百科的介绍：<br/>
<blockquote style="background-color:#DDD;">Red Hat于1999年8月11日在纳斯达克上市，2005年12月19日纳入纳斯达克100指数，2006年12月12日转到纽约证券交易所挂牌。<br/>
2018年10月28日，IBM 将以每股190美元的现金收购 Red Hat 所有已发行股份，总价值约为340亿美元。</blockquote><br/>
<br/>
<h2>★误解5——以为“自由软件 or 开源软件”的开发人员都是“义务的/无报酬的”</h2><br/>
　　互联网时代之前和初期，情况确实如此。<br/>
　　但如今 FOSS（Free and Open-Source Software）已经改变了全球软件行业的生态环境。<br/>
　　举个例子：由于 Linux 内核已经被大量/广泛地适用于各个领域，很多【大型】商业会让自己的程序员参与 Linux 社区的开发；同时，这些程序员拿的是商业公司的工资。<br/>
<br/>
<br/>
<h2>★误解6——以为“自由软件 or 开源软件”就没有版权</h2><br/>
　　虽然 FOSS（Free and Open-Source Software）允许用户获得源代码，允许用户自由地分发软件（包括源代码），但某些 FOSS 的 license 依然会有版权相关的条款（比如：有的会强调“署名权”，有的会强调“修改权”）。<br/>
　　引申阅读：<br/>
《<a href="https://www.gnu.org/philosophy/misinterpreting-copyright.zh-cn.html" rel="nofollow" target="_blank">对版权的误解 @ FSF 官网</a>》<br/>
<br/>
<br/>
<h2>★误解7——把“自由软件 or 开源软件”视作某种“共产主义”</h2><br/>
　　坦率地说，犯这种错误的人，既没有理解 FOSS（Free and Open-Source Software），也没有理解共产主义。<br/>
　　FOSS 与“共产主义”在本质上简直是【截然相反】滴。<br/>
<br/>
<h3>◇开放性 VS 封闭性</h3><br/>
　　前面俺已经说了：“开源软件”不光强调公开源码，而且强调【开放性】；相比之下，共产运动必将导致社会的【封闭性】。<br/>
　　为啥共产运动必将导致“封闭性”？<br/>
　　有耐心的同学可以去看<a href="https://zh.wikipedia.org/wiki/%E5%8D%A1%E5%B0%94%C2%B7%E6%B3%A2%E6%99%AE%E5%B0%94" rel="nofollow" target="_blank">卡尔·波普尔</a>的代表作《<a href="https://docs.google.com/document/d/1W3zcBUg55Mk5Vhzz3ajelXGh1YoOAxX8zzQvd9LniIs/" target="_blank">开放社会及其敌人</a>》（提醒一下：这是大部头的政治理论著作）<br/>
<br/>
<h3>◇自由 VS 奴役</h3><br/>
　　前面俺还说了：“自由软件”尽可能确保用户的【自由】；相比之下，共产运动必将导致对自由的【剥夺】（奴役）。<br/>
　　为啥共产运动必将导致“对自由的剥夺和奴役”？<br/>
　　对此感兴趣的同学可以去看一下<a href="https://zh.wikipedia.org/wiki/%E5%BC%97%E9%87%8C%E5%BE%B7%E9%87%8C%E5%B8%8C%C2%B7%E5%93%88%E8%80%B6%E5%85%8B" rel="nofollow" target="_blank">弗里德里希·哈耶克</a>的代表作《<a href="https://docs.google.com/document/d/1mmLgc9udwofBGrGD2DHqVq3pZZcaDDqTiw_8EN20wFs/" rel="nofollow" target="_blank">通往奴役之路</a>》。<br/>
<br/>
<h3>◇引申阅读</h3><br/>
　　批判“共产主义”和“马列主义”的博文，俺已经写过很多。具体参见博客上的 <a href="../../search/label/%E6%94%BF%E6%B2%BB.%E5%85%B1%E4%BA%A7%E8%BF%90%E5%8A%A8.md">政治.共产运动</a> 标签。<br/>
<br/>
<br/>
<h2>★误解8——认为“自由软件 or 开源软件”的质量不如“闭源商业软件”</h2><br/>
　　在20年前，很多人持有这种观点。如今越来越多的人开始意识到——FOSS 也可以打造出非常优秀的软件。<br/>
　　比如说大伙儿平时都在用的浏览器。IE 是完全闭源的商业软件，如今远远比不上 Chrome 和 Firefox。Firefox 是正宗的开源软件；Chrome 虽然不是开源软件，但它是在开源软件 Chromium 的基础上二次开发而成。<br/>
　　再比如 Web 服务器软件，长期占据三甲的，有两个（Apache、Nginx）是 FOSS，一个是闭源的（IIS）。而且 Apache + Nginx 的市场份额会明显高于 IIS。<br/>
　　（类似的例子还能举出很多）<br/>
　　另外，还有很多优秀的闭源商业软件在其内部使用了开源的库（library）。这些商业软件的成功，其内部使用的开源库功不可没。<br/>
　　引申阅读：<br/>
俺整理的“<a href="https://github.com/programthink/opensource" rel="nofollow" target="_blank">C/C++/Python 开源库清单</a>”<br/>
<br/>
<br/>
<h2>★误解9——把“自由软件”等同于“GPL 协议”（混淆这两者）</h2><br/>
　　（注：GPL 的全称是“GNU General Public License”，维基百科链接在“<a href="https://en.wikipedia.org/wiki/GNU_General_Public_License" rel="nofollow" target="_blank">这里</a>”）<br/>
　　这个错误连某些 FOSS 社区的人都会犯。<br/>
　　“使用 GPL 协议”的软件，必定是“自由软件”；但反过来就【不】成立。换句话说，除了 GPL 协议，还有很多其它协议，也可以确保其所属的软件是“自由软件”。<br/>
　　刚才提到了维基百科上有一个 license 对比清单，再次丢出来给列位看官参考（链接在“<a href="https://zh.wikipedia.org/wiki/%E8%87%AA%E7%94%B1%E5%8F%8A%E9%96%8B%E6%94%BE%E5%8E%9F%E5%A7%8B%E7%A2%BC%E8%BB%9F%E9%AB%94%E8%A8%B1%E5%8F%AF%E8%AD%89%E6%AF%94%E8%BC%83" rel="nofollow" target="_blank">这里</a>”）。清单中（第2个表格）有很多【非】GPL 的协议，也得到了 FSF 的认可（可以算是“自由的协议”）<br/>
<br/>
<br/>
<h2>★误解10——把“自由软件”等同于“与 GPL 兼容的协议”（混淆这两者）</h2><br/>
　　这条与前一条有点类似，也属于——连 FOSS 社区的人都会犯的错误。<br/>
　　“兼容 GPL 的协议”，其所属的软件必定是“自由软件”；但反过来就【不】成立。换句话说，还有很多【自由软件】的许可协议，与 GPL 是【不】兼容滴！<br/>
　　在 FSF（<a href="https://zh.wikipedia.org/wiki/%E8%87%AA%E7%94%B1%E8%BD%AF%E4%BB%B6%E5%9F%BA%E9%87%91%E4%BC%9A" rel="nofollow" target="_blank">自由软件基金会</a>）官网上有一个清单（链接在“<a href="https://www.gnu.org/licenses/license-list.html" rel="nofollow" target="_blank">这里</a>”），对各种许可协议进行分类，其中有一类是【GPL-Incompatible Free Software Licenses】。这一类协议，数量还不少。<br/>
<br/>
<br/>
<h2>★误解11——认为“开源软件许可证”的范畴包含了“自由软件许可证”（以为后者是前者的【真子集】）</h2><br/>
　　首先要承认一下：有段时间，俺也犯了这个错误。<br/>
　　如今要澄清的是：绝大部分“自由软件许可证”同时也算是“开源软件许可证”。<b>但有少数【例外】</b>。<br/>
<br/>
　　举个例子（例外）：<a href="https://zh.wikipedia.org/wiki/WTFPL" rel="nofollow" target="_blank">WTFPL</a><br/>
　　有一个比较鲜为人知的 license 叫做“WTFPL”，洋文全称是“Do What The Fuck You Want To Public License”。中文翻译成“你他妈的想干嘛就干嘛公共许可证”。<br/>
　　猛一看这名称，可能很多人以为这是个“恶搞的协议”（恶作剧）。但这个协议还是有点来头滴，其 2.0 版本的作者 <a href="https://en.wikipedia.org/wiki/Sam_Hocevar" rel="nofollow" target="_blank">Sam Hocevar</a> 曾经担任过 Debian 社区的负责人。<br/>
　　这个协议就属于刚才提到的【极少数例外】——它获得了 FSF 的认可，但没有获得 OSI 的认证。<br/>
<br/>
<br/>
<h2>★结尾</h2><br/>
　　俺写的这篇，难免会有遗漏。欢迎大伙儿补充 FOSS 相关的其它误解。<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2009/02/how-to-choose-opensource-project.md">如何选择开源项目？</a>》<br/>
《<a href="../../2015/06/GitHub-C-Cpp-Open-Source-Libraries.md">GitHub 通告：整理了一个 C 和 C++ 开源库的清单（含示例代码）</a>》<br/>
《<a href="../../2013/02/why-choose-python-5-tools.md">为啥俺推荐 Python[5]：作为瑞士军刀的 Python——顺便分享俺整理的 Python 开源库</a>》<br/>
<br/>
<!--BANNED
[1552398719667,1552404046839,1552405534086,1552406946537,1552436928884
,1552437038906,1552437794815,1552438051460,1552438229582,1552438480604
,1552440182753]
-->
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2019/03/Misunderstand-Free-and-Open-Source-Software.html
