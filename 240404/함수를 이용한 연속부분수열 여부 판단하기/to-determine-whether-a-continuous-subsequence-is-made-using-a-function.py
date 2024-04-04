def is_continuous_subsequence(A, B):
    n1 = len(A)
    n2 = len(B)
    
    for i in range(n1 - n2 + 1):  # 수열 A에서 수열 B의 길이만큼 순회
        if A[i:i+n2] == B:  # A의 부분 수열이 B와 일치하는지 확인
            return True
    return False

# 입력 받기
n1, n2 = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 함수 호출하여 결과 출력
if is_continuous_subsequence(A, B):
    print("Yes")
else:
    print("No")