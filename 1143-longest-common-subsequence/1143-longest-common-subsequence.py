class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # one extra row and col for easy comparison
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        # start from end in reverse 
        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1] # if chars match that means we should check for the diagonal cell, as that will be the next char in text1 and next char in text2
                else:
                    dp[i][j] = max(dp[i+1][j] , dp[i][j+1]) # looking for the next sub problem solution
        
        return dp[0][0]