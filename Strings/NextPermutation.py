"""

Given a number string find the next permutation of the number

"""


def NextPermu(s, n):
    firstIdx = -1
    for i in range(n-2, -1, -1):
        if s[i] < s[i+1]:
            firstIdx = i
            break
    if firstIdx == -1:
        return s[::-1]
    secondidx = -1

    for i in range(n-1, -1, -1):
        if s[i] > s[firstIdx]:
            secondidx = i
            break

    li = list(s)
    li[firstIdx], li[secondidx] = li[secondidx], li[firstIdx]
    li[firstIdx+1:] = li[firstIdx+1:][::-1]

    return "".join(li)


print(NextPermu('123', 3))
