class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        result = 0 # all single chars are palindrome

        for i in range(n):
            dp[i][i] = True
            result += 1
        
        for i in range(n-1): # len = 2 check
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                result += 1
            
        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff #substring length difference diff, you’re checking substrings of length diff + 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    result += 1
        
        return result