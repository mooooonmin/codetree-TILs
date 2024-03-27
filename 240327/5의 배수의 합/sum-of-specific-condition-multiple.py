a, b = map(int, input().split())

start = min(a, b)
end = max(a, b)

total_sum = 0

for num in range(start, end + 1):
    if num % 5 == 0:
        total_sum += num

print(total_sum)