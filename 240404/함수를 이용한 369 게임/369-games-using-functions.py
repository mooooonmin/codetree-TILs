def count_numbers(a, b):
    count = 0
    for num in range(a, b + 1):
        # 각 숫자를 확인하여 3, 6, 9 중 하나가 포함되거나 해당 숫자 자체가 3의 배수인 경우
        if '3' in str(num) or '6' in str(num) or '9' in str(num) or num % 3 == 0:
            count += 1
    return count

# 입력 받기
a, b = map(int, input().split())

# 함수 호출하여 결과 출력
print(count_numbers(a, b))