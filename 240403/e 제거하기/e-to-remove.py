def remove_first_e(input_str):
    # 문자열의 첫 번째 'e'를 찾음
    index = input_str.find('e')
    
    # 만약 'e'가 문자열에 존재할 경우
    if index != -1:
        # 해당 'e'를 제거한 결과를 반환
        return input_str[:index] + input_str[index+1:]
    else:
        # 'e'가 없을 경우 그대로 반환
        return input_str

# 입력 받기
input_str = input()

# 함수 호출하여 결과 출력
print(remove_first_e(input_str))