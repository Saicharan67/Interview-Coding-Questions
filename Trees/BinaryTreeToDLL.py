'''
Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). 
The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. 
The order of nodes in DLL must be the same as in 
Inorder for the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL. 
'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def BTDll(root):
    if not root:
        return None

    st = []
    prev = None
    head = None

    while root or st:
        if root:
            st.append(root)
            root = root.left
        else:
            root = st.pop()

            curr = root
            if prev == None:
                head = root
            else:
                prev.right = curr
            curr.left = prev
            prev = curr
            root = root.right
    return head


root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
root = BTDll(root)
prev = None
while root:
    print(root.data, end=" ")
    prev = root
    root = root.right
while prev:
    print(prev.data, end=" ")
    prev = prev.left
