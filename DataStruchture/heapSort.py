# 매개변수 > 리스트 타입
def downheap(i, size):
    while 2 * i <= size:
        # k는 왼쪽자식
        k = 2 * i

        if k < size and a[k] > a[k + 1]:
            k += 1

        if a[i] < a[k]:
            break

        a[i], a[k] = a[k], a[i]

        i = k


def create_heap(a):
    hsize = len(a) - 1
    for i in reversed(range(1, hsize//2+1)):
        # 리스트의 중간값을 root로 선택해서 트리생성
        downheap(i, hsize)


# 정렬
def heapSort(a):
    N = len(a) -1

    for i in range(N):
        a[1], a[N] = a[N], a[1]
        downheap(1, N-1)

        N -= 1


a = [None, 88, 77, 26, 93, 17, 49, 10, 15, 31, 22, 44, 55, 20]    # 14개

print("Heap Sort : ")
create_heap(a)
print(a)
print()
heapSort(a)
print(a)