from functools import lru_cache


def recurr(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr)

    return max(arr[0]+recurr(arr[2:]), arr[1]+recurr(arr[3:]))


'DP Approch'


def Dp(arr):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return max(arr)
    dp = [0]*len(arr)
    dp[0] = arr[0]
    dp[1] = max(arr[:2])
    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], arr[i]+dp[i-2])

    return dp[-1]


print(recurr([5, 20, 15, -2, 18]))
