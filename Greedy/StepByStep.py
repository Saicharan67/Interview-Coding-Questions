'''
Given a target A on an infinite number line, i.e. -infinity to +infinity.
You are currently at position 0 and you need to reach the target by moving according to the below rule:

In ith move you can take i steps forward or backward.
Find the minimum number of moves required to reach the target.

'''


class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 0
        A = abs(A)
        i = 1
        no = 0
        while 1:
            no += i
            if no == A:
                return i
            if no > A:
                break
            i += 1
        cur = no-A
        if(cur % 2 == 0):
            return i
        if((cur+i+1) % 2 == 0):
            return i+1
        return i+2
