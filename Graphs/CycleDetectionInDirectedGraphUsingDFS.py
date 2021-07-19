from GraphRepresentation import AdjList


def dfsCheck(i,adjlist,visited,dfsvisited):
    visited[i]=True
    dfsvisited[i]=True
    for x in adjlist[i]:
        if not visited[x]:
           if dfsCheck(x,adjlist,visited,dfsvisited):
               return True
        else:
            if dfsvisited[x]:
                return True
    dfsvisited[i]=False
    return False



def CheckCycleDirected(n,m):
    adjlist = AdjList(n,m)
    visited = [False]*(n+1)
    dfsvis = [False]*(n+1)

    for i in range(1,n+1):
        if not visited[i]:
            if dfsCheck(i,adjlist,visited,dfsvis):
                return True