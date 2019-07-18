from binHeap import Bheap
import copy

def menu():
    print("==================================")
    print("1. insert")
    print("2. delete_min")
    print("3. print_heap")
    print("4. sort")
    print("0. END")
    print("==================================")

    select = input(">> ")

    return select

def create_list():
    a = [None] * 1

    a.append([90, "수박"])
    a.append([80, "멜론"])
    a.append([70, "복숭아"])
    a.append([60, "망고"])
    a.append([20, "체리"])
    a.append([30, "포도"])
    a.append([35, "오렌지"])
    a.append([10, "바나나"])
    a.append([15, "뀰"])
    a.append([45, "레몬"])
    a.append([40, "딸기"])

    return a


if __name__ == "__main__":

    # 사용할 리스트 생성
    a = [None] * 1

    a.append([90, "수박"])
    a.append([80, "멜론"])
    a.append([70, "복숭아"])
    a.append([60, "망고"])
    a.append([20, "체리"])
    a.append([30, "포도"])
    a.append([35, "오렌지"])
    a.append([10, "바나나"])
    a.append([15, "뀰"])
    a.append([45, "레몬"])
    a.append([40, "딸기"])

    # print(a)
# [None, [90, '수박'], [80, '멜론'], [70, '복숭아'], [60, '망고'], [20, '체리'], [30, '포도'], [35, '오렌지'], [10, '바나나'], [15, '뀰'], [45, '레몬'], [40, '딸기']]

    bh = Bheap(a)
    bh.create_heap()


    while True:
        s = menu()
        print()

        if s == "1":
            print("데이터 입력 ([int, str])")
            key = int(input("key >> "))
            data = input("data >>")

            bh.insert([key, data])

        elif s == "2":
            d = bh.delete_min()
            print("삭제된 데이터 : ", d)

        elif s == "3":
            bh.print_heap()
            print()

        elif s == "4":
            slist = []  # 오름차순 정렬을 저장할 리스트

            bhcopy = [] # 원본 유지를 위한 복사본 리스트
            bhcopy = copy.deepcopy(bh)

            min = bhcopy.delete_min()

            while min != None:
                slist.append(min)
                min = bhcopy.delete_min()
            
            print("오름차순 정렬 : ", slist)


        elif s == "0":
            break

        else:
            print("다시입력")
            continue