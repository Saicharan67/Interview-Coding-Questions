'''
Given an unsorted array of size n. Array elements are in the range from 1 to n. One number from set {1, 2, …n} is missing and one number occurs twice in the array. Find these two numbers.

Examples: 

 Input: arr[] = {3, 1, 3}
Output: Missing = 2, Repeating = 3
Explanation: In the array, 
2 is missing and 3 occurs twice 
'''


def SwapSort(arr):
    #arr = [2, 1, 2]
    n = len(arr)
    i = 0
    print(n, i)
    while i < n:

        if arr[i] != arr[arr[i]-1]:
             arr[i], arr[arr[i]-1] =arr[arr[i]-1], arr[i] 
        else:
            i += 1

    return (arr)


print(SwapSort([2, 1, 1]))
