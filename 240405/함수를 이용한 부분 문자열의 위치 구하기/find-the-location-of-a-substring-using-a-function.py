def find_substring_index(input_str, target_str):
    index = input_str.find(target_str)
    if index != -1:
        return index
    else:
        return -1

input_str = input().strip()
target_str = input().strip()

print(find_substring_index(input_str, target_str))