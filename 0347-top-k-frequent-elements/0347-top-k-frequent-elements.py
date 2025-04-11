class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        topk = []

        for key, count in freq.items():
            heapq.heappush(heap, (count, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            cnt, key = heapq.heappop(heap)
            topk.append(key)
        
        return topk

        
