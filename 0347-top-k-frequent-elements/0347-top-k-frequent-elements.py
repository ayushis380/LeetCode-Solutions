class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap, topk = [], []
        heapq.heapify(heap)

        for key, count in freq.items():
            heapq.heappush(heap, (count, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            count, key = heapq.heappop(heap)
            topk.append(key)
        
        return topk

