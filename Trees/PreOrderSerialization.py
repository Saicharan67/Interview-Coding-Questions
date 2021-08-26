'''
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, we record the node's value. If it is a null node, we record using a sentinel value such as '#'.


For example, the above binary tree can be serialized to the string "9,3,4,#,#,1,#,#,2,#,6,#,#", where '#' represents a null node.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal serialization of a binary tree.

It is guaranteed that each comma-separated value in the string must be either an integer or a character '#' representing null pointer.

You may assume that the input format is always valid.

For example, it could never contain two consecutive commas, such as "1,,3".
Note: You are not allowed to reconstruct the tree.

 

Example 1:

Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

'''


class Solution:
    def isValidSerialization(self, p: str) -> bool:
        lis = p.split(',')
        st = []

        for i in lis:
            while st and i == st[-1] == "#":
                st.pop()
                if not st:
                    return False
                st.pop()
            st.append(i)
        print(st)
        return len(st) == 1 and st[0] == "#"
