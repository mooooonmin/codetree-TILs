n = int(input())

for i in range(n):
    start_number = 11 + i * 2  # 각 행의 시작 숫자
    for j in range(n):
        print(start_number + j * 2, end=" ")
    print()