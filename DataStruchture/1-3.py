# 수행시간 측정 코드

import random, time


random.seed(time.time())    #랜덤값이 계속 바뀜
startTime = time.time()



# 측정하고자 하는 코드 사용

a = []

for i in range(1000):
    for j in range(1000 ):
        b = []
        b.append(random.randint(1, 1000))







print("--- %s seconds --- " % (time.time() - startTime))