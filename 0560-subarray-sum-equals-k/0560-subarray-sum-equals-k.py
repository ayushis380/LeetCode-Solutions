class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        smap = defaultdict(int)
        smap[0] = 1
        presum = 0
        count = 0

        for n in nums:
            presum += n
            diff = presum - k
            if diff in smap:
                count += smap[diff]
            
            smap[presum] += 1
        
        return count
