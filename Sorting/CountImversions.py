"""
Inversion Count for an array indicates – how far (or close) the array is from being sorted. If the array is already sorted, then the inversion count is 0, but if the array is sorted in the reverse order, the inversion count is the maximum. 
Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j 
Example: 

Input: arr[] = {8, 4, 2, 1}
Output: 6

Explanation: Given array has six inversions:
(8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).

"""


def CountInversions(arr, n):

    temp = [0]*n
    return mergesort(arr, temp, 0, n-1)


def mergesort(arr, temp, l, r):
    invcount = 0
    if l < r:
        mid = (l+r)//2
        invcount += mergesort(arr, temp, l, mid)
        invcount += mergesort(arr, temp, mid+1, r)

        invcount += merge(arr, temp, l, mid, r)
    return invcount


def merge(arr, temp, l, mid, r):
    i = l
    j = mid+1
    k = l
    invcount = 0
    while i <= mid and j <= r:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            invcount = mid-i+1
            k += 1
            j += 1
    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= r:
        temp[k] = arr[j]
        k += 1
        j += 1

    for g in range(l, r+1):
        arr[g] = temp[g]
    return invcount
