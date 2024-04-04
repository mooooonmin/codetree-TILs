def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "true"
    else:
        return "false"

# 입력 받기
y = int(input())

# 함수 호출하여 결과 출력
print(is_leap_year(y))