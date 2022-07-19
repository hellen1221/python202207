#전역변수 
str = "Not Class Member"

#클래스의정의 : 파이썬에서는 항상 명시적으로 지정하자 self.str
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        print(self.str)

g = GString()
g.set("First Message")
g.print()
