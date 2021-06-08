"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)

"""


def swapPairs(head):
    if not head or not head.next:
        return head
    s = head
    f = head.next
    prev = None
    while f.next and f.next.next:
        s.next = f.next
        f.next = s
        if prev == None:
            head = f
        if prev:
            prev.next = f
        f, s = s, f
        prev = f
        s = f.next
        f = s.next
    return head
