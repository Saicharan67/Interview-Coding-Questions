"""
Given an unsorted array of size n. 
Array elements are in the range from 1 to n.
One number from set {1, 2, …n} is missing and one number occurs twice in the array.
Find these two numbers.

"""


def RepMiss(arr, n):
    Map = {}

    max = len(arr)
    for i in arr:
        if not i in Map:
            Map[i] = True

        else:
            print("Repeating =", i)

    for i in range(1, max + 1):
        if not i in Map:
            print("Missing =", i)


def RepMiss2(A):
    length = len(A)
    Sum_N = (length * (length + 1)) // 2
    Sum_NSq = ((length * (length + 1) *
                (2 * length + 1)) // 6)

    missingNumber, repeating = 0, 0

    for i in range(len(A)):
        Sum_N -= A[i]
        Sum_NSq -= A[i] * A[i]

    missingNumber = (Sum_N + Sum_NSq // Sum_N) // 2
    repeating = missingNumber - Sum_N

    ans = []
    ans.append(repeating)
    ans.append(missingNumber)

    return ans
