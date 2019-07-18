class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class Bst:
    def __init__(self):
        self.root = None



    def get(self, k):
        # tree와 key 같이 전달
        return self.get_item(self.root, k)

    # n = 트리의 root, k = 찾을 값
    def get_item(self, n, k):

        # bst가 없는 상태
        if n == None:
            return None


        # Root > 찾을 key값 --> 왼쪽 서브트리로
        if n.key > k:
            return self.get_item(n.left, k)

        elif n.key < k:
            return self.get_item(n.right, k)

        else:
            return n.value

    
    # 노드추가
    def put(self, key, value):
        self.root =  self.put_item(self.root, key, value)

    def put_item(self, n, k, v):
        # print("root : ", n)
        if n == None:
            # print("노드생성 : ", k, v)
            return Node(k, v)

        # Root > 찾을 key값 --> 왼쪽 서브트리로, 결과의 주소를 왼쪽 링크에 저장
        if n.key > k:
            # print("left1 : ", n.left)
            n.left = self.put_item(n.left, k, v)
            # print("left2 : ", n.left, n.key, n.value)

        elif n.key < k:
            # print("right1 : ", n.right)
            n.right = self.put_item(n.right, k, v)
            # print("right2 : ", n.right, n.key, n.value)

        # 해당 노드에 값을 갱신
        else:
            n.value = v

        # root의 좌, 우 노드가 없는 경우 해당 노드주소 리턴
        # print("None >> ", n.key, n.value)
        return n


    # 최소값 삭제
    def delete_min(self):

        if self.root == None:
            print("Empty")

        self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left == None:
            return n.right

        n.left = self.del_min(n.left)

        return n


    # 최대값 삭제
    def delete_max(selfe):
        if selfe.root == None:
            print("Empty")

        selfe.root = selfe.del_max(selfe.root)

    def del_max(self, n):
        if n.right == None:
            return n.left

        n.right = self.del_max(n.right)

        return n

    
    # 최소값 찾기
    def min(self):
        if self.root == None:
            return None

        return self.minimum(self.root)

    def minimum(self, n):
        # 왼쪽 마지막 노드인 경우 >> 최소값
        if n.left == None:
            return n

        return self.minimum(n.left)


    # 최댓값 찾기
    def max(self):
        if self.root == None:
            return None

        return self.maximum(self.root)

    def maximum(self, n):
        if n.right == None:
            return n

        return self.maximum(n.right)


    def inOrder(self, n):
        if n != None:
            if n.left:
                self.inOrder(n.left)

            print(str(n.key), n.value, end=", ")

            if n.right:
                self.inOrder(n.right)
                
                
    # 노드삭제
    def delete(self, k):
        self.root = self.del_node(self.root, k)
        
    def del_node(self, n, k):
        if n == None:
            return None
        
        # 현재노드의 키 값이 삭제할 값보다 크면
        elif n.key > k:
            n.left = self.del_node(n.left, k)

        elif n.key < k:
            n.right = self.del_node(n.right, k)

        else:
            # 자식노드가 없거나 하나인 경우
            if n.right == None:

                return n.left
            
            # 자식노드가 없는 경우
            if n.left == None:
                return n.right

            # 자식노드가 2개인 경우 >> 부모노드 역활을 할 노드 결정
            t = n
            # 오른쪽 노드의 가장 최소값
            n = self.minimum(t.right)
            n.right = self.del_min(t.right)
            n.left = t.left

        return n