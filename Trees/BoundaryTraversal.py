'''
Given a Binary Tree, find its Boundary Traversal. The traversal should be in the following order: 

Left boundary nodes: defined as the path from the root to the left-most node ie- the leaf node you could reach when you always travel preferring the left subtree over the right subtree. 
Leaf nodes: All the leaf nodes except for the ones that are part of left or right boundary.
Reverse right boundary nodes: defined as the path from the right-most node to the root. The right-most node is the leaf node you could reach when you always travel preferring the right subtree over the left subtree. Exclude the root from this as it was already included in the traversal of left boundary nodes.

'''


def LeftBoundary(root):
    res = []

    temp = root.left

    while temp:
        if temp.left or temp.right:
            res.append(temp.data)
        if temp.left:
            temp = temp.left
        else:
            temp = temp.right
    return res


def rightBoundary(root):
    res = []
    temp = root.right

    while temp:
        if temp.left or temp.right:
            res.append(temp.data)
        if temp.right:
            temp = temp.right
        else:
            temp = temp.left

    return res[::-1]


def leafs(root):
    if not root.left and not root.right:
        return [root.data]
    a = []
    b = []
    if root.left:
        a = leafs(root.left)
    if root.right:
        b = leafs(root.right)

    return a+b


def main(root):
    res = []
    if not root:
        return root
    res.append(root.data)
    res.extend(LeftBoundary(root))
    res.extend(leafs(root))
    res.extend(rightBoundary(root))

    return res
