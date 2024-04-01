# 두 정수 a, b 입력받기
a, b = map(int, input().split())

# 나머지 등장 횟수 저장할 리스트 초기화
remainder_count = [0] * b

# a가 1 이하가 될 때까지 반복하여 나머지 등장 횟수 계산
while a > 1:
    remainder = a % b  # 현재 나머지 계산
    remainder_count[remainder] += 1  # 해당 나머지 등장 횟수 증가
    a //= b  # a를 b로 나눈 몫을 계산하여 다음 반복을 위해 갱신

# 각 나머지가 등장한 횟수를 제곱하여 합을 계산
total_sum = sum([count ** 2 for count in remainder_count])

# 결과 출력
print(total_sum)