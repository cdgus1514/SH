# 재귀 >> 펙토리얼 ,피보나치수열, 진법변환


# 2^x
def fac(n):
    # 종료조건 (없으면 recursion error)
    if n <= 1:
        return 1

    return  n * fac(n-1)

print(fac(10))


# x
def fac2(n):
    res = 1

    for i in range(1, n+1):
        res *= i

    return res


print(fac2(10))



def fibo(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibo(n-1) + fibo(n-2)


s = 0

for i in range(10):
    s += fibo(i)
    print(s, end=" ")


print("\n----------------------------------------------")

# list = []
#
# def c(n):
#     if n == 0:
#         return 1
#     list.append(n%2)
#
#     return c(n//2)
#
# c(11)
#
# for i in range(len(list)-1, -1, -1):
#     print(list[i], end=" ")


def d2b(n):
    if n==0:
        return

    #print(n % 2, end=" ")  #순서대로
    d2b(n//2)
    print(n%2, end=" ") #역순


d2b(10)