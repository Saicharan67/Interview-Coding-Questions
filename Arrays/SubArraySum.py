"""
Given an unsorted array A of size N that 
contains only non-negative integers, find a
continuous sub-array which adds to a given number S.

"""


def SubArraySum(a, n, k):
    s = sum(a)
    i = 1
    curr = a[0]
    st = 0

    while i <= n:

        while curr > k and st < i-1:
            curr -= a[st]
            st += 1
        if curr == k:
            return [st+1, i]
        if i < n:
            curr += a[i]

        i += 1

    return [-1]
