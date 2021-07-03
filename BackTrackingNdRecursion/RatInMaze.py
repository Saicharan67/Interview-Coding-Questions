'''
Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
'''


def findPath(self, m, n):
    path = set()
    ans = []

    def dfs(i, j, res):

        if i >= n or j >= n or i < 0 or j < 0 or m[i][j] == 0 or (i, j) in path:
            return
        if i == n-1 and j == n-1:
            ans.append(''.join(res))
            return

        path.add((i, j))

        res.append('D')
        dfs(i+1, j, res)
        res.pop()

        res.append('U')
        dfs(i-1, j, res)
        res.pop()

        res.append('L')
        dfs(i, j-1, res)
        res.pop()

        res.append('R')
        dfs(i, j+1, res)
        res.pop()

        path.remove((i, j))

        return
    dfs(0, 0, [])

    return sorted(ans)
