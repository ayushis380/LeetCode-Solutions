class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        result = []
        result.append(intervals[0]) # to compare values

        for start, end in intervals[1:]:
            if start <= result[-1][1]: # last value from result and curr value compared
                result[-1][1] = max(end, result[-1][1])
            else:
                result.append([start, end])
        
        return result