class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for key, count in freq.items():
            heapq.heappush(heap, (count, key))

            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            cnt, key = heapq.heappop(heap)
            result.append(key)
        
        return result