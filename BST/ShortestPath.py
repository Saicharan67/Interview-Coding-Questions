"""
Consider you have an infinitely long binary tree having a pattern as below: 

  
               1
            /      \
           2        3
         /  \      / \
        4    5    6   7
      /  \  / \  / \ / \
     .  .  .  . .  .  .  .
Given two nodes with values x and y. The task is to find the length of the shortest path between the two nodes. 

"""


def shortestPath(x, y):
    v1 = []
    v2 = []

    while x:
        v1.append(x)
        x = x//2
    v1.reverse()

    while y:
        v2.append(y)
        y = y//2
    v2.reverse()

    for i in range(len(v1)-1, -1, -1):

        if v1[i] in v2:
            x = v2.index(v1[i])
            return len(v1)-1-i + len(v2)-1-x


print(shortestPath(8, 12))
