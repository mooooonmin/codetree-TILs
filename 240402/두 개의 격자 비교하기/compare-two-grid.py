# 격자의 행과 열 개수 입력
n, m = map(int, input().split())

# 첫 번째 격자 입력
grid1 = [list(map(int, input().split())) for _ in range(n)]

# 두 번째 격자 입력
grid2 = [list(map(int, input().split())) for _ in range(n)]

# 새로운 격자 생성
new_grid = [[0 if grid1[i][j] == grid2[i][j] else 1 for j in range(m)] for i in range(n)]

# 결과 출력
for row in new_grid:
    print(*row)