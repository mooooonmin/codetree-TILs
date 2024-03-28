n = int(input())

total_product = 1
i = 1

while total_product < n:
    total_product *= i
    if total_product >= n:
        break
    i += 1

print(i)