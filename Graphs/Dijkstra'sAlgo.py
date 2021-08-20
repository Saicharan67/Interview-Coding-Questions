'''
  Given a graph and a source vertex in the graph, find shortest paths from source to all vertices in the given graph.

  '''


from heapq import heappush, heappop
from collections import defaultdict


def ShortestPath(n, m, src):
    dt = defaultdict(list)
    for _ in range(m):
        x, y, w = map(int, input().split())
        dt[x].append([y, w])
        dt[y].append([x, w])

    dist = [float('inf')]*(n+1)  # 1 indexed

    dist[src] = 0
    h = [(0, src)]

    while h:
        d, u = heappop(h)

        for v, w in dt[u]:
            if dist[v] > dist[u]+w:
                dist[v] = dist[u]+w
                heappush(h, (dist[v], v))
    return dist


Distances = ShortestPath(8, 13, 1)

for i, n in enumerate(Distances[1:]):
    print(f"Shortest Distance form A - {chr(ord('@')+i+1)} is :", n)
