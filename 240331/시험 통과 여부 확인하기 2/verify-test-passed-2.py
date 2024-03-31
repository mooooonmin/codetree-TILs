num_students = int(input())  # 학생 수 입력 받기

passed_students = 0  # 통과한 학생 수 초기화

# 각 학생의 점수 입력 및 처리
for _ in range(num_students):
    scores = list(map(int, input().split()))  # 각 학생의 4과목 점수 입력 받기
    average_score = sum(scores) / len(scores)  # 평균 점수 계산

    if average_score >= 60:  # 평균 점수가 60 이상이면 통과
        print("pass")
        passed_students += 1
    else:  # 그렇지 않으면 불합격
        print("fail")

# 통과한 학생 수 출력
print(passed_students)