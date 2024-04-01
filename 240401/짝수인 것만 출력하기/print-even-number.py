n = int(input())
elements = list(map(int, input().split()))

# 짝수인 값만을 저장할 리스트 초기화
even_elements = []

# 주어진 원소 중 짝수인 값을 새로운 배열에 저장
for element in elements:
    if element % 2 == 0:  # 현재 원소가 짝수인지 확인
        even_elements.append(element)  # 짝수인 경우 새로운 배열에 추가

# 짝수인 값들을 공백을 사이에 두고 출력
print(*even_elements)