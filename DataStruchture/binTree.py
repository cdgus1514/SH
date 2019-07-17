###################################################################################################
# 이진트리의 단점 >> 널 링크 : N+1개 발생    >> 스레디드 이진트리(이진트리의 널링크 낭비를 최소화)
# 
# 이진 힙(정렬)
# 1) max heap : 부모노드 > 자식노드 (큰 값이 우에 >> 역순정렬)
# 2) min heap : 부모노드 < 자식노드 (큰 값이 아래 >> 오름차순 정렬)
#
# 3) down heap >> 위에서 아래로 내려가면서 max or min정렬 수행
# 4) up heap >> 아래에서 우로 올라가면서 max or min정렬 수행
#
# 이진 검색
#
###################################################################################################
class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


# 트리는 항상 root가 있어야 함
class BinaryTree:
    def __init__(self):
        self.root = None

    # n = Root
    # Root-left-Right
    def preOrder(self, n):

        if n != None:   # 트리가 비어있지 않은 경우
            print(str(n.item), " ", end="")

            if n.left:  # 있으먄 True
                # 왼쪽 노드가 있으면 (왼쪽노드로 재귀호출)
                self.preOrder(n.left)

            if n.right:
                self.preOrder(n.right)


    # left - Root - Right
    def inOrder(self, n):

        if n != None:   # 트리가 비어있지 않은 경우

            if n.left:  # 있으먄 True
                # 왼쪽 노드가 있으면 (왼쪽노드로 재귀호출)
                self.inOrder(n.left)

            print(str(n.item), " ", end="")

            if n.right:
                self.inOrder(n.right)


    # left - Right - Root
    def postOrder(self, n):

        if n != None:   # 트리가 비어있지 않은 경우

            if n.left:  # 있으먄 True
                # 왼쪽 노드가 있으면 (왼쪽노드로 재귀호출)
                self.postOrder(n.left)

            if n.right:
                self.postOrder(n.right)

            print(str(n.item), " ", end="")


    def leavelOrder(self, root):
        q = []
        q.append(root)

        while len(q) != 0:  # 큐가 비어있찌 않으면 반복문 실행
            # 첫번째 노드(데이터, 링크 모두 가지고있음)
            t = q.pop(0)
            print(str(t.item), " ", end="")

            if t.left != None:
                q.append(t.left)

            if t.right != None:
                q.append(t.right)


    # 왼쪽/오른쪽  끝까지 내려가고 리턴하면서 증감, 최대값이 높이
    def height(self, root):

        # 자식노드 없는 경우
        if root == None:
            return 0
        else:
            # 왼쪽 or 오른쪽 자식 중 큰 값에 +1 해서 부모 노드에 리턴
            return max(self.height(root.left), self.height(root.right))+1
        
    
    # 노드의 개수
    # 자기자신 + 1 해서 부모노드에 리턴
    def size(self, root):
        if root == None:
            return 0
        else:
            return 1 + self.size(root.left) + self.size(root.right)


    def copyTree(self, n):
        if n == None:
            return None

        else:
            # 재귀호출 >> 계속 내려가면서 생성한 노드 리턴
            left = self.copyTree(n.left)
            right = self.copyTree(n.right)
            
            # 
            return Node(n.item, left, right)


    def is_equal(self, n, m):
        if n == None or m == None:
            return n == m

        if n.item != m.item:
            return False

        # 트리가 비어있지 않고 데이터도 같다

        # 모두 True인 경우에만 같은 트리
        return (self.is_equal(n.left, m.left)) and (self.is_equal(n.right, m.right))