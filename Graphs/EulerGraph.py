

def Connected_Graph(adjlist):
    visted = [False]*(len(adjlist))
    node = -1
    for i in adjlist.keys():
        if len(adjlist[i]) > 0:
            node = i
            break
    if node == -1:
        return True

    def DFS(node):
        visted[node] = True
        for x in adjlist[node]:
            if not visted[x]:
                DFS(x)
    for i in adjlist.keys():
        if visted[i] == False and len(adjlist[i]) > 0:
            return False
    return True


def find_euler(adjlist):
    if not Connected_Graph(adjlist):
        return 0
    oddCount = 0

    for i in adjlist.keys():
        if len(adjlist[i]) & 1:
            oddCount += 1

    if oddCount > 2:
        return 0
    return 2 if oddCount == 0 else 1


def main(adjlist):
    res = find_euler(adjlist)
    if res == 0:
        print("Not euler")
    if res == 1:
        print("Semi Euler")
    else:
        print("Euler graph")
