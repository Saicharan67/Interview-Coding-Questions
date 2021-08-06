'''
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

 

Example 1:



Input: root = [1,null,3,2,4,null,5,6]
Output: [[1],[3,2,4],[5,6]]
Example 2:



Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
'''


from collections import defaultdict


class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        st = [root]
        res = []
        temp = [root.val]
        while st:

            res.append(temp)
            l1 = len(st)
            temp = []
            while l1:
                node = st.pop(0)
                if node.children:
                    for child in node.children:
                        if child:
                            st.append(child)
                            temp.append(child.val)
                l1 -= 1
        return res


class Solution:
    def levelOrder(self, root):
        dt = defaultdict(list)

        def recurr(root, row):
            if not root:
                return
            dt[row].append(root.val)

            if root.children:
                for x in root.children:
                    recurr(x, row+1)
        recurr(root, 0)
        res = []
        for key in dt.keys():
            res.append(dt[key])
        return res
