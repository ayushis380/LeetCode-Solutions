class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        heap = []
        for i in range(len(arr)):
            diff = abs(arr[i] - x)
            if len(heap) < k:
                heapq.heappush(heap, (-diff, i))
            elif diff < -heap[0][0]:
                heapq.heappushpop(heap, (-diff, i))
        
        result = [arr[p[1]] for p in heap]
        result.sort()
        return result

                 