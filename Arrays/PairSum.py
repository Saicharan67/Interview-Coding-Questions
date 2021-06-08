"""

Given an array arr[] and an integer sum, the task is to 
find the number of pairs ofintegers in the array whose sum is equal to sum.


"""


from collections import defaultdict
from icecream import ic


def CountPairs(arr, k):
    count = 0
    d = defaultdict(int)
    for i in range(len(arr)):
        d[arr[i]] += 1
    for i in range(len(arr)):
        temp = arr[i]-k
        # temp2 = arr[i]+k
        if d[temp]:
            count += 1
        # if d[temp2]:
        #     count += 1
        #d[arr[i]] = 0

    return count


if __name__ == '__main__':
    t = CountPairs([1, 5, 7, -1], 6)

    assert t == 2, 'Correct value is {}'.format(t)
