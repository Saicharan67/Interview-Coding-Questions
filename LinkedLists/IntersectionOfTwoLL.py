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

# O(1) space


def GetIntersection(ha, hb):
    la = 1
    lb = 1
    ta = ha
    tb = hb
    while ta:
        ta = ta.next
        la += 1
    while tb:
        tb = tb.next
        lb += 1
    if la > lb:
        while la != lb:
            ha = ha.next
            la -= 1
    else:
        while la != lb:
            hb = hb.next
            lb = -1
    while ha != hb:
        ha = ha.next
        hb = hb.next
    return ha
