import itertools


class Node:
    def __init__(self, data) -> None:

        self.data = data
        self.left = None
        self.right = None


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" "),


def CreateTree(preorder):
    if not preorder:
        return None
    else:
        root = Node(preorder[0])
        left = list(itertools.takewhile(lambda x: x < root.data, preorder[1:]))
        right = preorder[len(left) + 1:]

        root.left = CreateTree(left)
        root.right = CreateTree(right)
    return root


if __name__ == '__main__':
    root = CreateTree([15, 10, 5, 0, 13, 11, 14, 20])
    postorder(root)
