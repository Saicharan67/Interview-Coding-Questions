"""
Given two strings find the extra char present in the string

"""


from collections import defaultdict
from icecream import ic


def findImposter(s, t):
    temp = defaultdict(int)
    if len(t) > len(s):
        s, t = t, s
    for i in t:
        temp[i] += 1
    print(temp)
    for j in s:
        temp[j] -= 1
        if temp[j] < 0:
            return j


print(findImposter('aab', 'ab'))
