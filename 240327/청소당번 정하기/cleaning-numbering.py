n = int(input())

cnt_class = 0
cnt_pass = 0
cnt_rest = 0

for day in range(1, n + 1):
    if day % 12 == 0:
        cnt_rest += 1
    elif day % 3 == 0:
        cnt_pass += 1
    elif day % 2 == 0:
        cnt_class += 1

print(cnt_class, cnt_pass, cnt_rest)