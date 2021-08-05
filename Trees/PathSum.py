'''
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where each path's sum equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]

'''


class Solution:

    def pathSum(self, root, t: int):
        if not root:
            return []
        if not root.left and not root.right and t == root.val:
            return [[root.val]]
        tmp = self.pathSum(root.left, t-root.val) + \
            self.pathSum(root.right, t-root.val)
        return [[root.val]+i for i in tmp]
