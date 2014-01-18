#coding=utf-8

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout,QGroupBox,QLabel
from PyQt5.QtGui import QIcon
import res

class Box(QDialog):
    def __init__(self):
        super(Box, self).__init__()
        self.setWindowFlags(Qt.Dialog | Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | 0x00800000)
        # self.setWindowFlags(Qt.Dialog | Qt.WindowStaysOnTopHint | 0x00800000);
        self.setAttribute(Qt.WA_MacAlwaysShowToolWindow);
        self._initUi()
        self.windowPos = None
        self.mousePos = None
        self.dPos = None
        self.startMove = None


    def _initUi(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle("Simple")
        layout = QVBoxLayout()

        headWidget = QWidget()
        headLayout = QHBoxLayout()
        headWidget.setLayout(headLayout)
        layout.addWidget(headWidget)
        edit_icon = QWidget(self)
        edit_icon.resize(30,30)
        edit_icon.setStyleSheet("background: url(:/images/edit-icon);")
        edit_icon.move(20,15)
        label = QLabel("Login Form", self)
        label.resize(label.sizeHint())
        label.move(60,20)

        edit = QLineEdit()
        edit.setObjectName("username")
        edit.setPlaceholderText("username")
        layout.addWidget(edit)

        edit = QLineEdit()
        edit.setObjectName("password")
        edit.setPlaceholderText("password")
        layout.addWidget(edit)

        widget = QWidget()
        layout.addWidget(widget)
        loginLayout = QHBoxLayout()
        loginLayout.setContentsMargins(0,-10,0,0)
        loginLayout.setSpacing(30)
        widget.setLayout(loginLayout)
        # widget.setStyleSheet("background-color:blue")
        btn = QPushButton("登录")
        loginLayout.addWidget(btn)
        btn.clicked.connect(self.login)
        btn.setStyleSheet("margin:0;padding:5 0;border:0px;background-color: #26b9a5;color:white;")
        btn.setAutoDefault(False)

        btn = QPushButton("取消")
        loginLayout.addWidget(btn)
        btn.clicked.connect(self.close)
        btn.setStyleSheet("padding:5px 0;border:0px;background-color: #26b9a5;color:white;")
        btn.setAutoDefault(False)


        # layout.setContentsMargins(11,11,11,11)
        self.setLayout(layout)

    def login(self):
        edit = self.findChild(QLineEdit, "username")
        print "name = %s" % edit.text()

        edit = self.findChild(QLineEdit, "password")
        print "pass = %s" % edit.text()

    def mouseMoveEvent(self,event):
        if(self.startMove): self.move(event.globalPos() - self.dPos)

    def mousePressEvent(self, event):
        self.windowPos = self.pos()
        self.mousePos = event.globalPos()
        self.dPos = self.mousePos - self.windowPos
        self.startMove = True
        
    def mouseReleaseEvent(self, event):
        self.startMove = False

def main():
    app = QApplication(sys.argv)
    css = """
        Box {background: white;}
        QLineEdit {border: 1px solid #eee;height: 30px;}
    """
    app.setStyleSheet(css)
    w = Box()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
