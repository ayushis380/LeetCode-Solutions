class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxlen = 0
        numOfZeroes = 0
        start = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                numOfZeroes += 1
            
            while numOfZeroes - k > 0: # sliding window, if number of zeroes goes above k 
                if nums[start] == 0:
                    numOfZeroes -= 1
                start += 1
            
            maxlen = max(maxlen, end - start + 1)
        
        return maxlen
