from collections import defaultdict
import string
from icecream import ic


def fnx(strs, n, n1, idx):
    temp = set()
    for i in range(idx, n1):
        if strs[0][i] <= strs[1][i]:
            temp.add(i)
    for i in range(1, n-1):
        for j in range(idx, n1):
            if strs[i][j] > strs[i+1][j]:
                if j in temp:
                    temp.remove(j)
                    if len(temp) == 0:
                        return n1-idx
    flag = True
    maxi = 0
    eqls = 0
    gi = 0
    for i in range(n-1):
        eqls = 0
        gi = n1
        flag = True
        for j in temp:
            if strs[i][j] == strs[i+1][j]:
                eqls += 1
            else:
                maxi = max(maxi, j-idx-eqls)
                flag = False
                break
        if flag:
            maxi = max(maxi, gi-idx-eqls)
    return maxi


def minDeletionSize(strs) -> int:
    n = len(strs)
    n1 = len(strs[0])
    ans = 0
    for i in range(n1):
        satis = 0
        prev = strs[0][i]
        for j in range(n):
            if strs[j][i] < prev:
                satis = 1
                break
            prev = strs[j][i]

        if satis == 0:
            temp = fnx(strs, n, n1, i)
            ans = max(ans, n1-i-temp)
    ans = max(ans, 0)
    return n1-ans


print(minDeletionSize(["zyx", "wvu", "tsr"]))


# l = list(string.ascii_lowercase)
#     for i in l:
#         prev = ''
#         got = 0
#         for j in range(n):
#             if strs[j][idx] == i:
#                 if got == 0:
#                     prev = strs[j]
#                     got = 1
#                 else:
#                     for k in range(idx, n1):
#                         if strs[j][k] < prev[k]:
#                             ic(prev[k], j, k, strs[j][k])
#                             dt[k] += 1
#                         elif strs[j][k] == prev[k]:
#                             continue
#                         else:
#                             break
