# You are given N pairs of numbers.
#  In every pair, the first number is always smaller than the second number.
#  A pair (c, d) can follow another pair (a, b) if b < c.
#  Chain of pairs can be formed in this fashion.
# You have to find the longest chain which can be formed from the given set of pairs.


dp = [[0]*100]*100


def maxchain(Parr, n, prev, pos):
    if pos >= n:
        return 0
    if dp[pos][prev]:
        return dp[pos][prev]

    if Parr[pos][0] < prev:
        return maxchain(Parr, n, prev, pos+1)
    else:
        ans = max(maxchain(Parr, n, Parr[pos][1],
                  0)+1, maxchain(Parr, n, prev, pos+1))
        dp[pos][prev] = ans
        return ans


print(maxchain([[1, 2], [2, 3], [3, 4]], 3, 0, 0))


# Parr = sorted(Parr, key=lambda x: x[1])
#     # Initialize MCL(max chain
#     # length) values for all indices
#     mcl = [1 for i in range(n)]
#     print(Parr)
#     # Compute optimized chain
#     # length values in bottom up manner
#     for i in range(1, n):
#         for j in range(0, i):
#             if (Parr[i][0] > Parr[j][1] and mcl[i] < mcl[j]+1):
#                 mcl[i] = mcl[j] + 1
#     print(mcl)
#     return max(mcl)

def findLongestChain(pairs):
    pairs.sort()
    dp = [1] * len(pairs)

    for j in range(len(pairs)):
        for i in range(j):
            if pairs[i][1] < pairs[j][0]:
                dp[j] = max(dp[j], dp[i] + 1)

    return max(dp)
