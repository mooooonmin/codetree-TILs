def swap_case(input_str):
    result = ""
    for char in input_str:
        # 대문자인 경우 소문자로 변경
        if char.isupper():
            result += char.lower()
        # 소문자인 경우 대문자로 변경
        elif char.islower():
            result += char.upper()
        # 알파벳이 아닌 경우 그대로 유지
        else:
            result += char
    return result

# 입력 받기
input_str = input()

# 결과 출력
print(swap_case(input_str))