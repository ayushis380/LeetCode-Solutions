class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low, high = 0, len(nums)

        while low < high:
            if nums[low] == val:
                nums[low] = nums[high - 1]
                high -= 1
            else:
                low += 1
        
        return high