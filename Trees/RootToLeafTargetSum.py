'''
Given a binary tree and a number, return true if the tree has a 
root-to-leaf path such that adding up all the values along the 
path equals the given number. Return false if no such path can be found. 
 
'''


def targetsum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        if root.val == target:
            return True
        else:
            return False

    return targetsum(root.left, target-root.val) or targetsum(root.right, target-root.val)
