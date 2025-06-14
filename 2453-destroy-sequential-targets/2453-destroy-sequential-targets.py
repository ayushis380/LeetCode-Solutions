class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
#         nums[i] destroys any nums[j] where
#  (nums[j] - nums[i]) % space == 0
# ⇒ i.e., numbers that share the same remainder modulo space
        freq = defaultdict(int)
        best = (0, float("inf")) # maxDestroyedCount, minVal

        for n in nums:
            freq[n% space] += 1
        
        for n in nums:
            count = freq[n% space]
            
             # max count -> better candidate
            # same count -> choose min number
            if count > best[0] or (count == best[0] and n < best[1]):
                best = (count, n)
        
        return best[1]
        
        
        # Brute force - n ^ 2
        # minVal = float("inf")
        # maxDestroyed = float("-inf")

        # for i in range(len(nums)):
        #     destroyed = 0
        #     for j in range(len(nums)):
        #         if (nums[j] - nums[i]) % space == 0:
        #             destroyed += 1
            
        #     if destroyed >= maxDestroyed:
        #         maxDestroyed = destroyed
        #         minVal = min(minVal, nums[i])
        
        # return minVal
        
