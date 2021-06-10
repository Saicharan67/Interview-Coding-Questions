"""
Given an Array of non-negative intergers find if we can divide the array into two sub arrays of equal sum

"""

dp = ([[False for i in range(50)]
       for i in range(10)])


def EqualSumDp(a, n):
    s = sum(a)
    if s & 1:
        return False
    s = s//2

    for j in range(n+1):
        dp[j][0] = True
    for j in range(1, s+1):
        dp[0][j] = False

    for i in range(1, n+1):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if a[i-1] <= j:
                dp[i][j] |= dp[i-1][j-a[i-1]]
    print(dp)
    return dp[n][s]


print(EqualSumDp([1, 5, 5, 11], 4))
