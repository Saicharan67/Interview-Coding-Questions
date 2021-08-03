'''
Given a row of n coins of values arr[1], arr[2], ... arr[n], where n is even. Geek plays a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount geek can get if he moves first.

Note: Both of them play optimally

Example 1:

Input: N = 4, arr[] = {5, 3, 7, 10}
Output: 15
Explanation: 
Geek chooses 10.
Opponent chooses 7.
Geek chooses 5.
Opponent chooses 3.

'''
from functools import lru_cache


class Solution:

    def maxAmount(self, A, N):
        # code here
        @lru_cache(maxsize=None)
        def recurr(st, end):
            if st == end:
                return A[st]
            if end-st == 1:
                return max(A[st], A[end])

            return max(A[st]+min(recurr(st+2, end), recurr(st+1, end-1)), A[end]+min(recurr(st+1, end-1), recurr(st, end-2)))

        return recurr(0, N-1)
