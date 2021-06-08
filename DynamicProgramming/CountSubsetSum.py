"""
Given an array of non-negative intergers...,count the number of subset with an given differenc

Basically its saying that ki to find # subsets possible with an given number 


"""

dp = ([[0 for i in range(50)]
       for i in range(10)])


def CountSubsetSumDp(a, n, diff):
    x = sum(a)
    s = (x+diff)//2
    for j in range(n+1):
        dp[j][0] = 1
    for i in range(1, n+1):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if a[i-1] <= j:
                dp[i][j] += dp[i-1][j-a[i-1]]
    print(dp[n][s])
    return dp[n][s]


CountSubsetSumDp([1, 1, 2, 3], 4, 1)
