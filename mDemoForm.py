# mDemoForm.py
# DemoForm.ui(미리디자인으로만든 화면) + DemoForm.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


#폼디자인을 로딩
form_class= uic.loadUiType("DemoForm.ui")[0]
#클래스정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 QT 화면")

#진입점을 체크
if __name__ == "__main__":  #안해도 오케이
    app = QApplication(sys.argv)
    demoWindow= DemoForm()
    demoWindow.show() 
    app.exec_()


