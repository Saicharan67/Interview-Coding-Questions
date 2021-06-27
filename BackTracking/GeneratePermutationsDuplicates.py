"""

Given a collection of numbers, nums, that might contain duplicates, 
return all possible unique permutations in any order.


    Example 1:

    Input: nums = [1,1,2]
    Output:
    [[1,1,2],
    [1,2,1],
    [2,1,1]]

"""


def permuteUnique(nums):
    nums.sort()

    ans = []
    res = []

    def permute(nums, ans):
        if len(nums) == 0:
            res.append(ans)
            return
        for i in range(len(nums)):
            if i == len(nums)-1 or nums[i] != nums[i+1]:
                root = nums[i]
                left = nums[:i]
                right = nums[i+1:]
                permute(left+right, ans+[root])
    permute(nums, ans)
    return res
