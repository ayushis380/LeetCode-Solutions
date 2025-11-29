class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        area = 0

        while low < high:
            minht = min(height[low], height[high])
            area = max(area, minht * (high - low))

            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        
        return area