# Discourse 文档

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

Connect to your server via its IP address using SSH, or [Putty][put] on Windows:

    ssh root@192.168.1.1

Either use the root password from the email DigitalOcean sent you when the server was set up, or have a valid SSH key configured on your local machine.

### Install Docker / Git (Optional)

If you have reason to install your own version of Docker, you may do so. If docker is not installed, `discourse-setup` will automatically install it from get.docker.com.

### Install Discourse

Clone the [Official Discourse Docker Image][dd] into `/var/discourse`.

    sudo -s
    git clone https://github.com/discourse/discourse_docker.git /var/discourse
    cd /var/discourse

You will need to be root through the rest of the setup and bootstrap process.

### Email

> ⚠️ **Email is CRITICAL for account creation and notifications in Discourse.** If you do not properly configure email before bootstrapping YOU WILL HAVE A BROKEN SITE!

- Already have a mail server? Great. Use your existing mail server credentials.

- No existing mail server? Check out our [**Recommended Email Providers for Discourse**][mailconfig].

- To ensure mail deliverability, you must add valid [SPF and DKIM records](https://www.google.com/search?q=spf+dkim) in your DNS. See your mail provider instructions for specifics.

### Domain Name

> 🔔 Discourse will not work from an IP address, you must own a domain name such as `example.com` to proceed.

- Already own a domain name? Great. Select a subdomain such as `discourse.example.com` or `talk.example.com` or `forum.example.com` for your Discourse instance.

- No domain name? We can [recommend NameCheap](https://www.namecheap.com/domains/domain-name-search/), or there are many other [great domain name registrars](https://www.google.com/search?q=best+domain+name+registrars) to choose from.

- Your DNS controls should be accessible from the place where you purchased your domain name. Create a DNS [`A` record](https://support.dnsimple.com/articles/a-record/) for the `discourse.example.com` hostname in your DNS control panel, pointing to the IP address of your cloud instance where you are installing Discourse.

### Edit Discourse Configuration

Launch the setup tool at

    ./discourse-setup

Answer the following questions when prompted:

    Hostname for your Discourse? [discourse.example.com]: 
    Email address for admin account(s)? [me@example.com,you@example.com]: 
    SMTP server address? [smtp.example.com]: 
    SMTP port? [587]: 
    SMTP user name? [user@example.com]: 
    SMTP password? [pa$$word]: 
    Let's Encrypt account email? (ENTER to skip) [me@example.com]: 

This will generate an `app.yml` configuration file on your behalf, and then kicks off bootstrap. Bootstrapping takes between **2-8 minutes** to set up your Discourse. If you need to change these settings after bootstrapping, you can run `./discourse-setup` again (it will re-use your previous values from the file) or edit `/containers/app.yml` manually with `nano` and then `./launcher rebuild app`, otherwise your changes will not take effect.

### Start Discourse

Once bootstrapping is complete, your Discourse should be accessible in your web browser via the domain name `discourse.example.com` you entered earlier.

<img src="https://www.discourse.org/images/install/17/discourse-congrats.png" width="650">

### Register New Account and Become Admin

Register a new admin account using one of the email addresses you entered before bootstrapping.

<img src="https://www.discourse.org/images/install/17/discourse-register.png" width="650">

<img src="https://www.discourse.org/images/install/17/discourse-activate.png" width="650">

(If you are unable to register your admin account, check the logs at `/var/discourse/shared/standalone/log/rails/production.log` and see our [Email Troubleshooting checklist](https://meta.discourse.org/t/troubleshooting-email-on-a-new-discourse-install/16326).)

After registering your admin account, the setup wizard will launch and guide you through basic configuration of your Discourse.

<img src="https://www.discourse.org/images/install/17/discourse-wizard-step-1.png" width="650">

After completing the setup wizard, you should see Staff topics and **READ ME FIRST: Admin Quick Start Guide**. This guide contains advice for further configuring and customizing your Discourse install.

<img src="https://www.discourse.org/images/install/17/discourse-homepage.png">

### Post-Install Maintenance

- We strongly suggest you turn on automatic security updates for your OS. In Ubuntu use the `dpkg-reconfigure -plow unattended-upgrades` command. In CentOS/RHEL, use the [`yum-cron`](https://www.cyberciti.biz/faq/fedora-automatic-update-retrieval-installation-with-cron/) package.
- If you are using a password and not a SSH key, be sure to enforce a strong root password. In Ubuntu use the `apt-get install libpam-cracklib` package. We also recommend `fail2ban` which blocks any IP addresses for 10 minutes that attempt more than 3 password retries.
    - **Ubuntu**: `apt-get install fail2ban`
    - **CentOS/RHEL**: `sudo yum install fail2ban` (requires [EPEL](https://support.rackspace.com/how-to/install-epel-and-additional-repositories-on-centos-and-red-hat/))
- If you need or want a default firewall, [turn on ufw](https://meta.discourse.org/t/configure-a-firewall-for-discourse/20584) for Ubuntu or use `firewalld` for CentOS/RHEL 7 or later.

You will get email reminders as new versions of Discourse are released. Please stay current to get the latest features and security fixes. To **upgrade Discourse to the latest version**, visit `/admin/upgrade` in your browser and click the Upgrade button.

The `launcher` command in the `/var/discourse` folder can be used for various kinds of maintenance:

``` text
Usage: launcher COMMAND CONFIG [--skip-prereqs] [--docker-args STRING]
Commands:
    start:      Start/initialize a container
    stop:       Stop a running container
    restart:    Restart a container
    destroy:    Stop and remove a container
    enter:      Use nsenter to get a shell into a container
    logs:       View the Docker logs for a container
    bootstrap:  Bootstrap a container for the config based on a template
    rebuild:    Rebuild a container (destroy old, bootstrap, start new)
    cleanup:    Remove all containers that have stopped for > 24 hours

Options:
    --skip-prereqs             Don't check launcher prerequisites
    --docker-args              Extra arguments to pass when running docker
```

### Add More Discourse Features

Do you want...

* Users to log in *only* via your pre-existing website's registration system? [Configure Single-Sign-On](https://meta.discourse.org/t/official-single-sign-on-for-discourse/13045).

- Users to log in via [Google](https://meta.discourse.org/t/configuring-google-oauth2-login-for-discourse/15858), [Twitter](https://meta.discourse.org/t/configuring-twitter-login-for-discourse/13395), [GitHub](https://meta.discourse.org/t/configuring-github-login-for-discourse/13745), or  [Facebook](https://meta.discourse.org/t/configuring-facebook-login-for-discourse/13394)?

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