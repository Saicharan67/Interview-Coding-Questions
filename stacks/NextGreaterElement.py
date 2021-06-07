"""
Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
return the next greater number for every element in nums.
The next greater number of a number x is the first greater number to its traversing-order next in the array, 
which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.
"""


def nextGreaterElements(num):
    nums = num+num
    n = len(nums)
    st = []
    ans = [0]*n
    for i in range(n):

        while st and st[-1][1] < nums[i]:
            temp = st.pop()
            ans[temp[0]] = nums[i]

        st.append([i, nums[i]])
        ans[i] = -1

    print(ans)


nextGreaterElements([1, 2, 1])
