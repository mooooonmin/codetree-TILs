all_multiples_of_3 = True

for _ in range(5):
    num = int(input())
    if num % 3 != 0:
        all_multiples_of_3 = False
        break

if all_multiples_of_3:
    print(1)
else:
    print(0)