"""

Given n non-negative integers representing an elevation map where the 
width of each bar is 1, compute how much water it is able to trap after raining.

e can trap 2 units of water in the middle gap.

Input: arr[]   = {3, 0, 2, 0, 4}
Output: 7

"""
from icecream import ic


def WaterTraped(arr, n):
    water = 0
    l = [0]*n
    r = [0]*n
    l[0] = arr[0]
    for i in range(1, n):
        l[i] = max(l[i-1], arr[i])
    r[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        r[i] = max(r[i+1], arr[i])
    for i in range(n):
        water += min(l[i], r[i])-arr[i]
    return water


def WaterTrapedPointer(arr, n):
    l = 0
    r = n-1
    lm = 0
    rm = 0
    water = 0
    while l <= r:
        if lm <= rm:
            water += max(0, lm-arr[l])
            lm = max(lm, arr[l])
            l += 1
        else:
            water += max(0, rm-arr[r])
            rm = max(rm, arr[r])
            r -= 1
        ic(water)
    return water


print(WaterTrapedPointer([7, 0, 4, 2, 5, 0, 6, 4, 0, 5], 10))
