"""
Given a value N, if we want to make change for N cents, 
and we have infinite supply of each of S = { S1, S2, .. , Sm} valued 
coins, how many ways can we make the change? The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, 
there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
So output should be 4. For N = 10 and S = {2, 5, 3, 6}, 
there are five solutions:
{2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
So the output should be 5.


"""


def CountWays(arr, n, X):

    dp = [[0 for _ in range(X+1)] for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    print(dp)
    for i in range(1, n+1):
        for j in range(1, X+1):
            dp[i][j] = dp[i-1][j]
            if arr[i-1] <= j:
                dp[i][j] += dp[i][j-arr[i-1]]
    return dp[n][X]


print(CountWays([2, 5, 3, 6], 4, 10))
