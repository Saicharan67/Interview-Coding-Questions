from heapq import heappush, heappop
from collections import defaultdict


def ShortestPath(n, m, src):
    dt = defaultdict(list)
    for _ in range(m):
        x, y, w = map(int, input().split())
        dt[x].append([y, w])
        dt[y].append([x, w])

    dist = [float('inf')]*(n)  # 0 based

    dist[src] = 0
    h = [(0, src)]

    while h:
        current_distance, current_vertex = heappop(h)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > dist[current_vertex]:
            continue

        for neighbor, weight in dt[current_vertex]:
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heappush(h, (distance, neighbor))
