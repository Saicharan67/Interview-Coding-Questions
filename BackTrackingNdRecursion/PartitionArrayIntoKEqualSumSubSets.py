'''
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false

'''


class Solution:
    def canPartitionKSubsets(self, nums, k: int) -> bool:
        if(not ((sum(nums) % k) == 0)):
            return False

        def dfs(curr, k, nums):

            if(curr > target):
                return False

            if(curr == target):
                k -= 1
                # resetting curr value, first set found, search for next.
                curr = 0

            if(not nums):
                return True if(not k) else False

            for i in range(len(nums)):
                if(dfs(curr + nums[i], k, nums[:i] + nums[i+1:])):
                    return True

        nums.sort()
        target = sum(nums) // k

        if(nums[-1] > target):
            return False

        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return dfs(0, k, nums[::-1])
