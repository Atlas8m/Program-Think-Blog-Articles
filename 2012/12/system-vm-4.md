# 扫盲操作系统虚拟机[4]：虚拟系统的安装（多图） 

-----

<div class="post-body entry-content">
　　不少网友在博客留言中表达了对虚拟机系列的关注，所以今天再抽空发一篇。<br/>
　　在<a href="http://program-think.blogspot.com/2012/11/system-vm-3.html">上一篇帖子</a>，俺已经介绍了"如何适合你的虚拟机软件"。今天来扫盲一下如何在虚拟机软件中安装虚拟操作系统。因为本系列是扫盲，本文尽量写得傻瓜化一些，以迎合不懂技术的网友。<a name="more"></a><br/>
<br/>
<h2>★准备工作</h2><br/>
<h3>◇下载虚拟机软件</h3><br/>
　　由于篇幅有限，本文只介绍 VMware Workstation（<b>后面简称 VMware</b>） 和 VirtualBox 这两款虚拟机软件。<br/>
<br/>
　　<b>VirtualBox</b><br/>
　　因为是开源而且免费的，所以 VirtualBox 很容易获取。<br/>
　　用鼠标猛击“<a href="https://www.virtualbox.org/wiki/Downloads" rel="nofollow" target="_blank">这里</a>”，打开 VirtualBox 官网的下载页面。该页面上提供了针对 Windows、Mac OS X、Linux 的安装包，根据你的操作系统择一下载即可。下载完安装包，再顺便把扩展包也下了（扩展包不区分操作系统的）。<br/>
　　顺便表扬一下 VirtualBox 的短小精悍。（截至俺写本文时）最新的 4.2.4 版本也才90兆。<br/>
<br/>
　　<b>VMware</b><br/>
　　VMware 因为是商业软件，下载稍微麻烦点。<br/>
　　用鼠标猛击“<a href="https://downloads.vmware.com/" rel="nofollow" target="_blank">这里</a>”，打开 VMware 官网的下载页面。下载的时候，需要你输入一个 VMware 的帐号和口令。所以在下载前，你还得先用自己的邮箱去注册一个 VMware 的帐号（放心，是免费滴）。注册完帐号之后，你应该就可以顺利下载到安装包了。<br/>
　　拿到安装包还没完——这个安装包只能让你试用若干天。为了能长期用下去，你要么上网 Google 一下注册码，要么花银子买正版（因为俺博客搭建在 Google 平台，需要遵守美国法律，因此就无法在博文中公布“注册码”，还望谅解）<br/>
<br/>
<h3>◇准备一张安装盘</h3><br/>
　　拿到虚拟机软件之后，再准备一张你要安装的操作系统的安装盘，可以是传统的光盘，也可以是 ISO 格式的光盘镜像文件。<br/>
　　俺个人建议用光盘镜像文件，比较方便。一来传统的光盘容易坏（比如不小心划伤）；二来传统光盘不论是自己刻录还是买盗版盘，都要花银子滴。反之，光盘镜像文件可以直接从网上下载，也可以找朋友 COPY，省钱又省力 :)<br/>
　　经常有人问如何搞到正宗的 Windows 7 光盘镜像。想知道的网友，请看《如何防止黑客入侵[7]：Web相关的防范》一文的留言（请耐心看完第12楼的前几条留言），链接在“<a href="http://program-think.blogspot.com/2012/10/howto-prevent-hacker-attack-7.html?comment=1350739642972">这里</a>”。<br/>
<br/>
<h2>★安装虚拟机软件</h2><br/>
　　不论是 VMware 还是 VirtualBox，安装过程都比较简单。如果你是菜鸟级用户，只需一路按 Next 即可。所以，这部分俺就不浪费口水了。<br/>
　　顺便提醒一下：VMware Workstation 从 6.0 版本开始就变得很臃肿——软件装好之后至少占掉你 1GB 的硬盘空间。<br/>
<br/>
<h2>★虚拟机软件的配置</h2><br/>
　　虚拟机软件装好之后，需要简单设置一下。下面分别介绍 VMware 和 VirtualBox 的全局设置。<br/>
<br/>
<h3>◇VMware Workstation</h3><br/>
运行 VMware，在主菜单上点“Edit”，再点“Preferences”，弹出 VMware 全局设置的对话框。<br/>
<br/>
选“Workspace”标签页，设置今后你要创建的 Guest OS 的默认存放位置（如下图）。<br/>
如果你打算长期使用虚拟机，俺个人的建议是：单独开辟一个<b>大的硬盘分区</b>，专门用来存放你创建的 Guest OS。<br/>
<img alt="不见图 请翻墙" src="images/7V-kYPpFJ2XEMvGqCgWHpsnY01PzrxuMx_eq5fPl7gvat0PwOMzwJ_rgcB3U1VsFC1AYyhbU53KWgZaxAUG8Fx8-uTkoYoGKdiYUca7STH8PQdi1OOZIhZiqNKg"/><br/>
<br/>
选“Hot Keys”标签页，设置热键。<br/>
简单说一下热键的用途。<br/>
当某个 Guest OS 进入全屏模式，或者某个 Guest OS 捕获了鼠标键盘的输入，你可以通过按这个热键退回到 Host OS<br/>
如果你觉得默认的热键用起来还算顺手，就不用再设置了。<br/>
<img alt="不见图 请翻墙" src="images/V0gb4AaG7YWVzh78Zuco-oggoslB5RsWRfLhjLHyuH3GSqmAgP4_vQ5ANP6Qs0KUnk7USd2CmDjNhQh7VbWukgwz_IPgfGGrgbvt7KjODrUIp43cuJG4iKzhy5o"/><br/>
<br/>
选“Memory”标签页，设置内存参数。<br/>
首先，设置 VMware 预留的内存数量。如果你需要同时运行多个 Guest OS，就需要预留多一些内存。<br/>
其次，设置内存使用方式。有三个选项，俺简单解释一下：<br/>
选项1：所有的 Guest OS 都加载到物理内存<br/>
选项2和选项3：允许 Guest OS 使用 Host OS 的虚拟内存<br/>
如果你的物理内存足够大，建议用选项1（这样性能足够好）<br/>
<img alt="不见图 请翻墙" src="images/9JSs-MvebOqq203NVYM7XjVn2Eu69zAz3REuvX_MWCrJKY1ldLsuTjNmHpJQmC4UQY3jM24mTgA6_jhdwqnn6ygtn1-me1NY-SuvXEccESeCuxOiQbyKO2sWzXI"/><br/>
<br/>
<h3>◇VirtualBox</h3><br/>
运行 VirtualBox，在主菜单上点“管理”，再点“全局设定”，弹出 VirtualBox 全局设置的对话框。<br/>
<br/>
在左边选“常规”标签页，设置今后你要创建的 Guest OS 的默认存放目录（如下图）<br/>
如果你打算长期使用虚拟机，俺个人的建议是：单独开辟一个<b>大分区</b>，专门用来存放你创建的 Guest OS。<br/>
<img alt="不见图 请翻墙" src="images/lpjPqj0-P7ZZ9x2Jo5_r4SW_cL8ieYXsE5npG4urXteK146zksT-x9WKE2ByjOjo7zjR9Z4EGw33MtaprFcWxRFxWUDkzD8wkm9jAtbYuUPthDjjyf9Qod6leuM"/><br/>
<br/>
在左边选“热键”标签页，设置 VirtualBox 的热键。<br/>
简单说一下热键的用途。<br/>
当某个 Guest OS 进入全屏模式，或者某个 Guest OS 捕获了鼠标键盘的输入，你可以通过按这个热键退回到 Host OS<br/>
如果你觉得默认的热键用起来还算顺手，就不用再设置了。<br/>
<img alt="不见图 请翻墙" src="images/G0tPAGjDFLJMx_WJ0QklrlW1arblfzD0n07T4HzrqE0W3x9cU2RCGbdPC_844BFmdLQQR8mH3B3V5pgAFWrE69VoHSLrieI5hjylSNP1_H0CqU2vm7Uasqgu69c"/><br/>
<br/>
在左边选“扩展”标签页，添加扩展包。<br/>
要添加的扩展包就是刚才下载安装包的时候，一起下载的那个扩展包。<br/>
<img alt="不见图 请翻墙" src="images/tvyVcmqw3TYA0B1PHoo_MKkD8f0z6yjXa87WKOCmCDErr6RRM3aSFF4rHNejnsKkG8kVvd5RloffzPw6kAToZ3ABgmxXfWKvedWC02C2dW05uyF6bByucS-7JiU"/><br/>
<br/>
<h2>★安装 Guest OS</h2><br/>
下面分别介绍 VMware 和 VirtualBox 如何安装 Guest OS。<br/>
<br/>
<h3>◇VMware Workstation</h3><br/>
运行 VMware，在主菜单上点“File”，再点“New”，再点“Virtual Machine”，弹出创建 Guest OS 的向导。<br/>
<br/>
向导第1步<br/>
作为新手/菜鸟，你显然要用默认的 Typical 向导。<br/>
<img alt="不见图 请翻墙" src="images/MvKAwhqGw4L0ztHiXq7daXdxv6KQGFZxcAwNj4ItYopQ-jwkOuti70Dt-M2gLYTmscBMTpXVfmL9Pjwo6vvGbIUdz4RLlaaDmcrLlJJjTPZ30JoYFlr4p84csQo"/><br/>
<br/>
向导第2步<br/>
选第三个选项，意思就是说：先创建一个空白的 Guest OS，最后再自己装系统。<br/>
<img alt="不见图 请翻墙" src="images/gE8ITfiVW_GQQfyzOCLoxHwEclrBtigZOBWW8ms6hQNyhQotTjJT1e3dGdcXaeXAdyS0WL5fOnoB3b7R1cFxuuJyctQdMi3X6wIZSy7vjBFWcTNuPIeATFIeDc4"/><br/>
<br/>
向导第3步<br/>
选操作系统类型和版本<br/>
<img alt="不见图 请翻墙" src="images/w6SWw-M5N80CB31_z8625fFwL2DX3COYFV9eRi-hQ2rjHZHbY6uy0tLWZhMUsQrIwwCkHm_kyN3ySDU_sfeO-WM7jNGwtSEabJ5VXjTEleh0bhzF6HBgURun584"/><br/>
<br/>
向导第4步<br/>
填写 Guest OS 的名称和存储目录<br/>
<img alt="不见图 请翻墙" src="images/XceRdE2XBSDwd48mhtfo9WYZTtGAotszQp-2Q3KV2Rdwr1gq2SatZbjwPl_T2NzBc5BJoEtqPcQ_fG5TxQq64jDQaFccRliow_jrF5fzdd4noVxgERIdZK2dNEQ"/><br/>
<br/>
向导第5步<br/>
这个向导默认只会帮你加一块虚拟磁盘。这一步是让你配置虚拟磁盘的大小。<br/>
如果你需要多块磁盘，待会儿自己到 Guest OS 的设置选项中配置。<br/>
这步完成后，向导就结束了，一个空白的 Guest OS 也创建好了。<br/>
<img alt="不见图 请翻墙" src="images/AoT_1A8Sathf_xoq05G2IZtTnDdHwX3W-JGGeJj7prNLWB4IbNkh0OHaKAgwoDd9F-RykXQOk9Z7rpseIJwPNUHmYfmE5NeuzRn5CO4n0xElji_NcTknMmvalT8"/><br/>
<br/>
Guest OS 创建好之后，调出它的设置对话框。<br/>
<br/>
在“Hardware”标签页下，选择“Memory”，调整 Guest OS 的内存大小。如果你需要在这个 Guest OS 里面运行一些重量级的应用软件，就需要多配点内存给它。否则的话，直接用默认值即可。<br/>
<img alt="不见图 请翻墙" src="images/a3fWTVkVg2FFrhufAxM5aGyQcCVW2yH8eSZc5xs7J215iTbLny-KRu60LWtW8xvFb_X0XpHLle7l_2uCDmqfrKzp3amzlVMWjkwnT1G7ThxPUZ4VWMU7b77n2dA"/><br/>
<br/>
在“Hardware”标签页下，选择“Processors”，配置 CPU 的数量和每个 CPU 的核心数量。<br/>
<img alt="不见图 请翻墙" src="images/0oQPjX_oL0sppMKx_zL5_S48Y3QRKZjlo387BiFB_rAUhzWORUYFreIcaZGAVgSc3nvElzyYl5a-uHksgml-52my_VCFdpwg7ShxMZDVsVaIeSOIx_ZU-vVcpZE"/><br/>
<br/>
在“Hardware”标签页下，选择“CD/DVD”，然后在右边选（你要安装系统的那张安装光盘的）镜像文件。<br/>
<img alt="不见图 请翻墙" src="images/EmzJJA2bnvLOSyOjNZjSs1NSzPfTEr1gSyBWtdp9aGuXxUb4zYJqCyygpQWAerc6gOX73XrlQBi9tNUB7do3fdFnkJk9AFBdQNFFf7JcomYD6YGHgi-swMJOa2I"/><br/>
<br/>
上述步骤都配置完毕，点“Power On”按钮，Guest OS 就开机了。然后就是操作系统的安装过程（装系统就不用俺来教了吧？）<br/>
<br/>
<h3>◇VirtualBox</h3><br/>
运行 VirtualBox，在工具栏上点“新建”，弹出创建 Guest OS 的向导。<br/>
<br/>
向导第1步<br/>
选操作系统类型和版本<br/>
<img alt="不见图 请翻墙" src="images/uhcz_J97d6dBArorqAV6EwCXvuc-xzWUL8OVhFMk-mtwe_LF5LbhYEsFbf5ugSr437A64yeX1OI1t0tFzibGGskCoBmrC9vH7MfDLKL61ygGvO7whdjaPfI0iy4"/><br/>
<br/>
向导第2步<br/>
设置 Guest OS 的内存。<br/>
如果你需要在这个 Guest OS 里面运行一些重量级的应用软件，就需要多配点内存给它。否则的话，直接用默认值即可。<br/>
<img alt="不见图 请翻墙" src="images/IZ_dri-buWVHHP3NB8L0jzPArO4WzLMiWgzRA7Urasc208DDKJN8wKe3zkkfnvrlsUv4U8GSrG7h1u-h93OZaqYL6BmmiKJhK0DaaKbghZP1NfnV6vAYYK_ED4M"/><br/>
<br/>
向导第3步<br/>
创建一块虚拟硬盘给 Guest OS 用<br/>
<img alt="不见图 请翻墙" src="images/IVw5eIVaqEpDA5keZXU4kSTwg0GacHWCWqJSjF8vq-VC_Bfwi25lVDPYfkE4cAuY4TlRMQgYB63y8TL2RrcTKGlkwlf5IWXF7ZHFL_qogXaZmOaqETBsS90uinE"/><br/>
<br/>
向导第4步<br/>
选择虚拟硬盘的类型。<br/>
如果你不打算迁移到其它虚拟机软件，直接用 VirtualBox 自家的 VDI 格式。<br/>
如果今后有打算把创建出来的 Guest OS 迁移到 VMware，就可以选 VMDK 格式。<br/>
<img alt="不见图 请翻墙" src="images/kxEFyghdXa-6TbB7H6U7qwnfIWuOhDYP8sSE48rd-qqKc8QMmBxRF5zYtYR_IRPKdJVCrKOUDhGznrvxbERmwxjREKFig2udb6fweAIRpIQR7perVxQBOsF6Z4s"/><br/>
<br/>
向导第5步<br/>
选虚拟硬盘的分配方式。<br/>
除非你电脑的硬盘空间非常非常充裕，否则的话不要用“固定大小”。通常建议用“动态分配”方式。<br/>
<img alt="不见图 请翻墙" src="images/6DmhAlVgNtUGXDh3VDqAeT4J1wV6Hy6jHwv8Lr8rwT_KIUgu59cvDFE_s3C8xdEFT4rcDKR-GABl1BLkp_DMeTfTvQJcCltdtIWg0jr2jviwOSYTzfyF8ZutzVE"/><br/>
<br/>
向导第6步<br/>
这个向导默认只会帮你加一块虚拟磁盘。这一步是让你配置虚拟磁盘的大小。<br/>
如果你需要多块磁盘，待会儿自己到 Guest OS 的设置选项中配置。<br/>
这步完成后，向导就结束了，一个空白的 Guest OS 也创建好了。<br/>
<img alt="不见图 请翻墙" src="images/UrRrWZy-vxGODprOmsDlIbQ8gpJZVoSyfbl8v2gzBROIyAkkXTd17caoIRPja_5hw9xyLdPQ_2aB1acpsuYOoYDdVHxqgx8zQEPeDsR6ratJwuaUlpX3AvTdhYc"/><br/>
<br/>
Guest OS 创建好之后，调出它的设置对话框。<br/>
<br/>
在对话框左边“系统”，配置 CPU 的数量。<br/>
VirtualBox 还有一个特色功能，就是设定 Guest OS 使用的 CPU 上限。这个功能可以防止某个 Guest OS 把 CPU 耗尽，导致你的 Host OS 失去响应（假死）。<br/>
<img alt="不见图 请翻墙" src="images/-4JGkiHbd5WNWT1_F7RZtaz1tytwVyggHYzw7iHVNJFQ95hOj9hkAR2rw6D-4vDxme62t5HvJzWEwHap7qXFLJB4HuVxf6CmK_zgp3ZVhgP0JPuevaUKG2EvJ1Q"/><br/>
<br/>
在对话框左边“存储”，然后在右边选（你要安装系统的那张安装光盘的）镜像文件。<br/>
<img alt="不见图 请翻墙" src="images/qQ77T2UQEyctXuJWm-NzEJk5VHYcic20FVaLinEtE3N3YcIKd9DSAD6KLDL6EzDmDT3v73iYXljoTViOS9CePCaDBnp99zUn4InCBtZlP-qdQ0mSpH673s-AA3Q"/><br/>
<br/>
上述步骤都配置完毕，点工具条上的“启动”按钮，Guest OS 就开机了。然后就是操作系统的安装过程（装系统就不用俺来教了吧？）<br/>
<br/>
<h2>★结尾</h2><br/>
　　以上就是两款常见的虚拟机软件安装 Guest OS 的过程。列位看官如果有啥疑问，请到<a href="http://program-think.blogspot.com/2012/12/system-vm-4.html">本文留言</a>。本系列下一篇会介绍<a href="http://program-think.blogspot.com/2012/12/system-vm-5.html">虚拟系统的配置</a>。<br/>
<br/>
<a href="http://program-think.blogspot.com/2012/10/system-vm-0.html#index">回到本系列的目录</a>
</div>


------------------------------------------------

版权声明本博客所有的原创文章，作者皆保留版权。转载必须包含本声明，保持本文完整，并以超链接形式注明作者编程随想和本文原始地址：https://program-think.blogspot.com/2012/12/system-vm-4.html
