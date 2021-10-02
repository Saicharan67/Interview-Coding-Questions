"""

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

"""


def threeSum(nums):
    nums = sorted(nums)
    res = []
    for i, n in enumerate(nums):
        if i > 0 and n == nums[i-1]:
            continue
        l = i+1
        r = len(nums)-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1

    return res
