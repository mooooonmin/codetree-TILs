a, b, c = map(int, input().split())

no_multiple = True

for num in range(a, b+1):
    if num % c == 0:
        no_multiple = False
        break

if no_multiple:
    print("YES")
else:
    print("NO")