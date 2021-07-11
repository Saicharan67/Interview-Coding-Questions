def lca(root, p, q):
    if root is p or root is q:
        return root
    if not root:
        return None

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right
