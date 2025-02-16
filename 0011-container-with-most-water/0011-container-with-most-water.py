class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        water = 0

        while low < high:
            minw = min(height[low], height[high])
            cur_water = (high - low) * minw
            water = max(water, cur_water)

            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
            
        return water