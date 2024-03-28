n = int(input())

total_sum = 0
i = 1

while total_sum < n:
    total_sum += i
    if total_sum >= n:
        break
    i += 1

print(i)