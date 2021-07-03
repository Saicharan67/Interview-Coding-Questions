class Solution:
    # @param A : list of list of integers
    # @return an integer
    def cnt(self, A, mid):
        l = 0
        r = len(A)-1
        while l <= r:
            m = (l+r)//2

            if A[m] <= mid:
                l = m+1
            else:
                r = m-1
        return l

    def findMedian(self, A):
        l = 1
        r = 1000000000
        n = len(A)
        m = len(A[0])
        while l <= r:
            mid = (l+r)//2
            ct = 0
            for i in range(n):
                ct += self.cnt(A[i], mid)
            if ct <= (n*m)//2:
                l = mid+1
            else:
                r = mid-1
        return l
