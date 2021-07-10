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


def inorderIteration(root):
    s = []
    curr = root
    while(curr is not None or s):

        if curr is not None:
            s.append(curr)
            curr = curr.left
        else:
            curr = s.pop(-1)
            print(curr.data)
            curr = curr.right
    print()


def preorderIteration(root):
    s = [root]
    while s:
        temp = s.pop()
        print(temp.data)
        if temp.right:
            s.append(temp.right)
        if temp.left:
            s.append(temp.left)


def postorderIterative(root):
    s = [root]
    res = []
    while s:
        temp = s.pop()
        res.append(temp.data)

        if temp.left:
            s.append(temp.left)
        if temp.right:
            s.append(temp.right)
    return res[::-1]


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
        if temp is d_node:
            temp = None
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


def printLeftView(root):
    if root is None:
        return None
    else:
        q = []
        q.append(root)
        while(True):
            try:
                print(q[-1].data)
            except IndexError:
                break
            temp2 = len(q)
            while temp2:
                temp = q.pop(0)
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
                temp2 -= 1


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
    printLeftView(root)
    # print("The tree before the deletion:")
    # inorderIteration(root)
    # key = 8
    # deletion(root, key)
    # print("\nThe tree after the deletion;")
    # levelOrder(root)
