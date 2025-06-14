class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
# In 0/1 Knapsack-type problems, where each number can be used at most once, we must go backwards through the dp array when processing each number.
# If we went forward, we would accidentally reuse the same number multiple times in the same iteration, violating the "subsequence" (no repetition) constraint.

        dp = [float("-inf") for _ in range(target+1)]
        dp[0] = 0 # 0 ways to make sum = 0

        for n in nums:
            for t in range(target, n - 1, -1):
        # need to have already formed the sum t - n
        # dp[t - n] != -inf), then we can form sum t using one more number ⇒ dp[t - num] + 1
        # given n, what can we form? its t - n = if present then use it 
        # eg n = 2, t = 3 then we are looking for dp[3-2] = dp[1] - number of ways dp[1] was formed
                dp[t] = max(dp[t], dp[t-n] + 1) # +1 is we can include n now as we found t -n
        
        return dp[target] if dp[target] != float('-inf') else -1

