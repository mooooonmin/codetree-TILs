def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def find_lcm(n, m):
    return lcm(n, m)

# 입력 받기
n, m = map(int, input().split())

# 결과 출력
print(find_lcm(n, m))