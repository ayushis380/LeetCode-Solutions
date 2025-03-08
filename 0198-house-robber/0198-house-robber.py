class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0
        
        for i in range(len(nums)):
            temp = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = temp
        
        return prev1
