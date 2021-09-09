'''
You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

 

Example 1:


Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.

'''


class Solution:
    def orderOfLargestPlusSign(self, n: int, mines) -> int:
        t = [[0 for _ in range(n)]for _ in range(n)]
        b = [[0 for _ in range(n)]for _ in range(n)]
        l = [[0 for _ in range(n)]for _ in range(n)]
        r = [[0 for _ in range(n)]for _ in range(n)]

        s = set()
        for x, y in mines:
            s.add((x, y))
        for i in range(n):
            for j in range(n):
                if (i, j) not in s:

                    if i-1 < 0:
                        t[i][j] = 1
                    else:
                        t[i][j] = t[i-1][j]+1
        for i in range(n):
            for j in range(n):
                if (i, j) not in s:
                    if j-1 < 0:
                        l[i][j] = 1
                    else:
                        l[i][j] = l[i][j-1]+1
        for i in range(n):
            for j in range(n-1, -1, -1):
                if (i, j) not in s:
                    if j+1 == n:
                        r[i][j] = 1
                    else:
                        r[i][j] = r[i][j+1]+1
        for i in range(n-1, -1, -1):
            for j in range(n):
                if (i, j) not in s:
                    if i+1 == n:
                        b[i][j] = 1
                    else:
                        b[i][j] = b[i+1][j]+1
        maxi = 0

        for i in range(n):
            for j in range(n):
                maxi = max(maxi, min(t[i][j], b[i][j], l[i][j], r[i][j]))

        return maxi
