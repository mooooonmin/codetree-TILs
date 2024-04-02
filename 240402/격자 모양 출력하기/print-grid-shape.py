# 격자의 크기와 점의 개수 입력
n, m = map(int, input().split())

# 격자 초기화
grid = [[0] * n for _ in range(n)]

# 점의 위치 입력 및 격자에 표시
for _ in range(m):
    x, y = map(int, input().split())
    grid[x-1][y-1] = x * y

# 결과 출력
for row in grid:
    print(*row)