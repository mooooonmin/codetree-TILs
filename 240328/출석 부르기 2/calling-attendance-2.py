students = {
    1: "John",
    2: "Tom",
    3: "Paul",
    4: "Sam"
}

while True:
    number = int(input())
    if number in students:
        print(students[number])
    else:
        print("Vacancy")
        break