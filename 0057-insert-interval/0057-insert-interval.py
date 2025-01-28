class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]: # end is less than start of ith interval so NI should come before
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # start is greater than end of ith interval so interval will come before
                res.append(intervals[i])
            else: # overlapping
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        res.append(newInterval) # we dont merge newInterval till end as it can merge with other intervals
        return res

                