"""

Given an array of positive integers nums and a positive integer target, 
return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] 
of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

"""


def minSubArrayLen(target, nums) -> int:
    l = 0
    res = 0
    mini = len(nums)+1
    for i, n in enumerate(nums):
        res += n
        while res >= target:
            mini = min(mini, i - l + 1)
            res -= nums[l]
            l += 1

    return mini if mini <= len(nums) else 0
