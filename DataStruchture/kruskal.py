# 최초의 가중치 입력을 어떻게 할것인가
weight = [(0, 1, 9), (0, 2, 10), (1, 3, 10), (1, 4, 5), (1, 6, 3), (2, 3, 9), (2, 4, 7), (2, 5, 2), (3, 5, 4),
          (3, 6, 8),
          (4, 6, 1), (5, 6, 6)]

# 가중치를 기준으로 오름차순 정렬
weight.sort(key=lambda t: t[2])

print(weight)
print()

# 최소비용신장트리 리스트
mst = []

# 정점의 개수
N = 7

# 임의 리스트
p = []

# 각 정점리스트 생성
for i in range(N):
    p.append(i)


def find(u):
    # u가 정점과 같지 않으면
    if u != p[u]:
        # 경로압축
        p[u] = find(p[u])

    return p[u]


# 각각의 트리를 하나로 합칠때 사용
def union(u, v):
    root1 = find(u)
    print("DEBUG root1 : ", root1)
    root2 = find(v)
    print("DEBUG root2 : ", root2)

    p[root2] = root1


tree_edge = 0
mst_cost = 0  # 최소비용

while True:
    #
    if tree_edge == N - 1:
        break

    # (시작정점, 끝정점, 가중치)를 변숭 할당
    u, v, wt = weight.pop(0)

    # 싸이클 발생을 방지하기 위해 같지 않은 경우에만
    if find(u) != find(v):
        union(u, v)
        mst.append((u, v))
        mst_cost += wt  # 최종 비용 확인할 변수
        tree_edge += 1

print("DEBUG p : ", p)
print(

)
print("최소비용신장트리 kruskal 알고리즘")
print(mst)
print("최소비용 : ", mst_cost)