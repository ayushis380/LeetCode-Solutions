class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
# For each house, you want to find the nearest heater, and then compute the distance to it. The maximum of all these minimum distances will be your answer — because:
# So, you need at least enough radius to reach the farthest house from its nearest heater

        heaters.sort() # O(m*log(m))
        radius = 0

        for h in houses: #O(n)
            # Binary Search on the heaters array: log(m)
            idx = bisect.bisect_left(heaters, h) # bisect left then possible left index is returned

            # Distance to the left heater
            left_dist = float("inf") if idx == 0 else h - heaters[idx -1] # h is ahead of heaters[idx-1]
            # Distance to the right heater
            right_dist = float("inf") if idx == len(heaters) else heaters[idx] - h # idx is where h can be placed

            min_dist = min(left_dist, right_dist)
        # The heater radius must be large enough to cover the farthest house from its closest heater.
            radius = max(radius, min_dist)
        
        return radius

        # O((n+m)∗log(m))
        
