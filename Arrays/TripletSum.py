
"""

Given an array and a value, find if there is a triplet in 
array whose sum is equal to the given value. If there is such a triplet present in array, 
then print the triplet and return true. Else return false.

"""


def find3sum(a, n, x):
    d = set()

    for i in range(n-1):
        curr = x-a[i]
        for j in range(i+1, n):
            temp = curr-a[j]
            if temp in d:
                return True
            d.add(a[j])
    return False


assert(find3sum([1, 4, 45, 6, 10, 8], 6, 22))
