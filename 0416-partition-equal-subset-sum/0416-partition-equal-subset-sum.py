class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        dp = set([0])

        for val in nums:
            new_dp = set()

            for s in dp:
                if s + val == total//2:
                    return True
                
                new_dp.add(s + val)
                new_dp.add(s)
            
            dp = new_dp
        
        return False
