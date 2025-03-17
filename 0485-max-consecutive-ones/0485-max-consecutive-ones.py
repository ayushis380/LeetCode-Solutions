class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        presum = 0
        maxones = 0

        for val in nums:
            if val == 1:
                presum += 1
                maxones = max(maxones, presum)
            else:
                presum = 0
        
        return maxones
