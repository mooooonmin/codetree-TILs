def ascending_descending_sort(n, elements):
    # 오름차순 정렬 후 출력
    ascending_sorted = sorted(elements)
    print(" ".join(map(str, ascending_sorted)))

    # 내림차순 정렬 후 출력
    descending_sorted = sorted(elements, reverse=True)
    print(" ".join(map(str, descending_sorted)))

# 입력 받기
n = int(input())
elements = list(map(int, input().split()))

# 함수 호출
ascending_descending_sort(n, elements)