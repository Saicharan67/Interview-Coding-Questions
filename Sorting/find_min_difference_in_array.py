""""
Find minimum difference between any two elements by using sort function


Problem Description:

Given an unsorted array of integers, sort the array into a wave like array.


Sample Test Case:

 Input:  arr[] = {20, 10, 8, 6, 4, 2}
 
 Output: arr[] = {20, 8, 10, 4, 6, 2} OR
                 {10, 8, 20, 2, 6, 4}
                 
                 
Time Complexity - O(n Log n) 

"""

def findMinDiff(arr, n):
 
    # Sort array in ascending order
    arr = sorted(arr)
 
    # Initialize difference as infinite
    diff = 10**20
 
    # Find the min diff by comparing adjacent
    for i in range(n-1):
        if arr[i+1] - arr[i] < diff:
            diff = arr[i+1] - arr[i]
 
    return diff
 

arr = [1, 5, 3, 19, 18, 25]
n = len(arr)
print("Minimum difference is " + str(findMinDiff(arr, n)))


