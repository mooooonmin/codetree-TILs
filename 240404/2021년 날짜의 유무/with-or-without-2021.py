def is_valid_date(M, D):
    if M < 1 or M > 12:  # 올바른 월 범위 확인
        return False
    
    if M == 2:  # 2월인 경우
        if D < 1 or D > 28:  # 2월의 일 범위 확인
            return False
    elif M in [4, 6, 9, 11]:  # 4, 6, 9, 11월인 경우
        if D < 1 or D > 30:  # 30일까지 있는 월의 일 범위 확인
            return False
    else:  # 나머지 월인 경우
        if D < 1 or D > 31:  # 31일까지 있는 월의 일 범위 확인
            return False
    
    return True

# 입력 받기
M, D = map(int, input().split())

# 함수 호출하여 결과 출력
if is_valid_date(M, D):
    print("Yes")
else:
    print("No")