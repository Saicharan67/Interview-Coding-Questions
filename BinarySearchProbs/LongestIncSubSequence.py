'''

In the previous approach, when we have an element num that is not greater than all the elements in sub, we perform a linear scan to find the first element in sub that is greater than or equal to num. Since sub is in sorted order, we can use binary search instead to greatly improve the efficiency of our algorithm.

Algorithm

Initialize an array sub which contains the first element of nums.

Iterate through the input, starting from the second element. For each element num:

If num is greater than any element in sub, then add num to sub.
Otherwise, perform a binary search in sub to find the smallest element that is greater than or equal to num. Replace that element with num.
Return the length of sub.

Implementation

In Python, the bisect module provides super handy functions that does binary search for us.


'''
import bisect


def longest(nums):
    sub = []
    for num in nums:
        i = bisect.bisect_left(sub, num)

        if i == len(sub):
            sub.append(num)
        else:
            sub[i] = num
    return len(sub)


print(longest([10, 9, 2, 5, 3, 7, 101, 18]))
