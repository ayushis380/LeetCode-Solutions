class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 0... n-1 indexes
        # 1 ...n values - only these matter
        i = 0

        while i < n:
            correct_pos = nums[i] - 1 # eg 1 then it should have been placed at index 0
            
            #  1 2 15 3 - bring 3 to index 2
            if 1 <= nums[i] <= n and nums[correct_pos] != nums[i]: # bring values to correct pos
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i] # might need multiple swaps to place values at correct index- so i is not increased
            else:
                i += 1 # only increase when element is at correct index

        for i in range(n):
            if nums[i] != i + 1: # i in index so + 1
                return i + 1

        return n + 1                
