"""

Given an array print all permutations of the array


"""


def permute(arr, res):
    if len(arr) == 0:
        print(res)
        return
    else:
        for i in range(len(arr)):
            pivot = arr[i]
            left = arr[:i]
            right = arr[i+1:]
            permute(left+right, res+[pivot])


permute([1, 2, 3], [])
