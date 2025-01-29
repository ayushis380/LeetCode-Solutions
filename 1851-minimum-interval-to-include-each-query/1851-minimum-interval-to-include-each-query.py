class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort() # to go through sorted left values one by one
        heap = [] # taking min heap to store the size of an interval, if same size then right is the break point 
        i = 0
        result = {} # taking a map as we would go though sorted queries 

    # we need answer with original indexes of queries, so in place sorting is not done
        for q in sorted(queries): # this doesnt change queries, sorted returns a new list
            
            while i < len(intervals) and intervals[i][0] <= q: # left should be less than q
                l, r = intervals[i]
                heapq.heappush(heap, (r - l +1, r)) # size and r: r as smaller r means q is closer to it 
                i += 1
            
            while heap and heap[0][1] < q: # if right is less than q, then q doesn't lie in that interval
                heapq.heappop(heap)
            
            result[q] = heap[0][0] if heap else -1 # top is where q lies
        
        return [result[q] for q in queries] # converting to list
