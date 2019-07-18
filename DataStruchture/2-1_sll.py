from sllist import SLLList


if __name__ == '__main__':

    s = SLLList()
    s.insertFront("둘리")
    s.insertFront("도우너")
    s.insertRear("철수", s.head.link) # 헤드 링크 >> 2번째 노드 주소
    s.insertFront("마이콜")

    s.printList()
    # 헤더에 둘리
    # InsertFront : 도우너 >> 둘리
    # InsertRear : 도우너 >> 둘리 >> 철수
    # InsertFront : 마이콜 >> 도우너 >> 둘리 >> 철수


    name = input("endter a name : ")

    print(name, "는 %d번째 노드" % (s.search(name)))
    print(name, "는 " , s.search(name))


    print("\n첫 노드 삭제")
    s.deleteFront()
    s.printList()
    # 첫노드 삭제 >> 마이콜 삭제 : 도우너 >> 둘리 >> 철수

    print("\n다음 노드를 삭제한 리스트 : ")
    s.deleteRear(s.head.link)
    s.printList()
    # 마지막 노드 삭제 >> 철수 삭제 : 도우너 >> 둘리

    print()

    print(name, "앞에 삽입한 후 리스트 : ")
    s.insertFront(name)
    s.printList()

    print()

    name = input("삭제할 이전 노드 입력 >> ")
    p = s.searchNode(name)
    print("삭제할 노드 : ", p.link.name)
    s.deleteRear(p)
    print("노드 삭제 후 : ")
    s.printList()