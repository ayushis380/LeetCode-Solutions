class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        result = []
        heap = []

        for key, val in freq.items():
            heapq.heappush(heap, (val, key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            val, num = heapq.heappop(heap)
            result.append(num)
        
        return result
        
