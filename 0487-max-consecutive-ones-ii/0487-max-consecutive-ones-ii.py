class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
#     Valid State = one or fewer 0's in our current sequence
#     Invalid State = two 0's in our current sequence
        maxlen = 0
        start = 0
        freq = defaultdict(int)

        for end in range(len(nums)):
            val = nums[end]
            freq[val] += 1
            
            while freq[0] > 1:
                v_start = nums[start]
                freq[v_start] -= 1
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
        
        return maxlen


