class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
    # 1. find the lowest value L from end of nums - as we need next greater value so this need to swapped with something big
    # 2. swap L with next greater value than it from end - once placed the right values to it can be sorted to find next perm
    # 3. sort from L's index +1 till end - 

        n = len(nums)
        i = n - 2

        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        nums[i+1:] = reversed(nums[i+1:])
        