n = int(input())

# 위쪽 삼각형 출력
for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()

# 아래쪽 삼각형 출력
for i in range(n - 1):
    for j in range(i + 2):
        print("*", end=" ")
    print()