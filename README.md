# LittleTools

## ToDoNotice

![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)

#### 工具简介	

​		这个小工具是待办任务提醒，是使用python，基于微信的[server酱](http://sc.ftqq.com/3.version)进行开发的一款每日待办任务提醒小工具。只需要将待办任务放到**‘待办任务.xlsx’**文件中，然后运行ToDoNotice.py文件就可以进行推送。这里我使用pyinstaller将本工具打包为.exe文件。

#### 工具自定义

​	开发自己想要的模板需要对ToDoNotice.py文件进行修改。

​	首先是key要改成server酱中所绑定微信的key值。这样才能使消息发送到指定微信，在文件第45行。

​	然后修改时间，所需要修改的函数在文件第64行

​	之后进行文件打包 ，该过程需要安装pyinstaller，然后使用命令 打包一个只有.exe文件的包，在dist文件夹下。

```
	pip install pyinstaller
	pyinstaller -F ToDoNotice.py
```

​	在运行.exe文件之前，需要将**’cacert.pem‘**文件和**’待办任务.xlsx‘**都放在dist文件夹下，否则会出现报错。

#### 工具运行截图

![工具运行截图](ToDoNotice/result/result.jpg)

#### 安装

```
git clonehttps://github.com/Hezhing/LittleTools.git
```

