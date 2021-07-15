'''
We are given a graph which is disconnected

To Traverse BFS we will have a visited array 

'''
from GraphRepresentation import AdjList


def BFS(n, m):
    bfs = []
    visited = [False]*(n+1)
    adjlist = AdjList(n, m)
    for i in range(1, n+1):
        if not visited[i]:
            que = []
            que.append(i)
            visited[i] = True
            while que:
                temp = que.pop(0)
                bfs.append(temp)

                for x in adjlist[temp]:
                    if not visited[x]:
                        visited[x] = True
                        que.append(x)
    return bfs
