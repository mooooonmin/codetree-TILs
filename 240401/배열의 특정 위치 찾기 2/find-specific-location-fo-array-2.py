numbers = list(map(int, input().split()))  # 10개의 정수를 입력받음

sum_odd = sum(numbers[::2])  # 홀수 번째 입력받은 정수의 합 계산
sum_even = sum(numbers[1::2])  # 짝수 번째 입력받은 정수의 합 계산

# 두 합의 차를 출력
print(abs(sum_even - sum_odd))