def modify_numbers(a, b):
    if a < b:
        a += 10
        b *= 2
    else:
        a *= 2
        b += 10
    print(a, b)

a, b = map(int, input().split())
modify_numbers(a, b)