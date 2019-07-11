# 독심술
# 1-100까지 정수 입력
# 랜덤 정수 생성
# 랜덤 정수와 비교 후 크면 L, 작으면 H

# L >> 랜덤정수보다 큰 벙위에서 랜덤정수 출력
# H >> 랜덤정수보다 작은 범위에서 랜덤정수 출력
import random

num = int(input("1-100 사이 정수 입력 >> "))

computer_num = random.randint(1,100)


while True:
    if num == computer_num:
        print("C")
        break
    else:
        print(computer_num)
        hint = input(">> ")

        computer_num2 = computer_num

        if hint == "l" or hint == "L":
            computer_num = random.randint(computer_num,100)
        elif hint == "h" or hint == "H":
            computer_num = random.randint(1,computer_num)

