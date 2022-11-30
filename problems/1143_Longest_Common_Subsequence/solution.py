'''
    1143. Longest Common Subsequence
'''

class Solution:
    # Accepted	355 ms	21.9 MB
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0]*(len(text1) + 1) for _ in range(len(text2) + 1)]
              
              
        for i in range(len(text2) - 1, -1, -1):
            for j in range(len(text1) - 1, -1, -1):
                if text1[j] == text2[i]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                    
        
        return dp[i][j]
        
        

                
            
            

#.        l            
# text1 = abcde
# text2 = ace
#
# dp = [
#      a  b. c. d. e  -
#   a [3, 2, 2, 1, 1, 0],
#   c [2, 2, 2, 1, 1, 0],
#   e [1, 1, 1, 1, 1, 0],
#   - [0, 0, 0, 0, 0, 0]
# ]
#
#
#
#