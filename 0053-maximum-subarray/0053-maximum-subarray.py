class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float("-inf")
        presum = 0

        for n in nums:
            presum += n
            if presum > maxsum:
                maxsum = presum
            
            if presum < 0:
                presum = 0
        
        return maxsum