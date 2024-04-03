def shift_string(A, commands):
    for command in commands:
        if command == 'L':
            # 왼쪽으로 한 칸 이동
            A = A[1:] + A[0]
        elif command == 'R':
            # 오른쪽으로 한 칸 이동
            A = A[-1] + A[:-1]
    return A

# 입력 받기
A = input()
commands = input()

# 결과 출력
print(shift_string(A, commands))