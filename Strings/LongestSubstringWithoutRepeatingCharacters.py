"""

Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

"""
from icecream import ic
from collections import defaultdict


def lengthOfLongestSubstring(st: str) -> int:
    f = 0
    ans = 0
    dt = defaultdict(int)

    for i, n in enumerate(st):
        if n in dt:
            f = max(f, dt[n]+1)
            ic(n, f)
        dt[n] = i
        ans = max(ans, i-f+1)
        ic(ans)
    return ans


print(lengthOfLongestSubstring("abba"))
