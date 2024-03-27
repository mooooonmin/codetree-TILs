a, b = map(int, input().split())

total_sum = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        total_sum += i

print(total_sum)