# mDemoForm2.py
# DemoForm.ui(미리디자인으로만든 화면) + mDemoForm2.py
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹서버와 통신할 경우 
import urllib.request
#클로링
from bs4 import BeautifulSoup



#폼디자인을 로딩
form_class= uic.loadUiType("DemoForm2.ui")[0]
#클래스정의 QMainWindow
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    # slot method 정의
    def firstClick(self):
        #파일로 저장
        f = open("webtoon.txt", "wt", encoding="utf-8")

        try: 
            for i in range(1,11):
                url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" \
                + str(i)
                print(url)
                data = urllib.request.urlopen(url) 
                soup = BeautifulSoup(data, "html.parser")
                #특정한 태그를 검색
                cartoons = soup.find_all("td", class_="title")
                for item in cartoons:
                    item2 = item.find("a")
                    title = item2.text.strip()
                    print(title)
                    f.write(title + "\n")
        except:
            pass 

        f.close()

        self.label.setText("웹툰 크롤링 종료")
    def secondClick(self):
        self.label.setText("두번째클릭")
    def thirdClick(self):
        self.label.setText("세번째클릭")
#진입점을 체크
if __name__ == "__main__":  #안해도 오케이
    app = QApplication(sys.argv)
    demoWindow= DemoForm()
    demoWindow.show() 
    app.exec_()


