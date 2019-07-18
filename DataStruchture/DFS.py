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

adj_matrix = [[0,1,1,0,0,0],
              [0,0,0,1,0,0],
              [1,0,0,1,0,0],
              [0,1,1,0,1,1],
              [0,0,0,1,0,0],
              [0,0,0,1,0,0]]


Net = len(adj_list)
visited = [False for x in range(Net+1)]

# v : 정점
def dfs(v):
    # 방문했을 경우
    visited[v] = True
    print(v, " ", end="")

    for w in adj_list[v]:
        if not visited[w]:
            dfs(w)


print("DFS : ", end=" ")

for i in range(Net):
    if not visited[i]:
        dfs(i)

# DFS :  0  1  3  2  9  8  4  5  6  7