class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heap = []
        for x, y in points:
            dis = -(pow(x,2) + pow(y,2)) # to maintain max heap, removing bigger values
            if len(heap) < k:
                heapq.heappush(heap, (dis, x, y))
            elif dis > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (dis, x, y))
        for _, x, y in heap:
            result.append([x,y])
        return result