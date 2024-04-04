def is_perfect_number(num):
    if num % 2 == 0:  # 2로 나누어 떨어지는 경우
        return False
    if num % 10 == 5:  # 일의 자리가 5인 경우
        return False
    if num % 3 == 0 and num % 9 != 0:  # 3으로 나누어 떨어지면서 9로는 나누어 떨어지지 않는 경우
        return False
    return True

def count_perfect_numbers(a, b):
    count = 0
    for num in range(a, b + 1):
        if is_perfect_number(num):
            count += 1
    return count

# 입력 받기
a, b = map(int, input().split())

# 함수 호출하여 결과 출력
print(count_perfect_numbers(a, b))