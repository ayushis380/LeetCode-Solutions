class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [(amount + 1)] * (amount + 1) # for every amt we find the number of coins required
        dp[0] = 0

        for i in range(1, amount + 1):
            amt = i
            for cn in coins:
                if amt >= cn:
                    dp[i] = min(dp[i], 1 + dp[amt-cn])

        return dp[amount] if dp[amount] != (amount + 1) else -1
