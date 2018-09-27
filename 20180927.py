# -*- coding: utf-8 -*-
# __author__ = 'Lu'
from PyQt5.QtWidgets import QApplication,QMainWindow
from my import Ui_MainWindow
import sys
class mywindow(Ui_MainWindow,QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__=="__main__":
    app = QApplication(sys.argv)
    myshow=mywindow()
    myshow.show()
    sys.exit(app.exec_())

