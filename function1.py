# function1.py

def times(a,b):
    return a+b, a*b

result = times(3,4)
print(result)

def setValues(newValues):
    x = newValues
    print("함수내부", x)

result = setValues(5)
print(result)

def intersect(prelist, postlist) :
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect("HAM","SPAM"))