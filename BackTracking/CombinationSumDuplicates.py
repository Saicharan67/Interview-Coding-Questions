'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

'''


def combinationSum2(nums, target):
    nums.sort()
    ans = []

    def Combo(arr, res, target):
        if target < 0:
            return
        elif len(arr) == 0 and target > 0:
            return
        elif target == 0:
            ans.append(res)

        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            Combo(arr[i+1:], res+[arr[i]], target-arr[i])

    Combo(nums, [], target)
    return ans
