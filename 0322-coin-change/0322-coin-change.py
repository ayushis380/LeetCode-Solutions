class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        length = amount + 1 # we take to simplify using it in range
        dp = [(amount + 1)] * (length)
        dp[0] = 0

        for amt in range(1, length):
            for cn in coins:
                if cn == amt: # found the exact coin for the amt
                    dp[amt] = 1
                elif amt > cn:
                    dp[amt] = min(dp[amt], 1 + dp[amt-cn]) # min is required as there are multiple ways to form an amount but we need to consider the minimum way
        
        return dp[length-1] if dp[length-1] != (amount + 1) else -1 # we couldnt achieve amount
        