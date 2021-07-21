# Discourse 文档
Discourse 文档是通过官方文档的整理翻译过来的，下面的内容与官方的内容基本一致。

针对中文环境下的时候，我们对遇到的一些问题发布到我们的讨论区中以方便大家快速导航访问：

- [Discourse CentOS 8 全新安装手册](https://www.ossez.com/t/discourse-centos-8/594) - 在 CentOS/RHEL 平台上全新安装 Discourse 的过程和命令。

- [Discourse 如何不使用 Let’s Encrypt 而使用 CA 签名的密钥进行安装](https://www.ossez.com/t/discourse-lets-encrypt-ca/552) - 使用你自己已有的 CA 秘钥进行安装。

- [Discourse 设置 GTM](https://www.ossez.com/t/discourse-gtm/13240) - 使用 Google 的标签管理器来插入需要的 JS 代码。

## 云平台安装
**在基于云平台的 Discourse 安装通常不会超过 30 分钟**，哪怕你没有任何有关 Rails 或 Linux shell 的知识都能够顺利完成安装。
下面我们是通过 [DigitalOcean][do] 服务提供商来进行安装测的，但是所有的安装步骤都能够在
所有兼容 **Docker** 的云计算平台上进行，同时也可以在本地的服务器上完成安装。

>  🔔 如果你连 30 分钟都没有的话？你可以联系 Discourse 社区来帮你完成安装，Discourse 社区将会收取一次性 $150 （美元）的费用。 [单击此处链接来对服务进行购买](https://www.literatecomputing.com/product/discourse-install/) 。

### 创建一个新的云服务器

创建一个你的新云服务器，例如：[DigitalOcean](https://www.digitalocean.com/?refcode=5fa48ac82415) ，当然你也可以使用其他平台提供的服务器。

- 默认配置 **当前版本的 LTS Ubuntu 操作系统** 能够很好的工作。最少，需要一个 64 位的 Linux 操作系统，并且这个操作系统的内核需要更新到最新的版本。

- 默认配置 **1 GB** 的内存针对小型的 Discourse 社区通常都能很好的运行。但我们推荐针对大型社区使用 2 GB 的内存。

- 默认配置 **New York** 数据中心针对北美和欧洲来说都是不错的地理分区，如果你的 Discourse 用户使用的对象多是其他地理位置的用户，那么你可以选择离你稍近的数据中心。

- 输入域名 `discourse.example.com` 来在 DigitalOcean 中创建一个 Droplet（Droplet 是 DigitalOcean 定义的服务器名称）。当然你也可以购买使用你自己的域名，通常 Discourse 的安装需要一个真实的域名，没有办法通过 IP 地址安装，所以我们建议你首先购买域名或者使用你已有域名的二级域名。

创建你的新 Droplet，这个过程就等于你在 DigitalOcean 上创建了一个服务器，也等同你在其他平台上面创建了一个 VPS 或者服务器。
当完成创建后，你将会收到一个电子邮件，这个电子邮件中有你的 Root 用户的密码。
但是我们建议你 [设置使用 SSH keys](https://www.google.com/search?q=digitalocean+ssh+keys) ， 来增强你服务器访问的安全性。

### 访问你的云服务器

通过使用 IP 地址，并使用 SSH 来连接和访问你创建的服务器，或者针对 Windows 平台你可以安装 [Putty][put] 后运行下面的命令来进行连接：

    ssh root@192.168.1.1

如果你没有配置 SSH Key 的话，你可以使用 DigitalOcean 发给你的电子邮件中包含的密码来进行登录，
或者使用你本地的 SSH Key 来进行连接。

### 安装 Docker / Git （可选的）

如果你希望使用你自己的 Docker 版本，你可以现在在你新设置的服务器上进行安装。
如果你的服务器上没有默认安装 Docker，那么 `discourse-setup` 将会自动为你从 get.docker.com 下载后进行安装。

### 安装 Discourse

从 [官方 Discourse Docker 镜像][dd] 仓库中克隆代码到本地计算机的 `/var/discourse` 目录。

    sudo -s
    git clone https://github.com/discourse/discourse_docker.git /var/discourse
    cd /var/discourse

你只需要执行上面的命令即可，在 Discourse 安装的过程中需要 root 权限。

### 电子邮件

> ⚠️ **电子邮件系统在 Discourse 的用户创建过程中非常重要。** 
> 如果你没有在安装 Discourse 之前创建电子邮件 SMTP 服务器，那么你安装的 Discourse 无法访问也无法登录（HAVE A BROKEN SITE）！

- 如果你已经有你自己的 SMTP 邮件服务器了，那么你就可以直接使用你已有的邮件服务器配置信息。

- 还有没有邮件服务器？请访问  [**Discourse 推荐使用的邮件服务器**][mailconfig].

- 为了确保你的邮件能够被正常投递，你必须在你的 DNS 中添加有效的 [SPF 和 DKIM 记录](https://www.google.com/search?q=spf+dkim) 。请访问你邮件服务提供商的文档如何设置这些信息。

根据我们实际使用的情况，Discourse 的安装**必须**配置可用的域名和邮件服务器，针对中国境内的情况，你可以使用阿里云或者腾讯云提供的企业邮箱。
通常我们建议你使用境外的邮件服务器，比如说 AWS 的 SES，或者 MailGun 都是不错的服务，你可能需要一张国际信用卡完成校验。
但这一步是必须的，否则你的的 Discourse 无法完成安装。

### 域名

> 🔔 Discourse 不能通过 IP 地址来工作，你必须拥有一个域名或者二级域名来进行安装，例如 `example.com` 。

- 如果你已经拥有一个域名了，那么可以选择任何一个二级域名来进行安装，例如 `discourse.example.com` 或 `talk.example.com` 或 `forum.example.com` 来安装你的 Discourse 实例。

- 还没有域名的话，你可以访问 [NameCheap](https://www.namecheap.com/domains/domain-name-search/) 网站来搜索你喜欢的域名，或者直接 Google 搜索 [great domain name registrars](https://www.google.com/search?q=best+domain+name+registrars) 来选择你喜欢的域名注册商。

- 你的 DNS 控制台应该是能够访问的，在你购买域名后，你还需要访问你的 DNS 配置来配置 DNS。针对你安装的 Discourse 网站，你需要通过你的 DNS 创建一个 [`A` 记录](https://support.dnsimple.com/articles/a-record/) ，这个 A 记录需要将你要安装的域名指向到一个特定的 IP 地址。这个 IP 地址通常为你在第一步购买的服务器 IP 地址。

### 编辑 Discourse 配置

通过下面的命令运行配置工具

    ./discourse-setup

你需要根据下面的提示配置所有参数：

    Hostname for your Discourse? [discourse.example.com]: 
    Email address for admin account(s)? [me@example.com,you@example.com]: 
    SMTP server address? [smtp.example.com]: 
    SMTP port? [587]: 
    SMTP user name? [user@example.com]: 
    SMTP password? [pa$$word]: 
    Let's Encrypt account email? (ENTER to skip) [me@example.com]: 

上面的输入数据将会为你的 Discourse 实例创建一个  `app.yml` 文件，这个文件将会在安装进行后对你的 Discourse 实例进行配置。
整个安装启动过程可能需要耗费 **2-8 分钟** 来为你的配置 Discourse。
如果在安装完成后你还需要对你的配置进行修改，你可以再次运行  `./discourse-setup` 命令（这个命令将会把已经存在的 `app.yml` 文件重新载入）。
或者你也可以手动直接编辑 `/containers/app.yml` 文件中的内容，然后再次运行 `./launcher rebuild app`，否则你的修改是不会生效的。

### 启动 Discourse

一旦初始化安装配置完成后，你的 Discourse 示例应该可以通过你配置的域名 `discourse.example.com` 在浏览器上进行访问。

<img src="https://cdn.ossez.com/discourse-uploads/optimized/2X/8/8db53b9128ec4fb74872bdb7c1231ff04d525218_2_616x500.png" width="650">

### 注册一个新的管理员账号

使用你再启动配置过程中输入的电子邮件地址来注册一个管理员账号。

<img src="https://cdn.ossez.com/discourse-uploads/original/2X/9/99476eac0ffa4aa3a923aa7ae864fedf546dab0a.png" width="650">

<img src="https://cdn.ossez.com/discourse-uploads/original/2X/5/58660d377a00d9797be8b74036ace9d0ebf57fff.png" width="650">

(如果你不能注册你的管理账号（Admin），请通过路径`/var/discourse/shared/standalone/log/rails/production.log` 检查日志，或者访问 [电子邮件问题检查列表](https://meta.discourse.org/t/troubleshooting-email-on-a-new-discourse-install/16326) 。)

当你完成管理员账号的注册后，设置向导将会启动并指引你配置你的 Discourse 实例。

<img src="https://cdn.ossez.com/discourse-uploads/original/2X/9/944509dd0c049a2cec42d6108369fa5cf5d92d0d.png" width="650">

当完成所有的设置向导，你将会看到职员主题（Staff topics）和 **READ ME FIRST: Admin Quick Start Guide** 。
这个配置向导将会包含有针对后续配置的的一些建议和如何对你的 Discourse 安装实例进行自定义配置。

<img src="https://cdn.ossez.com/discourse-uploads/original/2X/8/8a60bc840705aaa1fc77b039a7babf77d6b4a10b.png" width="650">

### 安装后的维护

- 我们强烈建议打开你针对你操作系统的安全自动更新。在 Ubuntu 使用 `dpkg-reconfigure -plow unattended-upgrades` 命令。在 CentOS/RHEL，使用 [`yum-cron`](https://www.cyberciti.biz/faq/fedora-automatic-update-retrieval-installation-with-cron/) 包。
- 如果你使用的是密码登录你的操作系统，而不是使用 SSH Key 的话，请确保你使用强密码。在 Ubuntu 使用 `apt-get install libpam-cracklib` 包。我们推荐使用 `fail2ban` ，这个将会对 3 次登录失败的 IP 地址禁止登录 10 分钟。
    - **Ubuntu**: `apt-get install fail2ban`
    - **CentOS/RHEL**: `sudo yum install fail2ban` (需要 [EPEL](https://support.rackspace.com/how-to/install-epel-and-additional-repositories-on-centos-and-red-hat/))
- 如果你希望默认安装防火墙， 针对 Ubuntu [打开 ufw](https://meta.discourse.org/t/configure-a-firewall-for-discourse/20584) 或者针对 CentOS/RHEL 7 及其后续版本使用 `firewalld` 。

当 Discourse 有新版本更新的时候，你的邮件地址将会收到更新提示。
请随时更新你的 Discourse 实例到最新版本以确保所有的安全问题被修复。 
要 **更新 Discourse 到最新的版本**，请通过你的浏览器访问  `/admin/upgrade` 然后单击更新按钮。

`/var/discourse` 目录中的 `launcher` 命令被用来使用一些系统级别的维护：

``` text
Usage: launcher COMMAND CONFIG [--skip-prereqs] [--docker-args STRING]
Commands:
    start:      Start/initialize a container（启动/初始化容器）
    stop:       Stop a running container（停止一个运行的容器）
    restart:    Restart a container（重启容器）
    destroy:    Stop and remove a container （停止然后删除一个容器）
    enter:      Use nsenter to get a shell into a container （使用 nsenter 来访问容器内的 Shell）
    logs:       View the Docker logs for a container（查看一个容器的日志）
    bootstrap:  Bootstrap a container for the config based on a template（从配置模板中来启动一个容器的配置和初始化）
    rebuild:    Rebuild a container (destroy old, bootstrap, start new)（重构一个容器，将会删除老的容器，初始一个容器，启动新的容器）
    cleanup:    Remove all containers that have stopped for > 24 hours（针对停止运行超过 24 个小时的容器进行删除）

Options:
    --skip-prereqs             Don't check launcher prerequisites （不运行安装器的环境校验）
    --docker-args              Extra arguments to pass when running docker （传递给容器内的额外参数）
```

### 添加更多的 Discourse 特性

下面的内容是一些快速的链接，能够帮助你扩展 Discourse 安装的功能：

- Users to log in *only* via your pre-existing website's registration system? [Configure Single-Sign-On](https://meta.discourse.org/t/official-single-sign-on-for-discourse/13045).

- 用户可以使用 [Google](https://www.ossez.com/t/discourse-google-google-login/13582), [Twitter](https://meta.discourse.org/t/configuring-twitter-login-for-discourse/13395), [GitHub](https://www.ossez.com/t/discourse-github/13562), or  [Facebook](https://meta.discourse.org/t/configuring-facebook-login-for-discourse/13394) 进行注册登录。

- Users to post replies via email? [Configure reply via email](https://meta.discourse.org/t/set-up-reply-via-email-support/14003).

- Automatic daily backups? [Configure backups](https://meta.discourse.org/t/configure-automatic-backups-for-discourse/14855).

- Free HTTPS / SSL support? [Configure Let's Encrypt](https://meta.discourse.org/t/setting-up-lets-encrypt-cert-with-discourse-docker/40709). Paid HTTPS / SSL support? [Configure SSL](https://meta.discourse.org/t/allowing-ssl-for-your-discourse-docker-setup/13847).

- Use a plugin [from Discourse](https://github.com/discourse) or a third party? [Configure plugins](https://meta.discourse.org/t/install-a-plugin/19157)

- Multiple Discourse sites on the same server? [Configure multisite](https://meta.discourse.org/t/multisite-configuration-with-docker/14084).

- Webhooks when events happen in Discourse? [Configure webhooks](https://meta.discourse.org/t/setting-up-webhooks/49045).

- A Content Delivery Network to speed up worldwide access? [Configure a CDN](https://meta.discourse.org/t/enable-a-cdn-for-your-discourse/14857). We recommend [Fastly](http://www.fastly.com/).

- Import old content from vBulletin, PHPbb, Vanilla, Drupal, BBPress, etc? [See our open source importers](https://github.com/discourse/discourse/tree/main/script/import_scripts).

- A user friendly [offline page when rebuilding or upgrading?](https://meta.discourse.org/t/adding-an-offline-page-when-rebuilding/45238)

- To embed Discourse [in your WordPress install](https://github.com/discourse/wp-discourse), or [on your static HTML site](https://meta.discourse.org/t/embedding-discourse-comments-via-javascript/31963)?

Help us improve this guide! Feel free to ask about it on [meta.discourse.org][meta], or even better, submit a pull request.

[dd]: https://github.com/discourse/discourse_docker
[ssh]: https://help.github.com/articles/generating-ssh-keys
[meta]: https://meta.discourse.org
[do]: https://www.digitalocean.com/?refcode=5fa48ac82415
[put]: http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html
[mailconfig]: https://github.com/discourse/discourse/blob/main/docs/INSTALL-email.md