n = int(input())

# 위쪽 삼각형 출력
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

    # 빈 줄 출력
    print()

# 아래쪽 삼각형 출력
for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
    
    # 빈 줄 출력
    print()