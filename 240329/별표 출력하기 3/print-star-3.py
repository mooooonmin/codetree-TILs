n = int(input())

# 위쪽 삼각형 출력
for i in range(n):
    # 공백 출력
    for j in range(i):
        print(" ", end=" ")
    # 별표 출력
    for j in range(2 * (n - i) - 1):
        print("*", end=" ")
    print()