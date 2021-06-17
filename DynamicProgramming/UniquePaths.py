"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

"""
# Recursion Method


def UniquePath(m, n):
    if m == 1 or n == 1:
        return 1
    return UniquePath(m-1, n)+UniquePath(m, n-1)


print(UniquePath(7, 3))

# DP approch


def UniqueDp(m, n):
    dp = [[1 for _ in range(m)]for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[n-1][m-1]
