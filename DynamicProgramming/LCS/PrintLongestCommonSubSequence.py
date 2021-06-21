"""

Print the Longest Common SubSequence of two given strings

"""


def PrintLCS(s1, s2, n, m):
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
            ans += s1[i-1]
            i -= 1
            j -= 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
    return ans[::-1]


print(PrintLCS('abcde', 'abde', 5, 4))
