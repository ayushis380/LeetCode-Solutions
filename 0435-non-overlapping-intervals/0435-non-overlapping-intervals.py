class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        count = 0
        nonOverlap = []
        nonOverlap.append(intervals[0])

        for start, end in intervals[1:]:
            if start < nonOverlap[-1][1]:
                count += 1
                nonOverlap[-1][1] = min(end, nonOverlap[-1][1])
            else:
                nonOverlap.append([start, end])
        
        return count