class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for x, y in points:
            dist = -1 * sqrt (x * x + y * y)

            heapq.heappush(heap, (dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            dist, x, y = heapq.heappop(heap)
            result.append([x, y])

        return result