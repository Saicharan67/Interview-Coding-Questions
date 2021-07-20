
from collections import defaultdict, deque


def ShortestPath(n, m, src):
    dt = defaultdict(list)
    for i in range(m):
        x, y, w = map(int, input().split())
        dt[x].append([y, w])
        dt[y].append([x, w])
    dist = [float('inf')]*(n+1)
    q = deque([src])
    dist[src] = 0
    while q:
        temp = q.popleft()
        for x, w in dt[temp]:
            if dist[temp]+w < dist[x]:
                dist[x] = dist[temp]+w
                q.append(x)
            #print(dist[x], x)

    return dist
