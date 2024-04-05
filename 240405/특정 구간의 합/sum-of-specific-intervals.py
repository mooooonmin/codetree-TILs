A = []

def calculate_sum(a1, a2):
    total = 0
    for i in range(a1-1, a2):
        total += A[i]
    return total

def main():
    global A
    n, m = map(int, input().split())
    A = list(map(int, input().split()))

    for _ in range(m):
        a1, a2 = map(int, input().split())
        print(calculate_sum(a1, a2))

if __name__ == "__main__":
    main()