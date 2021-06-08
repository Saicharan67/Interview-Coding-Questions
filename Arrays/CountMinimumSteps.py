"""
Consider an array with n elements and value of all the elements is zero. We can perform following operations on the array. 
 

Incremental operations:Choose 1 element from the array and increment its value by 1.
Doubling operation: Double the values of all the elements of array.
"""


def play_the_game(target):
    result = 0
    n = len(target)
    while True:

        zero_count = 0
        i = 0
        while i < n:
            if (target[i] & 1) > 0:
                break
            elif (target[i] == 0):
                zero_count += 1
            i += 1
        if zero_count == n:
            return result
        for j in range(i, n):
            if (target[j] & 1):
                target[j] -= 1
                result += 1
        if i == n:
            for j in range(n):
                target[j] = target[j] // 2
            result += 1


print(play_the_game([2, 1]))
