###################################################################################################
# 양쪽으로 입/출 가능
#
###################################################################################################

from collections import deque

dq = deque("data")

for node in dq:
    print(node.upper(), end=" ")

print()

print("### push ###")
# 오른쪽 삽입
dq.append("r")
# 왼쪽 삽입
dq.appendleft("f")

print(dq)

print("\n## pop ###")
dq.pop()
print(dq)
dq.popleft()
print(dq)


print()

print(dq[-1])
print(dq[0])

# dq에 데이터가 있는지 확인 >> T. F
print("t" in dq)

dq.extend(" structure")
print(dq)

dq.extendleft(reversed("pyhon "))
print(dq)