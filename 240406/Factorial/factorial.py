def factorial(n):
    # 기저 조건: n이 0 또는 1일 때는 1을 반환
    if n == 0 or n == 1:
        return 1
    # 재귀적으로 n! 값을 계산하여 반환
    else:
        return n * factorial(n - 1)

n = int(input())
print(factorial(n))