'''

Given a Linked List of size N, where every node represents a sub-linked-list and contains two pointers:
(i) a next pointer to the next node,
(ii) a bottom pointer to a linked list where this node is head.
Each of the sub-linked-list is in sorted order.
Flatten the Link List such that all the nodes appear in a single level while maintaining the sorted order. 
Note: The flattened list will be printed using the bottom pointer instead of next pointer.

 

Example 1:

Input:
5 -> 10 -> 19 -> 28
|     |     |     | 
7     20    22   35
|           |     | 
8          50    40
|                 | 
30               45
Output:  5-> 7-> 8- > 10 -> 19-> 20->
22-> 28-> 30-> 35-> 40-> 45-> 50.
Explanation:
The resultant linked lists has every 
node in a single level.

'''


class ListNode:
    def __init__(self, data) -> None:
        self.val = data
        self.next = None


def mergetwolists(l1, l2):
    dummy = node = ListNode(0)
    while l1 and l2:
        if l1.data < l2.data:
            node.bottom = l1
            l1 = l1.bottom
        else:
            node.bottom = l2
            l2 = l2.bottom
        node = node.bottom
    node.bottom = l1 or l2
    return dummy.bottom


def Flatten(root):
    if not root or not root.next:
        return root

    rootNext = Flatten(root.next)

    TempRoot = mergetwolists(root, rootNext)

    return TempRoot
