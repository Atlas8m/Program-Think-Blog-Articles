# 扫盲 HTTPS 和 SSL-TLS 协议[0]：引子 

-----

<div class="post-body entry-content">
<center><img alt="不见图 请翻墙" src="images/H_exzSD20W99qSJhGkLJFPwj3gU7VF_t9VGsbHS19Zkky6Vgrhcn8OG4c3--8-qr3DjL-H6lOQVfYcYEZ5qQp19yOycAvaL-Dnl29AqINsIhWK6ITliRP_tBL4nZ4z_Vw0IO"/></center>
<br/>
　　今天这篇算是补之前的欠债——俺在4年前写过几篇关于 CA 证书的扫盲（“<a href="../../2010/02/introduce-digital-certificate-and-ca.md">这里</a>”和“<a href="../../2010/02/remove-cnnic-cert.md">这里</a>”），之后有不止一位热心读者建议俺写一篇关于 HTTPS 的扫盲。因为俺比较懒，当时没动笔，一拖就是两三年，都有点忘了。正好今年出了两个跟 HTTPS 相关的高危漏洞（<a href="https://en.wikipedia.org/wiki/Heartbleed" rel="nofollow" target="_blank">Heartbleed</a> 和 <a href="https://en.wikipedia.org/wiki/POODLE" rel="nofollow" target="_blank">PODDLE</a>），于是俺又想起这事儿。<br/>
　　本来想单独写一篇。等写完“背景知识”这一章节，发现篇幅已经很长了。所以就再开一个系列吧。<br/>
<a name="more"></a><br/>
　　事先声明：<br/>
　　既然叫做“扫盲”，所以俺尽量避免讲太多的“技术实现细节”（当然，更不会去讲“代码实现”）。本系列侧重于：尽可能通俗地介绍“设计思路”、“实现原理”，最后再聊聊“针对 HTTPS 的攻击手法”和“相关的安全防范措施”。一开始计划写3~4篇，后来篇幅有点失控，估计要写7~8篇。<br/>
　　虽然是扫盲，或许也能让 IT 技术人员从中获益——因为俺发现：连安全行业的某些程序员，对 HTTPS 的原理也所知甚少。<br/>
<br/>
为了方便阅读，把本系列帖子的目录整理如下（需翻墙）：<a name="index"> </a><br/>
1. <a href="../../2014/11/https-ssl-tls-1.md">背景知识、协议的需求、设计的难点</a><br/>
2. <a href="../../2014/11/https-ssl-tls-2.md">可靠密钥交换的难点，以及身份认证的必要性</a><br/>
3. <a href="../../2016/09/https-ssl-tls-3.md">扫盲几种密钥交换（密钥协商）算法</a><br/>
4. <a href="../../2018/09/https-ssl-tls-4.md">历史版本的演变及 Record 协议的细节</a><br/>
5. 握手过程的细节<br/>
6. 针对 HTTPS 的各种攻击手法<br/>
7. 各种相应的防范措施<br/>
<br/>
<br/>
<b>俺博客上，和本文相关的帖子（需翻墙）</b>：<br/>
《<a href="../../2021/03/Computer-Networks-Overview.md">计算机网络通讯的【系统性】扫盲——从“基本概念”到“OSI 模型”</a>》<br/>
《<a href="../../2014/01/dns.md">扫盲 DNS 原理，兼谈“域名劫持”和“域名欺骗／域名污染”</a>》<br/>
《<a href="../../2018/10/Comparison-of-DNS-Protocols.md">对比4种强化域名安全的协议——DNSSEC，DNSCrypt，DNS over TLS，DNS over HTTPS</a>》<br/>
《<a href="../../2010/04/howto-cover-your-tracks-0.md">如何隐藏你的踪迹，避免跨省追捕</a>》（系列）<br/>
《<a href="../../2019/09/Netcat-Tricks.md">扫盲 netcat（网猫）的 N 种用法——从“网络诊断”到“系统入侵”</a>》<br/>
《<a href="../../2019/04/Proxy-Tricks.md">如何让【不支持】代理的网络软件，通过代理进行联网（不同平台的 N 种方法）</a>》
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2014/11/https-ssl-tls-0.html
