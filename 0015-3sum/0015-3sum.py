class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.result = []
        length = len(nums)

        for i in range(length):
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(i, nums)
        
        return self.result
    
    def twoSum(self, i, nums):
        low, high = i+1, len(nums) - 1

        while low < high:
            total = nums[i] + nums[low] + nums[high]
            if total == 0:
                self.result.append([nums[low], nums[i], nums[high]])
                low += 1
                high -= 1
                while low < high and nums[low-1] == nums[low]:
                    low += 1
            elif total < 0:
                low += 1
            else:
                high -= 1