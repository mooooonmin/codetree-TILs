def count_divisions(n, count=0):
    # 기저 조건: 주어진 수가 1이 되면 작업 횟수를 반환
    if n == 1:
        return count
    
    # 짝수인 경우
    if n % 2 == 0:
        return count_divisions(n // 2, count + 1)
    # 홀수인 경우
    else:
        return count_divisions(n // 3, count + 1)

# 입력 받기
n = int(input())
# 결과 출력
print(count_divisions(n))