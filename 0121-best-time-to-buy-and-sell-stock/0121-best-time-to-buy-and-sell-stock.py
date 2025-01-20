class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minprice = prices[0]

        for prc in prices:
            minprice = min(minprice, prc)
            profit = max(profit, prc - minprice)
        
        return profit