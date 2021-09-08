'''

Given two lists sorted in increasing order, create a new list representing the intersection of the two lists. The new list should be made with its own memory — the original lists should not be changed.

Example 1:

Input:
L1 = 1->2->3->4->6
L2 = 2->4->6->8
Output: 2 4 6
Explanation: For the given first two
linked list, 2, 4 and 6 are the elements
in the intersection.

'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findIntersection(head1, head2):
    head = dummy = Node(0)
    while head1 and head2:

        if head1.data == head2.data:
            head.next = Node(head1.data)
            head = head.next
            head1 = head1.next
        elif head1.data > head2.data:
            head2 = head2.next
        else:
            head1 = head1.next

    return dummy.next
