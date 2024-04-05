def is_palindrome(s):
    return s == s[::-1]

A = input()

if is_palindrome(A):
    print("Yes")
else:
    print("No")