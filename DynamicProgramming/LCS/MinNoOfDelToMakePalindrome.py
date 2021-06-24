'''
Given a string of size ‘n’. The task is to remove or delete the minimum number of characters from the string so that the resultant string is a palindrome. 

Note: The order of characters should be maintained. 

Examples : 

Input : aebcbda
Output : 2
Remove characters 'e' and 'd'
Resultant string will be 'abcba'
which is a palindromic string

Input : geeksforgeeks
Output : 8

'''
from LongestPalindromicSubSequence import LongestPalindrom


def CountDeletions(s):
    return len(s)-LongestPalindrom(s)


print(CountDeletions('agbcba'))
