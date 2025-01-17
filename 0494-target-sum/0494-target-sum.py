class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # DFS with memoization
        # TC and SC = O(n * m), n is len of nums and m is sum(nums) as cur_sum goes through all sum combinations of nums, cur_sum can be greater than target

        dp = {} # map of (i, cur_sum) : number of ways 

        def dfs(i, cur_sum):
            if (i, cur_sum) in dp: # this memoization helps avoid TLE
                return dp[(i, cur_sum)]
            
            if i == len(nums):
                return 1 if cur_sum == target else 0
            
            dp[(i, cur_sum)] = (
                dfs(i + 1, cur_sum + nums[i]) +
                dfs(i + 1, cur_sum - nums[i])
            )
            return dp[(i, cur_sum)]
        
        return dfs(0, 0)