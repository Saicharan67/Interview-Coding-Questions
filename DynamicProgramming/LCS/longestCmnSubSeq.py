"""

Given two string print the length of longest common subsequence

"""


def RecurrLCS(s1, s2, n, m):
    if n == 0 or m == 0:
        return 0
    if s1[n-1] == s2[m-1]:
        return 1+RecurrLCS(s1, s2, n-1, m-1)
    else:
        return max(RecurrLCS(s1, s2, n, m-1), RecurrLCS(s1, s2, n-1, m))
