n, k, T = input().split()  # n, k, T를 입력받음
n = int(n)
k = int(k)

words = []  # 단어들을 저장할 리스트

# n개의 단어를 입력받아 리스트에 저장
for _ in range(n):
    word = input()
    if word.startswith(T):  # T로 시작하는 단어들만 저장
        words.append(word)

# T로 시작하는 단어들을 사전순으로 정렬
sorted_words = sorted(words)

# k번째 단어를 출력
print(sorted_words[k - 1])