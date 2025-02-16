class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = prices[0]

        for p in prices:
            minprice = min(minprice, p)
            profit = max(profit, p - minprice)
        
        return profit

