###################################################################################################
# 공간생성방법 >> 1) 링크리스트    2) 환형큐(rear를 계쏙 변경)  3) 무빙큐
#
# front(head) >> 출력
# rear (tail) >> 삽입
#
###################################################################################################
class Node:
    def __init__(self, item, n):
        self.item = item
        self.next = n


def add(item):
    global front    # 첫번째 노드
    global rear     # 마지막 노드
    global size

    new = Node(item, None)

    if size == 0:
        # 노드가 없을 경우 front와 rear 같은 노드를 가르킴
        front = new
    else:
        # 노드가 있는 경우 >> rear.next에 연결
        rear.next = new

    rear = new

    size += 1


def remove():
    global front
    global rear
    global size

    if size != 0:
        # 삭제할 데이터
        res = front.item
        
        # front는 첫번째 노드 삭제 후 다음노드로 변경
        front = front.next

        size -= 1

        # 큐에 노드가 없는 경우
        if size == 0:
            rear = None

    return res


def printQueue():
    p = front
    print("Print Queue : ", end="")

    while p:
        if p.next != None:
            print(p.item, "<<", end=" ")
        else:
            print(p.item)

        p = p.next


front = None
rear = None
size = 0


print("### add ###")
add("a")
add("b")
add("c")
add("d")
add("e")

printQueue()
print("Front : ", front.item)
print("Rear : ", rear.item)

print("\n### remove ###")
remove()
remove()

printQueue()
print("Front : ", front.item)
print("Rear : ", rear.item)