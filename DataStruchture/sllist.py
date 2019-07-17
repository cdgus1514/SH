# 전체 연결리스트 생성하는 클래스
class SLLList:
    
    # 각각의 노드들을 생성하는 클래스
    class Node:
        def __init__(self, name, link):
            self.name = name    # 데이터공간(여러개 넣을 수 있따
            self.link = link    # 다음 노드를 가르키는 역활

    def __init__(self):
        # 헤더 초기화 == "\0"
        self.head = None
        # 노드개수
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0   # 참이면 True 리턴

    def insertFront(self, name):
        # 비어있으면
        if self.isEmpty():
            self.head = self.Node(name, None)   # 객체생성 >> 헤더에 첫번째 노드 주소 저장
        # 있으면 앞에 삽입
        else:
            self.head = self.Node(name, self.head)
            # 헤더가 첫번째 노드 주소를 가지고있음
            # 헤더가 가지고있는 주소를 링크에 저장 후 추가하는 노드의 주소를 헤더에 저장

        self.size += 1


    def insertRear(self, name, p):
        p.link = SLLList.Node(name, p.link)
        # 추가하는 노드 링크에 앞 노드 링크에 있던 주소를 저장, 추가노드 앞 노드의 링크에 추가하는 노드 주소 저장
        # A - 추가노드 - B
        self.size += 1


    # 위치 찾기
    # targ : 노드 위치를 찾기위한 인덱스 역활
    # return 여러개 있으면 안조음 >> 동일 기능은 함수로 만들어 사용하는게 좋다
    def search(self, targ):
        # 헤더부터 시작
        p = self.head
        res = None

        for i in range(self.size):
            if targ == p.name:
                # 주소 리턴
                # return i
                res = i
                break
            # 못 찾으면 다음
            p = p.link

        #return None
        return res

    def searchNode(self, targ):
        p = self.head

        while p:
            if targ == p.name:
                return p

            p = p.link

        return None


    # 헤더만 수정하면 되기 때문에 매개변수 필요 없음
    def deleteFront(self):
        if self.isEmpty():
            # 데이터가 없는 상태에서 출력하려고 할 때
            raise EmptyError("Underflow")
        else:
            # 헤더에 첫번째 노드가 가르키는 링크로 변경 >> 첫번째 노드 접근 불가(자동으로 메모리 회수됨)
            self.head = self.head.link
            self.size -= 1

    # p 다음노드를 삭제하기 위해 삭제할 노드를 알려줘야 함
    def deleteRear(self, p):
        if self.isEmpty():
            raise EmptyError("Underflow")

        t = p.link  # 삭제할 노드 링크
        p.link = t.link # 이전 노드 링크에 삭제할 노드가 가지고있던 링크를 저장 >> 삭제할 노드 접근 불가
        self.size -= 1


    # 링크가 끝날 때 까지 출력
    def printList(self):
        p = self.head

        while p:
            if p.link != None:
                print(p.name, ">>", end=" ")
            else:
                # 마지막 노드면 그냥 출력
                print(p.name)

            p = p.link


class EmptyError(Exception):
    pass