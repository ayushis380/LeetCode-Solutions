class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort() # as per start day 
        n = len(events)
        maxDay = max([event[1] for event in events])
        pq = []
        ind, attend = 0, 0

        # pick all the days that can be started before current day 
        # then remove events whose end day is less than current day as they cant be attended now
        # if an event is left in pq, that means we can attend it - it got priorty over other events
        for day in range(1, maxDay + 1):
            while ind < n and events[ind][0] <= day:
                heapq.heappush(pq, events[ind][1])
                ind += 1
            
            while pq and pq[0] < day:
                heapq.heappop(pq)
            
            if pq:
                heapq.heappop(pq)
                attend += 1
        
        return attend
