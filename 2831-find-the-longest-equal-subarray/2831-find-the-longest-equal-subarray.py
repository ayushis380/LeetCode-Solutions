class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos = defaultdict(list) # For every distinct number x, consider only the indices where x appears.
        # To make them a continuous subarray, we may need to delete numbers in between them:
        for i, n in enumerate(nums):
            pos[n].append(i)
        
        maxlen = 0
        for n, ls in pos.items(): # # sliding window for each distinct number
            l = 0
            for r in range(len(ls)):
                # window length of number - freq of numbers
                # 1 3 2 3 1 3, 3 = [1, 3, 5], when l = 0, r = 2, it shows window from 1 to 5 and how many extra elements inbtwn
                # l and r are like freq of number, r - l = 2 and there are two 3s
                while ls[r] - ls[l] - (r - l) > k: # # while deletions needed > k, shrink window
                    l += 1 
                
                maxlen = max(maxlen, (r - l + 1)) ## r - l + 1 = number of kept elements in window

        return maxlen 
        
