# Given an array of n elements and an integer m.
#  The task is to find the maximum value of the
#  sum of its subarray modulo m i.e find the
# sum of each subarray mod m and print
# the maximum value of this modulo operation.
from icecream import ic


def MaxSumMod(a, n, m):
    maxi = 0
    for i in range(1, n):
        a[i] += a[i-1]
    ic(a)
    for i in range(n-1, 0, -1):
        maxi = max(maxi, a[i] % m)
        ic(maxi)
        for j in range(i+1, n):
            ic(j)
            maxi = max(maxi, (a[j]-a[j-i-1]) % m)
            ic(maxi)

    return maxi


print(MaxSumMod([7, 18], 2, 13))
