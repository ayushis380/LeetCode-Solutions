class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        minval = float("inf")
        
        while low <= high:
            mid = (low + high)//2
            if nums[low] <= nums[mid]:
                minval = min(minval, nums[low])
                low = mid + 1
            elif nums[mid] <= nums[high]:
                minval = min(minval, nums[mid])
                high = mid - 1
        
        return minval
