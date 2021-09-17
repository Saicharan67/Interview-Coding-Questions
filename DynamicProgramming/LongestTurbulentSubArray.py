'''
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

'''


class Solution:
    def maxTurbulenceSize(self, arr) -> int:
        dp = [[0, 0] for _ in range(len(arr))]
        print(dp)
        maxi = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                dp[i][0] = 1 + dp[i-1][1]
                maxi = max(maxi, dp[i][0])
            elif arr[i] > arr[i-1]:
                dp[i][1] = 1 + dp[i-1][0]
                maxi = max(maxi, dp[i][1])

        return maxi+1
