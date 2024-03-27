n = int(input())

cnt_leap = 0

for year in range(1, n + 1):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        cnt_leap += 1

print(cnt_leap)