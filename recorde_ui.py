# recorde_service와 의존적 관계

class StoreUI:

    def __init__(self, service):
        self.service = service

    def find_store(self):
        lat = float(input("현재 위도 >> "))
        lng = float(input("현재 경도 >> "))

        myposition = {"lat": lat, "lng": lng}
        store = self.service.find_nearest(myposition)

        print(store.title)
        print(store.lat, store.lng)

        if(input("continue >> ") == "y"):
            #재귀
            self.find_store()
        else:
            return