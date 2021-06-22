'''

Given two strings str1 and str2. 
The task is to remove or insert the minimum number of characters 
from/in str1 so as to transform it into str2. It could be possible that the same character needs to be 
removed/deleted from one point of str1 and inserted to some another point.

'''

from longestCmnSubSeq import DpLCS


def MinOperations(s1, s2):
    n = len(s1)
    m = len(s2)
    return n+m-2*DpLCS(s1, s2, n, m)


print(MinOperations('geeksforgeeks', 'geeks'))
