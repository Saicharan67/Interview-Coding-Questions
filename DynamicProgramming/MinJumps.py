"""

Given an array of non negative numbers, each element in the array reprents maximum jump length from that position. Initially you are at first position (0th index) of the array and you want to go to the last position. Find minimum number of jumps you need to make to reach the last position.
Note that there is always a way to reach the last position.

"""


def MinJumps(arr, n, idx):
    if n <= idx:
        return 0
    mini = 100000
    for i in range(1, arr[idx]+1):
        jumps = MinJumps(arr, n, idx+i)
        mini = min(jumps+1, mini)

    return mini


# using Dp

def DpMinJumps(arr):
    n = len(arr)
    jumps = [0 for i in range(n)]
    for i in range(n-2, -1, -1):
        if arr[i] >= n-i-1:
            jumps[i] = 1
        else:
            mini = 10000
            for j in range(i+1, n):
                if arr[i]+i >= j:
                    mini = min(mini, jumps[j])
            if mini != 10000:
                jumps[i] = mini+1
    return jumps[0]


print(DpMinJumps([1, 3, 6, 3, 2, 3, 6, 8, 9, 5]))


# Optimal Solution

def MinJumpsOptimim(a, n):
    if n <= 1:
        return 0
    if a[0] == 0:
        return -1
    maxReach = a[0]
    steps = a[0]
    jumps = 1
    for i in range(n):
        if i == n-1:
            return jumps
        maxReach = max(maxReach, i+a[i])
        steps -= 1
        if steps == 0:
            jumps += 1
            if i >= maxReach:
                return -1
        steps = maxReach-i
    return -1
