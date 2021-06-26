'''
Given the root node of the tree return if the tree is BST or not

'''

"The best way we can do this is find the inorder traversal and check if it is sorted"


class Node:
    def __init__(self, data) -> None:
        self.val = data
        self.left = None
        self.right = None

    prev = None

    def inorderIter(self, root):
        if root is None:
            return True
        if not self.inorderIter(root.left):
            return False
        if self.prev != None and self.prev.val >= root.val:
            return False

        prev = root

        if not self.inorderIter(root.right):
            return False

        return True


"Another way is to take min value in right and max value in left of node and check the conditions"


def isbst(root, l=None, r=None):
    if root is None:
        return True
    if l != None and root.val <= l.val:
        return False
    if r != None and root.val >= r.val:
        return False

    return (isbst(root.left, l, root) and isbst(root.right, root, r))
    return isbst(root)
