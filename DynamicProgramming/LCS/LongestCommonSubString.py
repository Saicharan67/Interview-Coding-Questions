"""
Given two strings print the longest common sub string in two strings

"""


def LCSubString(s1, s2, n, m):
    dp = [[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = 0
    return dp


print(LCSubString('babad', 'dabab', 5, 5))
