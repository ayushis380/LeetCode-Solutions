class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float("inf")
        start = 0
        total = 0

        for end in range(len(nums)):
            total += nums[end]
            
            while total >= target:
                minlen = min(minlen, end - start + 1)
                total -= nums[start]
                start += 1
            
        return minlen if minlen != float("inf") else 0