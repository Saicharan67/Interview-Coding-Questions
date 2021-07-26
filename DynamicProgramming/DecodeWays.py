'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

'''
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        if len(s) == 1:
            if s != "0":
                return 1
            else:
                return 0
        a = 0
        b = 0
        if s[0] != "0":
            a = self.numDecodings(s[1:])
            if int(s[:2]) < 27:
                b = self.numDecodings(s[2:])
        return a+b
