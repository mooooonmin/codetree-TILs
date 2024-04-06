def total_sum(start, end):
    if start == end:
        return start
    else:
        return start + total_sum(start + 1, end)

n = int(input())
print(total_sum(1, n))