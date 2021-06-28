'''
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The efficient way is the one that involves the least number of multiplications.

The dimensions of the matrices are given in an array arr[] of size N (such that N = number of matrices + 1) where the ith matrix has the dimensions (arr[i-1] x arr[i]).

Example 1:

Input: N = 5
arr = {40, 20, 30, 10, 30}
Output: 26000
Explaination: There are 4 matrices of dimension 
40x20, 20x30, 30x10, 10x30. Say the matrices are 
named as A, B, C, D. Out of all possible combinations,
the most efficient way is (A*(B*C))*D. 
The number of operations are -
20*30*10 + 40*20*10 + 40*10*30 = 26000.

'''

'Recursion approch'


def Solve(arr, i, j):
    if i >= j:
        return 0
    mini = float('inf')
    for k in range(i, j):
        tmp1 = Solve(arr, i, k)
        tmp2 = Solve(arr, k+1, j)
        ans = tmp1+tmp2+arr[i-1]*arr[k]*arr[j]

        mini = min(mini, ans)
    return mini


dp = [[-1 for _ in range(100)]for _ in range(100)]


def SolveMemo(arr, i, j):
    if i >= j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    dp[i][j] = float('inf')
    for k in range(i, j):
        tmp1 = SolveMemo(arr, i, k)
        tmp2 = SolveMemo(arr, k+1, j)
        ans = tmp1+tmp2+arr[i-1]*arr[k]*arr[j]

        dp[i][j] = min(dp[i][j], ans)
    return dp[i][j]
