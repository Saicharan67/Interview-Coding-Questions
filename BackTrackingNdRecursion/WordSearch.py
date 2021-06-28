'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

'''


def exist(b, word: str) -> bool:
    n = len(b)
    m = len(b[0])
    y = len(word)
    path = set()

    def SearchWord(i, j, x):

        if x == y:
            return True
        if i >= n or j >= m or i < 0 or j < 0 or word[x] != b[i][j] or (i, j) in path:
            return False
        p = 1
        path.add((i, j))
        res = SearchWord(i+1, j, x+p) or SearchWord(i, j+1, x +
                                                    p) or SearchWord(i, j-1, x+p) or SearchWord(i-1, j, x+p)
        path.remove((i, j))

        return res

    for i in range(n):
        for j in range(m):
            if SearchWord(i, j, 0):
                return True
    return False
