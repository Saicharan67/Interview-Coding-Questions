'''
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3is the length of the path [4,2,1,3] or [5,2,1,3].
'''


def diameterOfBinaryTree(self, root) -> int:

    self.max_path = 0

    def findMaxPath(node):
        if node == None:
            return 0
        left_path = findMaxPath(node.left)
        rigth_path = findMaxPath(node.right)
        self.max_path = max(left_path+rigth_path, self.max_path)

        return max(left_path, rigth_path)+1

    findMaxPath(root)
    return self.max_path
