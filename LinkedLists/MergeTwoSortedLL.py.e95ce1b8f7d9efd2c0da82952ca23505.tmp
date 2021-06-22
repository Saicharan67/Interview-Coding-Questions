"""

Merge two sorted linked lists and return it as a sorted list. 
The list should be made by splicing together the nodes of the first two lists.

"""


class ListNode:
    def __init__(self, data) -> None:
        self.val = data
        self.next = None


def mergeTwoLists(ll1: ListNode, ll2: ListNode) -> ListNode:
    if not ll1 or not ll2:
        return ll1 or ll2
    if ll2.val < ll1.val:
        ll1, ll2 = ll2, ll1
    x = ll1
    y = ll2
    l2 = ListNode(0)
    tmp = ll1
    while x and y:
        if x.val <= y.val:
            l2.next = x
            x = x.next

        else:
            l2.next = y
            y = y.next
        l2 = l2.next
    l2.next = x or y
    return tmp
