class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i, lst in enumerate(intervals):
            if lst[1] < newInterval[0]: # end < nI_start
                result.append(lst)
            elif lst[0] > newInterval[1]: # start > nI_end
                result.append(newInterval)
                return result + intervals[i:]
            else:
                newInterval = [min(lst[0], newInterval[0]), max(lst[1], newInterval[1])]
        
        result.append(newInterval)
        return result