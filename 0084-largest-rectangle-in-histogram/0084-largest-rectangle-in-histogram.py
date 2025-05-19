class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        length = len(heights)

        for i, ht in enumerate(heights):
            start = i
            
            while stack and stack[-1][1] > ht:
                start, old_ht = stack.pop()
                maxarea = max(maxarea, old_ht * (i - start))
            
            stack.append((start, ht))
        
        for start, ht in stack:
            maxarea = max(maxarea, ht * (length - start))
        
        return maxarea