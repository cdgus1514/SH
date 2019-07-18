# 해당 노드와 연결된 인접노드를 모두 검색 후 다음노드로 이동 후 검색 반복
# 방문했던 인접 노드는 재방문 안함

adj_list = [[1,2],
            [3],
            [3],
            [1,2,9,8],
            [5],
            [4,6,7],
            [7],
            [5,6],
            [3],
            [3]]


Net = len(adj_list)
visited = [False for x in range(Net+1)]

# v : 정점
def bfs(i):
    queue = []
    visited[i] = True
    queue.append(i)

    # 큐가 비어있지 않는 경우
    while len(queue) != 0:
        v = queue.pop(0)
        print(v, " ", end="")

        for w in adj_list[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)


for i in range(Net):
    if not visited[i]:
        bfs(i)

# BFS : 0  1  2  3  9  8  4  5  6  7