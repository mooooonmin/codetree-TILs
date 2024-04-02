# 5행 3열의 배열 입력받기
array = [input().split() for _ in range(5)]

# 배열의 각 원소를 대문자로 변환하여 출력
for row in array:
    print(' '.join(map(str.upper, row)))