"""
Given a rod of length n inches and an array of prices 
that includes prices of all pieces of size smaller than n. 
Determine the maximum value obtainable by cutting up the rod and
selling the pieces. For example, if the length of the rod is 8 
and the values of different pieces are given as the following, 
then the maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6) 


length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20


In unbounded knapsack their is only one change compared to 0/1 knapsack i.e 

****dp[i][j-wt[n-1]]****

wt arr => len arr
val arr => price arr
W => L

"""


def RodCutting(larr, parr, L):
    n = len(larr)
    dp = [[0 for j in range(L+1)]for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, L+1):

            if larr[i-1] <= j:
                dp[i][j] = max(parr[i-1]+dp[i][j-larr[i-1]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    print(dp)
    return dp[n][L]


print(RodCutting([1, 2, 3, 4, 5, 6, 7, 8], [9, 5, 8, 9, 10, 17, 17, 20], 8))
