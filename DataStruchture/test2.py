class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link


def pList(list):
    p = list

    while p:
        if p.link != None:
            print(p.data, ">> ", end=" ")
        else:
            print(p.data)

        p = p.link


def mList(p1, p2):
    head = Node(0, None)
    p = head

    p.link = p1

    while p.link != None:
        p = p.link

    p.link = p2
    return head.link


p1 = Node(1)
p2 = Node(3)
p3 = Node(5)
p4 = Node(9)
p1.link = p2
p2.link = p3
p3.link = p4

q1 = Node(2)
q2 = Node(4)
q3 = Node(8)
q4 = Node(12)
q1.link = q2
q2.link = q3
q3.link = q4

m1 = mList(p1, q1)
pList(m1)
