class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for val in nums:
            if len(heap) < k:
                heapq.heappush(heap, val)
            elif val > heap[0]:
                heapq.heappushpop(heap, val)
        
        return heap[0]