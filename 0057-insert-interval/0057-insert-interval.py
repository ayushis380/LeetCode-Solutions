class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(intervals)):
            # end of new Interval < start of exiting, so means nI is ending before
            if newInterval[1] < intervals[i][0]:  
                output.append(newInterval)
                return output + intervals[i:]
            elif newInterval[0] > intervals[i][1]: # start of nI is > end of existing, so nI will come afterwards
                output.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), 
                max(newInterval[1], intervals[i][1])]
        
        output.append(newInterval)
        return output
