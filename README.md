# speedtest-x

本仓库为 [LibreSpeed](https://github.com/librespeed/speedtest) 的延伸项目，LibreSpeed 是一个非常轻巧的网站测速工具。

speedtest-x 使用文件数据库来保存来自不同用户的测速结果，方便您查看全国不同地域与运营商的测速效果。


**❗ 注意**：基于网页测速的原理，程序会生成无用文件供测速者下载来计算真实下行带宽，一定程度上存在被恶意刷流量的风险，在对外分享你的测速页面后，请注意观察服务器流量使用情况，避免流量使用异常。

## 扩展细节
 - 用户测速会上传测速记录并保存至网站服务器
 - 不依赖 MySQL，使用文件数据库
 - IP 库改用 [ip.sb](https://ip.sb)，运营商记录更为精确

## 部署与使用

#### 常规部署 (环境要求：PHP 5.6+)

1、下载本仓库并解压到网站目录，访问 `{域名}/index.html` 进行测速

2、打开 `{域名}/results.html` 查看测速记录



**2020/12/22**

> 测速结果增加线性图表([@HuJK](https://github.com/HuJK))

**2020/12/10**

> 增加可配置项 `SAME_IP_MULTI_LOGS`，可设置是否允许同一IP记录多条测速结果

**2020/12/01**

> 增加 ipv6 支持
>
> 增加可配置项 `IP_SERVICE`，可选择使用的 IP 运营商解析服务，`ip.sb` 或 `ipinfo.io`

**2020/11/27**

> 下行测速文件默认大小与最大大小限制为 50M（源项目默认 100M，最大 1024M）

**2020/11/19**

> Docker 镜像上线 [https://hub.docker.com/r/badapple9/speedtest-x](https://hub.docker.com/r/badapple9/speedtest-x)

**2020/11/18**

> 上报速度与延迟值强制使用浮点类型，修复结果页表格按照下载速度或 ping 值排序错误的问题

**2020/11/16**

> 优化测速结果上报频率
>
> 掩去测速结果 IP D 段

**2020/11/13**

> Release

## 鸣谢
 - [LibreSpeed](https://github.com/librespeed/speedtest)
 - [ip.sb](https://ip.sb)
 - [SleekDB](https://github.com/rakibtg/SleekDB)
