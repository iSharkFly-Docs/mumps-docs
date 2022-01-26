# Protocol Buffers 安装
本文主要介绍 protobuf 编译器在 Windows 下的安装。

## 下载编译器
访问  https://github.com/protocolbuffers/protobuf/releases/ 链接然后针对不同的操作系统下载最新的编译器版本。

![protobuf-windows-01|475x500](https://cdn.ossez.com/discourse-uploads/original/2X/1/1dd39bd466048c1f7f5067e1605f396898dd873a.png)

下载完成后到本地计算机上找到这个文件并且解压。

## 解压文件
然后将下载的压缩文件解压到 D:\Dkits\protobuf 文件夹中。

当然你也可以解压到不同的文件夹中。

![protobuf-windows-02|690x281](https://cdn.ossez.com/discourse-uploads/original/2X/3/3e227fcacdddbdd7a5769b9e03f05a356dcb0fd0.png)

解压后的文件夹目录如下。

## 设置 PATH
当完成下面解压后，你可以将文件所在的 bin 目录中设置到 PATH 里面。

![protobuf-windows-03|528x500](https://cdn.ossez.com/discourse-uploads/original/2X/2/27bd6464431fa25136684e8f03e48255fc369c40.png)

上面就是设置好的 PATH 目录。

然后保存退出。

## 校验安装
在命令行工具中，运行命令：

`protoc --version`

如果能够看到版本输出的话，就说明你的 protoc 已经被正确的配置到操作系统中了。

![protobuf-windows-04|690x369](https://cdn.ossez.com/discourse-uploads/optimized/2X/9/9be96ab271c416ad37e06a641348cecae7ff9c52_2_690x369.png)

如上图，我们能看到正确的版本输出。

延伸阅读和参与讨论，请访问：[Protobuf 编译器 Windows 安装方法](https://www.ossez.com/t/protobuf-windows/13864)
