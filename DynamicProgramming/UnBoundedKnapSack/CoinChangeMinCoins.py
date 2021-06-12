"""

Given a value V, if we want to make change for V cents, 
and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?
If it’s not possible to make change, print -1.

"""


def MinCoins(carr, n, m):
    mx = float('inf')
    dp = [[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(m+1):
        dp[0][i] = mx
    for i in range(1, n+1):
        dp[i][0] = 0
    for i in range(1, m+1):
        if i % carr[0] == 0:
            dp[1][i] = i//carr[0]
        else:
            dp[1][i] = mx
    for i in range(2, n+1):
        for j in range(1, m+1):
            dp[i][j] = dp[i-1][j]
            if carr[i-1] <= j:
                dp[i][j] = min(dp[i-1][j], 1+dp[i][j-carr[i-1]])

    return dp[n][m] if dp[n][m] != mx else -1


print(MinCoins([2], 1, 3))
