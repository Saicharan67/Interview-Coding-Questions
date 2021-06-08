"""
Given two unsorted arrays of distinct elements, the task is 
to find all pairs from both arrays whose sum is equal to X.

"""


def CountPairs(a1, a2, k):
    s = set()
    for i in a1:
        s.add(i)
    for i in a2:
        if(k-i in s):
            print(k-i, i)
