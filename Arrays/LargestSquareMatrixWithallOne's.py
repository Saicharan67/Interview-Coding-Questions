"""

Given an mxn binary matrix, find the size of the largest sqaure submatrix of 1's present


"""


def MatrixOfOnes(m, r, c):
    dp = [[0 for _ in range(c)]for _ in range(r)]
    ans = 0
    for i in range(r):
        for j in range(c):
            dp[i][j] = m[i][j]
            if i > 0 and j > 0 and m[i][j] == 1:
                m[i][j] = min(m[i-1][j-1], m[i-1][j], m[i][j-1])+1
            ans = max(ans, m[i][j])
    return ans
