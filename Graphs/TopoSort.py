
from GraphRepresentation import AdjList


def DFSTopo(n, m):
    adjList = AdjList(n, m)
    visited = [False]*(n)
    dfs = []

    def DFS(x):
        visited[x] = True

        for y in adjList[x]:
            if not visited[y]:
                DFS(y)
        dfs.append(x)
    for i in range(n):
        if not visited[i]:
            DFS(i)
    dfs[:] = dfs[::-1]

    return dfs


n, m = map(int, input().split())


print(DFSTopo(n, m))
