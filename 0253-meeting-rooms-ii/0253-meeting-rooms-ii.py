class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        time = []

        for start, end in intervals:
            time.append([start, 1])
            time.append([end, -1])
        
        time.sort(key = lambda x: x[0])
        maxrooms = 0
        count = 0

        for t, val in time:
            count += val
            maxrooms = max(maxrooms, count)
        
        return maxrooms
        