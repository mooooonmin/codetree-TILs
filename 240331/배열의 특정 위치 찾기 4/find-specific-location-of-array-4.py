numbers = list(map(int, input().split()))

count = 0
total = 0

for num in numbers:
    if num == 0:
        break
    if num % 2 == 0:
        count += 1
        total += num

print(count, total)