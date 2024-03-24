inp = input()

arr = inp.split()

cm = int(arr[0])
kg = int(arr[1])

bmi = kg*10000//(cm*cm)

print(bmi)
if bmi >= 25:
    print("Obesity")