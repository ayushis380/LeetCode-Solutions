class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # bottom up
        dp = [float("inf")] * (len(days) + 1)
        dp[len(days)] = 0 # base case, imagine when j covers all index till end then it would be at len(days)
        # 7 8 20 = days, if at day = 7 we buy 30 day ticket then j would go till end of days

        for i in reversed(range(len(days))): # go in reverse to calculate the mincost for each day
            j = i # for each day, we pick the min from below loop
            
            for cost, duration in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + duration: 
                    j += 1
                
                dp[i] = min(dp[i], cost + dp[j]) # dp[j] is already calculated
        
        return dp[0]