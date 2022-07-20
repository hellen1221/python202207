# strDemo.py
print(dir(str))

strA = "Python은 강력해"
strB = "Python is very powerful"

print(len(strA))
print(len(strB))
print(strB.capitalize())
print(strB.startswith("Py"))
print(strB.endswith("ful"))
print(strB.endswith("ful",7))
print(strB.count("p"))
print(strB.count("p",7))

u = "<<< spam and ham >>>"
result = u.strip("<> ")
print(u)
print(result)


result = result.replace("spam", "spam egg")
print(result)
lst = result.split()
print(lst)
print(":)".join(lst)) # join은 리턴형이 str

