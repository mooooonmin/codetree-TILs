from collections import Counter

def can_rearrange(word1, word2):
    # 두 단어의 문자들이 동일한지 확인
    if Counter(word1) != Counter(word2):
        return "No"
    
    # 두 단어의 문자들의 순서가 동일한지 확인
    sorted_word1 = sorted(word1)
    sorted_word2 = sorted(word2)
    if sorted_word1 == sorted_word2:
        return "Yes"
    else:
        return "No"

# 두 단어를 입력받고 함수 호출
word1 = input()
word2 = input()
result = can_rearrange(word1, word2)
print(result)