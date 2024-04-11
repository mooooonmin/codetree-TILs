N, k = map(int, input().split())  # 원소의 수 N과 k를 입력받음
numbers = list(map(int, input().split()))  # N개의 숫자를 입력받아 리스트에 저장

# 숫자들을 오름차순으로 정렬
sorted_numbers = sorted(numbers)

# k번째 숫자를 출력
print(sorted_numbers[k-1])