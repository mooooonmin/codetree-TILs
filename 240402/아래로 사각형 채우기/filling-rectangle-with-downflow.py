# 한 변의 길이 n 입력
n = int(input())

# 숫자로 된 정사각형 생성
square = [[0] * n for _ in range(n)]

# 숫자 배치
num = 1
for j in range(n):
    for i in range(n):
        square[i][j] = num
        num += 1

# 결과 출력
for row in square:
    print(*row)