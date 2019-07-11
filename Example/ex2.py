# 쥐잡기
# (0,0) --- (10,10)
# 사용자가 입력한 좌표와 목표좌표 거리출력

import random
from math import sqrt, pow

T = int(input("반복 횟수 >> "))

#10X10 리스트 초기화
position = [[0]*10 for _ in range(10)]
# 현재위치 입력
myPosition = list(map(int, input("현재위치 입력(0-9)>> ").split(" ")))


# 목표위치 좌표설정
destination = []
for i in range(2):
    destination.append(random.randint(0,9))

print(destination)


for i in range(T):
    result = []

    # 거리계산
    for i in range(2):
        result.append(myPosition[i] - destination[i])

    # 거리비교
    if result[0]==0 and result[1]==0:
        print("정답")
        break
    elif i==T:
        print("탈락")
    else:
        # 삼각형 빛변의 길이
        calc = sqrt(pow(result[0], 2) + pow(result[1], 2))
        #print("%d" % calc)
        print(result)
        myPosition = list(map(int, input("위치조정>> ").split(" ")))