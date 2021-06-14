"""

Given an array a of size N and an integer K, 
the task is to divide the array into K segments 
such that sum of the largest subarray sum in minimized. 


"""


def ArraySum(nums, m):
    value = max(nums)
    total = sum(nums)
    while value < total:
        mid = (value+total)//2
        print(mid, value, total)
        temp = isvalid(mid, nums, m)
        print(temp)
        if (temp):
            total = mid
        else:
            value = mid+1
    return value


def isvalid(mid, nums, m):
    currtotal = 0
    subarrcount = 0
    for i in nums:
        if i > mid:
            return False
        if currtotal+i <= mid:
            currtotal += i
        else:
            subarrcount += 1
            currtotal = i
    subarrcount += 1

    return subarrcount <= m


print(ArraySum([7, 2, 5, 10, 8], 2))
