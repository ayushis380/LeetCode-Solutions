class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        self.result = []
        nums.sort()

        for i in range(n):
            if i == 0 or nums[i-1] != nums[i]:
                self.twosum(nums, i)
        
        return self.result
    
    def twosum(self, nums, i):
        low, high = i + 1, len(nums) - 1
        val = nums[i]
        
        while low < high:
            total = val + nums[low] + nums[high]
            if total == 0:
                self.result.append([val, nums[low], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low-1] == nums[low]:
                    low += 1
            elif total > 0:
                high -= 1
            else:
                low += 1
            
