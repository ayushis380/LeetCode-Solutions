class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # indexes, mono decreasing values
        output = []
        l, r = 0, 0

        while r < len(nums):
            while queue and nums[queue[-1]] < nums[r]:
                queue.pop()
            
            queue.append(r)

            if l > queue[0]: # if start of window has moved ahead of queue's top value(index), that means queue needs to be updated as it has stale index entries 
                queue.popleft()
            
            if (r + 1) >= k:
                output.append(nums[queue[0]])
                l += 1
            
            r += 1
        
        return output




