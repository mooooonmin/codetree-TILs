n = int(input())  # 단어의 개수를 입력받음
words = []        # 단어들을 저장할 리스트

# n개의 단어를 입력받아 리스트에 저장
for _ in range(n):
    word = input()
    words.append(word)

# 단어들을 사전순으로 정렬
sorted_words = sorted(words)

# 정렬된 단어들을 출력
for word in sorted_words:
    print(word)