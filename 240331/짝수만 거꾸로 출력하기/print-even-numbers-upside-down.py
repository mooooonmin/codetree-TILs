n = int(input())  # 정수 n 입력
numbers = list(map(int, input().split()))  # n개의 정수 입력

# 입력된 정수 중에서 짝수만 역순으로 출력
for num in reversed(numbers):
    if num % 2 == 0:
        print(num, end=" ")