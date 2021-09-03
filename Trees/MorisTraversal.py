

def getInorder(root):

    curr = root
    inorder = []
    while curr:
        if curr.left == None:
            inorder.append(curr.data)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right

            if prev.right == None:
                prev.right = curr
                curr = curr.left
            else:
                prev.right = None
                inorder.append(curr.data)
                curr = curr.right

    return inorder


def getPreorder(root):

    curr = root
    preorder = []
    while curr:
        if curr.left == None:
            preorder.append(curr.data)
            curr = curr.right
        else:
            prev = curr.left
            while prev.right and prev.right != curr:
                prev = prev.right

            if prev.right == None:
                prev.right = curr
                preorder.append(curr.data)
                curr = curr.left
            else:
                prev.right = None

                curr = curr.right

    return preorder
