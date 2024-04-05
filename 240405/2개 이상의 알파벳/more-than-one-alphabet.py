def has_multiple_characters(s):
    unique_chars = set(s)
    return len(unique_chars) >= 2

def main():
    A = input()

    if has_multiple_characters(A):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()