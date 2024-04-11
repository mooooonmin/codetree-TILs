n = int(input())  # 원소의 개수를 입력받음

# 수열 A와 수열 B를 입력받아 리스트에 저장하고 정렬
sequence_A = sorted(list(map(int, input().split())))
sequence_B = sorted(list(map(int, input().split())))

# 정렬된 두 수열이 동일한지를 비교
if sequence_A == sequence_B:
    print("Yes")
else:
    print("No")