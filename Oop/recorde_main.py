from Oop.recorde_service import StoreService
from Oop.record import Store
from Oop.recorde_ui import StoreUI

if __name__ == "__main__":
    print("프로그램 시작")

    list = [
        Store('치향저격', 37.502969, 127.026354),
        Store('노랑통닭', 37.500398, 127.024768),
        Store('광장족발', 37.544363, 127.054892),
        Store('향치저격', 37.506969, 127.021354),
    ]

    service = StoreService(list)
    ui = StoreUI(service)

    ui.find_store()