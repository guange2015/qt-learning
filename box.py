#coding=utf-8

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout,QGroupBox

class Box(QDialog):
    def __init__(self):
        super(Box, self).__init__()
        self.setWindowFlags(Qt.Dialog | Qt.WindowStaysOnTopHint | 0x00800000);
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

    def login(self):
        edit = self.findChild(QLineEdit, "username")
        print "name = %s" % edit.text()

        edit = self.findChild(QLineEdit, "password")
        print "pass = %s" % edit.text()

def main():
    app = QApplication(sys.argv)
    w = Box()
    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
