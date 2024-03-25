# 세 정수 입력 받기
a, b, c = map(int, input().split())

# 중앙값 구하기
if a <= b:
    if b <= c:
        median = b
    elif a <= c:
        median = c
    else:
        median = a
else:
    if a <= c:
        median = a
    elif b <= c:
        median = c
    else:
        median = b

# 중앙값 출력
print(median)