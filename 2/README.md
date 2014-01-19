使用qtdesgin协助设计界面
---

所有代码放在
https://github.com/hhuai/qt-learning/tree/master/2

#### 1. 使用QtDesigner设计好界面

在编译过后的qtbase/bin目录下会有一个Designer程序,这个就是qtdesigner。 
打开之后与vb,delphi很像，拖拖拉拉就把界面设计出来了。
这里面要注意的是, 如果需要二次操作的组件，将其objectName设好

![](http://hhuaiblog.qiniudn.com/qt3.png)

保存为ui文件，如 dialog.ui

#### 2. 将ui文件转为python格式

```
pyuic5 dialog.ui > dialog.py
```
注：  我使用的是virtualenv, 报错说找不到 **PyQt5.uic** 之类，进去修改这个脚本的 python2.7w为python就可以了

#### 3. 在你的程序中使用这个设计好的ui

直接贴代码好了，东西很少

```
from PyQt5.QtWidgets import *
from dialog import *
import sys

class Box(QDialog):
    def __init__(self):
        super(Box, self).__init__()
        ui = Ui_Dialog() 
        ui.setupUi(self)
        lcdNumber = self.findChild(QLCDNumber,'lcdNumber')
        lcdNumber.display(10)

def main():
    app = QApplication(sys.argv)
    f = Box()
    f.show()
    app.exec_()
    
if __name__ == '__main__':
    main()  
```

#### 4. 贴一个运行的图

![](http://hhuaiblog.qiniudn.com/qt4.png)
