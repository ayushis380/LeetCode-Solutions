class Solution:
    def trap(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        lmax, rmax = height[low], height[high]
        total = 0

        while low < high:
            if lmax < rmax:
                low += 1
                lmax = max(lmax, height[low])
                total += lmax - height[low]
            else:
                high -= 1
                rmax = max(rmax, height[high])
                total += rmax - height[high]
        
        return total
