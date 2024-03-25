info = input()
info2 = input()

arr = info.split()
arr2 = info2.split()

age = int(arr[0])
gender = (arr[1])

age2 = int(arr2[0])
gender2 = (arr2[1])

if (age >= 19 or age2 >= 19) :
    if gender == "M" or gender2 == "M" :
        print(1)
else :
    print(0)