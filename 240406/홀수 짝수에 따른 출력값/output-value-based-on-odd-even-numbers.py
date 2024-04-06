def sum_odd_or_even(n):
    total = 0
    # 홀수인 경우
    if n % 2 == 1:
        for i in range(1, n + 1, 2):
            total += i
    # 짝수인 경우
    else:
        for i in range(2, n + 1, 2):
            total += i
    return total

# 입력 받기
n = int(input())
# 결과 출력
print(sum_odd_or_even(n))