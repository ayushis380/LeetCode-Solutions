class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2

        # find the pivot, the value smaller than its right half
        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # Step 2: If such an element exists, find the next larger element(from end) to swap
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the suffix
        # In the first step we already went till the nums was in increasing order
        # so sorting after ith index will give the next greater value
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        