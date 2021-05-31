class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertNode(root, data):
    if root == None:
        root = Node(data)
    else:
        if root.data > data:
            root.left = insertNode(root.left, data)
        elif root.data < data:
            root.right = insertNode(root.right, data)
    return root


def minValue(root):
    curr = root
    while curr.left is not None:
        curr = curr.left
    return curr.data


def search(root, data):
    if root == None:
        return "Element Not Found   :("
    elif root.data == data:
        return "Element Found"
    elif root.data > data:

        result = search(root.left, data)
    else:
        result = search(root.right, data)

    return result


def delete(root, data):
    if root is None:
        return root
    elif root.data > data:
        root.left = delete(root.left, data)
    elif root.data < data:
        root.right = delete(root.right, data)
    else:
        if root.left == None:
            temp = root.right
            root = None
            return temp
        elif root.right == None:
            temp = root.left
            root = None
            return temp
        else:

            value = minValue(root.right)
            root.data = value
            root.right = delete(root.right, value)
    return root


def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" "),


def preorder(root):
    if root is not None:
        print(root.data, end=" "),
        preorder(root.left)
        preorder(root.right)


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" "),
        inorder(root.right)


def levelOrder(root):
    if root is None:
        return None
    else:
        q = []
        q.append(root)
        while(len(q)):

            temp = q.pop(0)
            print(temp.data, end=" ")
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)


def height(root):
    if root is None:
        return -1
    return 1+max(height(root.left), height(root.right))


def FindMin(root):
    if root is None:
        return
    if root.left is None:
        return root.data

    else:
        return FindMin(root.left)


r = insertNode(None, 15)
r = insertNode(r, 10)
r = insertNode(r, 20)
r = insertNode(r, 5)
r = insertNode(r, 13)
r = insertNode(r, 11)
r = insertNode(r, 14)
r = insertNode(r, 0)
# print(search(r, 20))
# print('InOrder Traversal : ', end=" ")
# inorder(r)
# r = delete(r, 10)
# print('\nInOrder Traversal : ', end=" ")
# inorder(r)
# print('Min in BST :', FindMin(r))
# print('Height of BST  : ', height(r))
# print('Level Order Traversal :', end=" ")
# levelOrder(r)

preorder(r)
print('\n')
postorder(r)
