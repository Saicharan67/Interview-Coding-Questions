dp = [[0]*10]*10

# recursive


def subarraysumdp(arr, n, k):
    if n == 0 or k == 0:
        if k == 0:
            return True
        elif n == 0 and k != 0:
            return False
    else:

        if arr[n-1] > k:
            return subarraysumdp(arr, n-1, k)
        else:
            return subarraysumdp(arr, n-1, k-arr[n-1]) | subarraysumdp(arr, n-1, k)


print(subarraysumdp([2, 3, 7, 8, 10], 5, 19))
