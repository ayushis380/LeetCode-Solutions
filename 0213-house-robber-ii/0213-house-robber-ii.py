class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(self.calculate(nums[0:n-1]), self.calculate(nums[1:n]), nums[0])
    
    def calculate(self, nums):
        prev2, prev1 = 0, 0

        for i in range(len(nums)):
            temp = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = temp
        
        return prev1
