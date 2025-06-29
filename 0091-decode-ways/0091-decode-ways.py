class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [-1] * len(s)

        def dfs(i):
            if i == len(s):
                return 1 # its like dp[len(s)] = 1
            
            if s[i] == '0' or i > len(s):
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = dfs(i+1)
            if i + 1 < len(s):
                if s[i] == '1' or (s[i] == "2" and s[i+1] in "0123456"):
                    dp[i] += dfs(i+2)
            
            return dp[i]
        
        dfs(0)
        print(dp)
        return dp[0]