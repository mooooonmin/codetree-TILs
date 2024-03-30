def print_stars(n):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("* " * n)
        else:
            print("* " + "  " * (n - 2) + "*")

n = int(input())

if 1 <= n <= 10:
    print_stars(n)
else:
    print("..")