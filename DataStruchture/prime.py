import sys

# 노드개수
N = 7

# 시작은 0
s= 0

g = [None for x in range(N+1)]

g[0] = [(1,9), (2,10)]
g[1] = [(0,9), (3,10), (4,5), (6,3)]
g[2] = [(0, 10), (3,9), (4,7), (5,2)]
g[3] = [(1,10), (2,9), (5,4), (6,8)]
g[4] = [(1,5), (2,7), (6,1)]
g[5] = [(2,2), (3,4), (6,6)]
g[6] = [(1,3), (3,8), (4,1), (5,6)]


visited = [False for x in range(N+1)]

# 최대값으로 리스트 초기화
D = [sys.maxsize for x in range(N+1)]

D[s] = 0

# 이전 상태 기억
previous = [None for x in range(N+1)]
previous[s] = s



for k in range(N):
    N -= 1
    min_value = sys.maxsize

    # 방문하지 않은 정점 중 최소값을 찾기 위해성
    for  j in range(N):
        if not visited[j] and D[j] <= min_value:
            min_value = D[j]
            m = j

    # 방문한 정점
    visited[m] = True

    #
    for w, wt in g[m]:
        if not visited[w]:

            if wt < D[w]:
                D[w] = wt
                previous[w] = m



print("최소비용신장트리 Prim 알고리즘")
mst_cost = 0

for i in range(1, N):
    print("(%d %d)" % (i, previous[i]), end=" ")
    mst_cost += D[i]

print("\n최소비용신장트리 가중치 : ", mst_cost)
