'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
from functools import lru_cache


def minCut(self, s: str) -> int:

    @lru_cache(maxsize=None)
    def Palindrome(s, i, j):
        if i >= j:
            return 0
        if s[i:j+1] == s[i:j+1][::-1]:
            return 0
        ans = float('inf')
        for k in range(i, j):

            if s[i:k+1] == s[i:k+1][::-1]:
                tmpans = Palindrome(s, i, k)+1+Palindrome(s, k+1, j)
                if tmpans < ans:
                    ans = tmpans
        return ans
    return Palindrome(s, 0, len(s)-1)
