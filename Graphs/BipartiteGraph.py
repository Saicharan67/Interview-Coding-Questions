'''
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.
'''
from GraphRepresentation import AdjList


def isBipartite(n, m):
    adjList = AdjList(n, m)
    colored = [-1]*(n+1)

    def bfscheck(i):
        q = [i]
        colored[i] = 1
        while q:
            temp = q.pop(0)
            for x in adjList[temp]:
                if colored[x] == -1:
                    q.append(x)
                    colored[x] = 1-colored[temp]
                else:
                    if colored[x] == colored[temp]:
                        return False
        return True

    for i in range(1, n+1):
        if colored[i] == -1:
            if bfscheck(i):
                return True
    return False
