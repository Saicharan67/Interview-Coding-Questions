'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
'''


maxi = -float('inf')


def maxPathSum(self, root) -> int:

    def Maxpath(root):
        if not root:
            return 0

        l = Maxpath(root.left)
        r = Maxpath(root.right)

        temp = max(max(l, r)+root.val, 0)
        self.maxi = max(self.maxi, l+r+root.val)

        return temp
    Maxpath(root)

    return (self.maxi)
