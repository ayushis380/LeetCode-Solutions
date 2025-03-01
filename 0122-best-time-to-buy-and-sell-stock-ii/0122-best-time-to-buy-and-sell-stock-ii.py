class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, i = 0, 0
        valley = peak = prices[0]

        while i < len(prices) -1:
            # find valleys
            while i < len(prices) -1 and prices[i] >= prices[i+1]:
                i += 1
            valley = i

            # find peaks
            while i < len(prices) -1 and prices[i] <= prices[i+1]:
                i += 1
            peak = i

            profit += prices[peak] - prices[valley]
        
        return profit
