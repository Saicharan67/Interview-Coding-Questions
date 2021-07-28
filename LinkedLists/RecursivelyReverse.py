'''
Given pointer to the head node of a linked list, 
the task is to recursively reverse the linked list. 
We need to reverse the list by changing links between nodes.

'''

def Reverse(prev,curr):
    if curr==None:
        return prev
    
    temp = curr.next
    curr.next = prev
    prev = curr
    curr = temp

    return Reverse(prev,curr)