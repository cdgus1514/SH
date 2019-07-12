from math import sqrt, pow

class Movie:

    # 생성자
    def __init__(self, title, kcount, fcount, kind):
        # instance variable
        self.title = title
        self.kcount = kcount
        self.fcount = fcount
        self.kind = kind

    # 거리계싼
    def get_distance(self, f, k):
        return sqrt(pow(self.kcount-k, 2) + pow(self.fcount -f, 2))


    # print할 때
    def __str__(self):
        return self.title +" : " + self.kind


##################### TEST ###########################
# movies = [
#     Movie("A", 10,1, "D"),
#     Movie("B", 10,6, "D"),
#     Movie("C", 10,16, "A"),
#     Movie("D", 10,20, "D"),
#     Movie("E", 3,7, "A"),
#     Movie("101번째 프로포즈", 3, 7, "D"),
#     Movie("10일간 원나잇 스탠드", 3, 7, "D"),
#     Movie("귀신의향기", 3, 7, "D"),
#     Movie("우리 지금 만나", 3, 7, "A"),
# ]

k = 3
f = 4

def fn(a, b):
    d1 = a.get_distance(k,f)
    d2 = b.get_distance(k,f)

    return d1 - d2


# 거리계산한 결과값 정렬해서 출력
#movies.sort(key=lambda m: m.get_distance(k,f))

# print(movies)
# for m in movies:
#     print(m.title)