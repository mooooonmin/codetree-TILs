# 최대공약수를 구하는 재귀 함수
def gcd(a, b):
    # 기저 조건: b가 0이면 a를 반환
    if b == 0:
        return a
    # 재귀적으로 gcd 함수 호출
    return gcd(b, a % b)

# 최소공배수를 구하는 재귀 함수
def lcm(a, b):
    return a * b // gcd(a, b)

# 주어진 수들의 최소공배수를 구하는 함수
def lcm_of_numbers(numbers, n):
    if n == 1:
        return numbers[0]
    else:
        return lcm(numbers[n - 1], lcm_of_numbers(numbers, n - 1))

# 입력 받기
n = int(input())
numbers = list(map(int, input().split()))

# 결과 출력
print(lcm_of_numbers(numbers, n))