numbers = list(map(int, input().split()))

total = 0
count = 0

for num in numbers:
    if num >= 250:
        break
    total += num
    count += 1

average = total / count if count > 0 else 0

print(total, round(average, 1))