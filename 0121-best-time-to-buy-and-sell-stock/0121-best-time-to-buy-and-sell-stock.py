class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minp = prices[0]

        for p in prices:
            profit = max(profit, p - minp)
            minp = min(minp, p)
        
        return profit