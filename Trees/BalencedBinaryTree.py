'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''
from functools import lru_cache


class TreeNode:
    def __init__(self, data) -> None:

        self.left = None
        self.right = None
        self.data = data


@lru_cache(maxsize=None)
def h(self, root: TreeNode) -> int:
    if not root:
        return 0
    return 1+max(self.h(root.left), self.h(root.right))


def isBalanced(self, root: TreeNode) -> bool:

    if not root:
        return True
    l = self.h(root.left)
    r = self.h(root.right)

    if abs(l-r) > 1:
        return False
    else:

        return self.isBalanced(root.left) and self.isBalanced(root.right)
