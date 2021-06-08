"""
Given a head of a tree find the preOrder traersal of a tree using Iteration Method

"""


def preOrder(root):
    if root is None:
        return None

    stack = [root]
    while stack:
        temp = stack.pop()
        print(temp.data)
        if temp.right:
            stack.append(temp.right)
        if temp.left:
            stack.append(temp.left)


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.left = Node(6)
    root.left.left = Node(4)
    root.left.left.left = Node(7)
    root.left.left.right = Node(8)
    root.left.left.right.right = Node(9)
    root.left.right = Node(5)
    preOrder(root)
