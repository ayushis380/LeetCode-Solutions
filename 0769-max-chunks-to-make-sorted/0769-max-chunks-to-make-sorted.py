class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        maxseen = -1

        for i, val in enumerate(arr):
            maxseen = max(maxseen, val)
            if maxseen == i:
                chunks += 1
        
        return chunks