numbers = list(map(int, input().split()))  # 최대 100개의 정수를 입력받음
last_three = []  # 마지막으로 주어진 3개의 정수를 저장할 배열 초기화

for num in numbers:  # 입력받은 정수를 순회
    if num == 0:  # 입력된 정수가 0이면
        break  # 반복문 종료
    last_three.append(num)  # 0이 나올 때까지 정수를 배열에 추가
    if len(last_three) > 3:  # 배열에 3개 이상의 정수가 들어있으면
        last_three.pop(0)  # 가장 오래된 값을 제거하여 3개로 유지

print(sum(last_three))  # 마지막 3개의 정수를 더하여 출력