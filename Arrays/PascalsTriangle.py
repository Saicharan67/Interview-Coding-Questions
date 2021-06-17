"""

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:



"""
from icecream import ic


def Generate(n):
    if n == 1:
        return [1]
    res = [[1]]
    for i in range(2, n+1):
        ic(i)
        tmp = [1]*i
        for j in range(1, i-1):
            tmp[j] = res[-1][j-1]+res[-1][j]
        res.append(tmp)
    return res


print(Generate(5))
