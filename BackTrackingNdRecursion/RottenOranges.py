'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
'''


def orangesRotting(self, grid) -> int:
    rotten = []
    # build initial array of rotten oranges
    rows = len(grid)
    columns = len(grid[0])
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 2:
                rotten.append((i, j))

    # get unvisited neighbors of all rotten oranges
    def add_neighbors(rotten):
        neighbors = []
        for i, j in rotten:
            if i > 0 and grid[i - 1][j] == 1:
                neighbors.append((i - 1, j))
                grid[i-1][j] = 2
            if j > 0 and grid[i][j - 1] == 1:
                neighbors.append((i, j - 1))
                grid[i][j-1] = 2
            if i < rows - 1 and grid[i + 1][j] == 1:
                neighbors.append((i + 1, j))
                grid[i + 1][j] = 2
            if j < columns - 1 and grid[i][j + 1] == 1:
                neighbors.append((i, j + 1))
                grid[i][j+1] = 2
        return neighbors

    minutes = 0
    while (1):
        rotten = add_neighbors(rotten)
        if len(rotten) == 0:
            break
        minutes += 1

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                return -1

    return minutes
