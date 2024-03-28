count = 0

while count < 3:
    number = int(input())
    if number % 2 == 0:
        print(number // 2)
        count += 1