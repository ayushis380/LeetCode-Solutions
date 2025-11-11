class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        target = n - 1

        for i in reversed(range(n)):
            if i + nums[i] >= target:
                target = i
        
        return True if target == 0 else False