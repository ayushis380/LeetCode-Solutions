class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        left = [0] * length
        right = [0] * length
        water = 0

        left[0] = height[0]
        right[length -1] = height[length -1]

        for i in range(1, length):
            left[i] = max(left[i-1], height[i-1])
        
        for i in range(length -2, -1, -1):
            right[i] = max(right[i+1], height[i+1])

        for i in range(length):
            ht = min(left[i], right[i])
            if ht > height[i]:
                water += ht - height[i]
        
        return water

        