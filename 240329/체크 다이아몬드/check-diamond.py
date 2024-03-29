n = int(input())

# 위쪽 삼각형 출력
for i in range(1, n + 1):
    # 왼쪽 공백 출력
    print(" " * (n - i), end="")
    # 별표 출력
    print("* " * i)

# 아래쪽 삼각형 출력
for i in range(n - 2, -1, -1):
    # 왼쪽 공백 출력
    print(" " * (n - i - 1), end="")
    # 별표 출력
    print("* " * (i + 1))