a = int(input())

for i in range(1, a + 1):
    if (i % 2 == 0) and (i % 4 != 0):  # 짝수이면서 4의 배수가 아닌 수
        continue
    if (i // 8) % 2 == 0:  # 8로 나눈 몫이 짝수인 수
        continue
    if i % 7 < 4:  # 7로 나눈 나머지가 4보다 작은 수
        continue
    print(i, end=" ")