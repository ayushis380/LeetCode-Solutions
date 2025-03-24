class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        length = amount + 1
        dp = [0] * length
        dp[0] = 1 # number of ways to have amount = 0

        for i in range(len(coins) - 1, -1, -1):
            for amt in range(1, amount+1):
                dp[amt] += dp[amt - coins[i]] if coins[i] <= amt else 0
        
        return dp[amount]