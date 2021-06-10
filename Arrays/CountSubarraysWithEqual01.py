"""

Given an array containing 0s and 1s. 
Find the number of subarrays having equal number of 0s and 1s.

"""


def countSubarrWithEqualZeroAndOne(arr, n):
    # Your code here
    import math

    def nCr(n, r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)

    s = 0
    ans = 0
    dt = {}
    dt[0] = 1
    for i in range(n):
        if arr[i]:
            s += 1
        else:
            s -= 1
        try:
            dt[s] += 1
        except:
            dt[s] = 1
    for key in dt.keys():
        if dt[key] >= 2:
            ans += nCr(dt[key], 2)
    return int(ans)
