n = int(input())  # 숫자의 개수를 입력받음
numbers = list(map(int, input().split()))  # n개의 숫자를 입력받아 리스트에 저장

sorted_numbers = []  # 현재까지 입력받은 숫자들을 정렬하여 저장할 리스트
output = []  # 중앙값을 저장할 리스트

# 홀수 번째 원소까지 읽으면서 중앙값을 출력
for i in range(n):
    sorted_numbers.append(numbers[i])  # 현재까지의 숫자를 정렬된 리스트에 추가
    sorted_numbers.sort()  # 정렬된 리스트를 오름차순으로 정렬
    if i % 2 == 0:  # 홀수 번째 원소를 읽었을 때 중앙값을 출력
        output.append(sorted_numbers[i // 2])  # 중앙값을 출력 리스트에 추가

# 결과 출력
print(' '.join(map(str, output)))