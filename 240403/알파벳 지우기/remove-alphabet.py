def extract_number(input_str):
    # 문자열에서 알파벳을 제외한 숫자만 추출하여 문자열로 반환
    return ''.join(char for char in input_str if char.isdigit())

# 두 문자열에서 숫자를 추출하여 각각 수를 구함
num1 = int(extract_number(input()))
num2 = int(extract_number(input()))

# 두 수의 합을 구하고 출력
print(num1 + num2)