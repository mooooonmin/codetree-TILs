def add(a, c):
    return a + c

def subtract(a, c):
    return a - c

def multiply(a, c):
    return a * c

def divide(a, c):
    if c != 0:
        return a // c  # '/' 연산 결과의 정수 부분만 반환
    else:
        return False  # 0으로 나눌 수 없음

# 입력 받기
a, o, c = input().split()
a = int(a)
c = int(c)

# 주어진 연산자에 따라 적절한 함수 호출하여 결과 출력
if o == '+':
    print(f"{a} + {c} = {add(a, c)}")
elif o == '-':
    print(f"{a} - {c} = {subtract(a, c)}")
elif o == '*':
    print(f"{a} * {c} = {multiply(a, c)}")
elif o == '/':
    result = divide(a, c)
    if result is not False:
        print(f"{a} / {c} = {result}")
    else:
        print(False)
else:
    print(False)  # 주어진 연산자가 사칙연산자가 아닌 경우