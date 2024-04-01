numbers = list(map(int, input().split()))  # 10개의 정수 입력받기

# 짝수 번째 값의 합 계산
sum_even_indices = sum(numbers[1::2])

# 3의 배수 번째 값의 평균 계산
sum_third_multiple_indices = sum(numbers[2::3])
count_third_multiple_indices = len(numbers[2::3])
average_third_multiple_indices = sum_third_multiple_indices / count_third_multiple_indices if count_third_multiple_indices > 0 else 0

print(sum_even_indices, round(average_third_multiple_indices, 1))  # 합과 평균 출력