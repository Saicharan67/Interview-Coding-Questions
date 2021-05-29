# recursive approch

def minDiff(arr, i, sumCal, sumTotal):

    if i == 0:
        return abs(sumTotal-2*sumCal)

    return min(minDiff(arr, i-1, sumCal+arr[i-1], sumTotal), minDiff(arr, i, sumCal, sumTotal))
# takes O(2^n)


# DP Approch

def findMin(a, n):
    s = sum(a)

    dp = [0 for i in range(s+1) for j in range(n+1)]

    for i in range(n+1):
        dp[i][0] = True

    for j in range(1, s+1):
        dp[0][j] = False

    for i in range(1, n+1):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if a[i-1] <= j:
                dp[i][j] |= dp[i-1][j-a[i-1]]

    for j in range(s//2, -1, -1):
        if dp[n][j] == True:
            diff = s-2*j
            break
    print(diff)
