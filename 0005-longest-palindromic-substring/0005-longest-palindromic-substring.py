class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP with TC n^2 and sc n^2 
        # expanding from i and i +1 takes O(1) sc and n^2 of TC
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]
        # we first build len = 1 and 2 then use them to find other palindromic substrings
        for i in range(n):
            dp[i][i] = True
            ans = [i, i] # set all substrings of len 1 as True 
        
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1] # check for len = 2 
        
        # dp[i][j] = True if s[i][j] and dp[i+1][j-1] is True eg abba. for len > 2
        for diff in range(2, n):
            for i in range(n - diff): # imagine 2 d array where row ind is start of string, col is end of string eg (0, 4) will be s[0:4] inclusive
                j = i + diff # i can't go beyond n-diff-1 as j need to be inbound
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i, j]
        
        i, j = ans
        return s[i: j+1]

