numbers = list(map(int, input().split()))  # 정수들을 리스트에 저장

output = []  # 출력을 저장할 리스트 초기화

# 0을 만날 때까지 리스트의 요소들을 순회하며 출력값을 계산하여 output 리스트에 저장
for num in numbers:
    if num == 0:
        break  # 0을 만나면 반복문 종료
    elif num % 2 == 0:
        output.append(num // 2)  # 짝수일 경우 2로 나눈 몫을 output 리스트에 추가
    else:
        output.append(num + 3)  # 홀수일 경우 3을 더한 값을 output 리스트에 추가

# output 리스트에 저장된 값들을 공백을 사이에 두고 출력
print(*output)