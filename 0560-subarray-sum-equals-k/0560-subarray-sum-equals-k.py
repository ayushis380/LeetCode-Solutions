class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumMap = {0 : 1}
        presum = 0
        count = 0

        for n in nums:
            presum += n

            if presum - k in sumMap:
                count += sumMap[presum - k]
            
            sumMap[presum] = sumMap.get(presum, 0) + 1
        
        return count
