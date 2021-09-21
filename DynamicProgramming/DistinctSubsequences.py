'''


Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.


Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag


'''


def numDistinct(s: str, t: str) -> int:
    dp = [[0 for _ in range(len(s))]for _ in range(len(t))]
    dp[0][0] = 1 if s[0] == t[0] else 0
    for i in range(1, len(s)):
        dp[0][i] = dp[0][i-1]
        if s[i] == t[0]:
            dp[0][i] += 1

    for i in range(1, len(t)):
        for j in range(i, len(s)):
            dp[i][j] = dp[i][j-1]
            if s[j] == t[i]:
                dp[i][j] += dp[i-1][j-1]

    print(dp[len(t)-1][len(s)-1])
print(12)