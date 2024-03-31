n = int(input())
grades = list(map(float, input().split()))

average = sum(grades) / n
rounded_average = round(average, 1)

if rounded_average >= 4.0:
    print(rounded_average)
    print("Perfect")
elif rounded_average >= 3.0:
    print(rounded_average)
    print("Good")
else:
    print(rounded_average)
    print("Poor")