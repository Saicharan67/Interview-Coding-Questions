'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting 
some or no elements without changing the order of the remaining elements.

'''
from longestCmnSubSeq import DpLCS


def LongestPalindrom(s):
    n = len(s)
    s1 = s[::-1]
    if s == s1:
        return n

    return DpLCS(s, s1, n, n)
