#try1.py 에러처리

def divide(a,b):
    return a/b

try:
    result = divide(5, "aaa")
    print("결과:{0}", format(result))
except ZeroDivisionError:
    print("0으로 나누면 안됨")
except TypeError:
    print("숫자이어야함")
else:
    print("결과:{0}", format(result))
finally:
    print("한번더체크")

print("전체코드 종료")