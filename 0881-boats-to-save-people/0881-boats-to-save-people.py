class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0

        while l <=r:
            # at most two people allowed
            remain = limit - people[r] # max(people) may or may not be limit, but not over it
            r -= 1 # took person from end 
            boats += 1

            if l <=r and remain >= people[l]: # l <= r as we decreased r in line 9 and think when l and r at same point, then there is only one person left which will make l > r due to line 9
                l += 1
        
        return boats