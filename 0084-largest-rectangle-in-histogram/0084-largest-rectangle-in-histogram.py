class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = [] # index, ht

        for i, ht in enumerate(heights):
            start = i # the start index of current height - this helps store till where it can be extended
            while stack and stack[-1][1] > ht: # pop bigger values as they cant be extended
                ipop, hpop = stack.pop()
                maxarea = max(maxarea, hpop * (i - ipop)) # calculate their area
                start = ipop  # extending to left for curr ht
            
            stack.append((start, ht))
        
        # calculate area from left value in stack
        # they got extended from end still start 
        for start, ht in stack:
            maxarea = max(maxarea, ht * (len(heights) - start))
        
        return maxarea