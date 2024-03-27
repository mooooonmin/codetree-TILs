a, b = map(int, input().split())

sum_multiples = 0
count_multiples = 0

for num in range(a, b + 1):
    if num % 5 == 0 or num % 7 == 0:
        sum_multiples += num
        count_multiples += 1

average = sum_multiples / count_multiples

print(sum_multiples, round(average, 1))