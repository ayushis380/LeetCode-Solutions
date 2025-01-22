class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.output = []

        for i in range(len(nums)):
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(i, nums)
        
        return self.output
        
    
    def twoSum(self, i, nums):
        val = nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = val + nums[left] + nums[right]
            
            if total == 0:
                self.output.append([val, nums[left], nums[right]])
                left += 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
            elif total > 0:
                right -= 1
            else:
                left += 1
        

