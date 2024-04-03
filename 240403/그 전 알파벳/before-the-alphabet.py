def previous_lowercase(char):
    if char == 'a':
        return 'z'
    else:
        return chr(ord(char) - 1)

# 입력 받기
char = input()

# 결과 출력
print(previous_lowercase(char))