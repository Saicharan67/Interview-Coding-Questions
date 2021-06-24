'''

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.
If multiple answers exist, you may return any of them.

(A string S is a subsequence of string T if deleting some number of characters from T
(possibly 0, and the characters are chosen anywhere from T) results in the string S.)



Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation:
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

'''
from icecream import ic


def PrintSCS(s1, s2, n, m):
    dp = [[0 for _ in range(m+1)]for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    i = n
    j = m
    ans = ''
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            ans += s2[j-1]
            j -= 1
            i -= 1
        else:
            if dp[i][j-1] < dp[i-1][j]:
                ans += s1[i-1]
                i -= 1
            else:
                ans += s2[j-1]
                j -= 1

    while i > 0:
        ans += s1[i-1]
        i -= 1
    while j > 0:
        ans += s2[j-1]
        j -= 1
    return ans[::-1]


print(PrintSCS(
    "bbbaaaba",
    "bbababbb", 8, 8))
