"""
Given two numbers n,m find the nth root of number m using binary search


"""


def BinaryRoot(n, m):
    l = 1
    h = m
    delta = int(0.01)
    while h-l > delta:
        mid = (h+l)/2
        if(mid**n < m):
            l = mid
        else:
            h = mid
    print(l)


BinaryRoot(3, 27)
