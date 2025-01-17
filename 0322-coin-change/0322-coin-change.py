class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        length = amount +1
        dp = [(amount+1)] * (length)
        dp[0] = 0

        for amt in range(1, length):
            for cn in coins:
                if amt == cn:
                    dp[amt] = 1
                elif amt > cn:
                    dp[amt] = min(dp[amt], 1 + dp[amt - cn])
        
        return dp[length - 1] if dp[length - 1] != amount + 1 else -1
