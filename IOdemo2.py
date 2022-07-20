#IO Demo2.py

f = open("demo.txt", "wt")
f.write("첫번째\n두번째\n세번째\n")
f.close()

#파일 읽고 처리
f = open("demo.txt", "rt")
result = f.read()  #문자열변수 result
print(result)
print(f.tell())
f.seek(0)
lst=f.readlines()
print(lst)
for item in lst:
    print(item, end="")
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")

f.close()
with open("demo.txt", "rt") as f:
    for item in f.readlines():
        print(item, end="")

