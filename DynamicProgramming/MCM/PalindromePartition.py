'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

'''
ans = -float('inf')


def Palindrome(s, i, j):
    if i >= j:
        return 0
    if s[i:j+1] == s[i:j+1][::-1]:
        return 0

    for k in range(i, j):
        tmpans = Palindrome(s, i, k)+Palindrome(s, k+1, j)+1
        ans = max(ans, tmpans)
    return ans
