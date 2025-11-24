class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        presum = 0
        result = 0
        freq[0] = 1

        for n in nums:
            presum = (presum + n%k + k) % k # Take modulo twice to avoid negative remainders
            result += freq[presum]
            freq[presum] += 1
        
        return result