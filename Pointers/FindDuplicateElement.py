"""

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

"""

# Method - 1    =>     O(nlogn)


def FindDup(arr):
    l = 0
    h = len(arr) - 1

    while l < h:
        mid = (h+l)//2
        count = 0
        for i in arr:
            if i <= mid:
                count += 1
        if count <= mid:
            l = mid+1
        else:
            h = mid
    return l


# Method - 2   =>    O(n)


"""

Using tortoise method slow ans fast pointer technique

"""


def FindDups(arr):
    slow = arr[0]
    fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    fast = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow
