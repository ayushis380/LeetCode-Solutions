class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el = -1
        count = 0

        for n in nums:
            if count == 0:
                el = n
            
            if n == el:
                count += 1
            else:
                count -= 1
        
        return el