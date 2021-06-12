"""

Find the Maximum amount of water that can be trapped within
a given set of basrs where each bar's width is 1 unit


"""
from icecream import ic


def MaxWaterTraped(a, n):
    water = 0
    l = 0
    r = n-1
    lm = 0
    rm = 0
    temp1 = 0
    while l <= r:

        if rm <= lm:
            temp = rm-a[r]
            if temp <= 0:
                water = max(water, temp1)
                temp1 = 0
            else:
                temp1 += temp
            rm = max(rm, a[r])
            r -= 1
        else:
            temp = lm-a[l]
            if temp <= 0:
                water = max(water, temp1)
                temp1 = 0
            else:
                temp1 += temp
            lm = max(lm, a[l])
            l += 1
    water = max(water, temp1)
    return water


print(MaxWaterTraped([7, 0, 4, 2, 5, 0, 6, 4, 0, 5], 10))
