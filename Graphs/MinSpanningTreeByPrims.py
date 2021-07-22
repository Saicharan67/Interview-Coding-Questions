'''
Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all 
the vertices together. A single graph can have many different spanning trees. A minimum spanning tree (MST) or 
minimum weight spanning tree for a weighted, connected, undirected graph is a spanning tree with a weight less than 
or equal to the weight of every other spanning tree. The weight of a spanning tree is the sum of weights given to each edge of the spanning tree.
How many edges does a minimum spanning tree has? 
A minimum spanning tree has (V – 1) edges where V is the number of vertices in the given graph. 
'''
from collections import defaultdict
from heapq import heappop, heappush


def MinSpanning(n, m):
    dt = defaultdict(list)
    for i in range(m):
        x, y, w = map(int, input().slpit())
        dt[x].append([y, w])
        dt[y].append([x, w])

    parent = [-1]*(n)
    key = [float('inf')]*n
    mstSet = [False]*(n)

    prq = [(0, 0)]
    key[0] = 0

    for i in range(n-1):
        u = heappop(prq)[1]

        mstSet[u] = True

        for x, w in dt[u]:
            if not mstSet[x] and w < key[x]:
                parent[x] = u
                key[x] = w
                heappush(prq, (key[x], x))
