"""

Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""


def setZeroes(m) -> None:

    c = len(m[0])
    r = len(m)
    row = False
    col = False
    for i in range(r):
        if m[i][0] == 0:
            col = True
    for i in range(c):
        if m[0][i] == 0:
            row = True
    for i in range(1, r):
        for j in range(1, c):
            if m[i][j] == 0:
                m[0][j] = 0
                m[i][0] = 0
    for i in range(1, r):
        if m[i][0] == 0:
            for j in range(1, c):
                m[i][j] = 0
    for i in range(c):
        if m[0][i] == 0:
            for j in range(1, r):
                m[j][i] = 0
    if row:
        for i in range(c):
            m[0][i] = 0
    if col:
        for j in range(r):
            m[j][0] = 0
