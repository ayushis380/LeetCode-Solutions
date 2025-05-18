class Solution:
    def trap(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        lmax, rmax = height[low], height[high]
        water = 0

        while low < high:
            if lmax < rmax:
                low += 1 # think of lmax as the smaller value as compared to rmax - smaller value decides the amount of water stored 
                lmax = max(lmax, height[low]) # comparing the max on left side to the height where we are at currently
                water += lmax - height[low]
            else:
                high -= 1
                rmax = max(rmax, height[high])
                water += rmax - height[high]
        
        return water
