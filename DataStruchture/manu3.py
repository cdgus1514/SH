from binTree import Node, BinaryTree

t = BinaryTree()

# n1 = Node("A")
# n2 = Node("B")
# n3 = Node("C")
# n4 = Node("D")
# n5 = Node("E")
# n6 = Node("F")
# n7 = Node("G")
# n8 = Node("H")
#
# n1.left = n2
# n1.right = n3
# n2.left = n4
# n2.right = n5
# n3.left = n6
# n3.right = n7
# n4.left = n8
#
# # root 노드 선택
# t.root = n1

n1 = Node("A")
n2 = Node("B")
n3 = Node("C")
n4 = Node("D")
n5 = Node("E")
n6 = Node("F")
n7 = Node("G")
n8 = Node("H")
n9 = Node("I")
n10 = Node("J")
n11 = Node("K")
n12 = Node("L")

n1.left = n2

n2.left = n5
n2.right = n3

n5.right = n6
n6.right = n7

n3.left = n8
n3.right = n4

n8.left = n11
n8.right = n9

n4.left = n10
n10.left = n12

t.root = n1



print("트리 높이 : ", t.height(t.root))
print("노드 개수 : ", t.size(t.root))

q = BinaryTree()
q.root = t.copyTree(t.root)
print("트리 비교 : ", t.is_equal(t.root, q.root))

print()

print("PreOrder : ", t.preOrder(t.root))
print("InOrder : ", t.inOrder(t.root))
print("PostOrder : ", t.postOrder(t.root))
print("LevelOrder : ", t.leavelOrder(t.root))