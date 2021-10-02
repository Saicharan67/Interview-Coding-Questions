"""

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

"""


def fourSum(nums, n):
    if nums and len(nums) < 4:
        return []
    nums.sort()
    res = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)):
            s = nums[i]+nums[j]
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            l = j+1
            r = len(nums)-1
            while l < r:
                t = s+nums[l]+nums[r]
                if t > n:
                    r -= 1
                elif t < n:
                    l += 1
                else:
                    res.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
    return res
