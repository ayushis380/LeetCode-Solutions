class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # explanation by Sean 
        # monotonic stack - looking back to place the values correctly
        # 0 2 3 4 5 1 2 3 4 6 - stack will be 0 2 3 4 5 - 0 5 6 - chunk with 0 is correctly placed
        # chunk 2 3 4 5 1 2 3 4 - will be one chunk with max of 5 - this indicates the max of chunk
        # so store the max of a chunk, this will help in future comparisons
        stack = []

        for num in arr:
            largest = num
            while stack and stack[-1] > num:
                largest = max(largest, stack.pop())
            
            stack.append(largest)
        
        return len(stack)