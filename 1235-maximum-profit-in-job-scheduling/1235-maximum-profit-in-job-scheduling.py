class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    # think of the subproblem : include or not include the job and when reach the end, return 0
    # sort it on basis of start time, so its easier to check which job has started and look for no overlaps
        intervals = sorted(zip(startTime, endTime, profit)) # dont lose the order
        cache = {} # memoiz

        def dfs(i):
            if i == len(intervals):
                return 0
            
            if i in cache:
                return cache[i]
            
            # dont include
            res = dfs(i + 1) # go to next index

            # include
            # j = i + 1 # looking for next valid index j with index i

            # below while loop causes N^2 complexity as its runnign under dfs
            # while j < len(intervals):
            #     if intervals[i][1] <= intervals[j][0]: # end time of i <= start time of j - so valid j value found
            #         break
            #     j += 1 # if not found then increase j

            # looking for a start time that is greater than equal to current index end time - run a binary search as values are sorted
            # placed at start time position - looking for intervals[i][1]
            j = bisect.bisect(intervals, (intervals[i][1], -1, -1)) # intervals is a tuple so need same format
            
            cache[i] = res = max(res, intervals[i][2] + dfs(j)) # include i profit and call dfs on j (as j is the next valid index)
            return res
        
        return dfs(0)