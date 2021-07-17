'''
Given an Graph (with components) detect whether it has cycle in it

'''
from GraphRepresentation import AdjList


def CheckCycle(n, m):
    adjlist = AdjList(n, m)
    visited = [False]*(n+1)

    def iscycle(i):
        q = [[i, -1]]
        visited[i] = True
        while q:
            curr, prev = q.pop(0)
            for x in adjlist[curr]:
                if not visited[x]:
                    visited[x] = True
                    q.append([x, curr])
                else:
                    if x != prev:
                        return True
        return False
    for i in range(1, n+1):
        if not visited[i]:
            if iscycle(i):
                return True
