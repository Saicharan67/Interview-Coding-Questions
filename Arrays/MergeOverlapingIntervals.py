"""

Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals. Let the intervals be represented as pairs of integers for simplicity. 
For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8}}. The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}. Similarly, {5, 7} and {6, 8} should be merged and become {5, 8}

"""


def MergeIntervals(arr, n):
    arr = sorted(arr, key=lambda x: x[0])
    temp = [arr[0]]
    for i in range(1, n):
        if arr[i][0] > temp[-1][1]:
            temp.append(arr[i])
        elif arr[i][1] > temp[-1][1]:
            temp[-1][1] = arr[i][1]
    return temp


print(MergeIntervals([[6, 8], [1, 9], [2, 4], [4, 7]], 4))
