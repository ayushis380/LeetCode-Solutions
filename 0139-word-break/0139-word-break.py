class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[length] = True

        for i in range(length - 1, -1, -1):
            for word in wordDict:
                if dp[i]:
                    break
                if (i + len(word) <= length) and s[i: i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
        
        return dp[0]
