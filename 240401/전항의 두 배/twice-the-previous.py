# 첫 번째 항과 두 번째 항 입력받기
a1, a2 = map(int, input().split())

# 결과를 저장할 리스트 초기화
sequence = [a1, a2]

# 10번째 항까지 계산하여 리스트에 추가
for _ in range(8):
    next_term = sequence[-1] + 2 * sequence[-2]  # 다음 항 계산
    sequence.append(next_term)

# 결과 출력
print(*sequence)