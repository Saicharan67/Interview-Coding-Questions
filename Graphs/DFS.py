
from GraphRepresentation import AdjList


def DFSTraversal(n, m):
    adjList = AdjList(n, m)
    visited = [False]*(n+1)
    dfs = []

    def DFS(x):
        visited[x] = True
        dfs.append(x)
        for y in adjList[x]:
            if not visited[y]:
                DFS(y)
    for i in range(1, n+1):
        if not visited[i]:
            DFS(i)
    return dfs


n, m = map(int, input().split())


print(DFSTraversal(n, m))
