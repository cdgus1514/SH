###################################################################################################
# 파이썬에서 스택을 구현하는 방법
# 1) 리스트를 사용하여 구현 (append, pop) >> 수식표현, 다항식, 함수호출 구현 시 사용
# infix AxB+CxD
# postfix ABxCDx+ >> [A*B][C][D][*][+] >> [AxB][CxD][+]
# preefix +xABxCD >> 
# 함수호출 main>a()>b()>c()

# underflow >> 스택이 비어있는 상태에서 출려할 경우
# overflow >> top이 스택의 크기를 초과할 경우

# PUSH 과정 >>    1) overflow 확인   2) 공간확보   3) 삽입
# POP  과정 >>    1) underflow 확인  2) 출력      3) 공간제거
# PEAK     >> TOP 데이터 확인(underflow 유무)

# 연결리스트로 구현 시 >> overflow 없음

# 스택에서 TOP은 전역적으로 같은 값을 가지고있어야 하기 떄문에 >> 전역변수로 선언
###################################################################################################

class Node:
    def __init__(self, item, link):
        self.item = item
        self.next = link


def push(item):
    global top
    global size

    # 공간확보 + 삽입
    top = Node(item, top)
    size += 1


# 리턴값만 필요
def pop():
    global top
    global size

    # underflow 유무 확인
    if size != 0:
        top_item = top.item
        top = top.next  # 다음 노드를 가리켜야함

        size -= 1

        return top_item
    else:
        print("Underflow")


# top에 있는 데이터를 출력
def peak():
    if size != 0:
        return top.item
    else:
        print("Underflow")


# top.next로 top부터 끝까지
def printStack():
    print("TOP : ", end="")
    p = top

    while p:
        if p.next != None:
            print(p.item, ">>", end=" ")
        else:
            print(p.item)

        p = p.next


top = None
size = 0

print("pushs")
push("aaa")
push("bbb")
push("ccc")
push("ddd")
push("eee")
printStack()

pop()
print("\npop")
printStack()

p = peak()
print("\ntop >> ", p)
