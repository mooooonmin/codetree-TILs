numbers = list(map(int, input().split()))

for i in range(1, len(numbers)):  # 두 번째 원소부터 마지막 원소까지 순회
    if numbers[i] % 3 == 0:  # 현재 원소가 3의 배수인지 확인
        print(numbers[i - 1])  # 3의 배수가 처음으로 등장하는 바로 앞의 원소 출력
        break  # 3의 배수가 발견되면 반복문 종료