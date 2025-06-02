class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # O(nlogn) and O(1) 
        # sorting and check for values from 1 to len(A)
        nums.sort()
        missing = 1 # first possible ans

        for n in nums: # checking for all values in sorted and finding missing
            if missing == n:
                missing += 1
        
        return missing
