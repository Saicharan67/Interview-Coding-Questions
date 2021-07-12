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
