class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = count = 0
        sumarr = defaultdict(int)
        sumarr[0] = 1

        for i, val in enumerate(nums):
            presum += val

            if presum - k in sumarr:
                count += sumarr[presum-k]
            
            sumarr[presum] += 1 # think if presum = x and we are looking for k then a presum whose value is (x-k) should be present 
        
        return count