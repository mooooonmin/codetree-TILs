# 격자의 크기 입력
n = int(input())

# 격자 초기화
grid = [[0] * n for _ in range(n)]

# 오른쪽 아래에서부터 시작하는 숫자
num = n * n

# 짝수 행일 때의 숫자 채우기
for i in range(n):
    if i % 2 == 0:
        for j in range(n-1, -1, -1):
            grid[j][i] = num
            num -= 1
    else:
        for j in range(n):
            grid[j][i] = num
            num -= 1

# 결과 출력
for row in grid:
    print(*row)