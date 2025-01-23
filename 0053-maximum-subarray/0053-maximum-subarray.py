class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum = 0
        maxsum = float("-inf")

        for val in nums:
            presum += val
            if presum > maxsum:
                maxsum = max(maxsum, presum)
            
            if presum < 0:
                presum = 0
        
        return maxsum