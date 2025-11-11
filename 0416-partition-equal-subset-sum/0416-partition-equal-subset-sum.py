class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        dp = set([0]) # sum possible
        target = total//2

        for i in range(len(nums)):
            tdp = set()
            for v in dp:
                sumNum = v + nums[i]
                if sumNum == target:
                    return True
                
                tdp.add(v)
                tdp.add(sumNum)

            dp = tdp
        
        return False

                
