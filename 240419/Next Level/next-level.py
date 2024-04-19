class User:
    def __init__(self, user_id, level):
        self.user_id = user_id
        self.level = level

# 첫 번째 객체 초기화
user1 = User("codetree", "10")

# 입력 받기
input_data = input().split()
user_id_input = input_data[0]
level_input = input_data[1]

# 새로운 객체 생성
user2 = User(user_id_input, level_input)

# 출력
print(f"user {user1.user_id} lv {user1.level}")
print(f"user {user2.user_id} lv {user2.level}")