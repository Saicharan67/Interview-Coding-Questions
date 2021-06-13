"""

Given an array arr[] of size N and a number K, the task is 
to partition the given array into K contiguous subarrays such 
that the sum of the maximum of each subarray is the maximum possible. 
If it is possible to split the array in such a manner, 
then print the maximum possible sum. Otherwise, print “-1“.

"""
from collections import defaultdict


def SubArrayMaxs(arr, n, k):
    if k > n:
        return -1
    c = arr
    c = sorted(c, reverse=True)
    dt = defaultdict(int)
    ans = 0
    for i in range(k):
        ans += c[i]
        dt[c[i]] += 1
    p = []
    v = []
    for i in range(n):
        v.append(arr[i])
        if dt[arr[i]]:
            dt[arr[i]] -= 1
            k -= 1
            if k == 0:
                while i+1 < n:
                    v.append(arr[i+1])
                    i += 1
            p.append(v)
            v = []

    print(ans)
    print(p)


SubArrayMaxs([1, 4, 5, 6, 1, 2], 6, 2)
