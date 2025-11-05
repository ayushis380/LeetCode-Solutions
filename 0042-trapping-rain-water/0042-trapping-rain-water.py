class Solution:
    def trap(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        lmax, rmax = height[low], height[high]
        water = 0

        while low < high:
            if lmax < rmax: # consider the min val
                low += 1
                lmax = max(height[low], lmax)
                water += lmax - height[low]
            else:
                high -= 1
                rmax = max(height[high], rmax)
                water += rmax - height[high]
        
        return water
            




        