class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        mink = high

        while low <= high:
            eat = low + (high - low) // 2
            time = 0

            for p in piles:
                time += ceil(p/eat)
            
            if time <= h:
                mink = min(mink, eat)
                high = eat - 1
            else:
                low = eat + 1
        
        return mink
