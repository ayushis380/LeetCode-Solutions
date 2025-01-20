class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    # finding all peaks and valleys as that will give the max profit
    # we can buy on multiple days - thats how its different from I part
        i = 0 
        length = len(prices) - 1
        valley, peak = prices[0], prices[0]
        profit = 0

        while i < length:
            while i < length and prices[i] >= prices[i+1]:
                i += 1
            valley = prices[i]

            while i < length and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]

            profit += (peak - valley)
        
        return profit
