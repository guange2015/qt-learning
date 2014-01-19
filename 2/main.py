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
