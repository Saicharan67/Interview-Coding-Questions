dp = [[0]*50]*10

# recursive


def subarraysumrecurr(arr, n, k):
    if n == 0 or k == 0:
        if k == 0:
            return True
        elif n == 0 and k != 0:
            return False
    else:

        if arr[n-1] > k:
            return subarraysumdp(arr, n-1, k)
        else:
            return subarraysumdp(arr, n-1, k-arr[n-1]) | subarraysumdp(arr, n-1, k)

# Dp approch


def subarraysumdp(arr, n, k):
    for i in range(n+1):
        dp[i][0] = True

    for j in range(1, k+1):
        dp[0][j] = False

    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] |= dp[i-1][j-arr[i-1]]

    return dp[n][k]


print(subarraysumdp([2, 3, 7, 8, 10], 5, 23))
