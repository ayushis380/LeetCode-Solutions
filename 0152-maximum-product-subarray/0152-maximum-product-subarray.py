class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxproduct = nums[0] # not 0 as nums contains -ve values as well
        curMin, curMax = 1, 1

        # array has both +ve and -ve numbers
        # curMax and curMin are max and min till that index
        # values can be zero as well which makes curMax and curMin to 0 - a breakpoint but
        # the third value in max and min equation handles it
        
        for val in nums:
            temp = val * curMax # curMax is overwritten 
            curMax = max(val * curMax, val * curMin, val) # [-1, 8] here 8 is picked
            curMin = min(temp, val * curMin, val) # [-1, -8] here -8 should be taken
            
            maxproduct = max(maxproduct, curMax)
        
        return maxproduct