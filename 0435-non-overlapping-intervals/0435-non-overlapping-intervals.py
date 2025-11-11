class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        count = 0
        store = []

        for start, end in intervals:
            if store and store[-1][1] > start:
                store[-1][1] = min(store[-1][1], end)
                count += 1
            else:
                store.append([start, end])
        
        # return len(intervals) - len(store)
        return count