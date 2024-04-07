def sort_string(s):
    # 문자열을 알파벳 오름차순으로 정렬
    sorted_string = sorted(s)
    # 정렬된 문자열을 문자열로 변환하여 반환
    return ''.join(sorted_string)

# 입력 받기
input_string = input()

# 함수 호출 및 결과 출력
print(sort_string(input_string))