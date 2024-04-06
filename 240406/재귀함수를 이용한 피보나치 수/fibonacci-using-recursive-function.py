def fibonacci(n):
    # 기저 조건: n이 1 이하일 때는 n을 반환
    if n <= 1:
        return n
    # 이전 두 항의 합으로 현재 항을 구함
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input())
print(fibonacci(n))