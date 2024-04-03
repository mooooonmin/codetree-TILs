def min_shift(a, b):
    for i in range(len(a)):
        if a[i:] + a[:i] == b:
            return i
    return -1

A = input()
B = input()

print(min_shift(A, B))