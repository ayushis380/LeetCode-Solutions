class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0

        for j in range(len(nums)): 
            if nums[i] != nums[j]: # go till they dont match
                i += 1 # increase i to assign the unmatched value at index i, we need all unique values, which is at index i 
                nums[i] = nums[j]
        
        return i + 1 # need length 