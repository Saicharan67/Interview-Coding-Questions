'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that all houses in this place form a binary tree. It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

 

Example 1:


Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

'''
from functools import lru_cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @lru_cache(maxsize=None)
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0
        incl = root.val
        excl = self.rob(root.left)+self.rob(root.right)

        if root.left:
            incl += self.rob(root.left.left)+self.rob(root.left.right)
        if root.right:
            incl += self.rob(root.right.left)+self.rob(root.right.right)

        return max(incl, excl)
