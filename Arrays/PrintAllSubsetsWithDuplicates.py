'''

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]

'''


def subsetsWithDup(arr):
    res = []
    arr.sort()

    def recur(arr, op=[]):
        res.append(op)
        for i in range(len(arr)):
            if i > 0 and arr[i] == arr[i-1]:
                continue
            recur(arr[i+1:], op+[arr[i]])

    recur(arr)
    return res
