

def findParent(node, parent):
    if node == parent[node]:
        return node
    parent[node] = findParent(parent[node], parent)

    return parent[node]


def union(u, v, parent, rank):
    u = findParent(u, parent)
    v = findParent(v, parent)

    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[u] > rank[v]:
        parent[v] = u
    else:
        parent[v] = u
        rank[u] += 1


def Kruskal(n, m):

    edges = []
    for _ in range(m):
        x, y, w = map(int, input().split())
        edges.append(x, y, w)

    edges = sorted(edges, key=lambda x: x[2])
    parent = [0]*n
    rank = [0]*n

    for i in range(n):
        parent[i] = i
    cost = 0
    mst = []
    for x, y, w in edges:
        if(findParent(x, parent) != findParent(y, parent)):
            cost += w
            mst.append([x, y])
            union(x, y, parent, rank)
    for i, j in mst:
        print(i, '-', j)
    return cost
