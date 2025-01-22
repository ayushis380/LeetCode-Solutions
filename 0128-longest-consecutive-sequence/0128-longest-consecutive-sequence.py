class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        maxlen = 0

        for val in nums:
            count = 0

            if val + 1 not in nums:
                while val in nums:
                    count += 1
                    val -= 1
            
            maxlen = max(maxlen, count)
        
        return maxlen
