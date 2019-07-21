# 정렬된 두개의 리스트를 하나의 리스트로 병합
def merge(a, b, low, mid, high):
    i = low
    j = mid + 1

    # 앞/뒷 부분을 합병해서 b에 저장
    for k in range(low, high+1):
        # 앞 부분을 모두 사용한 경우
        if i > mid:
            b[k] = a[j]
            j += 1
        
        # 뒷 부분을 모두 시용한 경우
        elif j > high:
            b[k] = a[i]
            i += 1

        elif a[j] < a[i]:
            b[k] = a[j]
            j += 1

        else:
            b[k] = a[i]
            i += 1

    for k in range(low, high+1):
        a[k] = b[k]
            

def merge_sort(a, b, low, high):
    # 정렬 끝
    if low > high:
        return

    mid = low + (high+low)//2

    merge_sort(a, b, low, mid)
    merge_sort(a, b, mid+1, high)

    merge(a, b, low, mid, high)
    




a = [52, 88, 77, 26, 93, 17, 49, 10, 15, 31, 22, 44, 55, 20]  # 14개
b = [None]*len(a)

print("정렬 전")
print(a)

merge_sort(a, b, 0, len(a)-1)
print("정렬 후")
print(a)

