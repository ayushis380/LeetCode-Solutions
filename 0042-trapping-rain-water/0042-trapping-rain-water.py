class Solution:
    def trap(self, height: List[int]) -> int:
# we know the current bar (pointed by left) will never be affected by any bar on the right of right. This is because rmax is already greater than lmax, and future bars can only reduce the impact of rmax on water calculations.
# even if the values are smaller in the middle it doesnt matter as we look for max values from both sides and then pick the minimum
        left, right = 0, len(height) - 1
        water = 0
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