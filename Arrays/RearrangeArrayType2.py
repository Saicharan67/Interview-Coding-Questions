"""

Rearrange an array such that ‘arr[j]’
becomes ‘i’ if ‘arr[i]’ is ‘j’ | Set 1

"""


def arrange(a, n):
    for i in range(n):
        a[a[i] % n] += n*(i)

    for i in range(n):
        a[i] = a[i]//n
    return a


print(arrange([1, 3, 0, 2], 4))
