'''
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
 

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0 for _ in range(len(word1)+1)]for _ in range(len(word2)+1)]
        
        for i in range(1,len(word1)+1):
            dp[0][i]=i
        for j in range(1,len(word2)+1):
            dp[j][0]=j
        
        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                
              
                if word1[j-1]==word2[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                     dp[i][j] = 1 + min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
        
        return dp[len(word2)][len(word1)]