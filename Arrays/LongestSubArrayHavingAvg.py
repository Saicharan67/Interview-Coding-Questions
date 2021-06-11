"""

Given an array of integers and an integer x. Find the length of maximum size subarray having an average of integers greater than or equal to x.

Examples:

Input : arr[] = {-2, 1, 6, -3}, x = 3
Output : 2
Longest subarray is {1, 6} having average
3.5 greater than x = 3.

"""


def longestsubarrayavg(arr, n, k):
    st = 0
    i = 0
    curr = 0
    maxi = -9999
    while i < n:
        curr += arr[i]
        while curr//(i-st+1) < k and st < i:
            curr -= arr[st]
            st += 1
        if curr//(i-st+1) >= k:
            maxi = max(maxi, i-st+1)
        i += 1
    return maxi


print(longestsubarrayavg([2, -3, 3, 2, 1], 5, 2))
