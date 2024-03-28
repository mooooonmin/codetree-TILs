total_age = 0
count = 0

while True:
    age = int(input())
    if age < 20 or age >= 30:
        break
    total_age += age
    count += 1

if count != 0:
    average_age = total_age / count
    print("{:.2f}".format(average_age))
else:
    print("예외처리")