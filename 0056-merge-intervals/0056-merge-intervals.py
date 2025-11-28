class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()

        for start, end in intervals:
            if result and  result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
                continue
            
            result.append([start, end])
        
        return result