class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = nums[0]
        curmax, curmin = nums[0], nums[0]

        for i in range(1, len(nums)):
            val = nums[i]
            
            temp = curmax
            curmax = max(val * curmax, val * curmin, val)
            curmin = min(val * curmin, temp * val, val)

            maxprod = max(maxprod, curmax)
        
        return maxprod
