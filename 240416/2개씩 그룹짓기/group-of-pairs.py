N = int(input())  # 만들어야 하는 그룹의 수 N을 입력받음
numbers = sorted(list(map(int, input().split())))  # 2 * N개의 숫자를 입력받고 정렬

# 각 그룹의 합 중 최댓값을 계산
max_sum = 0
for i in range(N):
    group_sum = numbers[i] + numbers[2*N-1-i]  # 각 그룹의 합을 구함
    max_sum = max(max_sum, group_sum)  # 최댓값 갱신

print(max_sum)