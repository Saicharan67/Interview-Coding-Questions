"""

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

"""


class ListNode:
    def __init__(self, data) -> None:
        self.val = data
        self.next = None


def ReverseNodesK(head, k):

    if not head or not head.next or k == 1:
        return head
    dummy = dummy2 = ListNode(0)
    dummy2.next = head
    l = head
    r = head
    while True:
        count = 0
        while r and count < k:
            r = r.next
            count += 1
        if count == k:
            prev, curr = r, l
            for _ in range(k):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            dummy.next = prev
            dummy = l
            l = r
        else:

            return dummy2.next
