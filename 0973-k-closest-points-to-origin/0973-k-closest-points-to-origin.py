class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for x, y in points:
            dist = sqrt(x ** 2 + y ** 2)
            heapq.heappush(heap, (-dist, x, y))

            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            d, x, y = heapq.heappop(heap)
            result.append([x, y])
        
        return result