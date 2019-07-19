listA = [52, 88, 77, 26, 93, 17, 49, 10, 15, 31, 22, 44, 55, 20]    # 14개
n = 0

# # select sort
# for i in range(len(listA)-1):
#     for j in range(i+1, len(listA)):
#
#         if listA[i] > listA[j]:
#             listA[i], listA[j] = listA[j], listA[i]
#
#
# print(listA)


# bubble sort
for i in range(len(listA)-1):   # 회전(0-13)
    n += 1
    print()
    for j in range(len(listA)-n):    #비교
        print(j)

        if listA[j] > listA[j+1]:
            listA[j], listA[j+1] = listA[j+1], listA[j]


print(listA)