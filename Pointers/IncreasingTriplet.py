'''
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
'''


def increasingTriplet(nums) -> bool:
    i = k = j = float('inf')

    for a in nums:
        if i >= a:
            i = a
        elif j >= a:
            j = a
        elif k >= a:
            k = a
    print(i, j, k)
    if i < j and j < k and i != float('inf') and j != float('inf') and k != float('inf'):
        return True
    else:
        return False


def increasingTriplet2(nums) -> bool:
    i = k = j = float('inf')

    for a in nums:
        if i >= a:
            i = a
        elif j >= a:
            j = a
        else:
            return True
    return False
