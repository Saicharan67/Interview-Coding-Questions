'''
Given a Binary Tree of size N, find the size of the Largest Independent Set(LIS) in it. A subset of all tree nodes is an independent set if there is no edge between any two nodes of the subset. Your task is to complete the function LISS(), which finds the size of the Largest Independent Set.

For example:
Consider the following binary tree.The LIS is
LIS: [10, 40, 60, 70, 80]
Size: 5.

Example1:

Input:
10 20 30 40 50 N 60 N N 70 80

Output:
5
Explanation: LIS of the above 
tree will be [10,40, 60, 70,80]

'''


def LISS(root):
    if not root:
        return 0
    incl = 1
    excl = LISS(root.left)+LISS(root.right)

    if root.left:
        incl += LISS(root.left.left)+LISS(root.left.right)
    if root.right:
        incl += LISS(root.right.left)+LISS(root.right.right)

    return max(incl, excl)
