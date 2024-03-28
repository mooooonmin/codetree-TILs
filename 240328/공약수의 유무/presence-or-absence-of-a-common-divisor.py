a, b = map(int, input().split())

exist_common_divisor = False

for num in range(a, b+1):
    if 1920 % num == 0 and 2880 % num == 0:
        exist_common_divisor = True
        break

if exist_common_divisor:
    print(1)
else:
    print(0)