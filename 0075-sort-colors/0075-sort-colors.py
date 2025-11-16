class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, curr = 0, 0
        high = len(nums) - 1

        while curr <= high :
            if nums[curr] == 0:
                nums[curr], nums[low] = nums[low], nums[curr]
                low += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr], nums[high] = nums[high], nums[curr]
                high -= 1
            
        