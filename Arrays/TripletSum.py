
from icecream import ic


def find3sum(a, n, x):
    a.sort()
    d = set()
    for i in a:
        d.add(i)
    for i in range(n-1):
        for j in range(i+1, n):
            temp = x - a[i]-a[j]
            if temp in d:
                return True
    return False


assert(find3sum([1, 4, 45, 6, 10, 8], 6, 13))
