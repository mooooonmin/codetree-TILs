def divide_even(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] //= 2

N = int(input())
numbers = list(map(int, input().split()))

divide_even(numbers)

for num in numbers:
    print(num, end=" ")