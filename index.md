## 目录

- [长期置顶](#长期置顶)
- [新闻](#news)
- [问题收集与解答](#question_index)
- [Welcome to SEC-I 2021.3.3](#Welcome-to-SEC-I-2021.3.3)


**最后更新日期**：2021.3.14

请使用`ctrl+F5`强制刷新来保证你获得的是最新的页面

## 长期置顶
[使用git和IDE进行写作业的演示视频](https://www.bilibili.com/video/BV1nh411Q7fs)
**git clone 的时候，不要使用你登陆seecoder的密码，而是使用发送到你的注册邮箱中的密码。**

Git教程
- http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/zh_cn/
- https://www.liaoxuefeng.com/wiki/896043488029600
- https://learngitbranching.js.org/
---

[提问的智慧](https://github.com/ryanhanwu/How-To-Ask-Questions-The-Smart-Way/blob/main/README-zh_CN.md)

学会如何更好的提问是成为一名合格的程序员的重要一步，并不是不愿意为大家解决问题，而是实际上不可能任何时候都有一个人可以快速便捷地为大家解决问题。总有一天，你需要依赖互联网来检索你的问题。所以，提问前先Google/Baidu一下你的问题，不仅可以锻炼你的搜索能力，也可以将时间和精力留给那些更重要的问题。

<!-- news starts -->
<span id="news"></span>
## 新闻
<!-- news end -->

<!-- questions starts -->
<span id="question_index"></span>
## 问题收集与解答
- [关于打开Java作业出现红色文件的情况](#Q0)  **2021.4.21**
- [本地通过了但是push上去就编译或者运行错误的几种可能](#Q1)  **2021.3.8**
- [从git获取题目时发生异常...](#Q2)  **2021.3.7**
- [两种不同的格式化方式导致currency_exchange代码不通过](#Q3)  **2021.3.6**
- [登陆coder的时候显示获取用户信息失败与GitLab创建时出现错误](#Q4)  **2021.3.6**
- [git clone的时候出现"fatal: User cancelled the authentication prompt/remote: HTTP Basic: Access denied/fatal: Authentication failed for .....](#Q5)  **2021.3.5**
- [coder上的试卷地址是用来干什么的？](#Q6)  **2021.3.5**
- [git clone的时候输入密码为什么输入不进去？](#Q7)  **2021.3.5**
- [为什么git clone的时候一直出现密码错误？](#Q8)  **2021.3.5**
- [clone下来后应该干什么？](#Q9)  **2021.3.5**
- [clone使用邮箱之中的密码也一直显示不正确怎么办？/coder里面修改密码的时候显示原密码错误怎么办？](#Q10)  **2021.3.5**
- [我该下载哪些软件？](#Q11)  **2021.3.3**
- [python 和 Anaconda有什么区别？](#Q12)  **2021.3.3**
- [IDEA和Pycharm安装的时候让我选择64-Bit或者其他的选项时该怎么选择？](#Q13)  **2021.3.3**
- [因为防火长城Git下载慢怎么办？](#Q14)  **2021.3.3**

<span id="Q0"></span>
#### Q:关于打开Java作业出现红色文件的情况 
**A**:![B590E405CD2CBE2D6AF6501E7EDAD097](https://pkun.oss-cn-beijing.aliyuncs.com/uPic/B590E405CD2CBE2D6AF6501E7EDAD097.png)

遇到上面这种情况该怎么办？

1. 点击File，然后点击close project
2. ![2925D31DD23E5B4436FB5C2F2356B135](https://pkun.oss-cn-beijing.aliyuncs.com/uPic/2925D31DD23E5B4436FB5C2F2356B135.png)在这个位置，点击open，找到2cd72aa4a*这个项目的文件夹位置
3. ![image-20210421104226986](/Users/pkun/Library/Application Support/typora-user-images/image-20210421104226986.png)选中图中的文件夹，然后点击ok就可以解决问题

#### 为什么会出现这样的问题？

因为clone下来的项目是一个Java项目，IDEA默认会先查看项目的根目录下有没有maven或者gradle这种包管理工具，如果有的话（对我们的项目来说就是pom.xml）就会按照对应的方式来解析我们的项目，如果你没有用任何包管理工具，你就需要打开项目后自己在project structure处设置你的文件夹的属性。

---
<span id="Q1"></span>
#### Q:本地通过了但是push上去就编译或者运行错误的几种可能 
**A**:- 可能是你写完函数之后还在源文件里调用了一次自己，比如
```python
def func():
    ...
# end
func()
```

---
<span id="Q2"></span>
#### Q:从git获取题目时发生异常[org.gitlab4j.api.GitLabApiException]:404 File Not Found 
**A**:转发来自吴林漾助教的解答{@458727969}："提醒一下同学们做题的时候不要移动文件，保持文件结构不变，但是可以在src文件夹下面新建文件。文件结构变了push上去和系统记录的文件结构不一致可能跑不出结果"

---
<span id="Q3"></span>
#### Q:两种不同的格式化方式导致currency_exchange代码不通过 
**A**:在currency_exchange的测试文件中，是从输出流中提取同学们的print语句print出来的字符串打印的，下列两种不同的格式化方法，在输出流中会不一样
![3365F305A095136802E60E0FFF0C35F7](https://pkun.oss-cn-beijing.aliyuncs.com/uPic/3365F305A095136802E60E0FFF0C35F7.jpg)
第一种会通过，但是第二种会显示out of range，如果同学们打断点调试的话，很容易就会发现这两种输出的方式输出流有很大的不同。
![A69253BEF3CE6ED1FD1383B20234C1B8](https://pkun.oss-cn-beijing.aliyuncs.com/uPic/A69253BEF3CE6ED1FD1383B20234C1B8.jpg) 
![87330C24866537A4D731D2BA5FD80078](https://pkun.oss-cn-beijing.aliyuncs.com/uPic/87330C24866537A4D731D2BA5FD80078.jpg) 
至于具体原因，大家可以自行查询python的文档。

---
<span id="Q4"></span>
#### Q:登陆coder的时候显示获取用户信息失败与GitLab创建时出现错误，如下图所示![UH1U3y](https://pkun.oss-cn-beijing.aliyuncs.com/uPic/UH1U3y.png) 
**A**:请联系吴林漾助教{@458727969}

---
<span id="Q5"></span>
#### Q:git clone的时候出现
```
fatal: User cancelled the authentication prompt.`
remote: HTTP Basic: Access denied
fatal: Authentication failed for .....
``` 
**A**:大概率是你第一次clone的时候输错了用户名或者密码，导致出现了问题，你需要查看[使用帮助](http://coder.seecoder.cn/help)，然后再次进行git clone，密码是发送到邮件中的密码。

还有一种可能是你曾经重置过邮箱，但是我们远端仓库记录的还是你第一次使用的邮箱，所以需要进行一次重置，请给这位助教{@936637810}发送信息，重置完后再次git clone

另一种可能是因为你一直用的是邮件里原始的密码进行登陆的，需要你在coder.seecoder.cn里面的修改密码处重新修改一下密码，原密码就是邮件中的密码，修改好后再次git clone，不过这个比较玄学，理论上没修改过的话是可以用原始密码登陆了，极有可能是同学们输出错误了，比如把i的大写和l弄错了。

可能你还需要看看你的邮箱有没有填错（？）如果你没有收到密码，需要检查一下邮箱里的垃圾桶，可能被当成垃圾邮件处理了。

如果还有任何问题，请和这一位助教私聊{@936637810}

---
<span id="Q6"></span>
#### Q:coder上的试卷地址是用来干什么的？ 
**A**:coder上试卷的地址是一个`git clone`使用的链接，你可以使用`git clone <url>`来把试卷下载下来，这个地址并不能直接打开。具体的使用情况请看[使用帮助](http://coder.seecoder.cn/help)

ps：coder上已经给出了一些使用帮助，大家使用一些新的软件或者新的网页的时候如果有什么不懂的地方，可以先**RTFM**

---
<span id="Q7"></span>
#### Q:git clone的时候输入密码为什么输入不进去？ 
**A**:很多软件输入密码的时候不会显示，git就是其中一个。

---
<span id="Q8"></span>
#### Q:为什么git clone的时候一直出现密码错误？ 
**A**:用户名请使用url里面的.cn后接着的那块看起来很像用户名的东西，密码是发送到你邮件之中的密码。

---
<span id="Q9"></span>
#### Q:clone下来后应该干什么？ 
**A**:clone下来后对阅读README，修改代码，然后使用[使用帮助](http://coder.seecoder.cn/help)中给出的方式提交。clone下来的文件在你clone的目录下面。

---
<span id="Q10"></span>
#### Q:clone使用邮箱之中的密码也一直显示不正确怎么办？/coder里面修改密码的时候显示原密码错误怎么办？ 
**A**:请和这一位助教私聊{@936637810}

---
<span id="Q11"></span>
#### Q:我该下载哪些软件？ 
**A**:python 版本3.*均可、JDK 最好是1.8，这两项是必要的，另外如果需要也可以下载Anaconda。IDE方面每个人都是自由的，你可以使用Pycharm、IDEA或者其他的IDE，不用IDE也可以。

ps：机房的环境为Pycharm、IDEA。上机考试需要同学们自己去熟悉环境。

---
<span id="Q12"></span>
#### Q:python 和 Anaconda有什么区别？ 
**A**:Anaconda是python的一个环境与包管理软件，自带一个python3。Anaconda并不是必要的，但是使用它可以节省同学们自己安装python包的时间，同时也帮同学们解决了一些潜在的包版本冲突问题。Python和Anaconda安装了其中一个，另一个就不用安装了，否则有可能引起一些奇怪的冲突。当然，在本门课程中你只有很小很小的概率会遇到包版本冲突。不使用Anaconda的时候，你需要使用`pip/pip3 install <package>`的方式来安装python包。如果速度很慢，请百度搜索`python pip 清华源`来进行换源。

---
<span id="Q13"></span>
#### Q:IDEA和Pycharm安装的时候让我选择64-Bit或者其他的选项时该怎么选择？ 
**A**:电脑是32Bit还是64Bit需要同学们查看自己的电脑的配置，具体如何查看可以百度。有一些配置通过英译中后可以正常理解。其中比较关键的是**环境变量**，环境变量会影响你能否在命令行之中使用一些指令，如果你需要在**任何位置**打开命令行时都可以使用某条指令，比如`javac`或者`python`，那你需要先将这两个东西添加到环境变量之中。网上有大量关于环境变量的教程，在百度中搜索即可。

---
<span id="Q14"></span>
#### Q:因为防火长城Git下载慢怎么办？ 
**A**:挂个梯子，或者使用群里面的文件。

---

<!-- questions ends -->

<span id='Welcome-to-SEC-I-2021.3.3'></span>
## Welcome to SEC-I 2021.3.3

本页面主要用于发布近期对同学们常见问题的收集和回答，以及一些必要的通知和常用链接，每次更新都会附上时间顺序，最新的消息将会被放在最顶上

本页面使用GithubPage进行发布，使用Markdown格式进行编写
