class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # move target closer
        target = len(nums) - 1

        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= target: # at that index and its step value
                target = i # move target closer to start index
        
        return True if target == 0 else False