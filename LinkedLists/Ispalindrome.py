"""
Given the head of a singly linked list, return true if it is a palindrome.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
"""


def isPalindrome(n):
    lst = [int(n) for n in str(n)]
    l=len(lst)
    if l==0 || l==1:
        return True
    elif len(lst)%2==0:
        for k in range (l)
        #####
    else:
        while (k<=((l-1)/2)):
            if (list[]):
                #####   

for i in range (999, 100, -1):
    for j in range (999,100, -1):
        if isPalindrome(i*j):
            print(i*j)
            break


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
