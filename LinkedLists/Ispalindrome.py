"""
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
"""


def isPalindrome(head):
    arr = []
    slow = head
    fast = head

    while fast and fast.next:
        arr.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if slow.val != arr[-1]:
            return False
        else:
            slow = slow.next
            arr.pop()
    return True


"""
Optimised
"""


def isPalindromee(head):

    fast = head
    rev = None
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, head = head, rev, head.next
    if fast:
        head = head.next
    while head:
        if slow.val != rev.next:
            return False
        else:
            slow = slow.next
            rev = rev.next
    return True
