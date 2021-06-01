from icecream import ic


def removeElement(nums, val) -> int:

    st = 0
    n = len(nums)
    for j in range(n):
        if nums[j] != val:
            nums[st] = nums[j]
            st += 1
    ic(nums)
    return j


removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
