class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic dec q
        q = deque()
        result = []
        l, r = 0, 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft() 
            if r >= k - 1:
                result.append(nums[q[0]]) # we are not popping from q, as the value can still be used in future
                l += 1 # already considered - window
            
            r += 1
        
        return result
