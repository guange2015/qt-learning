qt界面美化
-----

完整代码放在
https://github.com/hhuai/qt-learning/tree/master/1

####  1. 手写一个原生的登录框

```
class Box(QDialog):
    def __init__(self):
        super(Box, self).__init__()
        self.setWindowFlags(Qt.Dialog | Qt.WindowStaysOnTopHint);
        self.setAttribute(Qt.WA_MacAlwaysShowToolWindow);
        self._initUi()

    def _initUi(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle("Simple")
        layout = QVBoxLayout()

        edit = QLineEdit()
        edit.setObjectName("username")
        edit.setPlaceholderText("username")
        layout.addWidget(edit)

        edit = QLineEdit()
        edit.setObjectName("password")
        edit.setPlaceholderText("password")
        layout.addWidget(edit)

        widget = QGroupBox("")
        layout.addWidget(widget)
        loginLayout = QHBoxLayout()
        widget.setLayout(loginLayout)
        btn = QPushButton("登录")
        loginLayout.addWidget(btn)
        btn.clicked.connect(self.login)
        btn.setAutoDefault(False)

        btn = QPushButton("取消")
        loginLayout.addWidget(btn)
        btn.clicked.connect(self.close)
        btn.setAutoDefault(False)

        self.setLayout(layout)
```

一个VBox加一个HBox布局，下面是运行效果

![原生的](http://hhuaiblog.qiniudn.com/qt1.jpg)

#### 2. 来个自定义标题栏

原生的标题栏是系统的，我们很难去定制，在算在原生的cocoa或win32下定制也非常麻烦，解决办法是直接隐藏算系统的，我们自己在窗体中加一个我们自义的标题栏

* 去掉标题栏

  ``` 
  self.setWindowFlags(Qt.FramelessWindowHint ) 
  ```

 运行后发现，标题栏是去掉了，但窗口也不能进行拖动了。

* 加入自定义拖动消息

 重载 **mouseMoveEvent** **mousePressEvent** **mouseReleaseEvent** 来定义鼠标拖动时拉动窗口

* 自己定义标题栏

 这里没找到相应素材，找到再补，囧。。

#### 3. 塞点自定义小图标点缀一下

* 加入图标资源
  新建 **images**目录用于存放图片
    
* 定义qrc文件
    
    ```
    <RCC>
    <qresource prefix="/images">
      <file alias='edit-icon'>images/1.png</file>
    </qresource>
    </RCC>
    ```

* 编译qrc为python文件

    ```
    pyrcc5 res.qrc -o res.py
    ```
    
* 在程序中使用图标
    个人喜欢使用css的方式，如下

    ``` 
    edit_icon.setStyleSheet("background: url(:/images/edit-icon);") 
    ```
  
#### 4. 输入框美化

* 用css简单搞定

    ```
    QLineEdit {border: 1px solid #eee;height: 30px;}
    ```

#### 5. 按钮扁平化

* 同上

    ```
    btn.setStyleSheet("padding:5px 0;border:0px;background-color: #26b9a5;color:white;")
    ```

#### 6. 这是美化最终效果
![美化之后](http://hhuaiblog.qiniudn.com/qt2.png)
