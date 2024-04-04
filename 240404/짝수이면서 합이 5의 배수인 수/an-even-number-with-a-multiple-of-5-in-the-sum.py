def check_number(n):
    # 주어진 수가 짝수인지 확인
    if n % 2 == 0:
        # 각 자리 숫자의 합 계산
        digit_sum = sum(int(digit) for digit in str(n))
        # 합이 5의 배수인지 확인
        if digit_sum % 5 == 0:
            return "Yes"
        else:
            return "No"
    else:
        return "No"

# 입력 받기
n = int(input())

# 함수 호출하여 결과 출력
print(check_number(n))