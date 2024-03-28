def is_perfect(num):
    if num % 2 == 0:  # 2로 나누어 떨어지는 경우
        return False
    if num % 10 == 5:  # 일의 자리가 5인 경우
        return False
    if num % 3 == 0 and num % 9 != 0:  # 3으로 나누어 떨어지면서 9로는 나누어 떨어지지 않는 경우
        return False
    return True

def find_perfect_numbers(n):
    perfect_numbers = []
    for i in range(1, n + 1):
        if is_perfect(i):
            perfect_numbers.append(i)
    return perfect_numbers

n = int(input())
perfect_numbers = find_perfect_numbers(n)
print(*perfect_numbers)