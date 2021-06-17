"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

"""


def Major(arr):
    count = 1
    Element = 0
    for i in range(len(arr)):
        count += (1 if arr[i] == arr[Element] else -1)
        if count == 0:
            count = 1
            Element = i

    return arr[Element]


print(Major([2, 3, 3, 4, 3]))
