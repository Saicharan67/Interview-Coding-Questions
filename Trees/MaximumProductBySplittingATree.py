'''
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)

'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        def su(root):
            if root is None:
                return 0
            l = su(root.left)
            r = su(root.right)

            root.val += l+r

            return root.val
        su(root)
        susu = root.val
        print(root.val)

        def recurr(root, maxi):

            if not root:
                return 0

            if root.left:
                l = root.left.val
                temp = (susu-l)*l
                if temp > maxi:
                    maxi = temp
            if root.right:
                l = root.right.val
                temp = (susu-l)*l
                if temp > maxi:
                    maxi = temp

            t = recurr(root.left, maxi)
            p = recurr(root.right, maxi)

            maxi = max(maxi, t, p)

            return maxi
        return recurr(root, 0) % 1000000007
