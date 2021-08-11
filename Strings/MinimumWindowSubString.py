'''
Given two strings S and P. Find the smallest window in the string S consisting of all the characters(including duplicates) of the string P.  Return "-1" in case there is no such window present. In case there are multiple such windows of same length, return the one with the least starting index. 

Example 1:

Input:
S = "timetopractice"
P = "toc"
Output: 
toprac
Explanation: "toprac" is the smallest
substring in which "toc" can be found.

'''


class Solution:
    def minWindow(self, s: str, p: str) -> str:
        dt = {}
        if len(p) > len(s):
            return ""
        for i in p:
            if i not in dt:
                dt[i] = 1
            else:
                dt[i] += 1
        count = len(dt)
        i = 0
        j = 0
        ans = ""
        maxi = float('inf')
        while j < len(s):
            if s[j] in dt:
                dt[s[j]] -= 1
                if dt[s[j]] == 0:
                    count -= 1
            while count == 0:
                if j-i < maxi:
                    maxi = j-i

                    ans = s[i:j+1]

                if s[i] in dt:
                    dt[s[i]] += 1
                    if dt[s[i]] > 0:
                        count += 1
                i += 1
            j += 1
        return ans
