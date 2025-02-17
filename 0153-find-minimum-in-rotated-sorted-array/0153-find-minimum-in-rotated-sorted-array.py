class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        minv = float("inf")

        while low <= high:
            mid = low + (high - low)//2

            if nums[low] <= nums[mid]:
                minv = min(minv, nums[low])
                low = mid + 1
            else:
                minv = min(minv, nums[mid])
                high = mid - 1
        
        return minv