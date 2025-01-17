class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * (len(nums))

        for i in range(len(nums) - 1, -1 , -1): # last element can only have 1 as answer as its just 1 number
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]: # comparing at higher indexes than i, true only when small
                    dp[i] = max(dp[i], 1 + dp[j]) # adding 1 : means picking this ith index value with dp[j] 
        
        return max(dp)