dp = [[-1]*52]*5


def knapSack(wt, val, x, n):
    if(n == 0 or x == 0):
        return 0

    if dp[n][x] != -1:
        return dp[n][x]

    if wt[n-1] <= x:
        dp[n][x] = max(val[n-1]+knapSack(wt, val, x-wt[n-1],
                       n-1), knapSack(wt, val, x, n-1))
        return dp[n][x]
    else:
        dp[n][x] = knapSack(wt, val, x, n-1)
        return dp[n][x]


print(knapSack([10, 20, 30], [60, 100, 120], 50, 3))
