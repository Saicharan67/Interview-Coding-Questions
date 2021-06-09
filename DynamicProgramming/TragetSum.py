"""
Given an array of integers...find out the no of times we can have the array sum as target by assigning neg/pos sign to numbers


Its same as CountSubsetsWithGivenSum
"""

dp = ([[0 for i in range(6)]
       for i in range(6)])


def CountSubsetwithTargetDp(a, n, Target):
    x = sum(a)
    s = (x+Target)//2
    for j in range(n+1):
        dp[j][0] = 1
    for i in range(1, n+1):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if a[i-1] <= j:
                dp[i][j] += dp[i-1][j-a[i-1]]
    print(dp)
    return dp[n][s]


CountSubsetwithTargetDp([1, 1, 2, 3], 4, 1)
