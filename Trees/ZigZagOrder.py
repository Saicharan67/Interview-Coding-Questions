'''
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        temp = []
        res = []

        if not root:
            return []
        temp = [root]
        rev = 0
        while temp:
            y = []
            temp2 = len(temp)
            for _ in range(temp2):
                o = temp.pop(0)
                y.append(o.val)
                if o.left:
                    temp.append(o.left)
                if o.right:
                    temp.append(o.right)
            if rev % 2:
                res.append(y[::-1])
            else:
                res.append(y)
            rev += 1
        return (res)
