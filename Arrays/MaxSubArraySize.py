# Given an array of n positive integers and a
# positive integer k, the task is to find the maximum
#  subarray size such that all subarrays of that
#  size have the sum of elements less than k.
from icecream import ic


def MaxSubArraySize(a, n, k):
    for i in range(1, n):
        a[i] += a[i-1]
    for i in range(n-1, 0, -1):
        flag = 1
        if a[i] > k:
            flag = 0
            continue
        for j in range(i+1, n):
            if a[j]-a[j-i-1] > k:
                flag = 0
                continue
        if flag:
            return i
    return -1


ic(MaxSubArraySize([1, 2, 10, 4], 4, 14))


def Maxsub(a, n, k):
    ans = n
    suma = 0
    start = 0
    for i in range(n):
        suma += a[i]
        while suma > k:
            suma -= a[start]
            start += 1
            ans = min(ans, i-start+1)

            if suma == 0:
                break
        if suma == 0:
            ans = -1
            break
    return ans
