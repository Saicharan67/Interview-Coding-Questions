"""
Given an array arr[] of size n where every element is in range 
from 0 to n-1. Rearrange the given array so that arr[i] becomes arr[arr[i]]. 
This should be done with O(1) extra space.
"""


from icecream import ic


def arrange(arr, n):

    for i in range(n):

        arr[i] = n*(arr[arr[i]] % n)+arr[i]

    for i in range(n):

        arr[i] = arr[i] // n

    return arr


ic(arrange([4, 0, 2, 1, 3], 5))
