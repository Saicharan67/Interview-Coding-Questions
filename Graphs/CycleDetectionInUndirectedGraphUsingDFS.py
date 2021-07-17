from GraphRepresentation import AdjList


def CheckCycleDFS(n, m):
    adjList = AdjList(n, m)
    visited = [False]*(n+1)
    dfs = []

    def cycleDFS(curr, prev):
        visited[curr] = True
        for x in adjList[curr]:
            if not visited[x]:
                if cycleDFS(x, curr):
                    return True
            else:
                if x != prev:
                    return True
        return False

    for i in range(1, n+1):
        if not visited[i]:
            if cycleDFS(i, -1):
                return True
    return dfs


n, m = map(int, input().split())
