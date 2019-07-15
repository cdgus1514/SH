class Node:

    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right

def map():
    n1 = Node("H")
    n2 = Node("F")
    n3 = Node("S")
    n4 = Node("U")
    n5 = Node("E")
    n6 = Node("Z")
    n7 = Node("K")
    n8 = Node("N")
    n9 = Node("A")
    n10 = Node("Y")
    n11 = Node("T")

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n5.left = n9
    n7.right =n10
    n9.right = n11

    return n1

def PreOrder(n):
    if n != None:
        print(n.name, ">>", end=" ")
        PreOrder(n.left)
        PreOrder(n.right)


def InOrder(n):
    if n != None:
        InOrder(n.left)
        print(n.name, ">>", end=" ")
        InOrder(n.right)

def PostOrder(n):
    if n != None:
        PostOrder(n.left)
        PostOrder(n.right)
        print(n.name, ">>", end=" ")


start = map()
print("PreOrder for tour\n", end=" ")
PreOrder(start)

print("\n\nInOrder for tour\n", end=" ")
InOrder(start)

print("\n\nPostOrder for tour\n", end=" ")
PostOrder(start)