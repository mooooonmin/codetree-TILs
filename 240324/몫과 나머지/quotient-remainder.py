inp = input()

arr = inp.split()

a = int(arr[0])
b = int(arr[1])

div = a//b #몫
div2 = a%b

print(f'{div}...{div2}')