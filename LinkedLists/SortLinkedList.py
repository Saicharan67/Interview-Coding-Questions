'''
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def Merge(self, h1: ListNode, h2: ListNode) -> ListNode:
    node = dummy = ListNode(0)
    while h1 and h2:
        if h1.val < h2.val:
            node.next = h1
            h1 = h1.next
        else:
            node.next = h2
            h2 = h2.next
        node = node.next

    node.next = h1 or h2

    return dummy.next


def sortList(self, head: ListNode) -> ListNode:

    if not head or not head.next:
        return head
    prev = None
    sl = head
    ft = head
    while ft and ft.next:
        prev = sl
        sl = sl.next
        ft = ft.next.next
    prev.next = None
    x = self.sortList(head)
    y = self.sortList(sl)

    return self.Merge(x, y)
