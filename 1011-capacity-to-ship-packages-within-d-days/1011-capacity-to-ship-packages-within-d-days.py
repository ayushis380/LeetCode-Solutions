class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
    # Lower bound (low) should not be 1 — it should be max(weights) because no ship can carry less than the heaviest package
    # if low = 1 then sthink how would ship carry weights greater than 1, it need to atleast have max(weights)

        low, high = max(weights), sum(weights)
        result = high  # Start with the highest possible capacity

        while low <= high:
            midWt = low + (high - low) // 2
            totalwt = 0
            daysTook = 1  # Start with the first day, If all packages fit in one day, you'd return 0 days — which is invalid so not start with 0

            for w in weights:
                if totalwt + w > midWt: # because you want to start a new day only when it exceeds capacity.
                    daysTook += 1
                    totalwt = 0
                totalwt += w

            if daysTook > days:
                low = midWt + 1  # Need more capacity
            else:
                result = midWt  # Try smaller capacity
                high = midWt - 1

        return result
