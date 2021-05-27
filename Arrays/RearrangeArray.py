from icecream import ic


def arrange(arr, n):

    for i in range(n):

        arr[i] = n*(arr[arr[i]] % n)+arr[i]

    for i in range(n):

        arr[i] = arr[i] // n

    return arr


ic(arrange([4, 0, 2, 1, 3], 5))
