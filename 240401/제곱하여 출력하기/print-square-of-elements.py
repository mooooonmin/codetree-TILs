n = int(input())  # 원소의 개수를 입력받음

# n개의 원소를 공백을 기준으로 분리하여 리스트에 저장
elements = list(map(int, input().split()))

# 각 원소에 대해 제곱을 계산하여 출력
for element in elements:
    print(element ** 2, end=" ")