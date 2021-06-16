"""


Given an array a of size N and an integer K, the task is to divide the array into K segments such that sum of the minimums of K segments is maximized. 

"""


from icecream import ic

n = 9


def RecurrMin(a, i, k, mi):
    if i < 0:
        if k == 1:
            return mi
        else:
            return -float('inf')
    if k < 1:
        return -float('inf')
    x = mi+RecurrMin(a, i-1, k-1, a[i])
    y = -float('inf')
    if i == n-1:
        y = RecurrMin(a, i-1, k, a[i])
    else:
        y = RecurrMin(a, i-1, k, min(mi, a[i]))

    return max(x, y)


print(RecurrMin([6, 5, 3, 8, 9, 10, 4, 7, 10], 8, 4, 0))
