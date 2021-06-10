"""

Given two sorted arrays sort them accordingly with out extra space i.e O(1)

Input: ar1[] = {1, 5, 9, 10, 15, 20};
       ar2[] = {2, 3, 8, 13};
Output: ar1[] = {1, 2, 3, 5, 8, 9}
        ar2[] = {10, 13, 15, 20}

"""


def Merge(a1, a2, n1, n2):
    for i in range(n1):
        if a1[i] > a2[0]:
            a1[i], a2[0] = a2[0], a1[i]
            key = a2[0]
            j = 1
            while j < n2 and key > a2[j]:
                a2[j-1] = a2[j]
                j += 1
            a2[j-1] = key
