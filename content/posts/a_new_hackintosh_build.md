---
title: "A_new_hackintosh_build"
date: 2020-04-21T15:29:29+08:00
Catogories: ["折腾"]
draft: false
---

# 记一次黑苹果安装

这篇文章记录在全新电脑（白盘裸机）上安装macOS的方法和一些坑，以备后面查阅。

## 硬件概览

| 硬件 | 型号                              |
| ---- | :-------------------------------- |
| CPU  | i5-9400                           |
| 硬盘 | 西数SN550 500GB NVMe M.2 SSD      |
| 显卡 | UHD630 + 蓝宝石RX580 2048sp pulse |
| 主板 | 微星B360M迫击炮                   |

可能唯一的一个坑是这块rx580显卡，不过这坑是我自己要跳的，因为能打游戏又能黑苹果又能将价格压在1000元的全新显卡只有这一个，这块卡可以刷入rx570的vbios实现黑苹果免驱，我刷的是[这个](https://www.techpowerup.com/vgabios/218998/218998)vbios，刷vbios的教程网上到处都有，只需要注意备份好原有的vbios，大概返厂维修会有点用（其实我想问卡都坏了还怎么点亮刷回去呢🐶）

最近有一个新的黑苹果引导工具：OpenCore。不过我真的学不动了，我的打算是以后稳定在Mojave系统上，所以先用熟悉的clover凑合吧。

## 工具

- Windows 10 ISO镜像
- macOS Mojave 10.14.5 dmg镜像
- 8GB高速U盘
- 软件：UltraISO，etcher，diskgen
- clover EFI引导文件，我使用了[这里](https://github.com/SuperNG6/MSI-B360-Catalina-EFI)的10.14系统专用的EFI，这份EFI在我的两台机器：i5-9400+msi B360M迫击炮+rx580和i5-9600K+msi Z390战斧导弹+uhd630上都可以很好地工作。

## macOS+win10单硬盘双系统安装步骤

1. **BIOS设置**。对于这块微星主板，BIOS出厂设置的基础上只需要关闭CFG锁定就可以了。
2. **制作macOS启动盘**。另找一台电脑，将macOS dmg镜像使用etcher写入U盘，并替换EFI文件。有些人可能还在使用TransMac，可以试一下etcher这款工具，你会真香的。
3. **安装macOS**。安装macOS的步骤不需详谈。安装macOS后，在macOS的磁盘工具.app里分出一块空间，并将这块空间格式化为APFS文件系统，这块空间供Windows系统~~和游戏~~使用
4. **制作win10启动盘**。使用UltraISO将U盘写入Windows 10安装镜像。这一步我遇到了2个坑：
   1. UltraISO报”设备访问错误“：在diskgen里删除这块U盘上的所有分区，右键点击U盘选择转换为MBR分区表，提交操作后在Windows磁盘管理里新建一个分区并格式化为FAT32文件系统即可。
   2. UltraISO报”Error formating NTFS volume X“：在制作启动盘界面点击“便捷启动”，选择“写入新的硬盘主引导记录（MBR）”，选择“USB-HDD+”，再次写入即可。
5. **安装win10**。引导U盘安装win10，分区选择时将上一步分出的APFS分区删除，再在这个分区里安装。

简单五步即可成功，重启即可发现主板会自动加载clover，并且clover里有macOS和Windows 10的引导项，非常的简单优雅。我之前网上搜索到的单硬盘安装双系统都还要通过winPE或者easyUEFI等第三方工具进行一些操作实现，其实是不必要的。

## 参考文献

1. [VBIOS来源](https://www.techpowerup.com/vgabios/218998/218998)
2. [刷VBIOS方法](https://osx.cx/rx580-2048sp-shua-vbios-rx570.html)
3. [稳定使用的EFI配置](https://github.com/SuperNG6/MSI-B360-Catalina-EFI)
4. [UltraISO报”Error formating NTFS volume X“的解决方法](https://jingyan.baidu.com/article/d169e18687230b026711d818.html)