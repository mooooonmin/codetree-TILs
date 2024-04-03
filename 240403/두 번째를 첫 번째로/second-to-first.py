def replace_second_char(input_str):
    # 두 번째 문자
    second_char = input_str[1]

    # 입력 문자열을 리스트로 변환하여 각 문자를 확인하고 두 번째 문자와 같으면 첫 번째 문자로 바꿔줌
    result = [input_str[0] if char == second_char else char for char in input_str]

    # 결과 리스트를 문자열로 변환하여 반환
    return ''.join(result)

# 입력 받기
input_str = input()

# 함수 호출하여 결과 출력
print(replace_second_char(input_str))