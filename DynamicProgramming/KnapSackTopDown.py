dp = []


def knapSack(wt, val, x, n):
    for i in range(n+1):
        for j in range(x+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    for i in range(1, n+1):
        for j in range(1, x+1):
            if wt[i-1] <= j:
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[n-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][x]


print(knapSack([10, 20, 30], [60, 100, 120], 50, 3))
