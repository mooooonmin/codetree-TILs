total_sum = 0
count = 0

for _ in range(10):
    num = int(input())
    if 0 <= num <= 200:
        total_sum += num
        count += 1

average = total_sum / count if count > 0 else 0

print(total_sum, round(average, 1))