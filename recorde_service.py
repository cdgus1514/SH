# 비지니스 로직(print, input 안됨)

from math import sqrt, pow

class StoreService:

    def __init__(self, store_list):
        self.list = store_list


    def find_nearest(self, position):
        # 어떤 로직을 생성하기 전 준비하는 일 = 생성자

        def calcDistance(lat1, lng1, lat2, lng2):

            return sqrt(pow(lat1 - lat2, 2) + pow(lng1 - lng2, 2))


        #lat = position.lat
        #lng = position.lng
        lat = position["lat"]
        lng = position["lng"]
        result = None
        near = 100

        for store in self.list:
            slat = store.lat
            slng = store.lng
            #print(slat, slng, lat, lng)
            distance = calcDistance(slat, slng, lat, lng)

            if distance < near:
                near = distance
                result = store

        return result