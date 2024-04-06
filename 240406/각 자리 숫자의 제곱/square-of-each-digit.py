def sum_of_square_digits(n):
    # 정수를 문자열로 변환하여 각 자리 숫자를 추출
    digits = str(n)
    # 각 자리 숫자의 제곱의 합 계산
    total = sum(int(digit) ** 2 for digit in digits)
    return total

# 입력 받기
n = int(input())
# 결과 출력
print(sum_of_square_digits(n))