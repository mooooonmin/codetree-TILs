a, b, c = map(int, input().split())

exist_multiple = False

for num in range(a, b+1):
    if num % c == 0:
        exist_multiple = True
        break

if exist_multiple:
    print("YES")
else:
    print("NO")