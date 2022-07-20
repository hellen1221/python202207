# OSDemoPath.py

from glob import glob
import random

print(random.random())  #0~1
print(random.random())

print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])

print(random.sample(range(20), 10))
print(random.sample(range(30), 10))

from os.path import *
print(abspath("python.exe"))
print(basename("c:\\python39\\python.exe"))
print(getsize("c:\\python39\\python.exe"))

#운영체제정보 가져오기
from os import *
print("운영체제명 :",name)
#system("notepad.exe")

#파일리스트
import glob
result = glob.glob("c:\\work\\*.py") #list return
print(result)

