def find_min(a, b, c):
    return min(a, b, c)  # 파이썬 내장 함수 min을 이용하여 최솟값 반환

# 입력 받기
a, b, c = map(int, input().split())

# 함수 호출하여 결과 출력
print(find_min(a, b, c))