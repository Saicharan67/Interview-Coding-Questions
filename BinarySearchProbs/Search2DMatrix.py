"""


Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


"""


def MatrixSearch(arr, x):
    rows = len(arr)
    cols = len(arr[0])
    l = 0
    r = rows*cols-1

    while l <= r:
        mid = (l+r)//2
        num = arr[mid//cols][mid % cols]
        if num == x:
            return True
        elif num > x:
            r = mid-1
        else:
            l = mid+1
    return False
