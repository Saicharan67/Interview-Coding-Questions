"""
Given the heads of two singly linked-lists headA and headB, 
return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

"""


def getIntersectionNode(headA, headB):
    s = set()
    while headA:
        s.add(headA)
        headA = headA.next
    while headB:
        if headB in s:
            return headB
        headB = headB.next
    return None
