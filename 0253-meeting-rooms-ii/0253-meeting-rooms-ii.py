class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        time = []
        rooms = 0

        for s, e in intervals:
            time.append([s, 1])
            time.append([e, -1])
        
        time.sort()
        count = 0
        for t, val in time:
            count += val
            rooms = max(rooms, count)
        
        return rooms