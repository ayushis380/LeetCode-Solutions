class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el = nums[0]
        count = 0

        for val in nums:
            if count == 0:
                el = val
            if val == el:
                count += 1
            else:
                count -= 1
        
        return el