"""The cost of stock on each day is given in an array A[] of size N.
Find all the days on which you buy and sell the stock
 so that in between those days your profit is maximum.
"""


def sellandbuy(a, n):

    result = []
    start = 0
    end = 1
    while end < n:
        if a[start] < a[end] and a[end] > a[end-1]:
            end += 1
        else:
            if end-start > 1:
                result.append([start, end-1])
                start = end
                end = end+1
            else:
                start = end
                end = end+1

    if end-start > 1 and a[end-1] > a[start]:
        result.append([start, end-1])
        start = end
        end = end+1
    return result


print(sellandbuy([11, 42, 49, 96, 23, 20, 49, 26,
      26, 18, 73, 2, 53, 59, 34, 99, 25, 2], 18))


print("hi")
