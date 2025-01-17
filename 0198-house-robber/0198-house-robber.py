class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = -1, nums[0]
        
        for i in range(1, len(nums)):
            cur = nums[i]
            if i > 1: # at i = 0 prev2 = -1
                cur += prev2
            
            cur = max(cur, prev1)
            prev2 = prev1
            prev1 = cur
        
        return prev1

        
