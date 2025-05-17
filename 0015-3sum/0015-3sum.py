class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []

        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                if nums[i] <= 0: # already sorted, so values ahead of index i will be bigger than 0 
                    self.twoSum(nums, i)
        
        return self.result
    
    def twoSum(self, nums, i):
        val = nums[i]
        low = i + 1
        high = len(nums) - 1

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
        

