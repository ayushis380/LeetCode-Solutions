class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[length] = True # last index of s + 1

        for i in range(length -1, -1, -1): # checking from last
            for word in wordDict: # comparing each word 
                if (i + len(word)) <= length and s[i : i + len(word)] == word: # <= as dp[length] is also set
            # if higher indexes are true that means it can be used to evaluate lower indexes
                    dp[i] = dp[i + len(word)] 
                
                if dp[i]: # if true
                    break
        
        return dp[0]
