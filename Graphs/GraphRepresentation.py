'''Given a graph with N nodes and M edges then we will represent using

1) Adjacency Matric
2) Adjacency List
'''
from collections import defaultdict


def AdjMat(n, m):
    adjmat = [[0 for _ in range(n+1)]for _ in range(n+1)]
    for i in range(m):
        u, v = input().split()
        adjmat[u][v] = 1  # weight instead of 1
        adjmat[v][u] = 1  # if it is undirected


def AdjList(n, m):
    adjlist = defaultdict(list)

    for i in range(m):
        u, v = input().split()
        adjlist[u].append(v)  # .append([v,w]) if weight present
        adjlist[v].append(u)  # if it is undirected
