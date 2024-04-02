# 첫 번째 문자열 입력
A = input()

# 두 번째 문자열 입력
B = input()

# 문자열 B가 문자열 A의 부분 문자열로 등장하는 횟수를 구하여 출력
count = 0
for i in range(len(A) - 1):
    if A[i:i+2] == B:
        count += 1

print(count)