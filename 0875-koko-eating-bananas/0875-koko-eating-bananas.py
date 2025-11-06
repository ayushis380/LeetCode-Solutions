class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        mink = float("inf")

        while low <= high:
            eat = low + (high - low)//2
            time = 0
            for p in piles:
                time += ceil(p / eat)
            
            if time > h: # not able to finish, increase eating speed
                low = eat + 1
            else:
                mink = min(mink, eat)
                high = eat -1 # able to finish, check for lower eating speed
        
        return mink
