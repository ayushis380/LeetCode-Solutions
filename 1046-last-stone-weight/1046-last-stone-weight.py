class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-val for val in stones]
        heapq.heapify(heap)

        while len(heap) >= 2:
            y = -1 * heapq.heappop(heap)
            x = -1 * heapq.heappop(heap)

            if y != x:
                heapq.heappush(heap, -(y - x))
        
        return 0 if len(heap) == 0 else (-1 * heapq.heappop(heap))