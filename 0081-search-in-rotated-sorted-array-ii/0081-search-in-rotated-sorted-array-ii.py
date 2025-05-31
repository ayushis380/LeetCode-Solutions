class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            # If the target is found at mid
            if nums[mid] == target:
                return True

            # If duplicates are present at low, mid, and high
            # cannot determine if the left half or right half is sorted, because they look the same due to duplicates
            # binary search would not make progress (i.e., wouldn't move the pointers), and you could miss the target
            
            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
            # If the left half is sorted
            elif nums[low] <= nums[mid]:
                # Check if target is in the sorted left half
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Otherwise, the right half must be sorted
            else:
                # Check if target is in the sorted right half
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return False

