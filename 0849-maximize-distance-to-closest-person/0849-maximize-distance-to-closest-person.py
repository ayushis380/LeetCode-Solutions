class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [n] * n 
        right = [n] * n

        for i, seat in enumerate(seats):
            if seat: left[i] = 0 # when empty
            elif i > 0: left[i] = left[i-1] + 1 # considering the dist for evry index

        for i in range(n-1, -1, -1):
            if seats[i]: right[i] = 0
            elif i < n-1: right[i] = right[i+1] + 1
        
        return max(min(left[i], right[i]) for i in range(n))
