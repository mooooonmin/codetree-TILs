def absolute_values(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])

N = int(input())
numbers = list(map(int, input().split()))

absolute_values(numbers)

for num in numbers:
    print(num, end=" ")