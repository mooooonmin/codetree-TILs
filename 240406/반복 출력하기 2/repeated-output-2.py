def print_hello_world(n):
    if n == 0:
        return
    print("HelloWorld")
    print_hello_world(n - 1)

n = int(input())
print_hello_world(n)