class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        reach = len(cost)
        dp = [-1] * len(cost)

        def dfs(i):
            if i >= reach:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return dp[i]
        
        dfs(0)
        return min(dp[0], dp[1])