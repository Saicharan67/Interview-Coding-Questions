'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
Explanation:
Column -1: Only node 9 is in this column.
Column 0: Nodes 3 and 15 are in this column in that order from top to bottom.
Column 1: Only node 20 is in this column.
Column 2: Only node 7 is in this column.
'''
from collections import defaultdict
import functools


def verticalTraversal(self, root):
    dt = defaultdict(list)

    def cmp(a, b):
        if a[1] > b[1]:
            return 1
        elif a[1] < b[1]:
            return -11
        else:
            if a[0] > b[0]:
                return 1
            else:
                return -1

    def tree(root, pos, row):

        if not root:
            return

        dt[pos].append([root.val, row])

        tree(root.left, pos-1, row+1)
        tree(root.right, pos+1, row+1)
    tree(root, 0, 0)

    res = []
    for i in sorted(dt.keys()):
        k = []
        temp = sorted(dt[i], key=functools.cmp_to_key(cmp))
        for x in temp:
            k.append(x[0])
        res.append(k)
    return res
