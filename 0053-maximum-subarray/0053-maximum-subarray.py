class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum = 0
        maxsum = float("-inf")

        for n in nums:
            presum += n
            if presum > maxsum:
                maxsum = presum
            
            if presum < 0:
                presum = 0
        
        return maxsum