class Product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

def main():
    # 첫 번째 객체 초기화
    product1 = Product("codetree", "50")
    print("product", product1.code, "is", product1.name)

    # 두 번째 객체 입력 받아 초기화
    name, code = input().split()
    product2 = Product(name, code)
    print("product", product2.code, "is", product2.name)

if __name__ == "__main__":
    main()