class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * len(cost)

        def dfs(i):
            if i >= len(cost):
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            res = min(dfs(i+1), dfs(i+2)) + cost[i]
            dp[i] = res
            return res
        
        dfs(0)
        return min(dp[0], dp[1])