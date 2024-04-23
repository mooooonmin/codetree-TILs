class Person:
    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

def main():
    n = int(input())
    people = []

    # 입력 받기
    for _ in range(n):
        name, address, city = input().split()
        people.append(Person(name, address, city))

    # 사전순으로 정렬
    people.sort(key=lambda x: x.name)

    # 가장 느린 사람의 정보 출력
    slowest_person = people[-1]
    print("name", slowest_person.name)
    print("addr", slowest_person.address)
    print("city", slowest_person.city)

if __name__ == "__main__":
    main()