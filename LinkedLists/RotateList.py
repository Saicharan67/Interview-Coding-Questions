'''

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head

        l = 1
        temp = head

        while temp.next:
            l += 1
            temp = temp.next
        temp.next = head

        k = k % l
        k = l-k
        prev = None
        curr = head
        while k > 0:
            prev = curr
            curr = curr.next
            k -= 1
        prev.next = None
        return curr
