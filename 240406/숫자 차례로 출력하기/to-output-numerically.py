def print_numbers_up(n):
    if n == 0:
        return
    print_numbers_up(n - 1)
    print(n, end=' ')

def print_numbers_down(n):
    if n == 0:
        return
    print(n, end=' ')
    print_numbers_down(n - 1)

n = int(input())
print_numbers_up(n)
print()
print_numbers_down(n)