class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True # end of s

        for i in reversed(range(n)):
            for wrd in wordDict:
                wlen = len(wrd)
                
                if dp[i]:
                    continue
                if i + wlen <= n and s[i: i + wlen] == wrd:
                    if dp[i + wlen] == True:
                        dp[i] = True
        
        return dp[0]
                