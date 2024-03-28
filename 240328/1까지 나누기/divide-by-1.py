n = int(input())

quotient = n
count = 0

for i in range(1, n):
    if quotient <= 1:
        break
    quotient //= i
    count += 1

print(count)