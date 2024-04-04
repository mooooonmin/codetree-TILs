def div(N):
    total = 0  # 총합을 저장할 변수 초기화
    for i in range(1, N + 1):
        total += i  # 1부터 N까지의 합을 계산
    result = total // 10  # 총합을 10으로 나눈 몫을 계산
    return result  # 결과 반환

# 입력 받기
N = int(input())

# 함수 호출하여 결과 출력
print(div(N))