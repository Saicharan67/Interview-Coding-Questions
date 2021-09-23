'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000
Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000
Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000

'''


def findMedianSortedArrays(self, nums1, nums2) -> float:
    A, B = nums1, nums2
    tot = len(A)+len(B)
    half = tot//2

    if len(A) > len(B):
        A, B = B, A

    l = 0
    r = len(A)-1

    while True:
        i = (l+r)//2
        j = half-i-2

        Aleft = A[i] if i >= 0 else -float('inf')
        Bleft = B[j] if j >= 0 else -float('inf')
        Aright = A[i+1] if i+1 < len(A) else float('inf')
        Bright = B[j+1] if j+1 < len(B) else float('inf')

        if Aleft <= Bright and Bleft <= Aright:
            if tot % 2:
                return min(Aright, Bright)
            else:
                return (max(Aleft, Bleft)+min(Aright, Bright))/2
        elif Aleft >= Bright:
            r = i-1
        elif Bleft >= Aright:
            l = i+1
