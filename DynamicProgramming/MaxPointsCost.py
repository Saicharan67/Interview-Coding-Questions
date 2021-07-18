'''
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
'''


class Solution:
    def maxPoints(self, points) -> int:
        rows = len(points)
        cols = len(points[0])
        dp = [[-1 for _ in range(cols)]for _ in range(rows)]

        for i in range(cols):
            dp[0][i] = points[0][i]

        for i in range(1, rows):
            prev = dp[i-1][0]
            for j in range(cols):
                prev = max(prev-1, dp[i-1][j])
                dp[i][j] = max(points[i][j]+prev, dp[i][j])

            prev = dp[i-1][cols-1]
            for j in range(cols-1, -1, -1):
                prev = max(prev-1, dp[i-1][j])
                dp[i][j] = max(points[i][j]+prev, dp[i][j])
        ans = 0
        for i in range(cols):
            ans = max(ans, dp[rows-1][i])
        return ans
