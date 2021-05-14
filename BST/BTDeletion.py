class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def deletion(root,key):

    if root is None:
       return Node(key)
    else:
        if root.left is None:
            root.left = deletion(root.left,key)
        elif root.right is None:
            root.right = deletion(root.right,key)



