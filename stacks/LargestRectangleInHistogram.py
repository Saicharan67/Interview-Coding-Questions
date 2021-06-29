"""

Given an array of integers heights representing the histogram's
 bar height where the width of each bar is 1, 
return the area of the largest rectangle in the histogram.


"""

# Mostly correct solution


def largestRectangleArea(h):
    ma = max(h)
    mi = min(h)
    n = len(h)
    ans = max(ma, mi*n)

    tmph = mi+1
    while tmph <= ma:
        st = 0
        end = 0
        while end < n:
            print(ans, end, st)
            if h[end] >= tmph:
                end += 1
            else:

                end += 1
                st = end
                ans = max(ans, tmph*(end-st))

        ans = max(ans, tmph*(end-st))

        tmph += 1
    return ans

# Correct Solution


def LargestRect(h):
    h.append(0)
    st = [-1]
    ans = 0
    for i, x in enumerate(h):

        while h[i] < h[st[-1]]:

            tmp = h[st.pop()]

            idx = i-st[-1]-1
            ans = max(ans, idx*tmp)

        st.append(i)
        print(st)
    h.pop()

    return ans


print(LargestRect([1, 3, 6, 3, 1]))
