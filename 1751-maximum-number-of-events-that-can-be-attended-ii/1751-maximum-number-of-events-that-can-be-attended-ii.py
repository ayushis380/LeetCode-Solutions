class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # like maximum profit in scheduling with an extra k 
        events.sort()
        n = len(events)
        dp = {}
        start_times = [e[0] for e in events] # already sorted

        def dfs(i, count):
            if i >= n or count == 0: # out of bound or no k left
                return 0
            
            if (i, count) in dp:
                return dp[(i, count)]
            
            # not attend
            res = dfs(i+1, count)

            # attend - use binary search
            j = bisect.bisect_right(start_times, events[i][1]) # look for end time in sorted start_times to meet no overlap condition
            res = max(res, events[i][2] + dfs(j, count - 1))

            dp[(i, count)] = res
            return res
        
        return dfs(0, k)
