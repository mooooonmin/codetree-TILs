def print_star(n, current=1):
    if current > n:
        return
    print("*" * current)
    print_star(n, current + 1)

n = int(input())
print_star(n)