parent = [0]*100000

rank = [0]*100000


def makeset(n):
    for i in range(n):
        parent[i] = i


def findParent(node):
    if node == parent[node]:
        return node
    parent[node] = findParent(parent[node])

    return parent[node]


def union(u, v):
    u = findParent(u)
    v = findParent(v)

    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[u] > rank[v]:
        parent[v] = u
    else:
        parent[v] = u
        rank[u] += 1
