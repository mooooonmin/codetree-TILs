a, b = map(int, input().split())

total_sum = 0

for num in range(a, b + 1):
    if num % 6 == 0 and num % 8 != 0:  # 6의 배수이면서 8의 배수가 아닌 경우
        total_sum += num

print(total_sum)