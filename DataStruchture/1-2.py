# lambda >> 일회용 함수

# a = [2,5,4,6,8,11,3,12]
#
# even = list(filter(lambda x: (x % 2 == 0), a))
# print(even)
#
#
# tenTimes = list(map(lambda x: (x * 10), a))
# print(tenTimes)



b = [ [0,1,8], [7,5,2], [15,2,1], [10,3,7] ]

# 첫번째 리스트 값으로 정렬
b.sort()
print(b)

# 3번째 리스트 값으로 정렬
b.sort(key=lambda x: x[2])
print(b)