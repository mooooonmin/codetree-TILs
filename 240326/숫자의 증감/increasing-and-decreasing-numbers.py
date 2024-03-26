# 변수 선언, 입력
inp = input()
arr = inp.split()
c = arr[0]
n = int(arr[1])

# 출력
if c == 'A': 
	for i in range(1, n + 1):
		print(i, end=" ")
else:
	for i in range(n, 0, -1):
		print(i, end=" ")