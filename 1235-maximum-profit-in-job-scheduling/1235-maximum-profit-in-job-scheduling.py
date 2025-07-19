class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    # for each job, there are two options, either to schedule it or not
# schedule the job at index i that ends at endTime[i], then all the jobs which have a startTime before endTime[i] can be discarded.
        jobs = sorted(zip(startTime, endTime, profit))
        dp = {}

        def dfs(i):
            if i == len(jobs):
                return 0
            
            if i in dp:
                return dp[i]
            
            res = dfs(i + 1) # not take i 
            # jobs[i][1] is end time of i => current job
            # in the list of start times for all jobs
            j = bisect.bisect(jobs, (jobs[i][1], -1, -1))
            print("for i ", i, " j is : ", j)
            dp[i] = max(res, jobs[i][2] + dfs(j))
            return dp[i]
        
        dfs(0)
        print(list(dp.items()))
        return dfs(0)