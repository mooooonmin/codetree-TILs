def is_prime(num):
    if num < 2:  # 2 미만의 수는 소수가 아님
        return False
    for i in range(2, int(num**0.5) + 1):  # 제곱근까지만 확인
        if num % i == 0:  # 나누어 떨어지면 소수가 아님
            return False
    return True

def sum_of_primes(a, b):
    prime_sum = 0
    for num in range(a, b + 1):
        if is_prime(num):
            prime_sum += num
    return prime_sum

# 입력 받기
a, b = map(int, input().split())

# 함수 호출하여 결과 출력
print(sum_of_primes(a, b))