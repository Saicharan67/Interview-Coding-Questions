"""
Given an array of non-negative intergers...count no of subsets with given difference

Basically its saying that ki to find # subsets because

s1 + s2 = sum
s1 - s2 = diff
______________
s1 = (sum+diff)//2
_______________

find subsets with sum s1

"""

dp = ([[0 for i in range(6)]
       for i in range(6)])


def CountSubsetwithDiffDp(a, n, diff):
    x = sum(a)
    s = (x+diff)//2
    for j in range(n+1):
        dp[j][0] = 1
    for i in range(1, n+1):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if a[i-1] <= j:
                dp[i][j] += dp[i-1][j-a[i-1]]
    print(dp)
    return dp[n][s]


CountSubsetwithDiffDp([1, 1, 2, 3], 4, 1)
