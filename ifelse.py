# ifelse.py
# 다중라인 ^+/
# score = int(input("점수입력"))

# if 90 <= score <= 100:
#     grade = 'A'
# elif 80 <= score < 90:
#     grade = 'B'
# elif 70 <= score < 80:
#     grade = 'C'
# else:
#     grade = 'D'

# print("등급은 ", grade)

# value =5
# while value > 0:
#     print(value)
#     value -= 1

# lst = [1,2,3]
# for item in lst:
#     print(item)



lst = list(range(1,11))
print([i**2 for i in lst if i > 5]) 

lst = [10, 30, 500]
iterL = filter(None, lst)
for item in iterL:
    print(item)

def getB20(i):
    return i > 20

print("필터링")
iterL = filter(getB20, lst)
for item in iterL:
    print(item)

print("람다함수")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)

