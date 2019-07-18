# 리스트로 구현
# i = root
# i의 자식노드 >> [left]ix2, [right](ix2)+1
# i의 부모노드 >> i//2

class Bheap:
    # a : 리스트
    def __init__(self, a):
        # a[0]는 사용 안함
        self.a = a
        # 리스트에 0번부터 있으면 0*x = 0 이기 때문에
        self.N = len(a) -1


    def create_heap(self):

        for i in range((self.N//2), 0, -1):
            # 리스트의 중간값을 root로 선택해서 트리생성
            self.downheap(i)

    
    def insert(self, key):
        # 리스트에 추가, 개수증감
        self.N += 1
        self.a.append(key)
        self.upheap(self.N)


    # 루트에 최소값 삭제 >> 오름차순 정렬
    def delete_min(self):
        # 리스트가 비어있는 경우
        if self.N == 0:
            print("Empty")
            return None

        # 최소값
        min = self.a[1]

        # 첫 노드와 마지막 노드 자리 변경 후 뒤에서부터 삭제
        self.a[1], self.a[-1] = self.a[-1], self.a[1]
        del self.a[-1]

        self.N -= 1
        
        # 힙 재수행
        self.downheap(1)


        return min


    def downheap(self, i):
        
        # 왼쪽자식노드가 있는 경우 반복
        while 2 * i <= self.N:
            # k는 왼쪽자식
            k = 2 * i

            # 이차리스트 [리스트개수[키값]]
            # [[], [10, "apple"], ...] key=10
            if k < self.N and self.a[k][0] > self.a[k+1][0]:
                # 오른쪽 자식으로 만들기
                k += 1

            # 부모 < 자식
            if self.a[i][0] < self.a[k][0]:
                break


            self.a[i], self.a[k] = self.a[k], self.a[i]


            # 부모 > 자식 -> 자식이 부모로 올라감
            i = k


    def upheap(self, j):

        # j > 1 : j는 루트가 아님
        # j가 부모보다 클때까지 반복
        while j > 1 and self.a[j//2][0] > self.a[j][0]:
            self.a[j], self.a[j//2] = self.a[j//2], self.a[j]
            
            # 부모 > 자식 -> 자식이 부모로 올라감
            j = j//2


    def print_heap(self):

        for i in range(1, (self.N+1)):
            print("[%2d %s]" % (self.a[i][0], self.a[i][1]), end=" ")

        print("\nheap size : ", self.N)