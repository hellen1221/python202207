# DemoButton.py
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()  #deginer setupUi

    def setupUI(self):
        btn1 = QPushButton("닫기", self)
        # 좌측상단(x,y)
        btn1.move(20, 20)
        # 해당 위젯 시그널에 슬롯메서드를 연결
        btn1.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_() 