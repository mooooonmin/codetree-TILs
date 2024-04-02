# 세 개의 문자열 입력
str1 = input()
str2 = input()
str3 = input()

# 각 문자열의 길이 계산
lengths = [len(str1), len(str2), len(str3)]

# 가장 긴 문자열과 가장 짧은 문자열의 길이 차 계산
max_length = max(lengths)
min_length = min(lengths)
difference = max_length - min_length

# 결과 출력
print(difference)