class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, n//2
        count = 0

# greedily match as many such pairs as possible, without revisiting already paired elements
# You risk using up large values on elements that could’ve been paired with smaller large values
# Greedy from the middle ensures earlier access to the “just large enough” element, preserving the larger values for later pairings if needed.
        while i < n//2 and j < n:
            if nums[i] < nums[j]:
                count += 1
                i += 1 # only increase when matched
            j += 1
            
        return n - 2 * count
