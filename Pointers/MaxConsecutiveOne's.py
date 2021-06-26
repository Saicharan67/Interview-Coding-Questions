'''

Given a binary array nums and an integer k, return the maximum number of 
consecutive 1's in the array if you can flip at most k 0's.


Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

'''
from icecream import ic


def longestOnes(nums, k: int) -> int:
    ans = 0
    i = 0
    j = 0
    n = len(nums)
    temp = k
    cnt = 0
    if k == 0:
        for h in nums:
            if h == 1:
                ans += 1
            else:
                cnt = max(cnt, ans)
                ans = 0
        return max(ans, cnt)

    while j < n:

        while j < n and temp > 0:
            if nums[j] == 0:
                temp -= 1
            j += 1
        while j < n and nums[j] != 0:
            j += 1

        ans = max(ans, j-i)
        if nums[i] == 0 and i < j:
            i += 1
            temp += 1
        elif nums[i] == 1 and i < j:
            i += 1
    return ans


print(longestOnes([0, 0, 1, 1, 0, 0, 1, 1,
      1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
