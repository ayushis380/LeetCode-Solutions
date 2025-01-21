class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpile = max(piles)
        least = 1
        result = 0

        while least <= maxpile:
            mid = least + (maxpile - least)//2
            hours = 0

            for p in piles:
                hours += ceil(p/mid)
            
            if hours <= h:
                result = mid
                maxpile = mid - 1
            else:
                least = mid + 1

        return result 
        


        

