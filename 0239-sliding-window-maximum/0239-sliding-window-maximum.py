class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque() # monotonic decreasing 
        l, r = 0, 0
        result = []
    # performing popleft and pop on queue
    # both pop values from different ends

        while r < len(nums):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop() # removing the top element - on rightmost
            
            queue.append(r)

            # shift in window 
            if l > queue[0]: # means we have already added this nums[queue[0]] value to output and its ok to pop it
                queue.popleft() # removing first value - on leftmost

            if r >= k - 1:
                # see we are not popping value from queue 
                # so to make sure the values are from l - r window, we do a check l > queue[0]
                result.append(nums[queue[0]]) # first value is the largest
                l += 1
            
            r += 1
        
        return result 

