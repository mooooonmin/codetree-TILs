n = int(input())

divisors_sum = 0

# n의 약수 구하기
for i in range(1, n):
    if n % i == 0:
        divisors_sum += i

# 약수의 합이 n과 같은지 판별
if divisors_sum == n:
    print("P")
else:
    print("N")