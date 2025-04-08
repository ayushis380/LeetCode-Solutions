class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[length] = True

        for i in range(length - 1, -1, -1):
            for wrd in wordDict:
                if i + len(wrd) <= length and s[i: i+len(wrd)] == wrd:
                    dp[i] = dp[i+len(wrd)]
                
                if dp[i]:
                    break
        print(dp)
        return dp[0]
