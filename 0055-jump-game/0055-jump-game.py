class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        target = length - 1 # if nums = 0 at last index thats ok as its the last index and we need to reach the last index

        for i in range(length - 1, -1, -1):
            if i + nums[i] >= target: # index + step value should be able to reach the target
                target = i
        
        return True if target == 0 else False