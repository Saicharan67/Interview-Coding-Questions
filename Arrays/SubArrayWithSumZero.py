"""
Given an array find out if we can divide the array such that we can find a continuous 
sub array with sum as zero

"""


def SubArray(arr):
    d = set()
    temp = 0
    for i in range(len(arr)):
        temp += arr[i]
        if temp in d:
            return True
        d.add(temp)
    return False


assert SubArray([4, 2, -3, 1, 6])
