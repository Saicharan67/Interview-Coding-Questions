

def knapSack(wt, val, capacity, NumberOfItems):
    dp = [[0 for i in range(capacity+1)] for i in range(NumberOfItems+1)]
    for i in range(NumberOfItems+1):
        for j in range(capacity+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    for i in range(1, NumberOfItems+1):
        for j in range(1, capacity+1):
            if wt[i-1] <= j:
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp


print(knapSack([4, 8, 5, 3, 6], [35, 10, 15, 32, 25], 11, 5))
