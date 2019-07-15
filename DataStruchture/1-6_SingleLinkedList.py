

class SLLList:

    class Node:

        def __init__(self, name, link):
            self.name = name
            self.link = link


    def __init__(self):
        # 헤더
        self.head = None
        # 노드개수
        self.size = 0


    def size(self):
        return self.size


    def isEmpty(self):
        return self.size == 0


    def InsertFront(self, name):
        # 비어있으면
        if self.isEmpty():
            self.head = self.Node(name, None)
        # 있으면 앞에 삽입
        else:
            self.head = self.Node(name, self.head)

        self.size += 1


    def InsertRear(self, name, p):
        p.next = SLLList.Node(name, p.next)
        self.size +=1


    #위치 찾기
    def Search(self, targ):
        # 헤더부터 시작
        p = self.head

        for i in range(self.size):
            if targ == p.name:
                # 주소 리턴
                return i

            # 못 찾으면 다음
            p = p.next

        return None