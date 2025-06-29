class Solution:
    def rob(self, nums: List[int]) -> int:
#  if we are solving for an array size of 6, we need an array of size 7 to store the results of the subproblems for 0 to 6 houses. The final answer will be stored in dp[6]
        dp = [-1] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0] # dp[i] will represent the optimal solution for the first i houses

        for i in range(2, len(nums) + 1):
            take = dp[i-2] + nums[i-1]
            skip = dp[i-1]
            dp[i] = max(take, skip)
        
        return dp[len(nums)]