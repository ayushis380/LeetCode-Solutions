class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        output = [[intervals[0][0], intervals[0][1]]]

        for i in range(1, len(intervals)):
        # cur_start <= old_end
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(intervals[i][1], output[-1][1])
            else:
                output.append([intervals[i][0], intervals[i][1]])
        
        return output

