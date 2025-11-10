class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        return max(self.check(nums[:n-1]), self.check(nums[1:n]), nums[0])
    
    def check(self, arr):
        prev1, prev2 = 0, 0
        # 0 0 2 = 0 2 3 2 = 2 3 4
        for i in range(len(arr)):
            tmp = prev2
            prev2 = max(prev2, arr[i] + prev1)
            prev1 = tmp
        
        return prev2