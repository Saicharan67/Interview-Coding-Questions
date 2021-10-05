'''
Given a list of colors and a list of vertices and edges, assign labels of colors
to elements of a graph subject to certain constraints such as no two adjacent vertices 
share the same color.
'''
from typing import List
class Graph:
    def __init__(self, edges, N):
        self.adj = [[] for _ in range(N)]
        for (src, dest) in edges:
            self.adj[src].append(dest)
            self.adj[dest].append(src)

def greedyColoring(graph, N):
    result = []
    k = -1
    result.append(0)
    for i in range(1,N):
        result.append(-1)
    available: List[bool] = []
    for i in range(N):
        available.append(False)
    for i in range(1,N):
        for j in graph.adj[i]:
            if result[j] != -1:
                available[result[j]] = True
        for k in range(N):
            if available[k] == False:
                p = k
                break
        result[i] = p
        for m in graph.adj[i]:
            if result[m] != -1:
                available[result[m]] = False
    for i in range(N):
        print("Vertex "+ str(i)+" --> Color ", result[i])
    

if __name__ == '__main__':
    edges = [(0, 1), (0, 4), (0, 5), (4, 5), (1, 4), (1, 3), (2, 3), (2, 4)]
    N = 6
    graph = Graph(edges, N)
    greedyColoring(graph, N)