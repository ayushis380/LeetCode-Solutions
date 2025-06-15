class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {len(days) : 0} # index - > min cost for that index

        def dfs(i):
            if i in dp:
                return dp[i]
            
            dp[i] = float("inf")
            j = i

            for cost, duration in zip(costs, [1, 7, 30]):
                print(j)
                while j < len(days) and days[j] < duration + days[i]: # cover the duration for different tickets
                    j += 1

                dp[i] = min(dp[i], cost + dfs(j))
                print("end")
            
            return dp[i]
        
        return dfs(0)
 