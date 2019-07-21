# __ 변경하지 말아라


class Store:
    # 1. 명사
    # 2. __str__ (디버그)

    def __init__(self, subject, lat, lng): # self : 새로 생성한 메모리공간(s1, s2변수에 데이터를 담을 공간)
        self.title = subject              # default 변수 (score 값 없으면 0 입력)
        self.lat = lat
        self.lng = lng

    def __str__(self):
        return self.title + " : "+str(self.lat) + ":" + str(self.lng)



# s1 = Record('KOR', 70)
# s2 = Record('ENG', 80)
# s3 = Record('MAT', 60)
# s4 = Record('SCI', 50)
#
# slist = (s1,s2,s3,s4)