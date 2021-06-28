'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

'''


def Rotate(arr, k):
    n = len(arr)
    k %= n
    for i in range(n//2):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
    print(arr)

    for i in range(k//2):
        arr[i], arr[k-i-1] = arr[k-i-1], arr[i]
    print(arr)

    for i in range((n-k)//2):
        arr[i+k], arr[n-i-1] = arr[n-1-i], arr[i+k]
    print(arr)


Rotate([1, 2, 3, 4, 5, 6, 7], 3)
