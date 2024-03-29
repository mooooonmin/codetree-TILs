n = int(input())

for i in range(n):
    print("*" * (n - i), end="")  # 왼쪽 별표 출력
    print(" " * (2 * i), end="")  # 가운데 공백 출력
    print("*" * (n - i), end="")  # 오른쪽 별표 출력
    print()