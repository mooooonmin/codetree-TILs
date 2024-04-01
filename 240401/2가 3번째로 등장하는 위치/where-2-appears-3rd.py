# 정수의 개수 n 입력받기
n = int(input())

# n개의 정수를 리스트로 입력받기
numbers = list(map(int, input().split()))

# 2가 몇 번째로 등장하는지 확인하기 위한 변수 초기화
count = 0

# 주어진 정수들을 순회하면서 2가 몇 번째로 등장하는지 파악
for idx, num in enumerate(numbers):
    if num == 2:
        count += 1
        if count == 3:  # 2가 3번째로 등장했을 때 해당 인덱스를 출력하고 반복 종료
            print(idx + 1)
            break

# 2가 3번째로 등장하지 않는 경우를 고려하여 출력
else:
    print("2가 3번째로 등장하지 않았습니다.")