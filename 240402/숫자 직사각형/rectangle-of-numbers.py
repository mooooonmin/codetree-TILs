# 세로변의 길이 n과 가로변의 길이 m을 입력받음
n, m = map(int, input().split())

# 숫자로 이루어진 직사각형을 저장할 2차원 배열 초기화
rectangle = [[0] * m for _ in range(n)]

# 직사각형에 숫자 할당
num = 1
for i in range(n):
    for j in range(m):
        rectangle[i][j] = num
        num += 1

# 직사각형 출력
for row in rectangle:
    print(*row)