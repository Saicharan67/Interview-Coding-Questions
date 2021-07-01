'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

'''


def letterCombinations(digits):
    d = {2: ['a', 'b', 'c'],
         3: ['d', 'e', 'f'],
         4: ['g', 'h', 'i'],
         5: ['j', 'k', 'l'],
         6: ['m', 'n', 'o'],
         7: ['p', 'q', 'r', 's'],
         8: ['t', 'u', 'v'],
         9: ['w', 'x', 'y', 'z']}
    ans = []
    n = len(digits)
    if n == 0:
        return []

    def dfs(dig, res):
        if len(res) == n:
            ans.append(res)
            return
        for ch in d[int(dig[0])]:
            res += ch
            dfs(dig[1:], res)
            res = res[:-1]
    dfs(digits, '')

    return ans
