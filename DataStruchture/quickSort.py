def qsort(a, low, hight):
    if low < hight:
        pivot = partition(a, low, hight)
        qsort(a, low, pivot+1)
        qsort(a, pivot+1, hight)


def partition(a, pivot, hight):
    i = pivot + 1
    j = hight

    while True:
        # 아직 확인 안한 데이터가 있따 >> pivot보다 큰 경우 까지 반복
        while i < hight and a[i] < a[pivot]:
            i += 1

        # 끝에서 pivot방향으로 pivot보다 작을때 까지 반복
        while j > pivot and a[j] > a[pivot]:
            j -= 1


        # 만났을 경우
        if i >= j:
            break

        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1


    a[pivot], a[j] = a[j], a[pivot]

    return i



a = [62, 88, 77, 26, 93, 17, 49, 10, 15, 31, 22, 44, 55, 20]    # 14개

qsort(a, 0, len(a)-1)

print(a)