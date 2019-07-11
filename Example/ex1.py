# 복불복
# 총 인원 입력받은 후 입력받은 수 중 임의의 수 하나를 지정
# 팀원들 각자 Enter입력 후 사용자가 정해진 숫자인 경우 당첨, 나머지는 꽝
import random

person = int(input("총 인원 수 입력 >> "))

num = random.randrange(1,person)

for i in range(person):
    guess = int(input("입력 >> "))

    if guess == num:
        print("당첨")
        break
    else:
        print("꽝")