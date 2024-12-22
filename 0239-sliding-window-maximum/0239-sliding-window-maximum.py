class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque() # stores indices of nums and is monotonically decreasing(in regards with nums values)
        l, r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]: 
                q.pop() # pop all smaller values than the value at index r
            
            q.append(r)

            if l > q[0]: # happens when old window's index of max value is still in the queue
            # eg 1 3 1 2 0 5, k = 3, when l = 2, q still stores index of value 3 
                q.popleft() # l is the start of the window
            
            if (r + 1) >= k: # r + 1 as k denotes size and r is an index
                output.append(nums[q[0]])
                l += 1 # only increment it when we have updated the max value of curr window
            
            r += 1 # r is for the end index of window
        
        return output