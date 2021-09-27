
'''

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

Example 1:

Input: 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
Output: 6
Explanation: 
The shortest path without eliminating any obstacle is 10. 
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:

Input: 
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
Output: -1
Explanation: 
We need to eliminate at least two obstacles to find such a walk.

'''


def shortestPath(self, grid, k: int) -> int:
    m, n = len(grid), len(grid[0])
    start = m-1, n-1, k
    queue = [(0, start)]
    seen = {start}
    for steps, (i, j, k) in queue:
        if k >= i + j - 1:
            return steps + i + j
        for i, j in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if m > i >= 0 <= j < n:
                state = i, j, k - grid[i][j]
                if state not in seen and state[2] >= 0:
                    queue.append((steps + 1, state))
                    seen.add(state)
    return -1
