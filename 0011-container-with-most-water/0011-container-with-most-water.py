class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        water = 0

        while low < high:
            minht = min(height[low], height[high])
            store = (high - low) * minht
            water = max(water, store)

            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        
        return water
            

