'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

'''


# Will get TLE in some cases even if we used Memo

# for that we need to add some optimisations lines

# if s[i:k+1]==s[i:k+1][::-1]:
#       tmpans = Palindrome(s,i,k)+1+Palindrome(s,k+1,j)
#       if tmpans<ans:
#           ans=tmpans

def Palindrome(s, i, j):
    if i >= j:
        return 0
    if s[i:j+1] == s[i:j+1][::-1]:
        return 0
    ans = -float('inf')
    for k in range(i, j):
        tmpans = Palindrome(s, i, k)+Palindrome(s, k+1, j)+1
        ans = max(ans, tmpans)
    return ans
