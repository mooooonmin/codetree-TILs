# 숫자의 개수 n 입력받기
n = int(input())

# n개의 정수를 리스트로 입력받기
numbers = list(map(int, input().split()))

# 정렬된 숫자 리스트에서 인접한 두 숫자의 차이를 계산하여 최소값 찾기
min_difference = float('inf')  # 최소값을 저장할 변수를 무한대로 초기화
for i in range(1, n):
    difference = numbers[i] - numbers[i - 1]  # 인접한 두 숫자의 차이 계산
    if difference < min_difference:
        min_difference = difference

# 최소값 출력
print(min_difference)