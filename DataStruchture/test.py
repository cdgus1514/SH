# 1) 두 개의 노드를 병함 (순서X)
# 2) 두 개의 노드를 순서대로 병합

class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link


def printList(list):
    p = list

    while p:
        if p.link != None:
            print(p.data, ">>", end=" ")
        else:# 마지막 노드면 그냥 출력
            print(p.data)

        p = p.link


def mergeSortList(p1, p2):
    # 병합 리스트를 만들 새로운 노드 헤더 생성
    head = Node(0, None)
    p = head

    # p1리스트와 p2리스트 모두 마지막 노드일 때 까지 비교 >> 작은수 부터 큰수로
    while p1 != None and p2 != None:
        if p1.data < p2.data:
            p.link = p1
            p1 = p1.link
        else:
            p.link = p2
            p2 = p2.link

        # 다음노드
        p = p.link

    # p1과 p2중 하나가 마지막 노드까지 갔을 경우
    if p1 != None:  # p1리스트의 남은 노드를 추가
        p.link = p1

    if p2 != None:  # p2리스트의 남은 노드를 추가
        p.link = p2

    return head.link


def mergeList(p1, p2):
    head = Node(0, None)
    p = head

    p.link = p1

    # 첫번째 노드의 마지막 노드까지 이동
    while p.link != None:
        p = p.link

    # 첫번째 리스트의 마지막 노드 링크에 두번째 리스트의 첫번쨰 노드 연결
    p.link = p2

    return head.link


p1 = Node(1)
p2 = Node(3)
p3 = Node(6)
p1.link = p2
p2.link = p3

q1 = Node(4)
q2 = Node(5)
q3 = Node(9)
q1.link = q2
q2.link = q3


m1 = mergeList(p1, q1)
printList(m1)


# m2 = mergeSortList(p1, q1)
# printList(m2)


