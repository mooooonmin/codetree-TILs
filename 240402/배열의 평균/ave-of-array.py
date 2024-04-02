# 2행 4열의 배열 입력받기
array = [list(map(int, input().split())) for _ in range(2)]

# 가로 평균 계산
row_avg = [sum(row) / len(row) for row in array]

# 세로 합과 세로 평균 계산
col_sums = [sum(col) for col in zip(*array)]
col_avg = [sum(col) / len(array) for col in zip(*array)]

# 전체 평균 계산
total_sum = sum(sum(row) for row in array)
total_avg = total_sum / (len(array) * len(array[0]))

# 결과 출력
print(' '.join(f"{avg:.1f}" for avg in row_avg))
print(' '.join(f"{avg:.1f}" for avg in col_avg))
print(f"{total_avg:.1f}")