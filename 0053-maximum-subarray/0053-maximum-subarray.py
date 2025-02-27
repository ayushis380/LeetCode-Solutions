class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float("-inf")
        presum = 0

        for i in range(len(nums)):
            presum += nums[i]
            if presum > maxsum:
                maxsum = presum
            
            if presum < 0:
                presum = 0
        return maxsum
            
