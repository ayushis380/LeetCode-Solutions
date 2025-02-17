class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        stack = []
        area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                i_old, h_old = stack.pop()
                area = max(area, h_old * (i - i_old))
                start = i_old
            
            stack.append((start, h))
        
        for start, h in stack:
            area = max(area, h * (length - start))
        
        return area
        


