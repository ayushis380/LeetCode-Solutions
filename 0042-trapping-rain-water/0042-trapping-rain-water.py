class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        left, right = 0, len(height) - 1
        lmax, rmax = height[left], height[right]

        while left < right:
            if lmax < rmax:
                left += 1
                lmax = max(lmax, height[left])
                water += lmax - height[left]
            else:
                right -= 1
                rmax = max(rmax, height[right])
                water += rmax - height[right]
        
        return water