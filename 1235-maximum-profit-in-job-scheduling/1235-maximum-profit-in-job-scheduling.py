class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)
        dp = {}

        def dfs(i):
            if i >= n:
                return 0
            
            if i in dp:
                return dp[i]

            # not pick
            res = dfs(i+1)

            # pick i and pick j - the job whose start time is greater than equal to i's end time, so used bisect.bisect
            # we are always returning the max profit seen so far
            # this ensures whenever we pick jth job, it will be the job with max profit
            # as there can be multiple jobs that start after i, but we need to take the one with max profit
            j = bisect.bisect(jobs, (jobs[i][1], -1, -1))
            res = max(res, jobs[i][2] + dfs(j))

            dp[i] = res
            return res
        
        return dfs(0)
