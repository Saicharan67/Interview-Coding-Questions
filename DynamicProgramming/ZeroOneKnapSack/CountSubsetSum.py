"""
Given an array of non-negative intergers...,count the number of subset possible with an given number 


"""

dp = ([[0 for i in range(6)]
       for i in range(6)])


def CountSubsetSumDp(a, n, s):

    for j in range(n+1):
        dp[j][0] = 1
    for i in range(1, n+1):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if a[i-1] <= j:
                dp[i][j] += dp[i-1][j-a[i-1]]
    print(dp)
    return dp[n][s]


CountSubsetSumDp([2, 3, 5, 5, 10], 6, 10)
