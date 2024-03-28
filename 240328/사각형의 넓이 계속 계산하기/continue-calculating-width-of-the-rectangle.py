while True:
    # 가로, 세로, 문자
    width, height, character = input().split()

    width = int(width)
    height = int(height)
    area = width * height
    print(area)
    
    if character == 'C':
        break