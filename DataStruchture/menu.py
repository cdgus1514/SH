#from sllist import SLLList
from cllist import CLLList

def menu():
    while True:
        print("1. insertFront")
        print("2. insertRear")
        print("3. delete")
        print("4. search")
        print("5. printlist")
        print("6. end")
        select = int(input(">> "))

        if select == 1:
            name = input("이름 입력 >> ")
            s.insertFront(name)
            print()

        elif select == 2:
            name = input("이름 입력 >> ")
            name2 = input("추가할 이전 노드 입력 >> ")
            p = s.searchNode(name2)
            # print(p.link)
            s.insertRear(name, p[0].link)
            print()

        elif select == 3:
            name = input("삭제할 노드 입력 >> ")
            p = s.searchNode(name)
            # print("삭제한 노드 : ", p[1].link.name)
            s.delete(name)
            print()

        elif select == 4:
            name = input("찾을 이름 입력 >>")
            p = s.searchNode(name)

            if p == None:
                print("찾는 이름이 없다")
            else:
                print(name, "은 %d번째 노드 입니다." % (s.search(name)+1))
                # print("다음 노드 :", p.link.name)
                print("다음 노드 :", p[1].link.name)
                print()

        elif select == 5:
            s.printList()
            print()

        elif select == 6:
            exit = input("계속 하시겠습니까? (y/n) >> ")
            if exit == "y" or exit == "Y":
                continue
            elif exit == "n" or exit == "N":
                break

        else:
            print("잘못 입력하였습니다.")
            pass


if __name__ == "__main__":

    s = CLLList()
    menu()