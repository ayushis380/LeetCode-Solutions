class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length = len(nums)
        i = length - 2

        while i >= 0 and nums[i] >= nums[i+1]: # find the smallest number from end
            i -= 1
        
        j = length - 1
        # from end find just bigger num than nums[i] 
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = sorted(nums[i+1:])


        