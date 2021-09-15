'''
Given a Binary Search Tree (BST), modify it so that all greater values in the given BST are added to every node. For example, consider the following BST.

              50
           /      \
         30        70
        /   \      /  \
      20    40    60   80 

The above tree should be modified to following 

              260
           /      \
         330        150
        /   \       /  \
      350   300    210   80

'''

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def modify(root):
    p = [0]

    def recurr(root):
        if root:
            recurr(root.right)
            root.data += p[-1]
            p[-1] = root.data
            recurr(root.left)

    recurr(root)
    return root
