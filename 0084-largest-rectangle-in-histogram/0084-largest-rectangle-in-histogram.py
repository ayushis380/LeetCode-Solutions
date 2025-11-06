class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        length = len(heights)
        area = 0

        for i, ht in enumerate(heights):
            start = i
            while stack and stack[-1][0] > ht:
                val, ind = stack.pop()
                area = max(area, val * (i - ind))
                start = ind
            
            stack.append([ht, start])
        
        for i in range(len(stack)):
            ht, ind = stack.pop()
            area = max(area, ht * (length - ind))

        return area
