class Message:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time
    
    def display(self):
        print("secret code : {}".format(self.secret_code))
        print("meeting point : {}".format(self.meeting_point))
        print("time : {}".format(self.time))

# 입력을 받고 Message 객체 생성
secret_code, meeting_point, time = input().split()
message = Message(secret_code, meeting_point, time)

# 출력
message.display()