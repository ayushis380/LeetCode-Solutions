class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)

        for i in range(1, len(nums)):
            ndp = set()
            for val in dp:
                partsum = val + nums[i]
                if partsum == sum(nums)// 2:
                    return True
                ndp.add(val + nums[i])
                ndp.add(val)
            
            dp = ndp
        
        return False

