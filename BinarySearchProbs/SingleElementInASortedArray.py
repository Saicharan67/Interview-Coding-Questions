"""
You are given a sorted array consisting of only integers 
where every element appears exactly twice, except for one 
element which appears exactly once. 
Find this single element that appears only once.

"""


def singleNonDup(arr):
    n = len(arr)
    left = 0
    right = n-2
    while left < right:
        mid = (left+right)//2
        if (arr[mid] == arr[mid ^ 1]):
            left += 1
        else:
            right -= 1
    return arr[left]


print(singleNonDup([1, 1, 2, 3, 3, 4, 4, 5, 5]))
