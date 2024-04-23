class Information:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

    def print_info(self):
        print("code :", self.code)
        print("color :", self.color)
        print("second :", self.second)

def main():
    input_data = input().split()
    code = input_data[0]
    color = input_data[1]
    second = int(input_data[2])

    info = Information(code, color, second)
    info.print_info()

if __name__ == "__main__":
    main()