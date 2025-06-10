class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
# A Max-Heap is a data structure that can take items, and can remove and return the maximum, with both operations taking O(logN) time. It does this by maintaining the items in a special order (within the array), or as a balanced binary tree

        heap = [-st for st in stones]
        heapq.heapify(heap) # O(N)

        while len(heap) > 1:
            # three O(logN) operations
#  the three is an ignored constant. This means that we're doing N⋅O(logN)=O(NlogN) operations
            y = -1 * heapq.heappop(heap)
            x = -1 * heapq.heappop(heap)

            if y != x:
                heapq.heappush(heap, -1 * (y - x))
        
        return -1 * heap[0] if len(heap) else 0