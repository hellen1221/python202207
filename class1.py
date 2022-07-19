# class1.py
# 1) 클래스정의
class Person:
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스
p1=Person()
#3)인스턴스 호출
p1.print()