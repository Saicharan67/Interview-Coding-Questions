

from collections import defaultdict


def ShortestPathDAG(n, m, src):

    dt = defaultdict(list)
    for i in range(m):
        x, y, w = map(int, input().split())
        dt[x].append([w, y])
    visited = [False]*(n+1)
    dfs = []

    def DFS(x):
        visited[x] = True

        for y, w in dt[x]:
            if not visited[y]:
                DFS(y)
        dfs.append(x)
    for i in range(1, n+1):
        if not visited[i]:
            DFS(i)
    dist = [float('inf')]*(n+1)
    dist[src] = 0

    while dfs:
        temp = dfs.pop()
        if dist[temp] != float('inf'):
            for y, w in dt[temp]:
                if dist[temp]+w < dist[y]:
                    dist[y] = dist[temp]+w
