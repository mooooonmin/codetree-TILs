first, second = map(int, input().split())  # 첫째항과 둘째항을 입력받음

sequence = [first, second]  # 첫째항과 둘째항으로 이루어진 수열 초기화

# 세 번째 항부터 10개의 항을 생성하여 수열에 추가
for _ in range(8):
    next_term = (sequence[-2] + sequence[-1]) % 10  # 전전항과 전항의 합을 10으로 나눈 나머지를 구함
    sequence.append(next_term)  # 계산한 항을 수열에 추가

# 수열을 공백을 사이에 두고 출력
print(*sequence)