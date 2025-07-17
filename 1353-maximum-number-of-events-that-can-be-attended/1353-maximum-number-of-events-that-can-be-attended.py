class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # events.sort(key = lambda x: (x[0], x[1]))
# greedy strategy: if it's possible to attend both meetings i and j on day k, we should prioritize the one with the earlier end time
        n = len(events)
        events.sort()
        maxDay = max([event[1] for event in events])
        pq = []
        j, total = 0, 0

        for i in range(1, maxDay + 1):
            while j < n and events[j][0] <= i: # start day is less than or equal to i
                heapq.heappush(pq, events[j][1]) # all meetings available to attend on day i or earlier
                j += 1
            while pq and pq[0] < i:
                heapq.heappop(pq) # can no longer be attended
            
            if pq:
                heapq.heappop(pq)
                total += 1
        
        return total