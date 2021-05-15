class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" "),
        inorder(root.right)


def insertion(root, key):

    if root is None:
        root = Node(key)
        return

    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        if temp.left is None:
            temp.left = Node(key)
            break
        else:
            q.append(temp.left)
        if temp.right is None:
            temp.right = Node(key)
            break
        else:
            q.append(temp.right)


def deleteDeepestNode(root, d_node):
    q = []
    q.append(root)
    while(len(q)):
        temp = q.pop(0)
        print(temp.data)
        if temp is d_node:
            print(temp)
            temp = None
            print(temp)
            return
        if temp.right:
            if temp.right is d_node:
                temp.right = None
                return
            else:
                q.append(temp.right)
        if temp.left:
            if temp.left is d_node:
                temp.left = None
                return
            else:
                q.append(temp.left)
        # if temp.left:
        #     q.append(temp.left)
        # if temp.right:
        #     q.append(temp.right)


def deletion(root, key):

    if root is None:
        return root

    if root.left is None and root.right is None:
        if root.data == key:
            return None
        else:
            return root
    q = []
    q.append(root)
    key_node = None
    while(len(q)):
        temp = q.pop(0)
        if temp.data == key:
            key_node = temp
        if temp.left:
            q.append(temp.left)
        if temp.right:
            q.append(temp.right)

    if key_node:
        x = temp.data
        deleteDeepestNode(root, temp)
        key_node.data = x


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


if __name__ == '__main__':
    root = Node(10)
    insertion(root, 11)
    insertion(root, 7)
    insertion(root, 12)
    insertion(root, 9)
    insertion(root, 15)
    insertion(root, 8)
    print("The tree before the deletion:")
    levelOrder(root)
    key = 8
    deletion(root, key)
    print("\nThe tree after the deletion;")
    levelOrder(root)
