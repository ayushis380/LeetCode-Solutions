class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # buy at i : explore for i + 1 
    # sell at i : explore i + 2 (need 1 day cooldown)
    # cooldown: means skip i and maybe buy at i +1: always an option for both

        dp = {} # (i, buying) : max_profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i+1, buying)

            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        
        return dfs(0, True)

