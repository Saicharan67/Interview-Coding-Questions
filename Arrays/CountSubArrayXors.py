"""

Given an array of integers arr[] and a number m, count the number of subarrays having XOR of their elements as m.
Examples: 

Input : arr[] = {4, 2, 2, 6, 4}, m = 6
Output : 4
Explanation : The subarrays having XOR of 
              their elements as 6 are {4, 2}, 
              {4, 2, 2, 6, 4}, {2, 2, 6},
               and {6}

"""


def CountSubArrays(arr, m):
    from collections import defaultdict
    dt = defaultdict(int)
    cnt = 0
    currsum = 0
    dt[0] = 1
    for i in arr:
        currsum ^= i
        if dt[currsum ^ m]:
            cnt += dt[currsum ^ m]

        dt[currsum] += 1
    return cnt


print(CountSubArrays([5, 6, 7, 8, 9], 5))
