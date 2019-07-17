# 이중연결리스트 >> 링크가 두개

class DLList:

    class Node:
        def __init__(self, name, age, pre, next):
            self.name = name
            self.age = age
            self.prev = pre
            self.next = next

    def __init__(self):
        self.head = self.Node(None, None, None, None)
        self.tail = self.Node(None, None, self.head, None)
        self.head.next = self.tail
        # self.head = None
        # self.tail = None
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.size == 0   # True 리턴


    # 앞에 삽입
    def insertBefor(self, name, age, p=None):
        # 처음 데이터를 넣을 경우
        if p == None:
            new = self.Node(name, age, self.head, self.tail)
            # new = self.Node(name, age, None, None)
            self.head.next = new
            self.tail.prev = new
            self.size += 1

            return

        t = p.prev  # 다음노드 prev
        new = self.Node(name, age, t, p)    # 추가노드 prev(다음노드의 prev >> 이전노드) next(p >> 다음노드)
        p.prev = new    # 새 노드의 다음노드 prev에 추가노드 주소 저장
        if t != None:
            t.next = new

        self.size += 1

    # 뒤에 삽입
    def insertAfter(self, name, age, p):
        t = p.next  # 새 노드의 이전노드 next
        new = self.Node(name, age, p, t)    #추가노드 prev(이전노드), next(이전노드 next >> 다음노드)
        p.next = new    # 이전노드
        t.prev = new    # 다음노드

        self.size += 1



    def delete(self, node):
        f = node.prev   # 삭제할 노드의 이전노드
        r = node.next   # 삭제할 노드의 다음노드

        f.next = r  # 이전노드의 next에 다음노드 저장
        r.prev = f  # 다음노드의 prev에 이전노드 저장

        self.size -= 1

        return node.name


    def searchNode(self, targ):
        p = self.head

        while p:
            if targ == p.name:
                return p

            # 뒤로 갈 경우
            p = p.next

        return None


    # 링크가 끝날 때 까지 출력
    def printList(self):
        if self.isEmpty():
            print("리스트 없음")
        else:
            # 헤더의 다음노드부터 시작 >> (현재 헤더는 none)
            p = self.head.next

            while p != self.tail:   # 헤더 다음노드부터 테일을 만날 떄 까지 반복
                if p.next != self.tail:
                    print('[' + p.name + ', ' + str(p.age) + ']', ' <=> ', end="")
                else:
                    print('[' + p.name + ', ' + str(p.age) + ']')

                p = p.next


class EmptyError(Exception):
    pass