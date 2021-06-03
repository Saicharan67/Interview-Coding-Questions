from icecream import ic


def sort012(arr, n):
    i = 0
    j = n-1
    mid = 0
    while mid <= j:
        if arr[mid] == 0:
            arr[mid], arr[i] = arr[i], arr[mid]
            mid += 1
            i += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[j] = arr[j], arr[mid]
            j -= 1
    return arr


print(sort012([0, 2, 1, 2, 0], 5))
