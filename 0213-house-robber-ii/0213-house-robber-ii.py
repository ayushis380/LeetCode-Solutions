class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        return max(self.helper(nums[:n-1]), self.helper(nums[1:n]), nums[0])

    def helper(self, nums):
        prev2, prev1 = 0, 0

        for i in range(len(nums)):
            tmp = prev2 + nums[i]
            prev2 = prev1
            prev1 = max(prev1, tmp)
        
        return prev1