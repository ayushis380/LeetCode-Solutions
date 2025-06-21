class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # for the time paid painter is occupied, the free painter can complete painting
        # we are targeting for time >= remain as sum of time of paid painter >= remaining 
        # i, time, remain : it can be changed to i, remain - time; time - time >= remain - time => 0 >= remain - time
        # eg if 4 walls at i = 0 then 4 - 1 - time[0] will give remaining, as painted 1 and in time unit 1 free painter painted another
        
        n = len(cost) # walls
        # decision tree will be pick or not pick wall - by paid painter
        dp = {}

        @cache
        def dfs(i, remain):
            if remain <= 0:
                return 0 # found a valid sol
            
            if i == len(cost):
                return float("inf") # not found a sol, a good way to flag it as we take min
            
            if (i, remain) in dp:
                return dp[(i, remain)]
            
            paint = cost[i] + dfs(i+1, remain - 1 - time[i]) # the order in which we paint doenst matter
            skip = dfs(i+1, remain)
            
            dp[(i, remain)] = min(paint, skip)
            return dp[(i, remain)]
        
        return dfs(0, n)
