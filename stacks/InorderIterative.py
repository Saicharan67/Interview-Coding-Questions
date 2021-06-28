'''
Print the Inorder traversal of binary tree in Iterative Method


        10
     /      \ 
    20       30 
  /    \    /
 40    60  50
Output: 40 20 60 10 50 30

'''


class Node:
    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data


def InorderIterative(root):
    st = []
    left = root
    while root or st:
        while root:
            st.append(root)
            root = root.left

        temp = st.pop()
        print(temp.data)
        root = temp.right


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(50)
    root.left.left = Node(40)

    root.left.right = Node(60)
    InorderIterative(root)
