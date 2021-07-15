'''
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
'''


def subarraySum(self, nums, k: int) -> int:
    res = 0
    currsum = 0
    dt = {}

    for i in nums:
        currsum += i
        if currsum == k:
            res += 1
        if currsum-k in dt:
            res += dt[currsum-k]
        if currsum in dt:
            dt[currsum] += 1
        else:
            dt[currsum] = 1

    return res
