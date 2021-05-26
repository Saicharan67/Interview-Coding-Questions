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
    t = CountPairs([8, 12, 16, 4, 0, 20], 4)

    assert t == 5, 'Correct value is {}'.format(t)
