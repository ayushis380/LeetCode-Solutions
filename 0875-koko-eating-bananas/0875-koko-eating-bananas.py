class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mink = 0
        low = 1
        high = max(piles)

        while low <= high:
            eat = low + (high - low)//2
            time = 0

            for p in piles:
                time += ceil(p/eat)
            
            if time <= h:
                mink = eat
                high = eat - 1
            else:
                low = eat + 1
        
        return mink

