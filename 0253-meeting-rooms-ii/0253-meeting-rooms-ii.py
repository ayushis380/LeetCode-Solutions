class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # Greedy approach
        time = []
        rooms = 0
        count = 0

        for start, end in intervals:
            time.append([start, 1])
            time.append([end, -1])
        
        time.sort(key = lambda x: (x[0], x[1])) # start can be same for some so then sort on basis of end

        for t, flag in time:
            count += flag # flag can be 1 or -1
            rooms = max(rooms, count) # max seen so far gives us the result
        
        return rooms
            


