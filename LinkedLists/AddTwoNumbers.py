"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    dummy = node = ListNode(0)
    carry = 0
    div = 0
    while l1 or l2 or carry:
       # for i in range(3):
        v1, v2 = 0, 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, div = divmod(v1+v2+carry, 10)
        node.next = ListNode(div)
        node = node.next
    return dummy.next
