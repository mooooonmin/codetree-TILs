cnt_even = 0

for _ in range(5): 
    num = int(input())
    if num % 2 == 0:
        cnt_even += 1

print(cnt_even)