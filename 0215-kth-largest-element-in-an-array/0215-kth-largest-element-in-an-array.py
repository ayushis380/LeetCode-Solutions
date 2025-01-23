class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        heapq.heapify(heap)

        for val in nums:
            heapq.heappush(heap, val)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]