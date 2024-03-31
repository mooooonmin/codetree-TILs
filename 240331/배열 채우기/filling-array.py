arr = []

# 한 줄에 입력된 여러 개의 정수를 공백을 기준으로 분리하여 정수로 변환하여 리스트에 추가
input_str = input()
nums = input_str.split()
for num_str in nums:
    num = int(num_str)
    if num == 0:
        break
    arr.append(num)

# 입력된 숫자들을 뒤에서부터 출력
while arr:
    print(arr.pop(), end=" ")