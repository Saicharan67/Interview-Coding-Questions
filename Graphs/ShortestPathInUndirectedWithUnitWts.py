'''
Given a node src find the shorest path from src to all the other nodes
'''


from GraphRepresentation import AdjList
from collections import deque


def ShortestPath(n, m, src):
    adjlist = AdjList(n, m)
    dist = [float('inf')]*(n)   # o based indexing
    q = deque([src])
    dist[src] = 0
    while q:
        temp = q.popleft()
        for x in adjlist[temp]:
            if dist[temp]+1 < dist[x]:
                dist[x] = dist[temp]+1
                q.append(x)

    return dist
