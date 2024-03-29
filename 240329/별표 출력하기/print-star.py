n = int(input())

# 위쪽 삼각형 출력
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# 아래쪽 삼각형 출력
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()