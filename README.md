qt 学习系列
---

代码为了保持简洁，全部用python来写，其实和c++的没什么两样。


1. [界面美化入门][1]
1. [使用qt-designer加速界面设计][2]


## 环境准备



### 一、 编译Qt 5.2.0


#### 1. 下载源码

版本是: **Qt 5.2.0**

#### 2. 查看代码目录下的README

```
cd <path>/qt-everywhere-opensource-src-<version>
./configure -prefix $PWD/qtbase -opensource -nomake tests
make -j 4
```

##### 第二行可以加上不编译example
```
./configure -prefix $PWD/qtbase -opensource -nomake tests -nomake examples
```
这里还可以配 debug , static方式
```
./configure --help
```

比如编一个不需要webkit的静态调试版本
```
./configure -prefix $PWD/qtbase -opensource -nomake tests -nomake examples -debug -static -skip qtwebkit
```

#### 3. 进入漫长的编译

我在OSX10.9 xcode5下，组合编了几个，都没有什么问题，在我的电脑上，要webkit大约三小时，不要的1个半小时左右

---

### 二、编译PyQt5

安装教程在这里
http://pyqt.sourceforge.net/Docs/PyQt5/installation.html

大概步骤就是先装 sip, 再来安装pyqt, 这里只要指定上面编译的qmake路径就好了

测试一下是否安装成功

```
>>> import PyQt5
```

[1]: http://hhuai.github.io/blog/2015/01/18/learning-qt-1/
[2]: http://hhuai.github.io/blog/2015/01/18/learning-qt-2/
