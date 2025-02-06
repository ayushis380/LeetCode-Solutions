class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # for O(1) look up, dont over write
        maxcount = 0

        for n in nums_set:
            count = 0
            
            if n + 1 not in nums_set:
                while n in nums_set:
                    count += 1
                    n -= 1
            
            maxcount = max(maxcount, count)
        
        return maxcount