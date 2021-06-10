"""

Merge two sorted arrays into a new array efficiently


"""


def Merge(a1, a2):
    res = []
    n1 = len(a1)
    n2 = len(a2)

    f = 0
    s = 0

    while f < n1 and s < n2:
        if a1[f] < a2[s]:
            res.append(a1[f])
            f += 1
        else:
            res.append(a2[s])
            s += 1

    if f < n1:
        res += a1[f:]
    if s < n2:
        res += a2[s:]
    print(res)


Merge([3, 4, 5], [1, 2, 6])
