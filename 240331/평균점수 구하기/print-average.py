scores = list(map(float, input().split()))

average = sum(scores) / len(scores)
print(round(average, 1))