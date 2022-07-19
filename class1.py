# class1.py
# 1) 클래스정의
class Person:
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스
p1 = Person()
p2 = Person()
p1.name="이현숙"
#3)인스턴스 호출
p1.print()
p2.print()

#동적추가
Person.title = "new"
print(p1.title)
print(p2.title)
print(Person.title)