class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        # store max from each side 
        left = [0] * length
        right = [0] * length
        water = 0

        left[0], right[0] = height[0], height[length - 1]

        for i in range(1, length):
            left[i] = max(left[i-1], height[i-1])
        
        for i in range(length - 2, -1, -1):
            right[i] = max(right[i+1], height[i+1])
        
        for i in range(length):
            minval = min(left[i], right[i])
            if minval > height[i]:
                water += minval - height[i] 
        
        return water


        