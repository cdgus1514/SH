from dllist import DLList

def menu():
    while True:
        print("1. insertBefore")
        print("2. insertAfter")
        print("3. delete")
        # print("4. search")
        print("4. printlist")
        print("0. end")
        select = int(input(">> "))

        if select == 1:
            name = input("이름 입력 >> ")
            age = input("나이 입력 >>")
            pos = input("삽입할 위치(앞) >> ")
            p = s.searchNode(pos)
            s.insertBefor(name, age, p)
            print("-------------------------------------------")

        elif select == 2:
            name = input("이름 입력 >> ")
            age = input("나이 입력 >>")
            pos = input("삽입할 위치(뒤) >> ")
            p = s.searchNode(pos)
            s.insertAfter(name, age, p)
            print("-------------------------------------------")

        elif select == 3:
            pos = input("삭제할 이름 입력 >> ")
            p = s.searchNode(pos)
            print(p)
            # print("삭제한 노드 : ", p[1].link.name)
            s.delete(p)
            print("-------------------------------------------")

        # elif select == 4:
        #     name = input("찾을 이름 입력 >>")
        #     p = s.searchNode(name)
        #
        #     if p == None:
        #         print("찾는 이름이 없다")
        #     else:
        #         print(name, "은 %d번째 노드 입니다." % (s.search(name)+1))
        #         # print("다음 노드 :", p.link.name)
        #         print("다음 노드 :", p[1].link.name)
        #         print()

        elif select == 4:
            s.printList()
            print("-------------------------------------------")

        elif select == 0:
            print("###################END#####################")
            break


if __name__ == "__main__":

    s = DLList()
    s.insertBefor('aaa', 10)
    menu()