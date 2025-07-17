class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        person = (i for i, val in enumerate(seats) if val)
        prev, future = None, next(person)
        ans = 0

        for i, seat in enumerate(seats):
            if seat:
                prev = i # takes future value, filled seat
            else:
            # future needs to take next filled seat which is greater than i
            # while future and future < i - not used as future can be 0
                while future is not None and future < i: 
                    future = next(person, None)
                
                left = float("inf") if prev is None else i - prev
                right = float("inf") if future is None else future - i

                ans = max(ans, min(left, right))
        
        return ans