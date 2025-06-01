class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i, length = 0, len(prices) - 1
        valley, peak = prices[0], prices[0] # old peaks and valleys to start with 

        while i < length: # when i >= len(prices)- 1 it exists, meaning we have taken last value in consideration
        # values were decreasing but then increased which made if cond exit - so got a valley 
            while i < length and prices[i] >= prices[i+1]: 
                i += 1
            valley = prices[i]

        # values were increasing but then decreased which made if cond exit - so got a peak 
            while i < length and prices[i] <= prices[i+1]:
                i += 1
            peak = prices[i]

            profit += peak - valley
        
        return profit

    # below code causes TLE
# At the end of the array, once i == length - 1, both while loops do not execute because the condition i + 1 < length fails, So the loop gets stuck at the last index

        # profit = 0
        # i, length = 0, len(prices)
        # valley, peak = prices[0], prices[0] # old peaks and valleys to start with 

        # while i < length:
        # # values were decreasing but then increased which made if cond exit - so got a valley 
        #     while i + 1 < length and prices[i] >= prices[i+1]: 
        #         i += 1
        #     valley = prices[i]

        # # values were increasing but then decreased which made if cond exit - so got a peak 
        #     while i + 1 < length and prices[i] <= prices[i+1]:
        #         i += 1
        #     peak = prices[i]

        #     profit += peak - valley
        
        # return profit