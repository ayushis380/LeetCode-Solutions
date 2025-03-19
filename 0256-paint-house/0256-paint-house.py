class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
    # 2 D Dp - houses on rows, colors on cols (red, blue, green)
    # bottom up - at each row we have the min cost of painting till that house (row) using different colors
    # at row = 2, color = 1 (blue) means taking costs[2][1] and min cost of red and green from row = 1
    # here we have the sub problems that can be used again
    # eg We only need to calculate the cost of painting the 2nd house red once

        n = len(costs)
        dp = [[0] * 3 for i in range(n)]

        for c in range(3): # first row - first house 
            dp[0][c] = costs[0][c]
        
        for i in range(1, n): # start from second house
            for c in range(3): # c+1 and c+2 for other colors, %3 to keep within bound
                dp[i][c] = costs[i][c] + min(dp[i-1][(c+1)%3], dp[i-1][(c+2)%3])
        
        return min(dp[n-1]) # min from last house - last row - holds cost to paint all the colors
    

