"""Given an array of integers arr,
 find the sum of min(b), where b ranges
 over every (contiguous) subarray of arr.
 Since the answer may be large, return the answer modulo 109 + 7."""


def subarrayminimum(a):
    st = []
    n = len(a)
    left = [-1]*n
    right = [n]*n
    for i in range(n):
        while st and a[i] < a[st[-1]]:
            temp = st.pop()
            right[temp] = i
        left[i] = st[-1] if st else -1
        st.append(i)
    res = 0
    for el, (a, b) in enumerate(zip(left, right)):
        res += a[el]*(b-el)(el-a)
    return res
