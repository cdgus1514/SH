# 마지막 노드 확인 >> 1) 링크 == head    2) 중간에서 시작 시 중간 노드의 링크 p, p == node.link

# 전체 연결리스트 생성하는 클래스
class CLLList:
    # 각각의 노드들을 생성하는 클래스
    class Node:
        def __init__(self, name, link):
            self.name = name  # 데이터공간(여러개 넣을 수 있따
            self.link = link  # 다음 노드를 가르키는 역활

    def __init__(self):
        # 헤더 초기화 == "\0"
        self.head = None
        # 노드개수
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0  # 참이면 True 리턴


    def insertFront(self, name):
        # 비어있으면
        if self.isEmpty():
            # self.head = self.Node(name, None)  # 객체생성 >> 헤더에 첫번째 노드 주소 저장
            # 환영연결리스트 첫 노드 입력 == 마지막 노드 >> 추가되는 노드의 링크에 헤더 주소 저장
            p = self.Node(name, None)
            self.head = p
            p.link = p
            # print(self.head, " ", p.link)

        # 있으면 앞에 삽입
        else:
            p = self.Node(name, None)
            p.link = self.head  # 생성 노드에 헤더가 가지고있는(원래 첫번쨰 노드 주소) 주소값 저장
            # self.head = p  # 헤더에 추가한 노드 주소값 저장

            # 마지막 노드 확인
            last = self.searchEnd()
            last.link = p
            self.head = p   # 헤더에 추가한 노드 주소값 저장

        self.size += 1

    def insertRear(self, name, p):
        new = CLLList.Node(name, p.link)
        p.link = new

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

        # return None
        return res

    def searchNode(self, targ):
        p = self.head
        pre = p

        while p:
            if targ == p.name:
                return pre, p

            pre = p
            p = p.link

        return None

    # 환형연결리스트 인 경우 사용
    def searchEnd(self):
        p = self.head

        while True:
            # 첫 노드의 링크값부터 시작, 링크값과 헤더의 주소값이 같으면 >> 마지막 노드 
            if p.link == self.head:
                return p   # p[0], p[1]

            p  = p.link


    #현재 노드를 삭제 처리
    def delete(self, data):
        if self.isEmpty():
            # 데이터가 없는 상태에서 출력하려고 할 때
            raise EmptyError("Underflow")

        if self.head.name == data:  # 첫 노드 삭제 시
            # 마지막 노드의 링크 찾아서 수정
            last = self.searchEnd()
            last.link = self.head.link

            #삭제할 노드의 링크를 헤더에 저장
            self.head = self.head.link
            self.size -= 1

        elif self.head == self.head.link and self.head.name == data:   # 노드가 한개 + 삭제할 노드인 경우
            self.head == None
            self.size -= 1

        else:   # 첫번째 노드가 아닌 경우
            # 삭제 할 이전노드 찾기
            t = self.searchNode(data)       # 삭제할 이전노드의 링크
            t[0].link = t[0].link.link      # 삭제할 노드가 가지고있던 링크 >> t[0].link = t[1].link

        self.size -= 1


    # 링크가 끝날 때 까지 출력
    def printList(self):
        p = self.head

        if self.head == None:
            print("없다")
            return

        while True:
            if p.link != self.head:
                print(p.name, ">>", end=" ")
            else:
                # 마지막 노드면 그냥 출력
                print(p.name)
                break

            p = p.link


class EmptyError(Exception):
    pass