'''
Given a Binary Tree, write a function that returns the size of the largest subtree which is also a Binary Search Tree (BST). If the complete Binary Tree is BST, then return the size of the whole tree.
Examples: 
 

Input: 
      5
    /  \
   2    4
 /  \
1    3

Output: 3 
The following subtree is the 
maximum size BST subtree 
   2  
 /  \
1    3


Input: 
       50
     /    \
  30       60
 /  \     /  \ 
5   20   45    70
              /  \
            65    80
Output: 5
The following subtree is the
maximum size BST subtree 
      60
     /  \ 
   45    70
        /  \
      65    80
'''


def LargestBST(root):
    if not root:
        return [0, float('inf'), -float('inf'), True]
    elif not root.left and not root.right:
        return [1, root.val, root.val, True]

    l = LargestBST(root.left)
    r = LargestBST(root.right)
    res = [0, 0, 0, 0]
    if l[3] and r[3] and l[1] < root.val and root.val > r[2]:

        res[2] = min(r[2], l[2], root.val)
        res[1] = max(r[1], [1], root.val)

        res[0] = 1+l[0]+r[0]
        res[3] = True

        return res
    res[0] = max(l[0], r[0])
    res[3] = False
    return res
