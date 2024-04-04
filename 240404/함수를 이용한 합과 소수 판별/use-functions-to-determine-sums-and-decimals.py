def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def count_primes_with_even_digit_sum(a, b):
    count = 0
    for num in range(a, b + 1):
        if is_prime(num) and sum_of_digits(num) % 2 == 0:
            count += 1
    return count

# 입력 받기
a, b = map(int, input().split())

# 함수 호출하여 결과 출력
print(count_primes_with_even_digit_sum(a, b))