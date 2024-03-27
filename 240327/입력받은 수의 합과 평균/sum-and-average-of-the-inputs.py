n = int(input())
total_sum = 0

for _ in range(n):
    num = int(input())
    total_sum += num

average = total_sum / n  # 평균 계산

print(total_sum, round(average, 1))